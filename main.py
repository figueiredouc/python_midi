from midiutil.MidiFile import MIDIFile
from note import Note
from data_notes import *
from chord import *

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


# note_c0 = Note(DataNote("c",0).pitch(),time=0,duration= 4)
# note_d0 = Note(DataNote("d",0).pitch(),time=0.5,duration= 4)
# note_e0 = Note(DataNote("e",0).pitch(),time=1,duration= 4)

c_major_chod = Chord("c").major()

for note in c_major_chod:
	mf.addNote(track, channel, note.pitch, note.time, note.duration, volume)



# mf.addNote(track, channel, note_c0.pitch, note_c0.time, note_c0.duration, volume)
# mf.addNote(track, channel, note_d0.pitch, note_d0.time, note_d0.duration, volume)
# mf.addNote(track, channel, note_e0.pitch, note_e0.time, note_e0.duration, volume)


# write it to disk
with open("output.mid", 'wb') as outf:
    mf.writeFile(outf)


 
        