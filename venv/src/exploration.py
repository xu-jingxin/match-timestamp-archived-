from music21 import *
from venv.tests.test_matcher import midi_stream, mxl_stream

print(midi_stream == mxl_stream)  # False; streams with same note but different offsets not equal

n1 = note.Note('C#')
n2 = note.Note('D-')
print(n1)
print(n2)
print(n1 == n2)  # False; enharmonic not evaluated as equal



