# Bepaal de faculteit van een getal met behulp van een while-loop.

def facul(getal):
    teller = 1
    while True:
        if getal == 0 :
            break
        teller = teller * getal
        getal = getal - 1

        
    return teller

    
    


        



print( facul(1) ) # 1
print( facul(2) ) # 2
print( facul(3) ) # 6
print( facul(4) ) # 24
print( facul(5) ) # 120