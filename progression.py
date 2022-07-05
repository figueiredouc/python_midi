from chord import *
class Progression(object):
    """docstring for note"""

    def __init__(self, root):
        self.root = root #note

    def p1(self):

        data = {"a": 69,"b": 71,"c": 60,"d": 62,"e": 64,"f": 65,"g": 67}
        rules = [[0,1],[5,0],[3,1],[4,1]]
        time = [1,2,3,4]
        progression = []
        root_pitch =  data[self.root]
        i = 0

        for chord in rules:
            if (chord[1]==0):
                progression.append(Chord(self.root,time = time[i]).major())
            else:
                progression.append(Chord("c",time = time[i]).minor())
            i = i+1
        return progression


        


        
