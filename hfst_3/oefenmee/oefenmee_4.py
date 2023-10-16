"""
Maak de app na volgens de foto bij oefen mee 3.
Je zal de parameters columnspan & rowspan van .grid() moeten gebruiken.
"""

import tkinter as tk
app = tk.Tk()

label_1 = tk.Label(master=app, text="(0,0)")
label_1.grid(row=0, column=0) # Rij 1, kolom 0

# label_2 = tk.Label(master=app, text= "(1,0)")
# label_2.grid(row=1, column=0) # Rij 3, kolom 0

label_3 = tk.Label(master=app, text= """(2,0)  rowspawn = 2               """)
label_3.grid(row=1, column=0, rowspan=2) # Rij 5, kolom 0

# label_4 = tk.Label(master=app, text="(0,1)")
# label_4.grid(row=0, column=1) # Rij 1, kolom 0

label_5 = tk.Label(master=app, text= "(1,1)")
label_5.grid(row=1, column=1) # Rij 3, kolom 0

label_6 = tk.Label(master=app, text= "(2,1)")
label_6.grid(row=2, column=1) # Rij 5, kolom 0


label_7 = tk.Label(master=app, text="(0,2) columnspawn = 2")
label_7.grid(row=0, column=2, columnspan=2) # Rij 1, kolom 0

label_8 = tk.Label(master=app, text= "(1,2)")
label_8.grid(row=1, column=2) # Rij 3, kolom 0

label_9 = tk.Label(master=app, text= "(2,2)")
label_9.grid(row=2, column=2) # Rij 5, kolom 0

app.mainloop()


app.mainloop()


app.mainloop()
