# Maak voor deze oefen mee gebruik van onderstaande dictionary-structuur.
inception_film = {
    'jaar': 2010,
    'genre': ['Actie', 'Sciencefiction', 'Thriller'],
    'cast': [ 
        {'acteur': 'Leonardo DiCaprio', 'rol': 'Cobb'},
        {'acteur': 'Joseph Gordon-Levitt', 'rol': 'Arthur'},
        {'acteur': 'Ellen Page', 'rol': 'Ariadne'}
    ],
    'locaties': ['Parijs', 'Los Angeles', 'Tokio'],
    'box_office': {'budget': 160000000, 'opbrengst': 829895144},
    'awards': {'Oscars': 0, 'Golden Globes': 4}
}
print(inception_film['jaar'])
print(inception_film['genre'][1])
print(inception_film['box_office']["opbrengst"])
print(inception_film['cast'][0]["rol"])

inception_film['awards']["Oscars"] = 4
inception_film["regiseur"] = "Christopher Nolan"
inception_film["cast"][2]["acteur"] =  'Tom Hardy'
inception_film["cast"][2]["rol"] =  'Eames'
print(inception_film)
