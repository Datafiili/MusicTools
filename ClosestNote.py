## -------------------- Closest Note -------------------- ##
#Written by: Aarni Junkkala

import MidiToNote as MTN
#Returns the midi number of the note that is closest to targetpos
def findClosestNote(noteName, targetpos):
    #Test the target
    if float(int(targetpos)) == float(targetpos): #Checks if target position is integer
        #if note is already in the position, then returns the target position
        if MTN.MidiToNote(targetpos) == noteName:
            return targetpos
    
    #Looks for closest above
    num = targetpos
    if float(int(targetpos)) != float(targetpos):
        num = int(targetpos)
    above = num
    
    while True:
        if MTN.MidiToNote(num) == noteName:
            above = num
            break
        num += 1
        
    below = num
    num = targetpos
    while True:
        if MTN.MidiToNote(num) == noteName:
            below = num
            break
        num -= 1
    
    #Looks witch one is closer and returns that
    if abs(below - targetpos) < abs(above - targetpos):
        return below
    else:
        return above
    
if __name__ == '__main__':
    print(findClosestNote("e",60))