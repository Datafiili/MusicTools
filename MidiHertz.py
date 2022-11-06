## -------------------- Midi Hertz -------------------- ##
#Written by: Aarni Junkkala

#A4 of midi = 220.Hz
#A4 of the piano is A5 in midi
#That is the reasoning for using (n - 57) instead of (n - 49)
def CalculateHertz(n): #n = number of the midi
    return 2 ** ((n - 69) / 12) * 440

#TODO: other way around, where code returns the note that is closest to hertz

print(CalculateHertz(45))