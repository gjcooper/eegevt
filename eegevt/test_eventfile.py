import unittest
from .eventfile import EventFile, load_efile, save_efile

class EventFileTestCases(unittest.TestCase):
    def setUp(self):
        self.BESAfile = 'testfiles/BESA.evt'
        self.NSfile = 'testfiles/NS2.ev2'

    def test_load_BESA_efile(self):
        efile = load_efile(self.BESAfile)
        self.assertEqual(efile.events[-1].code, '2')

    def test_load_NS_efile(self):
        efile = load_efile(self.NSfile)
        self.assertEqual(efile.events[-1].code, '1')
