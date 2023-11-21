"""
Volg de instructies van oefen mee 12.
In deel 1 van de oefen mee maak je het uiterlijk van een rekenmachine.
In deel 2 zal je deze ook echt laten werken.

    Tip! Je kan instellingen van widgets ook inladen via een dictionary.
         Op deze manier kan je veel gelijkaardige widgets snel opstellen en aanpassen.
         Er is een voorbeeld onderaan de oefen mee voorzien.
"""

import tkinter as tk
venster = tk.Tk()
veld = tk.Entry(master=venster,highlightbackground='green')
veld.grid(row=0, column=0)
operator = ""

def number1():
    
    veld.insert(0,1)

def number2():
    
    veld.insert(0,2)

def number3():
    
    veld.insert(0,3)

def number4():
    
    veld.insert(0,4)

def number5():
    
    veld.insert(0,5)

def number6():
    
    veld.insert(0,6)

def number7():
    
    veld.insert(0,7)

def number8():
    
    veld.insert(0,8)

def number9():
    
    veld.insert(0,9)

def clear():
    veld.delete(0,"end")

def equal():
    regel = veld.get()
    index = regel.find(operator)
    
    getal2 = regel[0:index]
    getal1 = regel[index+1:]
    print(getal1)
    print(getal2)
        
    
    if operator == "+":
        
      resultaat = int(getal2)+int(getal1)
    if operator == "-":
        resultaat = int(getal2)-int(getal1)
    if operator == "*":
        resultaat = int(getal2)*int(getal1)
    if operator == "/":
        resultaat = int(getal2)/int(getal1)
      

      
    label = tk.Label(master=venster,text= resultaat)
    label.grid(row=1,column=0)

def plus():
    global operator
    veld.insert(0,"+")
    operator = "+"


def minus():
    global operator
    veld.insert(0,"-")
    operator = "-"

def multipocation():
    global operator
    veld.insert(0,"*")
    operator = "*"

def delen():
    global operator
    veld.insert(0,"/")
    operator = "/"








settings = {
    "master": venster, "padx": 60, "pady": 10,
    "highlightthickness": 2,"highlightbackground": "black"
}

button1 = tk.Button(**settings, text="1", command=number1)
button1.grid(row=1, column=1)
button2 = tk.Button(**settings, text="2", command=number2)
button2.grid(row=1,column=2)
button3 = tk.Button(**settings, text="3", command=number3)
button3.grid(row=1, column=3)
button4 = tk.Button(**settings, text="4", command=number4)
button4.grid(row=2,column=1)
button5 = tk.Button(**settings, text="5", command=number5)
button5.grid(row=2, column=2)
button6 = tk.Button(**settings, text="6", command=number6)
button6.grid(row=2,column=3)
button7 = tk.Button(**settings, text="7", command=number7)
button7.grid(row=3, column=1)
button8 = tk.Button(**settings, text="8", command=number8)
button8.grid(row=3,column=2)
button9 = tk.Button(**settings, text="9", command=number9)
button9.grid(row=3, column=3)
buttonclear = tk.Button(**settings, font=("Calibri", 20), text= "clear",command=clear)
buttonclear.grid(row=4,column=2, columnspan=2, pady=5)


buttonplus = tk.Button(**settings, text="+", command=plus)
buttonplus.grid(row=0, column=4)
buttonmin = tk.Button(**settings, text="-", command=minus)
buttonmin.grid(row=1,column=4)
buttondelen = tk.Button(**settings, text="/", command=delen)
buttondelen.grid(row=2, column=4)
buttonmaal = tk.Button(**settings, text="*", command=multipocation)
buttonmaal.grid(row=3,column=4)
buttonequal = tk.Button(**settings, text="=", command=equal)
buttonequal.grid(row=4,column=4)






venster.mainloop()


