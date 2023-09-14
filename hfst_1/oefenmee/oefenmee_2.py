# Start de oefen mee met onderstaande dictionary.
fruitmand = { # Sleutel is fruit, waarde is aantal
    "appel": 5,
    "banaan": 3,
    "kers": 50
}
#niveau 1
fruit = "appel"
print(fruitmand[fruit])

#niveau 2
fruit = "mango"
nieuw_fruit  = "mango"
nieuw_aantal = 1
fruitmand[nieuw_fruit] = nieuw_aantal
print(fruitmand[fruit])
#niveau 3
fruit = "banaan"
nieuw_aantal = 8
fruitmand["banaan"] = nieuw_aantal
print(fruitmand['banaan'])

#niveau 4
terugleggen_fruit = "kers"
fruitmand.pop(terugleggen_fruit)
print(fruitmand)