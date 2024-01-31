" Maak oefen mee 14 op basis van de uitleg in OneNote. "
def deel():
    x = input("Geef een getal op: ")
    y = input("Geef een getal op: ")
    if type(x) == int and type(y) == int:
        x = int(x)
    else:
        raise ValueError("Integer geven ipv strings")
    
    if x > y:
        raise 
    
    if y != 0 and x != 0 and y > 0 and x > 0:
        return x/y
    else: 
        raise ZeroDivisionError("Je deelt met nul en je bent een snul!")




    