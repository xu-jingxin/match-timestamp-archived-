from typing import Union

from music21 import *
from music21.stream import Score, Part, Opus


def midi_load(midi_path):
    midi_stream: Union[Score, Part, Opus] = converter.parse(midi_path)
    return midi_stream.flatten()

def mxl_load(mxl_path):
    mxl_stream = converter.parse(mxl_path)
    return mxl_stream.flatten()
