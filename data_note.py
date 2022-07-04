class DataNote(object):

    data = {
        "a": 69,
        "b": 71,
        "c": 60,
        "d": 62,
        "e": 64,
        "f": 65,
        "g": 67,
    }
    """docstring for note"""
    def __init__(self, note, octave=0):
        self.pitch = data[note] * (12*octave) #note
        self.octave = time #octave
        
