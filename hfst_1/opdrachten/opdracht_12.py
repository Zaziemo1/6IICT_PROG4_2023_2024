# Start de opdracht met onderstaande dictionary.
import random
land_hoofdstad = { 
    "belgie": "brussel",
    "frankrijk": "parijs",
    "nederland": "amsterdam",
    "duitsland": "berlijn",
    "engeland": "londen",
}
vragen = 0
count = 0
landen = list(land_hoofdstad.keys())
for land in random.choices(landen,k=3):
    vraag = input(f"Wat is de hoofdstad van {land} ")
    if vraag == land_hoofdstad[land]:
        count = count+1
    vragen = vragen+1
    if vragen == 3:
        break
print(f"Je hebt {count} vragen van de 5 goed")
