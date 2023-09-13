def voeg__toe(telefoonboek, naam, nummer): 
 sublijst = []
 sublijst.append(naam)
 sublijst.append(nummer)
 telefoonboek.append(sublijst)v
 "return het boek, met naam & nummer erbij"
 return telefoonboek



 

telefoonboek = [ 

 ["Jan Janssen", "+32 470 998301"], 

 ["Piet Joris", "+32 483 313220"], 

 ["Kor Neel", "+32 453 231456"], 

 ["Piet Dirkx", "+31 269 542463"] 

] 

 

telefoonboek = voeg__toe(telefoonboek, "Jos", 123) 

# [ 

#     ["Jan Janssen", "+32 470 998301"], 

#     ["Piet Joris", "+32 483 313220"], 

#     ["Kor Neel", "+32 453 231456"], 

#     ["Piet Dirkx", "+31 269 542463"], 

#     ["Jos", 123] 

# ] 

print(telefoonboek) 