""" oefening 3 (   / 8): Authenticatie app

Baseer je op kerst_oefening_3.exe om de authenticatie app op te bouwen.
Onderstaande vereisten bevatten de zaken waar je zeker op moet letten.

Grafische vereisten:
    - Bouw de app na zoals in de exe (de widgets moeten allemaal op dezelfde plaats staan).
    - De titel van de app is "Authenticator".
    - De gebruiker kan de grootte van de app niet wijzigen (Tip: gebruik resizable).
    - Het label bovenaan is onderlijnd en heeft als font "Euphemia" met grootte 16.
    - Het label bovenaan heeft een padding van 30 links en rechts van zich.
    - De Entry in het midden heeft een padding van 10 boven en onder zich.
    - Beide knoppen hebben een breedte (width) van 12.
    - Het label onderaan heeft een padding van 10 ENKEL boven zich.

Functionele vereisten:
    - Op de knop inloggen duwen moet nagaan of de huidige gebruiker bestaat.
      Doe dit door te controleren of de inhoud van de Entry in de lijst gebruikers voorkomt.
      ---> Dit is het geval: maak het label bovenaan groen en wijzig naar "Welkom, *gebruiker*!"
      ---> Dit is niet het geval: maak het label bovenaan rood en wijzig naar "Ongeldige login!"
    - Na het drukken op de knop inloggen moet de Entry volledig leeggemaakt worden, 
      dit ongeacht of de login gelukt is of niet.
    - Op de knop status drukken toont de status ENKEL als de admin is ingelogd.
      ---> De admin is ingelogd: wijzig label onderaan naar "Dit is de status..." in het groen.
      ---> De admin is niet ingelogd: wijzig label onderaan naar "Geen recht voor status..." in het rood.

      Tip! Hou de huidig ingelogd gebruiker bij in een globale variabele.
           Je kan deze gebruiken om te controleren of de admin is ingelogd.

"""

# Lijst met verschillede soorten gebruikers.
gebruikers = ["admin", "personeel"] 
import tkinter as tk



app= tk.Tk()
app.title("Authenticator")
app.resizable(width=False,height=False)
toegang = ""
def inlog():
    gebruiker = Username.get()
    global toegang
    if gebruiker in gebruikers:
        Titel.configure(text=f"Welkom {gebruiker}",font=("Euphemia",16,"underline"),fg="green")
        Username.delete(0,"end")
        toegang = f'{gebruiker}'
    else:
        Titel.configure(text="Ongeldig",font=("Euphemia",16,"underline"),fg="red")
        Username.delete(0,"end")
        toegang = 'Invalid'

def statusweergeven():
    global toegang
    if toegang == 'admin':
        Status.configure(text="Dit is de status",fg="green")
    else:
        Status.configure(text="Geen toegang",fg="red")




Titel = tk.Label(master=app,text="Gelieve in te loggen!",font=("Euphemia",16,"underline"))
Titel.grid(column=0,row=0,padx=30,)

Gebruikersnaam = tk.Label(master=app,text="Geef een gebruikersnaam:")
Gebruikersnaam.grid(column=0,row=1)

Username = tk.Entry(master=app)
Username.grid(column=1,row=1,pady=10)

Inloggen = tk.Button(master=app,text="Inloggen",width=12,command=inlog)
Inloggen.grid(column=0,row=2,)

StatusTonen = tk.Button(master=app,text="Toon Status",width=12,command=statusweergeven)
StatusTonen.grid(column=1,row=2,)

Status = tk.Label(master=app,text="Hier komt de status")
Status.grid(column=0,row=3,pady=10)



app.mainloop()





