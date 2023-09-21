# Start de opdracht met onderstaande code.
deelnemers = ["Lucas", "Emma", "Jan", "Piet", "Maud"]

deelnemers_talen = {    
    "Lucas": "python",    
    "Piet": "assembly",    
    "Maud": "ruby"
}
while True:
    for deelnemer in deelnemers:
       if deelnemer not in deelnemers_talen:
          print(f"{deelnemer} moet de lijst nog invullen doe dat NU!")
          favourite_talen = input("Wat is uw favourite taal? ")
          deelnemers_talen[deelnemer] = favourite_talen
       else:
          print(f"Hallo {deelnemer}, Dank u wel voor het invullen!")
    print(deelnemers_talen)
    break
        

    
    