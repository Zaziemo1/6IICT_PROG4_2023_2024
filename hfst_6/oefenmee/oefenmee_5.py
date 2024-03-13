# Niveau 1: bepaal sommatie vagetal eegetal getal recursief.
def sommatie(getal):
    if getal == 1:
        return 1
    
    vorige_sommato = sommatie( getal-1 )
    return  getal + vorige_sommato



    




# Niveau 2: bepaal sommatie vagetal eegetal getal met while-loop.
# def sommatie(getal):
#     print("-------------------------")
#     teller = 0
#     while True:
#         if getal == 0 :
#             break
#         teller = teller + getal
#         getal = getal - 1

        
#     return teller


print( sommatie(1) )   # 1
print( sommatie(2) )   # 3
print( sommatie(3) )   # 6
print( sommatie(4) )   # 10
print( sommatie(5) )   # 15
print( sommatie(100) ) # 5050
