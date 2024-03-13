# Bepaal recursief of een woord een palindroom is.
def palindroom(woord):
    previouswoord = woord
    if len(woord) == 1:
        return woord
    letter = woord[-1]
    woord = woord[0:-1]
    woord = palindroom(woord)[0]
    palin = letter + woord
    if palin == previouswoord:
        return palin, True
    else:
        return palin, False



print( palindroom("lepel")[1] ) # True
print( palindroom("mes")[1]   ) # False
print( palindroom("otto")[1]  ) # True
print( palindroom("auto")[1]  ) # False
