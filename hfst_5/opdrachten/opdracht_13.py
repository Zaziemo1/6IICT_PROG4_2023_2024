# Maak een klasse Rechthoek & Vierkant zoals aangegeven in opdracht 13.
class Rechthoek():

    def __init__(self,x,y,breedte,hoogte) -> None:
        self.x = x
        self.y = y
        self.breedte = breedte
        self.hoogte = hoogte
        pass

    def get_oppervlakte(self):
        self.oppervlakte = self.breedte * self.hoogte
        return self.oppervlakte
    
    def get_omtrek(self):
        self.omtrek = self.breedte + self.breedte + self.hoogte + self.hoogte
        return self.omtrek
    
    def set_breedte(self,nieuwe_breedte):
        self.breedte = nieuwe_breedte
    
    def set_hoogte(self,nieuwe_hoogte):
        self.hoogte = nieuwe_hoogte

class Vierkant(Rechthoek):
    def __init__(self, x, y, breedte) -> None:
        self.x = x
        self.y = y
        self.breedte = breedte
        self.hoogte = breedte
    def set_breedte(self, nieuwe_breedte):
        super().set_hoogte(nieuwe_breedte)
        super().set_breedte(nieuwe_breedte)

    pass

" Via onderstaande code kan je niveau 1 testen. "
r_1 = Rechthoek(1,1 , 2,4) # Volgorde parameters: (x,y  ,  breedte,hoogte)
r_2 = Rechthoek(7,9 , 8,5)

print( r_1.get_oppervlakte() ) # 8
print( r_2.get_omtrek() )      # 26

r_1.set_breedte(7)
print(r_1.breedte) # 7

r_2.set_hoogte(1)
print(r_2.hoogte)  # 1


" Via onderstaande code kan je niveau 2 testen. "
vierkant = Vierkant(0,0 , 7)

print( vierkant.get_oppervlakte() ) # 49
vierkant.set_breedte(5)

print( vierkant.breedte, vierkant.hoogte) # 5 5
