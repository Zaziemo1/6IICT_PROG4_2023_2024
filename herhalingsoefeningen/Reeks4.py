""" Maak het spel galgje na. 

 

Gebruik hiervoor een willekeurig woord uit  

onderstaande lijst (uitbreiden mag). 

 

Vraag de gebruiker naar een letter of 

om het woord te raden. Het spel stopt 

als het woord correct is of na 7 vragen. 

 

Print in het eerste geval "gewonnen!". 

In het tweede geval "verloren!".  

 

Tip! stel een lijst op met erin de 

gevonden letters. Vul deze eerst 

volledig met _ . Als de gebruiker een  
             letter geeft die in het woord zit,  
             vervang de overeenkomstige _ door deze  
             letter. 

 

>>> Gok letter / Raad woord (1/7): a 

Woord: _ _ _ _ 

>>> Gok letter / Raad woord (2/7): e 

Woord: e _ e _ 

>>> Gok letter / Raad woord (3/7): t 

Woord: e _ e _ 

>>> Gok letter / Raad woord (4/7): v 

Woord:e v e _ 

>>> Gok letter / Raad woord (5/7): even 

gewonnen! 

""" 


import random 

woorden = ["bxnn", "even", "stuk", "volk"] 
kansen = 7
kans = 0
lijst = ["_","_","_", "_"]
woord = random.choice(woorden)
while kans != kansen:

    print(lijst)
    print(f"{kans}/7")
    gekozenletter = input("Gok letter   ")
    
    kans=kans+1
    
    for index,letter in enumerate(woord):
        if gekozenletter == letter:
            lijst[index]= letter
        

    if "_" not in lijst:
        print(lijst)
        print("Gewonnen")
        break

if "_" in lijst:
 if kans == kansen:
    print("Helaas u heeft verloren")
    
        
    
        
        

    
    
    

