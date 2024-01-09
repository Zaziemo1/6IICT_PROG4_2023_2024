try:   
    fruit_lijst = ["Appel", "Banaan", "Meloen", "Mango", "Druif"]
    getal = int( input("Hoeveel fruit uit de lijst wil je printen: ") )
    
    getal = 5


    for i in range(getal):
        fruit = fruit_lijst[i]
        print(fruit)
except ValueError:
    print("Gelieve een nummer in geven!")
except IndexError:
     print("De fruitmand is nu leeg!")



