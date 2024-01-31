" Maak oefen mee 11 op basis van de uitleg in OneNote. "


getal = input("Geef een getal TUSSEN 1 en 10: ")
if getal.isnumeric():
    getal = int(getal)
else:
  raise ValueError("GEEF EEN GETAL OP")
if getal < 10 and getal > 1:
    uitkomst = getal*2
    print(f"{getal} maal 2 is {uitkomst}")
else:
  raise ValueError("GEEF EEN GETAL TUSSEN 1 EN 10!")




