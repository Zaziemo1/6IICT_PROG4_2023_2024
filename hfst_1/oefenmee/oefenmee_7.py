# Start de oefen mee met onderstaande dictionary.
gasten = { # Sleutel is naam, waarde is job.
    "Lebron":     "Basketballer",
    "Mike oxlong":    "acteur",
    "Floydgaming":   "gamer",
    "Ahmed ibn abdelaziz batata ou rizo m3ah tajine ou dwaz fill bebsi shwarma": "piloot"
}

gast = ""

while gast != "STOP":
    gast = input("Wie komt er binnen? ")
    if gast in gasten:
        print(f"Welkom {gasten[gast]} {gast}. Kom binnen!")
    else:
        if gast == "STOP":
            break
        print("Je staat niet op de lijst! Wegwezen!!")
    
