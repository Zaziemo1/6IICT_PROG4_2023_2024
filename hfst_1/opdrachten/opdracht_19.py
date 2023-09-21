# Gebruik onderstaande gemengde structuur om de opdracht op te lossen.
vlucht_reservering_systeem = {
    'vluchten': {
        'VL001': {
            'van': 'New York',
            'naar': 'Los Angeles',
            'vertrektijd': '2023-09-01 10:00',
        },
        'VL002': {
            'van': 'Chicago',
            'naar': 'Miami',
            'vertrektijd': '2023-09-02 12:00',
        },
        # Meer vluchtvermeldingen...
    },
    'passagiers': {
        'P001': {
            'naam': 'Alice Smith',
            'geboekte_vluchten': ['VL001'],
        },
        'P002': {
            'naam': 'Bob Johnson',
            'geboekte_vluchten': ['VL002'],
        },
        # Meer passagiersvermeldingen...
    }
}
print("Dag beste gebruiker. Waarmee kan ik helpen?")



def vlucht_boeken(passnmr):
    passnummer = str(f'P00{passnmr}')
    passagiernaam = input("Wat is uw naam?    ")
    for vluchtnr, vluchtinfo in vlucht_reservering_systeem['vluchten'].items():
        print(f"    - {vluchtnr}: {vluchtinfo['van']} --> {vluchtinfo['naar']} om {vluchtinfo['vertrektijd']}")
    
    while True:
        nmrvlucht = input("Wat is uw vlucht nummer?    ")
        
        if keuze == 1:
            if nmrvlucht  in vlucht_reservering_systeem['vluchten'].keys():
                break
            else:
                print("Geef een Geldige vlucht nummer!")

             
    if passagiernaam != vlucht_reservering_systeem['passagiers']['P001']['naam']:
        if passagiernaam != vlucht_reservering_systeem['passagiers']['P002']['naam']:
            vlucht_reservering_systeem['passagiers'][passnummer] = {'naam': passagiernaam, 'geboekte_vluchten' : [nmrvlucht]}
    
    return passnmr+1

def passiergs_bekijken():
    for vluchtnr, vluchtinfo in vlucht_reservering_systeem['vluchten'].items():
        print(f"    - {vluchtnr}: {vluchtinfo['van']} --> {vluchtinfo['naar']} om {vluchtinfo['vertrektijd']}")
      
    while True:
        vlucht_nmr = input("Welke vluchtt wilt u bekijken?    ")
        if vlucht_nmr in vlucht_reservering_systeem['vluchten'].keys():
            break
        else:
            print("Geef een geldige vlucht nummer op! ")

    
    for persoon, persooninfo in vlucht_reservering_systeem['passagiers'].items():
        if vlucht_nmr in persooninfo['geboekte_vluchten']:
            print(persooninfo['naam'])

    
    


passnmr = 3         
while True:
    keuze = int(input(" (optie 1) Boek een vlucht. of (optie 2) Lijst van passagier tonen. "))

    if keuze == 1:
        passnmr = vlucht_boeken(passnmr)
    
    if keuze == 2:
        passiergs_bekijken()
    
    if keuze == 3:
        print(vlucht_reservering_systeem)
    
    if keuze == 4:
        break