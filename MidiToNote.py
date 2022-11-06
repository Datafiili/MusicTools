## -------------------- Midi to note -------------------- ##
#Written by: Aarni Junkkala

#Converts midi number into note name and vice versa
#Mini numbers go in logical order, where 0 = C, 1 = C# and so on.
noteList = ["c", "c#", "d", "d#", "e", "f", "f#", "g", "g#", "a", "a#", "b"] #Nots also have flat names, but they aren't implemented here (yet)

#returns the name of the note.
def MidiToNote(n): #n = number
    return noteList[n % 12]

#Shows octave as same way that DAWs usually show them.
def MidiToNoteOctave(n): #n = number
    return noteList[n % 12] + str(int(n / 12))

#Puts the midi to 4th octave (C4) as it has the middle C .
def NoteToMidi(n): #n = note
    n = n.lower()
    return noteList.index(n) + 60

#Puts the midi to octave of your choice.
def NoteToMidiOctave(n,o): #o = octave
    n = n.lower()
    return (noteList.index(n) + (12 * o))

if __name__ == '__main__':
    print(MidiToNote(60)) #c
    print(MidiToNoteOctave(60)) #c5
    print(NoteToMidi("C")) #60
    print(NoteToMidiOctave("A",5)) #69