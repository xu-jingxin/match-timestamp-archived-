
def isMatched(first, second):
    for i in range(len(first)):
        if first[i] == second[i]:
            continue
        else:
            return False
    return True

def match(mxl_stream, midi_stream):
    #len(mxl_stream.notes) == len(midi_stream.notes)
    pass