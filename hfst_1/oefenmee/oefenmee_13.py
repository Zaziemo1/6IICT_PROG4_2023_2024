# Start de oefen mee met onderstaande dictionary.
fruitmand = { # Sleutel is fruit, waarde is aantal
    "appels": 2,
    "bananen": 3,
    "kersen": 10,
    "mango's": 1
}

while True:
    for fruit in fruitmand:
        kopen = int(input(f"Hoeveel {fruit} bijkopen (huidig aantal is {fruitmand[fruit]}): "))
        fruitmand[fruit] = fruitmand[fruit] + kopen
    print(f"in de fruitmand zit momenteel: {fruitmand}")
    vraag = input("Wil je nog meer bijkopen? nee of ja? ")
    if vraag.lower() == "nee":
        break