## -------------------- Scale -------------------- ##
#Written by: Aarni Junkkala

import MidiToNote as MTN

class Scale:
    def __init__(self, names, distances):
        self.names = names
        self.distances = distances
    
Scales = [
    #Chromatic (12 notes)
    Scale(["Chromatic","Dodecatonic"],[0,1,2,3,4,5,6,7,8,9,10,11]),
    #Nonatonic (9 notes)
    Scale(["Nonatonic blues", "Nonatonic blues scale", "nine-note blues scale", "nine-note blues", "nine note blues scale", "nine note blues"], [0,2,3,4,5,7,9,10,11]),

    #Heptatonic (7 notes)
    Scale(["Major"],[0,2,4,5,7,9,11]),
    Scale(["Minor"],[0,2,3,5,7,8,10]),
    Scale(["Heptatonic blues", "Heptatonic blues scale", "seven-note blues scale", "seven-note blues", "seven note blues scale", "seven note blues"], [0,2,3,5,6,9,10]),

    #Hexatonic (6 notes)
        #blues
    Scale(["Hexatonic blues", "Hexatonic blues scale", "six-note blues scale", "six-note blues", "six note blues scale", "six note blues"], [0,3,5,6,7,10]),
    Scale(["Hexatonic blues minor", "Hexatonic blues minor scale", "six-note blues minor scale", "six-note blues minor", "six note blues minor scale", "six note blues minor"],[0,2,3,4,7,10]),
    ]

#Returns the list of midi for the scale
def GetMidiOfScale(RootNote, ScaleName): #Returns a list that includes all the notes on the scale
    CorrectScale = None
    #Finds the scale based on the name.
    for i in range(len(Scales)):
        if CorrectScale != None:
            break
        for k in range(len(Scales[i].names)):
            if Scales[i].names[k].lower() == ScaleName.lower():
                CorrectScale = Scales[i]
                break
    
    #Copying all the notes to new list
    NoteDifference = []
    for i in range(len(CorrectScale.distances)):
        NoteDifference.append(CorrectScale.distances[i])
    
    #Modulus of 12 to lower the notes to be octave zero
    for i in range(len(NoteDifference)):
        NoteDifference[i] %= 12
    
    
    for i in range(1,11):
        for k in range(len(CorrectScale.distances)):
            NoteDifference.append(NoteDifference[k] + (12 * i))
    
    return NoteDifference

#Returns the notes of the scale
def GetNotesOfScale(RootNote, ScaleName): #Returns a list that includes all the notes on the scale    
    #Get's the midi of the rootnote
    RootMidi = MTN.NoteToMidiOctave(RootNote.lower(),0)
    
    CorrectScale = None
    #Finds the scale based on the name.
    for i in range(len(Scales)):
        if CorrectScale != None:
            break
        for k in range(len(Scales[i].names)):
            if Scales[i].names[k].lower() == ScaleName.lower():
                CorrectScale = Scales[i]
                break
    
    #Copying all the notes to new list
    NoteDifference = []
    for i in range(len(CorrectScale.distances)):
        NoteDifference.append(CorrectScale.distances[i])
    
    NoteNames = []
    for i in range(len(NoteDifference)):
        NoteNames.append(MTN.MidiToNote(RootMidi + NoteDifference[i]))
    
    return NoteNames

if __name__ == '__main__':
    print(GetMidiOfScale("a", "minor"))
    print(GetNotesOfScale("d", "major"))