import unittest
import os
from eegevt.eventfile import EventFile, load_efile, save_efile

class EventFileTestCases(unittest.TestCase):
    def setUp(self):
        resdir = os.path.join('eegevt', 'tests', 'resources', '')
        self.BESAfile = resdir + 'BESA.evt'
        self.NSfile = resdir + 'NS2.ev2'

    def test_load_BESA_efile(self):
        print(os.getcwd(), self.BESAfile)
        efile = load_efile(self.BESAfile)
        self.assertEqual(efile.events[-1].code, '2')
        self.assertEqual(len(efile.events), 33)

    def test_load_NS_efile(self):
        efile = load_efile(self.NSfile)
        self.assertEqual(efile.events[-1].code, '1')
        self.assertEqual(len(efile.events), 35)

if __name__ == '__main__':
    unittest.main()
