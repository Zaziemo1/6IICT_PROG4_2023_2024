# Maak een klasse Speler & Spel zoals aangegeven in opdracht 10.
import random
class Speler():

    
    

    def __init__(self,naam,level,score):
        self.naam = naam
        self.level = level
        self.score = score
    
    def info(self):
        print(f"naam = {self.naam}, level = {self.level}, score = {self.score}")
    
    def level_up(self):
        self.level += 1
        print(f"{self.naam} is level {self.level} geworden!")
    
    def verhoog_score(self, nieuwescore):
        
        
        if type(nieuwescore) != int:
            raise ValueError("Het is een string!")

        self.nieuwescore = nieuwescore
        self.score = self.score + self.nieuwescore
        print(self.score)
        

    
    pass


class Spel():

    def __init__(self,game):

        self.game = game
        self.spelers = []
         
        pass
    
    def speler_toevoegen(self,speler: 'Speler'):
        if type(speler) == Speler:
            self.speler = speler
            self.spelers.append(speler)
            print(f"{speler.naam} doet mee aan {self.game}")
        else:
            raise ValueError("'speler_toevoegen' vereist Speler, niet type(speler).")
    
    def spelen(self):
        self.winnaar = random.choice(self.spelers)
        for speler in self.spelers:
            if self.winnaar == speler:
                self.winnaar.score = speler.score + 100
                break

        
        print(f"{self.winnaar.naam} heeft gewonnen! Nieuwe score is {self.winnaar.score}!")
    
    def scorebord(self):
        print("Huidige score board:")
        for speler in self.spelers:
            print(f"-      {speler.naam} ,(LVL {speler.level}) {speler.score} score!")
        



    


