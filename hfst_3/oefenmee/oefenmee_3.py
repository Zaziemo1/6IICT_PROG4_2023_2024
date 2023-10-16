"""
Maak de app na volgens de foto bij oefen mee 3.
Je hebt maar 3 labels nodig om deze app te maken.
"""

import tkinter as tk
app = tk.Tk()

label_1 = tk.Label(master=app, text="Hallo")
label_1.grid(row=1, column=0) # Rij 1, kolom 0

label_3 = tk.Label(master=app, text= "klas")
label_3.grid(row=1, column=2) # Rij 3, kolom 0

label_5 = tk.Label(master=app, text= "6IICT")
label_5.grid(row=2, column=2) # Rij 5, kolom 0

app.mainloop()
