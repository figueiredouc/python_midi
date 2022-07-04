from midiutil.MidiFile import MIDIFile
from note import Note
from data_notes import *

# create your MIDI object
mf = MIDIFile(1)     # only 1 track
track = 0   # the only track

time = 0    # start at the beginning
mf.addTrackName(track, time, "Sample Track")
mf.addTempo(track, time, 120)

# add some notes
channel = 0
volume = 100

# pitch = 60           # C4 (middle C)
# time = 0            # start on beat 0
# duration = 1         # 1 beat long
# mf.addNote(track, channel, pitch, time, duration, volume)

# pitch = 64           # E4
# time = 0             # start on beat 2
# duration = 1         # 1 beat long
# mf.addNote(track, channel, pitch, time, duration, volume)

# pitch = 67           # G4
# time = 1             # start on beat 4
# duration = 1         # 1 beat long
# mf.addNote(track, channel, pitch, time, duration, volume)


aa =DataNote("c",0)

print(aa.pitch())


# c = Note(DataNote("c",1).pitch,0,1)
# mf.addNote(track, channel, c.pitch, c.time, c.duration, volume)

# # write it to disk
# with open("output.mid", 'wb') as outf:
#     mf.writeFile(outf)

        