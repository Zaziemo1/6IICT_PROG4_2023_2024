"""
Onderstaande code plaats een label, telkens als op de knop wordt geduwd.
Pas de code aan volgens de instructies bij oefen mee 7.
"""

import tkinter as tk
app = tk.Tk()

# Functie maakt & plaatst een label.
def maak_label():
    button = tk.Button(master=app, text="Click for free virus!",command=maak_label)
    button.pack()

# 1) Knop aanmaken.
    # master: geef aan tot welke GUI de knop behoort.
    # text: boodschap van de knop.
    # command: aan welke functie is de knop gelinkt.
knop = tk.Button(master=app, text="FREE VBUCKS", command=maak_label)

# 2) Knop plaatsen.
knop.pack()

app.mainloop()
