""" Oefening 5 (  / 6 )
Maak onderstaande boekenwinkel-app verder af.
Het menu is reeds gemaakt. Jij zal de opties in dit menu verder uitwerken.

Er zijn 3 opties waaruit de bediende kan kiezen.
Alle opties maken gebruik van de dictionary catalogus.
    1) Toon details van boek.
    2) Voeg boek toe (aan dictionary catalogus).
    3) Geef overzicht van catalogus.

"""

catalogus = { # De start-catalogus van de boekenwinkel.
    'The Foundation': {'auteur': 'Asimov', 'datum': '1951'},
    '2001: A Space Odyssey': {'auteur': 'Clarke', 'datum': '1968'},
    'Rocketship Galileo': {'auteur': 'Heinlein', 'datum': '1947'},
}

while True: # Start de app.
    # Overzicht keuzemenu
    print("Menu: ")
    print("  1) Toon details van boek.")
    print("  2) Voeg boek toe.")
    print("  3) Toon catalogus.")
    print("  4) Stop de app.")

    # Kies een van de 4 opties.
    optie = input("Selecteer wat je wilt doen: ")

    if optie == "1":   # Toon details van opgevraagd boek.
        """ 1) Toon details van boek.
        Vraag de gebruiker naar de titel van een boek.
        

        Komt het boek voor in de dictionary catalogus, print dan alle informatie als volgt.
            >>> Het boek *titel* is geschreven door *auteur* en gepubliceerd in *datum*.

        Als het boek niet voorkomt in de dictionary catalogus, print dan het volgende.
            >>> Kan boek *titel* niet vinden.
        """
        titel = input("Hoe heet het boek?    ")
        if titel in catalogus:
            print(f"het boek {titel} is geschreven door {catalogus[titel]['auteur']} en gepubliceerd in {catalogus[titel]['datum']}")
        else:
            print(f"Kan boek {titel} niet vinden!")


    elif optie == "2": # Voeg boek toe aan de dictionary catalogus.
        """ 2) Voeg boek toe.
        Vraag de gebruiker om een *titel*, *auteur* & *publicatiedatum*.
        Voeg vervolgens een nieuw element toe aan de dictionary catalogus. Dit element 
        heeft als sleutel de *titel*, de waarde is een sub-dict met de overige info.

        Het element ziet er dus in het algemeen als volgt uit.
            *titel*: {'auteur': *auteur*, 'datum': *publicatiedatum*}
        Een specifiek voorbeeld is.
            'The Foundation': {'auteur': 'Asimov', 'datum': '1951'}

        Het is toegelaten om een titel die reeds bestaat in de catalogus te overschrijven.
        """
        boek = input("Hoe heet uw boek?    ")
        auteur = input("Wie heeft uw boek geschreven?      ")
        datum = input("Wanneer is deze gepubliceerd?     ")
        catalogus[boek] = {'auteur':auteur, 'datum': datum}
        

    elif optie == "3":
        """ 3) Geef overzicht van catalogus.
        Print ieder boek (met auteur) dat zich in de dictionary catalogus bevindt.
        De print moet als volgt eruitzien.
            >>> Volgende boeken staan momenteel in de catalogus:
            >>>     - The Foundation (Asimov)
            >>>     - 2001: A Space Odyssey (Clarke)
            >>>     - Rocketship Galileo (Heinlein)
            >>>     - enzoverder voor ieder ander boek in de catalogus...
        """
        print("De volgende boeken staan in de catalogus:    ")
        for book in catalogus:
            print("-",book,"(",catalogus[book]['auteur'],")")

    elif optie == "4": # Stop de app.
        print(f"\nBedankt voor het gebruiken van deze app.")
        break

    else: # Verkeerde input gegeven.
        print(f"\nDit is geen optie. Gelieve opnieuw te proberen.")

