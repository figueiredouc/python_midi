from note import Note
from data_notes import *
class Chord(object):
    """docstring for chord"""
    def __init__(self, root,time= 0):
        self.root = root #root note
        self.data = {"major": [0,4,7]}
        self.time = time


    def major(self):
        rule = [0,4,7]
        chord = []
        for step in rule:
            chord.append(Note(DataNote(self.root,0).pitch() + step,time = self.time))
        return chord



