import unittest
import filecmp
import re
import os
from eegevt.eventfile import load_efile, save_efile


class EventFileTestCases(unittest.TestCase):
    def setUp(self):
        self.resdir = os.path.join('eegevt', 'tests', 'resources', '')
        self.BESAfile = self.resdir + 'BESA.evt'
        self.NSfile = self.resdir + 'NS2.ev2'

    def tearDown(self):
        for outfile in ['NS2_minimal_recoded.ev2', 'BESA_minimal_recoded.evt',
#                        'NS2_recoded.ev2']:
                        'NS2_recoded.ev2', 'NS2_withheader_recoded.ev2']:
            try:
                os.remove(self.resdir + outfile)
            except OSError:
                pass

    def test_load_BESA_efile(self):
        efile = load_efile(self.BESAfile)
        self.assertEqual(efile.events[-1].code, 2)
        self.assertEqual(len(efile.events), 33)

    def test_load_BESA_noextra(self):
        efile = load_efile(self.resdir + 'BESA_noextra.evt')
        self.assertEqual(efile.events[-2].time, 5744629)
        self.assertEqual(len(efile.events), 4)

    def test_load_NS_efile(self):
        efile = load_efile(self.NSfile)
        self.assertEqual(efile.events[-1].code, 1)
        self.assertEqual(len(efile.events), 35)

    def test_load_NS_efile_with_header(self):
        efile = load_efile(self.resdir + 'NS2_withheader.ev2')
        self.assertEqual(efile.events[-1].code, 1)
        self.assertEqual(len(efile.events), 7)

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

    def test_mod_code(self):
        # v0.2.2 expects str's as codes
        # v0.3+ should fail but doesn't
        efile = load_efile(self.NSfile)
        efile.mod_code(5, 12)
        self.assertEqual(efile.events[5].code, 12)
        efile = load_efile(self.BESAfile)
        efile.mod_code(5, 12)
        self.assertEqual(efile.events[5].code, 12)
        efile.events[4].code = 3
        self.assertEqual(efile.events[4].code, 3)

    def test_save_Neuroscan(self):
        fp = self.resdir + 'NS2_minimal.ev2'
        fp2 = fp.replace('.ev2', '_recoded.ev2')
        efile = load_efile(fp)
        save_efile(efile)
        self.assertTrue(filecmp.cmp(fp, fp2, shallow=False))

    def test_save_NS_efile_with_header(self):
        fp = self.resdir + 'NS2_withheader.ev2'
        fp2 = fp.replace('.ev2', '_recoded.ev2')
        efile = load_efile(fp)
        save_efile(efile)
        efile2 = load_efile(fp2)
        pattern = '[\s]+'
        self.assertEqual(len(efile.raw), len(efile2.raw))
        raw1 = [list(filter(bool, re.split(pattern, l))) for l in efile.raw]
        raw2 = [list(filter(bool, re.split(pattern, l))) for l in efile2.raw]
        self.assertEqual(raw1, raw2)

    def test_save_BESA(self):
        # BESA evt files seem to have spurious whitespace
        fp = self.resdir + 'BESA_minimal.evt'
        fp2 = fp.replace('.evt', '_recoded.evt')
        efile = load_efile(fp)
        save_efile(efile)
        efile2 = load_efile(fp2)
        pattern = '[\s,]+'
        self.assertEqual(len(efile.raw), len(efile2.raw))
        raw1 = [list(filter(bool, re.split(pattern, l))) for l in efile.raw]
        raw2 = [list(filter(bool, re.split(pattern, l))) for l in efile2.raw]
        self.assertEqual(raw1, raw2)

    def test_mod_and_save(self):
        efile = load_efile(self.NSfile)
        efile.events[4].code = 247
        save_efile(efile)
        ef2 = load_efile(self.resdir + 'NS2_recoded.ev2')
        self.assertEqual(ef2.events[4].code, 247)
