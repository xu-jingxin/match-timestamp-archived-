import unittest

from music21 import note, stream
from venv.src.matcher import *

#create streams
note_list = [note.Note('C'), note.Note('D'), note.Note('E-'), note.Note('F')]
mxl_stream = stream.Stream(note_list)
mxl_stream.show('text')

note_list = [note.Note('C'), note.Note('D'), note.Note('E-'), note.Note('F')]
midi_stream = stream.Stream(note_list)

t = 0
for note in midi_stream:
    note.offset = t + 0.5

midi_stream.show('text')


class MatcherTest(unittest.TestCase):
    def test_match_equal(self):
        self.assertTrue(isMatched(mxl_stream, midi_stream))


#Template
class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)  # add assertion here


if __name__ == '__main__':
    unittest.main()
