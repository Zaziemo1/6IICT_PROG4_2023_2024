"""
Vul dit bestand aan met de instructies in OneNote.
"""
class Account():
    def __init__(self,naam,balans,type) -> None:
        self.naam = naam
        self.balans = balans
        self.type = type
        pass

    def overzicht(self):
        print(f"{self.naam}, balans = {self.balans}, type account = {self.type}")

    def storten(self,bedrag):
        self.bedrag = bedrag
        if type(bedrag) != int:
            print("Ongeldige bedrag ontvangen! ")
        else:
            self.balans = self.balans+ self.bedrag
            print(f"{self.bedrag} ingestort, Nieuwe balans is {self.balans}")
    
    def afhalen(self,pinnen):
        self.pinnen = pinnen
        if self.pinnen > self.balans:
            print("Ontoereikende balans.")
        else:
            self.balans = self.balans - self.pinnen
            print(f"{self.pinnen} euro uitgepint! Nieuwe balans is {self.balans}!")


class Bank():
    def __init__(self,naam,bonus) -> None:
        self.naam = naam
        self.accounts = []
        self.bonus = bonus
    
    def toevoegen(self,account : Account):
        if type(account) == Account:
            self.accounts.append(account)
            print(f"{account.naam} toegevoegd aan {self.naam}")
        else:
            print("Geen geldige account opgegeven!")
    
    def overzicht(self):
        print(f"{self.naam} heeft de volgende accounts: ")
        for member in self.accounts:
            print(f" - {member.naam} ({member.type}) : {member.balans} euro." )
    
    def bonus_uitkeren(self):
        for member in self.accounts:
            if member.type == "premium":
                member.balans = member.balans + (self.bonus*2)
                print(f"{self.bonus*2} Bonus aan {member.naam}! Balans is nu {member.balans}!")
            else:
                member.balans = member.balans + self.bonus
                print(f"{self.bonus} Bonus aan {member.naam}! Balans is nu {member.balans}!")

    
    