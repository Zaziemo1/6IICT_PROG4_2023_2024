""" 
Maak een app aan die 3 labels bevat.
De inhoud van de 3 labels is:
    - Label 1: hallo
    - Label 2: klas
    - Label 3: 6iict
"""
import tkinter as tk
app = tk.Tk()

# Eerste label
label_1 = tk.Label(master=app, text="Label 1: hallo")
label_1.grid(row=0,column=0)

# Tweede label
label_2 = tk.Label(master=app, text="Label 2: klas")
label_2.grid(row=1,column=0)

# Derde label
label_3 = tk.Label(master=app, text="Label 3: 6iict")
label_3.grid(row=2,column=0)

app.mainloop()
