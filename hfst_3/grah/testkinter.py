import tkinter as tk
import random

app = tk.Tk()
counter = 0
def lebron_james():
    global counter
    counter = counter + random.randint(0,999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999)
    label = tk.Label(master=app,text=counter)
    label.pack()



button = tk.Button(master=app,text="CLICK NOW FOR FREE VIRUS" , command=lebron_james)
button.grid(row=1,column=0)
button.pack()


app.mainloop()