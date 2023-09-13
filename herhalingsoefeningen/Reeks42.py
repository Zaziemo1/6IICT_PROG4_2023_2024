""" Maak een calorie-tracker. 

 

 Vraag de gebruiker hoeveel calorieën deze 

 vandaag verbrand heeft. Voeg deze waarde 

 toe aan een lijst. 

 

 Print vervolgens (op basis van de lijst): 

- Hoeveel dagen de gebruiker de app gebruikt. 
 - totaal verbrande calorieën. 

 

Na deze print is het de volgende dag. 

 Vraag opnieuw naar het aantal verbrande calorieën 

    & print vervolgens bovenstaande info. 
 

    Dit proces stopt als de gebruiker -1 ingeeft. 

 

 >>> (Dag 1) Hoeveel calorieën verbrand: 1800 

 Op 1 dag(en) heb je 1800kCal verbrand. 

 >>> (Dag 2) Hoeveel calorieën verbrand: 3000 

 Op 2 dag(en) heb je 4800kCal verbrand. 

 >>> (Dag 3) Hoeveel calorieën verbrand: -1 

""" 
def calorientracker():
  calorie = 0
  
  totaal = 0
  dag = 1
  while calorie >=0:
   calorie = int(input("Hoeveel calorien verbrand?    "))
   totaal = totaal + calorie
   if calorie <0:
     break
   print(f"Op {dag} dag(en) heb je {totaal} Cal verbrand.")
   dag=dag+1

calorientracker()




