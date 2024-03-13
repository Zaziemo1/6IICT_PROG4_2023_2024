# Bepaal de som van alle elementen (en sub-elementen) in een (geneste) lijst.
def som_lijst(lijst):
    som = 0
    for index,getal in enumerate(lijst):
        if type(getal) != int:
            som = som + som_lijst(getal)
        else:
            som = som + getal

    return som


print( som_lijst([1,2,3,4]) )           # 10
print( som_lijst([1, [2,3], 4]) )       # 10
print( som_lijst([1,2,[3,[4]]]) )       # 10
print( som_lijst([1, [2, [3, [4]]]]) )  # 10
