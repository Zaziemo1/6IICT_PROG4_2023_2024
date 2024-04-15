""" Oefening 3: (  / 5)

!!! OPGELET: voor deze oefening mag je het internet NIET gebruiken. !!!

Gebruik recursie om een machtsberekening uit te voeren.
Je mag tijdens deze oefening geen gebruik maken van **, pow() of soortgelijke functies.

TIP:
    2^4 = 2 * 2^3 
              2^3 = 2 * 2^2 
                        ... Enzoverder tot waar?

"""
def macht(grondtal,exponent):
    if exponent == 0:
        return 1
    machtsverheffing = macht(grondtal,exponent-1)

    return machtsverheffing * grondtal



print( macht(3,0) ) # 3^0: 1
print( macht(9,0) ) # 9^0: 1
print( macht(2,3) ) # 2^3: 8
print( macht(3,2) ) # 3^2: 9
print( macht(2,8) ) # 2^8: 256
