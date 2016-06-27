import unittest
import os
from eegevt.eventfile import EventFile, load_efile, save_efile


class EventFileTestCases(unittest.TestCase):
    def setUp(self):
        self.resdir = os.path.join('eegevt', 'tests', 'resources', '')
        self.BESAfile = self.resdir + 'BESA.evt'
        self.NSfile = self.resdir + 'NS2.ev2'

    def test_load_BESA_efile(self):
        efile = load_efile(self.BESAfile)
        self.assertEqual(efile.events[-1].code, '2')
        self.assertEqual(len(efile.events), 33)

    def test_load_BESA_noextra(self):
        efile = load_efile(self.resdir + 'BESA_noextra.evt')
        self.assertEqual(efile.events[-2].time, '5744629')
        self.assertEqual(len(efile.events), 4)

    def test_load_NS_efile(self):
        efile = load_efile(self.NSfile)
        self.assertEqual(efile.events[-1].code, '1')
        self.assertEqual(len(efile.events), 35)

    def test_nonexistent_file(self):
        with self.assertRaises(FileNotFoundError):
            load_efile(self.resdir + 'NotAFile.evt')

    def test_unknown_ext(self):
        with self.assertRaises(ValueError):
            load_efile(self.resdir + 'BadExt.err')

    def test_malformed_line(self):
        with self.assertRaises(TypeError):
            load_efile(self.resdir + 'malformedline.ev2')

    def test_malformed_BESA_header(self):
        with self.assertRaises(ValueError):
            load_efile(self.resdir + 'BESAheaderbad.evt')
