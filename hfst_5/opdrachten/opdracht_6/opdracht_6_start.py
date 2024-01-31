import pygame

class Speler():
    def __init__(self,x_speler,y_speler,afb_speler,snelheid_speler,mag_bewegen, achter_breedte,achter_hoogte):
        self.x_speler = x_speler
        self.y_speler = y_speler
        self.afb_speler = afb_speler
        self.snelheid_speler = snelheid_speler
        self.mag_bewegen = mag_bewegen

        self.obstakels = []
        self.achter_breedte = achter_breedte
        self.achter_hoogte = achter_hoogte

    def bewegen(self,toetsen):
        self.beweging = (0,0)

        self.mag_bewegen = True

        self.toekomstogigebeweging(toetsen) 
        self.raaktRand()
        self.raaktObstakel()

        if self.mag_bewegen == True: # Als speler na checks nog mag bewegen, verplaats hem dan naar de nieuwe positie.
            self.x_speler = self.nieuwe_x_speler
            self.y_speler = self.nieuwe_y_speler

    
    def toekomstogigebeweging(self,toetsen):
        self.toetsen = toetsen
        if self.toetsen[pygame.K_LEFT]:        
            self.beweging = (-self.snelheid_speler, 0)
        elif self.toetsen[pygame.K_RIGHT]:        
            self.beweging = (self.snelheid_speler, 0)
        elif self.toetsen[pygame.K_UP]:      
            self.beweging = (0, -self.snelheid_speler)
        elif self.toetsen[pygame.K_DOWN]:     
            self.beweging = (0, self.snelheid_speler)


    def obstalkelen(self,muis):
        if muis:
            self.positie_muis = pygame.mouse.get_pos() # Haal huidige positie muis op.
            self.x_positie_obstakel, self.y_positie_obstakel = self.positie_muis[0]-afb_obstakel.get_width()//2, self.positie_muis[1]-afb_obstakel.get_height()//2 # Zet obstakel gecentreerd op positie van muis.
            self.obstakel = pygame.Rect(self.x_positie_obstakel, self.y_positie_obstakel, afb_obstakel.get_width(), afb_obstakel.get_height()) # Maak obstakel aan.
            self.obstakels.append(self.obstakel) # Voeg obstakel toe aan lijst.
        
        if self.toetsen[pygame.K_l]:
            self.obstakels = []


    def raaktRand(self):
        
        self.nieuwe_x_speler = self.x_speler + self.beweging[0]
        self.nieuwe_y_speler = self.y_speler + self.beweging[1]
        self.rect_speler  = pygame.Rect(self.nieuwe_x_speler,self.nieuwe_y_speler,self.afb_speler.get_width(),self.afb_speler.get_height())

        if (self.nieuwe_x_speler < 0) or (self.nieuwe_x_speler+self.afb_speler.get_width() > self.achter_breedte):
            self.mag_bewegen = False
        if (self.nieuwe_y_speler < 0) or (self.nieuwe_y_speler+self.afb_speler.get_height() > self.achter_hoogte):
            self.mag_bewegen = False
        
        pass
    def raaktObstakel(self):

        if self.rect_speler.collidelist(self.obstakels) != -1:
            self.mag_bewegen = False
    def tekenen(self, frame):
        frame.blit(self.afb_speler, (self.x_speler,self.y_speler)) # Teken speler.



# Start pygame & wijzig titel van spel.
pygame.init()
pygame.display.set_caption('Opdracht 6')
running = True

# Maak frame aan met bepaalde grootte (gelijk aan grootte van achtergrond).
achtergrond = pygame.image.load(r"hfst_5/opdrachten/opdracht_6/veld.png") 
achter_breedte, achter_hoogte = achtergrond.get_width(), achtergrond.get_height()
frame = pygame.display.set_mode((achter_breedte, achter_hoogte))

# Zet speler klaar
x_speler, y_speler, snelheid_speler = achter_breedte//2, achter_hoogte//2, 5

afb_speler = pygame.image.load(r"hfst_5/opdrachten/opdracht_6/speler.png")
speler = Speler(x_speler,y_speler,afb_speler,snelheid_speler,True,achter_breedte,achter_hoogte)


# Zet een lege lijst klaar waarin obstakels bewaard worden.
# De obstakels worden bewaard als pygame Rects (zie regel 48) om collisie met speler te detecteren.

afb_obstakel = pygame.image.load(r"hfst_5/opdrachten/opdracht_6/obstakel.png")

# Maak een pygame klok om de FPS van het spel te bepalen.
klok = pygame.time.Clock()
FPS = 60

while running:
    toetsen = pygame.key.get_pressed() 
    muis = pygame.mouse.get_pressed()[0]
       
    " ACTIE 1: verwerk inputs van gebruiker. "
    pygame.event.pump() # Zorg ervoor dat pygame toetsen/muis mag ophalen.
    speler.bewegen(toetsen)
    speler.obstalkelen(muis)

    for event in pygame.event.get():  # Haal alle pygame events op.
        if event.type == pygame.QUIT: # Als het 'type' QUIT geregistreerd is.
            running = False           # Dan stel running gelijk aan False.

    " ACTIE 2: spel-staat wijzigen. "
    klok.tick(FPS) # Zorg voor constante framerate. 
    " Actie 3: teken & toon frame. "
    frame.blit(achtergrond, (0,0)) # Maak frame leeg door het wit te maken.
    speler.tekenen(frame)
    for obstakel in speler.obstakels: frame.blit(afb_obstakel, (obstakel[0],obstakel[1])) # Teken obstakels.
    pygame.display.flip() # Toon frame
pygame.quit()