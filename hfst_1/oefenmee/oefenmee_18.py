# Maak voor deze oefen mee gebruik van onderstaande lijst van dictionaries.
film_reviews = [
    {'Matrix': 9.2, 'Avatar': 8.8, 'Fury': 9.0, 'Skyfall': 8.1},
    {'Matrix': 3.5, 'Avatar': 1, 'Fury': 8, 'Skyfall': 4},
    {'Matrix': 10, 'Avatar': 3, 'Fury': 7, 'Skyfall': 5}
]

persoon = 0
for review in film_reviews:
    teller = 0
    persoon = persoon + 1
    print(f"Persoon {persoon} gaf:")
    for film in review:
        print(f"    {film} een {review[film]} op 10")
        teller = teller + review[film]
    teller = teller /4
    print(f"Persoon {persoon} heeft de films een gemiddelde score van {teller} op 10 gegeven")
    


    

    
        
        