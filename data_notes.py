class DataNote(object):
    temp = 60

    """docstring for note"""
    def __init__(self, note, octave):
        self.note = note #note
        self.octave = octave #start at beat
        
    def pitch(self):

        data = {
            "a": 69,
            "b": 71,
            "c": 60,
            "d": 62,
            "e": 64,
            "f": 65,
            "g": 67,
        }
        return data[self.note] + (self.octave*12)
