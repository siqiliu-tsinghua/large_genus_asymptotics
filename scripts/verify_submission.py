"""Compile a copy of the single TeX source alone and compare the approved paper."""
from pathlib import Path
import argparse
import json
import re
import shutil
import subprocess
import sys
import tempfile

from export_tex import inspect_standalone
from workflow import Engine, ROOT, WorkflowError, atomic_write, digest, encoded, require, stamp


def group(text, start):
    require(text[start] == '{', 'Invalid aux group.')
    depth = 1
    position = start + 1
    while depth:
        require(position < len(text), 'Unclosed aux group.')
        character = text[position]
        if character == '\\':
            position += 2
            continue
        depth += (character == '{') - (character == '}')
        position += 1
    return text[start+1:position-1], position


def labels(path):
    source = path.read_text(encoding='utf-8')
    result = {}
    for match in re.finditer(r'\\newlabel\{', source):
        key, position = group(source,match.end()-1)
        if key.endswith('@cref'):
            continue
        data, _ = group(source,position)
        number, _ = group(data,0)
        result[key] = number
    return result


def check_reference_pdf(engine, exported):
    path = engine.safe(exported['source_pdf'])
    require(path == engine.safe('build/main.pdf'), 'Expected the complete approved manuscript PDF.')
    require(digest(path.read_bytes()) == exported['source_pdf_sha256'],
            'Approved manuscript PDF changed since export.')
    return path


def verify(root=ROOT):
    engine = Engine(root)
    engine.audit_records()
    receipt_path = engine.safe('build/export_receipt.json')
    exported = json.loads(receipt_path.read_text(encoding='utf-8'))
    reference_pdf = check_reference_pdf(engine, exported)
    source = engine.safe(exported['output'])
    require(digest(source.read_bytes()) == exported['output_sha256'], 'Export source changed.')
    inspect_standalone(source.read_text(encoding='utf-8'))
    require(engine.state['active_unit'] is None, 'Finish the paper review first.')
    for uid in engine.publication_units():
        engine.assert_fresh(uid)
    before = digest(encoded({uid:engine.fingerprint(uid) for uid in engine.included_units()}))
    require(before == exported['source_hash'], 'Article changed since export.')
    isolation = Path(tempfile.mkdtemp(prefix='hodge-submission-')).resolve()
    require(isolation.is_relative_to(Path(tempfile.gettempdir()).resolve()), 'Invalid isolation directory.')
    shutil.copy2(source,isolation/'paper.tex')
    require([p.name for p in isolation.iterdir()] == ['paper.tex'], 'Isolation starts with one source only.')
    output = engine.safe('build/submission-check')
    output.mkdir(parents=True,exist_ok=True)
    commands = []

    def run(command, name):
        commands.append(command)
        result = subprocess.run(command,cwd=isolation,capture_output=True,
                                text=True,encoding='utf-8',errors='replace')
        atomic_write(output/name,result.stdout+result.stderr)
        require(result.returncode == 0,'Isolated command failed: '+command[0]+'; see '+name)
        return result.stdout

    latex = ['xelatex','-no-shell-escape','-interaction=nonstopmode',
             '-file-line-error','-halt-on-error','-recorder','paper.tex']
    previous_aux = None
    recorders = []
    for iteration in range(1,6):
        run(latex,'xelatex-%02d.log' % iteration)
        recorder = isolation/'paper.fls'
        recorders.append(recorder.read_text(encoding='utf-8'))
        shutil.copy2(recorder,output/('paper-pass-%02d.fls' % iteration))
        log = (isolation/'paper.log').read_text(encoding='utf-8')
        diagnostics = [line for line in log.splitlines()
                      if re.search(r'^!|LaTeX Warning:|LaTeX Font Warning:|'
                                   r'Package .+ Warning:|Missing character:|Emergency stop',line)]
        current_aux = (isolation/'paper.aux').read_bytes()
        if not diagnostics and current_aux == previous_aux:
            break
        previous_aux = current_aux
    require(not diagnostics,'Unresolved isolated TeX diagnostics: '+repr(diagnostics))
    layout = [line for line in log.splitlines() if line.startswith('Overfull ')]
    require(not layout,'Isolated overfull boxes: '+repr(layout))
    tex_root = Path(run(['kpsewhich','-var-value=TEXMFROOT'],'tex-root.log').strip()).resolve()
    require(tex_root.is_dir(),'Cannot identify the standard TeX installation.')
    inputs = set()
    for line in '\n'.join(recorders).splitlines():
        if line.startswith('INPUT '):
            path = Path(line[6:].strip().strip('"'))
            path = (isolation/path).resolve() if not path.is_absolute() else path.resolve()
            require(not path.is_relative_to(engine.root),'Isolated compiler read a project file: '+str(path))
            require(path.is_relative_to(isolation) or path.is_relative_to(tex_root),
                    'Non-distribution external input: '+str(path))
            inputs.add(str(path))
    run(['pdftotext','-layout','-eol','unix','paper.pdf','paper.txt'],'pdftotext.log')
    manuscript_text = output/'approved-main.txt'
    result = subprocess.run(['pdftotext','-layout','-eol','unix',str(reference_pdf),
                             str(manuscript_text)],capture_output=True,text=True,encoding='utf-8')
    require(result.returncode == 0,'Cannot extract the approved main PDF text.')
    require((isolation/'paper.txt').read_bytes() == manuscript_text.read_bytes(),
            'The standalone PDF text differs from the approved complete manuscript.')
    current_labels = labels(isolation/'paper.aux')
    require(current_labels == labels(engine.safe('build/main.aux')),
            'Standalone label numbers differ from the approved manuscript.')
    require(digest(source.read_bytes()) == exported['output_sha256'], 'Source changed during isolated compilation.')
    check_reference_pdf(engine, exported)
    require(before == digest(encoded({uid:engine.fingerprint(uid) for uid in engine.included_units()})),
            'Article changed during isolated verification.')
    for suffix in ('pdf','aux','log','fls','txt'):
        shutil.copy2(isolation/('paper.'+suffix),output/('paper.'+suffix))
    result = {'schema_version':1,'time':stamp(),'passed':True,'strict':True,
        'source':exported['output'],'source_sha256':exported['output_sha256'],
        'source_hash':before,'isolation_directory':str(isolation),
        'initial_isolation_files':['paper.tex'],'tex_distribution_root':str(tex_root),
        'recorder_passes_checked':len(recorders),
        'compiler_commands':commands,'compiler_project_inputs':[],
        'runtime_inputs':sorted(inputs),'diagnostics':diagnostics,'layout_diagnostics':layout,
        'text_identical_to_approved_manuscript':True,'label_numbers_preserved':len(current_labels),
        'pages':(isolation/'paper.txt').read_text(encoding='utf-8').count('\f'),
        'pdf':'build/submission-check/paper.pdf','pdf_sha256':digest((output/'paper.pdf').read_bytes())}
    atomic_write(output/'verification.json',encoded(result))
    exported['isolated_compilation_pending'] = False
    exported['isolated_verification'] = 'build/submission-check/verification.json'
    atomic_write(receipt_path,encoded(exported))
    return result


def main():
    argparse.ArgumentParser(description=__doc__).parse_args()
    try:
        result = verify()
        print(encoded({key:result[key] for key in ('passed','source','pages','label_numbers_preserved',
              'compiler_project_inputs','text_identical_to_approved_manuscript','pdf')}),end='')
        return 0
    except (WorkflowError,OSError,ValueError,UnicodeError) as error:
        print('Standalone verification error: '+str(error),file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    raise SystemExit(main())
