import unittest

import music21.stream

from venv.src.loaders import *


class LoadersTest(unittest.TestCase):
    def test_mxl_load(self):
        mxl = mxl_load('/home/xujingxin07/IdeaProjects/NOODLE/Sample_files/Bach_WTC.mxl')
        self.assertIsInstance(
            mxl, music21.stream.Stream)
        self.assertTrue(mxl.isFlat)
        # add assertion here
        mxl.show('text')


    def test_midi_load(self):
        midi = midi_load('/home/xujingxin07/IdeaProjects/NOODLE/Sample_files/Bach_WTC.mid')
        self.assertIsInstance(midi, music21.stream.Stream)
        self.assertTrue(midi.isFlat)
        # midi.show('text')


class MyTestClass(unittest.TestCase):
    def test(self):
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
