"""
How to run these tests::

  $ tox
"""
from pathlib import Path

ROOTDIR = Path(__file__).parent.parent

SETUP_INFO = {}

# load SETUP_INFO:
fn = ROOTDIR / 'lino_ciao' / 'setup_info.py'
with open(fn, "rb") as fd:
    exec(compile(fd.read(), fn, 'exec'))

from lino.utils.pythontest import TestCase

class PackagesTests(TestCase):

    def test_packages(self):
        self.run_packages_test(SETUP_INFO['packages'])

class SpecsTests(TestCase):

    def test_overview(self):
        self.run_simple_doctests('docs/specs/overview.rst')
