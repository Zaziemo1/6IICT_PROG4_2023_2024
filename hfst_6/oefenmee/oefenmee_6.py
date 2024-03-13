# Draai een woord om.
def draaiom(woord):
    if len(woord) == 1:
        return woord
    letter = woord[-1]
    woord = woord[0:-1]
    woord = draaiom(woord)
    return letter + woord
    




print( draaiom("Hallo") )       # ollaH
print( draaiom("Dag") )         # gaD
print( draaiom("f"))            # f
print( draaiom("Iedereen") )    # neeredeI

