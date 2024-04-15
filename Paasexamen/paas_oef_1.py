""" OEFENING 1: (  / 5)

!!! OPGELET: Het eenvoudigst is om de code niveau-per-niveau op te lossen.               !!!
!!!          Ben je klaar met een niveau, neem de code dan mee naar het volgende niveau. !!!

Onderstaande code gebruikt een API om 2 willekeurige getallen (0-5) te genereren.
Vervolgens wordt het eerste door het tweede getal gedeeld.

De code staat in een while-loop. 
De persoon geeft iedere loop aan of deze nog een breuk wilt (y)
of de loop wilt stoppen (n).
"""

import requests

class VijfError(Exception):
    pass


nog_eens = ""
while True:
    try:
        if nog_eens == "n":
            break
        API = "http://www.randomnumberapi.com/api/v1.0/random?min=0&max=6&count=2" # Genereer twee getallen tussen 0 & 5.
        getallen = requests.get(API, timeout=3).json()
        getal_1, getal_2 = getallen[0], getallen[1]
        if getal_1 != 5 and getal_2 != 5:
            print(f"{getal_1} / {getal_2} = {getal_1/getal_2}")
        else:
            raise VijfError("5 is geen mooi getal!")
    except ZeroDivisionError:
        print("Kan niet delen door nul!")
    except requests.exceptions.ConnectionError:
        print("Geen verbinding met de API!")
    finally:
        nog_eens = input("Nog een breuk genereren (y/n): ")



""" NIVEAU 1: (  / 2)
Iedere loop kunnen er 2 fouten ontstaan (zoek welke specifieke Exceptions dit zijn).
 1) Delen door 0.
 2) Geen verbinding met de API. (Tip! Zet de wifi af, en voer hierna het script uit)

Vang bovenstaande twee fouten op, en leg via print uit wat er exact mis ging. 
Doe dit door op volgende wijze een try-except toe te voegen in de while-loop:
 while True:
    try:
        *CODE DIE MOMENTEEL IN DE WHILE_LOOP STAAT*
    except ...:

VOORBEELD:
 1 / 3 = 0.33
 Nog een breuk genereren (y/n)? y
 Kan niet delen door 0!
 Kan geen verbinding maken met de API!
 2/2 = 1
 Nog een breuk genereren (y/n)? n
"""



""" NIVEAU 2: (  / 2)
Indien er iets fout gaat in Niveau 1, 
wordt de gebruiker niet gevraagd of deze nog een breuk wilt.

Zorg ervoor dat volgende regel ALTIJD uitgevoerd wordt (dus ook als een Exception is opgetreden):
 nog_eens = input("Nog een breuk genereren (y/n): ")

VOORBEELD:
 Kan niet delen door 0!
 Nog een breuk genereren (y/n)? y
 Kan geen verbinding maken met de API!
 Nog een breuk genereren (y/n)? y
 2/2 = 1
 Nog een breuk genereren (y/n)? n
"""



""" NIVEAU 3: (  / 1)
Maak een CustomException aan.
Deze moet geraised worden wanneer getal_1 OF getal_2 gelijk is aan 5.
Kies zelf hoe je deze exception noemt, en welke boodschap erbij hoort.

Vang deze fout niet op. Laat het programma in dit geval dus gewoon crashen.

VOORBEELD:
 1 / 3 = 0.33
 Nog een breuk genereren (y/n)? y
 2 / 4 = 0.5
 Nog een breuk genereren (y/n)? y
 5 / 2 = 2.5
 *Python crasht* RandomFiveError: ik vind vijf geen mooi getal!
"""
