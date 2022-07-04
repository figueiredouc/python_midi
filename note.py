class Note(object):
    """docstring for note"""
    def __init__(self, pitch, time=0, duration=1):
        self.pitch = pitch #note
        self.time = time #start at beat
        self.duration=duration #duration in beats
        
