try:
    getal = int( input("Geef een getal in: ") )
    deling_10 = 10/getal
except:
    print(f"Het getal 0 kan je niet gebruiken als deler.")
    getal = 1
    deling_10 = 10
    
print(f"10 gedeeld door {getal} is gelijk aan {deling_10}")
print("Programma is klaar")
