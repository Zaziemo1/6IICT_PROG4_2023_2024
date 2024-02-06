import pygame

class Speler():
    def __init__(self,x_speler,y_speler,afb_speler,snelheid_speler,snelheid_kogel):
        self.x_speler = x_speler
        self.y_speler = y_speler
        self.afb_speler = afb_speler
        self.snelheid_speler = snelheid_speler

        self.x_kogels = []
        self.y_kogels = []
        self.snelheid_kogel = snelheid_kogel


        
    def bewegen(self,toetsen):
        self.toetsen = toetsen
        if self.toetsen[pygame.K_LEFT]   and   self.x_speler > 0:        
            self.x_speler = self.x_speler - self.snelheid_speler
        if self.toetsen[pygame.K_RIGHT]  and   self.x_speler+afb_speler.get_width() < frame_breedte:        
            self.x_speler = self.x_speler + self.snelheid_speler
        if self.toetsen[pygame.K_UP]     and   self.y_speler > 0:      
            self.y_speler = self.y_speler - self.snelheid_speler
        if self.toetsen[pygame.K_DOWN]   and   self.y_speler+afb_speler.get_height() < frame_hoogte:     
            self.y_speler = self.y_speler + self.snelheid_speler
    
    
    
    def schieten(self):

        self.toetsen = toetsen
        if self.toetsen[pygame.K_SPACE]:
            self.x_kogels.append(self.x_speler + afb_speler.get_width()) 
            self.y_kogels.append(self.y_speler + afb_speler.get_height()//2) 

        pass

# Start pygame & wijzig titel van spel.
pygame.init()
pygame.display.set_caption('Opdracht 5')
running = True

# Maak frame aan met bepaalde grootte.
frame_breedte, frame_hoogte = 800, 400
frame = pygame.display.set_mode((frame_breedte, frame_hoogte))

# Zet alle benodigde afbeeldingen & hun startposities klaar.
# x_kogels & y_kogels zijn lijsten omdat ze de posities van alle geschoten kogels zullen bevatten.
afb_speler = pygame.image.load(r"hfst_5/opdrachten/opdracht_5/vliegtuig.png")
afb_kogel = pygame.image.load(r"hfst_5\opdrachten\opdracht_5\kogel.png")
speler = Speler(0,frame_hoogte//2,afb_speler,10,1)





# Maak een pygame klok om de FPS van het spel te bepalen.
klok = pygame.time.Clock()
FPS = 60

while running:
    " ACTIE 1: verwerk inputs van gebruiker. "
    pygame.event.pump() # Zorg ervoor dat pygame toetsen mag ophalen.
    toetsen = pygame.key.get_pressed() # Haal toetsen op.

    # Beweeg spelertuig op basis van toetsen.
    speler.bewegen(toetsen)

    # Zet nieuwe kogel langs spelertuig door toe te voegen aan lijsten x_kogels & y_kogels.
    speler.schieten()
    
    # Sluit spel af bij indrukken knop rechts-bovenaan.
    for event in pygame.event.get():  # Haal alle pygame events op.
        if event.type == pygame.QUIT: # Als het 'type' QUIT geregistreerd is.
            running = False           # Dan stel running gelijk aan False.

    " ACTIE 2: spel-staat wijzigen. "
    klok.tick(FPS) # Zorg voor constante framerate.
    for index, speler.x_kogel in enumerate(speler.x_kogels): speler.x_kogels[index] = speler.x_kogel + speler.snelheid_kogel # Beweeg de kogels.

    " Actie 3: teken & toon frame. "
    frame.fill((0,0,0), (0,0,frame_breedte,frame_hoogte)) # Maak frame leeg door het zwart te maken.
    frame.blit(afb_speler, (speler.x_speler,speler.y_speler)) # Teken spelertuig.
    for index, x_kogel in enumerate(speler.x_kogels): frame.blit(afb_kogel, (speler.x_kogels[index],speler.y_kogels[index])) # Teken kogels.
    pygame.display.flip() # Toon frame.

pygame.quit()