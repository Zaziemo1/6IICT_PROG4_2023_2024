import pygame


class Speler():
    def __init__(self,x,y,snelheid,afb_speler) -> None:
        self.x = x
        self.y = y
        self.snelheid = snelheid

    def bewegen(self,toetsen):
        self.toetsen = toetsen

        if self.toetsen[pygame.K_LEFT]:
            self.x = self.x - self.snelheid
        if self.toetsen[pygame.K_RIGHT]:
            self.x = self.x + self.snelheid
    

pygame.init()

afb_speler = pygame.image.load(r"hfst_5/opdrachten/opdracht_6/speler.png")
screen = pygame.display.set_mode((640, 480))


while True:
    speler = Speler(50,50,2,afb_speler)
    screen.fill((0,0,0))
    toetsen = pygame.key.get_pressed()
    pygame.event.pump()
    # Check for events
    for event in pygame.event.get():
        # Check for the quit event
        if toetsen[pygame.K_q] or event.type == pygame.QUIT:
            # Quit the game
            pygame.quit()
        if toetsen[pygame.K_f]:
            pygame.display.toggle_fullscreen()
    speler.bewegen(toetsen)
    rect_speler  = pygame.Rect(speler.x,speler.y,speler.afb_speler.get_width(),speler.afb_speler.get_height())

        

    pygame.display.update()