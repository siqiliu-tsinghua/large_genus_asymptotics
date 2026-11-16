"""Meaningful source-export cases; the complete article is also compiled alone."""
from pathlib import Path
import sys
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'scripts'))
from export_tex import Expander, export, inspect_standalone, remove_comments
from workflow import WorkflowError, digest, encoded
from verify_submission import check_reference_pdf


class StandaloneSourceTests(unittest.TestCase):
    def make_export_fixture(self, root):
        (root/'build').mkdir()
        (root/'sections/one').mkdir(parents=True)
        (root/'main.tex').write_text(
            '\\documentclass{article}\n\\begin{document}\n'
            '\\input{sections/one/section}\n\\bibliography{references}\n'
            '\\end{document}\n', encoding='utf-8', newline='\n')
        (root/'sections/one/section.tex').write_text(
            '\\section{One}\\label{sec:one}\nText.\n', encoding='utf-8', newline='\n')
        (root/'build/main.bbl').write_text(
            '\\begin{thebibliography}{X}\n\\bibitem{X} Example.\n'
            '\\end{thebibliography}\n', encoding='utf-8', newline='\n')
        pdf = root/'build/main.pdf'
        pdf.write_bytes(b'%PDF-1.7\nTest-only approved PDF fixture.\n')
        files = {name:digest((root/name).read_bytes())
                 for name in ('main.tex', 'sections/one/section.tex')}
        receipt = {'unit':None, 'strict':True, 'passed':True, 'diagnostics':[],
                   'source_hash':digest(encoded({'one':files})), 'pdf':'build/main.pdf',
                   'pdf_sha256':digest(pdf.read_bytes())}
        (root/'build/build_receipt.json').write_text(encoded(receipt), encoding='utf-8', newline='\n')
        return SimpleNamespace(
            root=root.resolve(), state={'active_unit':None},
            units={'one':{'directory':'sections/one'}},
            safe=lambda name:(root/name).resolve(),
            relative=lambda path:Path(path).resolve().relative_to(root.resolve()).as_posix(),
            audit_records=lambda:None, included_units=lambda:['one'],
            publication_units=lambda:['one'], assert_fresh=lambda uid:None,
            fingerprint=lambda uid:files, assert_no_retired_inputs=lambda paths:None)

    def test_export_creates_and_refreshes_published_pdf_without_local_receipts(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            engine = self.make_export_fixture(root)
            output = root/'submission/paper.tex'
            with patch('export_tex.Engine', return_value=engine):
                first = export(output, root)
                self.assertEqual((root/'submission/paper.pdf').read_bytes(),
                                 (root/'build/main.pdf').read_bytes())
                self.assertEqual(first['pdf_output'], 'submission/paper.pdf')
                self.assertEqual(first['pdf_output_sha256'], first['source_pdf_sha256'])
                # A fresh clone has the generated PDF but no ignored export receipt.
                (root/'build/export_receipt.json').unlink()
                (root/'submission/paper.pdf').write_bytes(b'%PDF-old published build')
                second = export(output, root)
                self.assertEqual((root/'submission/paper.pdf').read_bytes(),
                                 (root/'build/main.pdf').read_bytes())
                self.assertEqual(first['output_sha256'], second['output_sha256'])
                self.assertEqual({p.name for p in output.parent.iterdir()}, {'paper.tex','paper.pdf'})

    def test_export_preserves_unexpected_submission_files(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            engine = self.make_export_fixture(root)
            (root/'submission').mkdir()
            extra = root/'submission/notes.md'
            extra.write_text('Keep this file.\n', encoding='utf-8', newline='\n')
            with patch('export_tex.Engine', return_value=engine):
                with self.assertRaisesRegex(WorkflowError, 'only the standalone TeX'):
                    export(root/'submission/paper.tex', root)
            self.assertEqual(extra.read_text(encoding='utf-8'), 'Keep this file.\n')
            self.assertFalse((root/'submission/paper.pdf').exists())

    def test_published_companion_cannot_be_changed_after_export(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            engine = self.make_export_fixture(root)
            with patch('export_tex.Engine', return_value=engine):
                receipt = export(root/'submission/paper.tex', root)
            self.assertEqual(check_reference_pdf(engine,receipt), (root/'build/main.pdf').resolve())
            (root/'submission/paper.pdf').write_bytes(b'%PDF-unrelated paper')
            with self.assertRaisesRegex(WorkflowError, 'Published companion PDF'):
                check_reference_pdf(engine,receipt)

    def test_reference_pdf_cannot_be_replaced_after_export(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root/'build').mkdir()
            pdf = root/'build/main.pdf'
            pdf.write_bytes(b'%PDF-original approved manuscript')
            engine = SimpleNamespace(safe=lambda name:(root/name).resolve())
            receipt = {'source_pdf':'build/main.pdf','source_pdf_sha256':digest(pdf.read_bytes())}
            self.assertEqual(check_reference_pdf(engine,receipt),pdf.resolve())
            pdf.write_bytes(b'%PDF-another manuscript build')
            with self.assertRaisesRegex(WorkflowError,'changed since export'):
                check_reference_pdf(engine,receipt)
            receipt['source_pdf'] = 'build/another.pdf'
            with self.assertRaisesRegex(WorkflowError,'complete approved'):
                check_reference_pdf(engine,receipt)

    def test_nested_source_and_inline_bibliography_preserve_tex_comments(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root/'chapter').mkdir()
            (root/'main.tex').write_text(
                '% internal main\n\\documentclass{article}\n'
                '\\newcommand{\\sample}{% suppress a newline\nword% another comment\n}\n'
                '\\begin{document}\n\\input{chapter/one}\n'
                '\\bibliographystyle{alpha}\n\\bibliography{references}\n\\end{document}\n',
                encoding='utf-8',newline='\n')
            (root/'chapter/one.tex').write_text(
                '% \\input{never-read}\n\\section{One}\\label{sec:one}\n'
                'A 10\\% value. \\input{chapter/two}\n',encoding='utf-8',newline='\n')
            (root/'chapter/two.tex').write_text('Second.\\cite{Example}\n',encoding='utf-8',newline='\n')
            bbl = ('\\begin{thebibliography}{X}\n\\bibitem[X]{Example} An author.\n'
                   '\\end{thebibliography}\n')
            expander = Expander(root,bbl)
            merged = expander.expand(root/'main.tex')
            inspect_standalone(merged)
            self.assertIn('A 10\\% value.',merged)
            self.assertIn('word%\n}',merged)
            self.assertIn('Second.\\cite{Example}',merged)
            self.assertEqual(expander.bibliography_count,1)
            self.assertEqual(set(expander.inputs),{'main.tex','chapter/one.tex','chapter/two.tex'})
            self.assertNotIn('internal main',merged)

    def test_cycle_and_outside_inputs_cannot_be_exported(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root/'first.tex').write_text('\\input{second}\n',encoding='utf-8',newline='\n')
            (root/'second.tex').write_text('\\input{first}\n',encoding='utf-8',newline='\n')
            with self.assertRaisesRegex(WorkflowError,'Cyclic'):
                Expander(root,'').expand(root/'first.tex')
            with self.assertRaisesRegex(WorkflowError,'escapes'):
                Expander(root,'').resolve('../outside.tex')

    def test_no_silent_export_of_unsupported_external_material(self):
        with self.assertRaisesRegex(WorkflowError,'Verbatim'):
            remove_comments('\\verb|a%b|')
        with self.assertRaisesRegex(WorkflowError,'external'):
            inspect_standalone('\\includegraphics{private.pdf}')
        source = ('\\begin{document}See checks/run.py.\n'
                  '\\begin{thebibliography}{X}\\end{thebibliography}\\end{document}')
        with self.assertRaisesRegex(WorkflowError,'engineering'):
            inspect_standalone(source)


if __name__ == '__main__':
    unittest.main()
