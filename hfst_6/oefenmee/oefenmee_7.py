# Tel alle cijfers in een getal op.
def optellen(getallen):
    getallen = str(getallen)
    if len(getallen) == 1:
        return getallen
    getal = int(getallen[-1])
    getallen = getallen[0:-1]
    getallen = int(optellen(getallen))
    return getal + getallen

print( optellen(12345) )            # 15
print( optellen(5) )                # 5
print( optellen(4687612962034330) ) # 64
print( optellen(6728003096702784) ) # 69