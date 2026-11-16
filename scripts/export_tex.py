"""Export the approved article as one standalone TeX source and its final PDF.

The source needs only XeLaTeX and standard TeX distribution packages/fonts.
The PDF is copied from the strict complete manuscript build.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import sys
import uuid

from workflow import Engine, ROOT, WorkflowError, atomic_write, digest, encoded, require, stamp


def remove_comments(source: str) -> str:
    """Remove comment text while retaining a trailing %'s whitespace semantics.

    This article has no verbatim material or TeX catcode changes. Refuse those
    rather than pretending a lexical expander can interpret arbitrary TeX.
    """
    require(not re.search(r'\\(?:verb\*?\b|catcode\b|begin\{(?:verbatim|Verbatim|lstlisting|minted)\})', source),
            'Verbatim/catcode material requires an explicit export implementation.')
    result = []
    for line in source.splitlines(keepends=True):
        comment = None
        for position, character in enumerate(line):
            if character != '%':
                continue
            preceding = position - 1
            while preceding >= 0 and line[preceding] == '\\':
                preceding -= 1
            if (position - 1 - preceding) % 2 == 0:
                comment = position
                break
        if comment is None:
            result.append(line)
        elif line[:comment].strip():
            result.append(line[:comment] + '%\n')
    return ''.join(result)


class Expander:
    """Expand the article's explicit project-root-relative inputs, without execution."""

    command = re.compile(r'\\(input|bibliography|bibliographystyle)\s*\{([^{}]+)\}')

    def __init__(self, root: Path, bibliography: str):
        self.root = root.resolve()
        self.bibliography = remove_comments(bibliography)
        self.bibliography_count = 0
        self.inputs: dict[str, str] = {}

    def resolve(self, name: str) -> Path:
        require(not any(character in name for character in '\\#{}'),
                'Dynamic TeX input is not supported by the standalone exporter.')
        path = (self.root / name).resolve()
        if not path.suffix:
            path = path.with_suffix('.tex')
        require(path.is_relative_to(self.root), 'TeX input escapes the article root.')
        require(path.is_file(), 'Missing TeX input: ' + name)
        return path

    def expand(self, path: Path, stack: tuple[Path, ...] = ()) -> str:
        path = path.resolve()
        require(path.is_relative_to(self.root), 'TeX input escapes the article root.')
        require(path not in stack, 'Cyclic TeX input: ' + path.name)
        data = path.read_bytes()
        require(b'\r' not in data and not data.startswith(b'\xef\xbb\xbf'),
                'Export inputs must use UTF-8/LF without BOM.')
        self.inputs[path.relative_to(self.root).as_posix()] = digest(data)
        source = remove_comments(data.decode('utf-8'))

        def replace(match: re.Match[str]) -> str:
            command, name = match.groups()
            if command == 'input':
                return self.expand(self.resolve(name), (*stack, path))
            if command == 'bibliographystyle':
                return ''
            self.bibliography_count += 1
            require(self.bibliography_count == 1, 'Expected a single article bibliography.')
            return self.bibliography

        return self.command.sub(replace, source)


def inspect_standalone(source: str) -> None:
    active = remove_comments(source)
    external = re.search(
        r'\\(?:input|include|includeonly|includegraphics|bibliography|bibliographystyle|'
        r'addbibresource|InputIfFileExists|IfFileExists|openin|openout|write18)\b', active)
    require(external is None, 'Unexpanded/external TeX command in export: '
            + (external.group(0) if external else ''))
    require(active.count(r'\begin{document}') == 1
            and active.count(r'\end{document}') == 1, 'Expected one complete article.')
    require(active.count(r'\begin{thebibliography}') == 1
            and active.count(r'\end{thebibliography}') == 1,
            'The complete bibliography must be inline.')
    require(not re.search(r'(?i)(?:\bchecks/|\bcalculations/|\bbuild/|\.py\b|\.md\b|'
                          r'python|source bundle|accompanying calculations|installation commands)', active),
            'Internal engineering material remains in the article.')


def export(output: Path, root: Path = ROOT) -> dict:
    engine = Engine(root)
    require(engine.state['active_unit'] is None, 'Finish the active review before final export.')
    engine.audit_records()
    included = engine.included_units()
    require(set(included) == set(engine.publication_units()),
            'Final export requires the complete approved article.')
    for uid in included:
        engine.assert_fresh(uid)
    fingerprints = {uid:engine.fingerprint(uid) for uid in included}
    source_hash = digest(encoded(fingerprints))
    receipt_path = engine.safe('build/build_receipt.json')
    build = json.loads(receipt_path.read_text(encoding='utf-8'))
    require(build['unit'] is None and build['strict'] and build['passed']
            and not build['diagnostics'] and build['source_hash'] == source_hash,
            'Run the strict complete manuscript build before exporting.')
    pdf_data = engine.safe(build['pdf']).read_bytes()
    require(digest(pdf_data) == build['pdf_sha256'],
            'The reviewed manuscript PDF was changed.')
    bbl = engine.safe('build/main.bbl')
    expander = Expander(engine.root, bbl.read_text(encoding='utf-8'))
    source = '% !TeX program = xelatex\n' + expander.expand(engine.safe('main.tex'))
    require(expander.bibliography_count == 1, 'Expected one bibliography to inline.')
    required_sections = {engine.units[uid]['directory']+'/section.tex' for uid in included}
    require(required_sections <= set(expander.inputs), 'The generated assembly omits an approved section.')
    engine.assert_no_retired_inputs(expander.inputs)
    frozen_paths = {path for files in fingerprints.values() for path in files if not path.startswith('@')}
    require(set(expander.inputs) <= frozen_paths | {'sections/included.tex'},
            'The generated assembly reads an input outside the approved source closure.')
    inspect_standalone(source)
    labels = re.findall(r'\\label\{([^{}]+)\}', source)
    require(len(labels) == len(set(labels)), 'Duplicate labels in the merged article.')
    output = output.resolve()
    require(output.is_relative_to(engine.root), 'Export output must stay in the workspace.')
    require(output.suffix == '.tex', 'Export output must be a TeX source.')
    require(output.parent != engine.root and not any(
        output.is_relative_to(engine.safe(folder)) for folder in ('sections','tex','frontmatter','workflow')),
        'Choose a separate submission directory for the generated file.')
    pdf_output = output.with_suffix('.pdf')
    extras = [path for path in output.parent.iterdir() if path not in {output, pdf_output}] if output.parent.exists() else []
    require(not extras, 'Submission directory may contain only the standalone TeX source and its PDF.')
    previous = engine.safe('build/export_receipt.json')
    old = json.loads(previous.read_text(encoding='utf-8')) if previous.is_file() else None
    if output.exists() and output.read_text(encoding='utf-8') != source:
        require(old is not None, 'Refusing to overwrite an unrecognized existing submission source.')
        require(old['output'] == engine.relative(output)
                and digest(output.read_bytes()) == old['output_sha256'],
                'The previous submission source was edited; preserve those edits before exporting.')
    if pdf_output.exists():
        require(pdf_output.is_file(), 'The companion PDF path is not a regular file.')
    atomic_write(output, source)
    # The companion PDF is a generated artifact, refreshed on every export.
    temporary_pdf = pdf_output.with_name('.workflow-' + uuid.uuid4().hex + '.tmp')
    try:
        temporary_pdf.write_bytes(pdf_data)
        temporary_pdf.replace(pdf_output)
    finally:
        temporary_pdf.unlink(missing_ok=True)
    require(source_hash == digest(encoded({uid:engine.fingerprint(uid) for uid in included})),
            'Article changed while exporting.')
    require(digest(engine.safe(build['pdf']).read_bytes()) == build['pdf_sha256'],
            'The reviewed manuscript PDF changed while exporting.')
    result = {'schema_version':1,'time':stamp(),'source_hash':source_hash,
        'source_pdf':build['pdf'],'source_pdf_sha256':build['pdf_sha256'],
        'output':engine.relative(output),'output_sha256':digest(output.read_bytes()),
        'pdf_output':engine.relative(pdf_output),'pdf_output_sha256':digest(pdf_output.read_bytes()),
        'expanded_inputs':expander.inputs,'bibliography_sha256':digest(bbl.read_bytes()),
        'single_file':True,'engine':'xelatex',
        'requires_project_files_or_bibtex':False,'isolated_compilation_pending':True}
    atomic_write(previous, encoded(result))
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', default='submission/paper.tex')
    arguments = parser.parse_args()
    try:
        result = export(Path(arguments.output))
        print(encoded(result), end='')
        return 0
    except (WorkflowError, OSError, ValueError, UnicodeError) as error:
        print('Export error: ' + str(error), file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    raise SystemExit(main())
