"""
Volg de instructies van oefen mee 8.
Je zal een simpel rekenmachine maken met behulp van 2 Entries, 1 label & 1 button.
    
    Tip! De methode .get() van entries geeft altijd een string.
         Je kan hier natuurlijk niet mee rekenen.
"""
import tkinter as tk
app = tk.Tk()
def delete():
    global veld
    global veld2
    veld.delete(0,"end") # Hiermee verwijder je alles in het entryveld
    veld2.delete(0,"end") 

def bereken():
    global veld
    global veld2
    
    getal1=veld.get()
    getal2=veld2.get()

    if not getal1.isnumeric():
        return
    if not getal1.isnumeric():
        return
    resultaat=(int(getal1)+int(getal2))
    label = tk.Label(master=app, text=resultaat)
    label.pack()

    
# 1) Inputveld aanmaken.
    # master: geef aan tot welke GUI het inputveld behoort.

button = tk.Button(master=app, text="Clear",command=delete)
button2 = tk.Button(master=app, text="Calculate",command=bereken)
veld = tk.Entry(master=app)
veld2 = tk.Entry(master=app)
veld.get()
veld2.get()
# 2) Inputveld plaatsen
veld.pack()
veld2.pack()
button.pack()
button2.pack()


app.mainloop()
