"""Meaningful source-export cases; the complete article is also compiled alone."""
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'scripts'))
from export_tex import Expander, inspect_standalone, remove_comments
from workflow import WorkflowError


class StandaloneSourceTests(unittest.TestCase):
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
