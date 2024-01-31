import pygame
import sys
from particle import BoringParticle, Bouncingparticle
import random

# Constantes.
BREEDTE, HOOGTE = 1500, 820
FPS = 120
AANTAL_PARTICLES = 100

white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0,0,0)


colorlist = [white, red, green, blue,black]
# Start pygame.
pygame.init()
pygame.display.set_caption("Fire Storm Simulation")
scherm = pygame.display.set_mode((BREEDTE, HOOGTE))
klok = pygame.time.Clock()

# TODO 1: Vul lijst *particles* aan met objecten van de klasse *BoringParticle*.
#         Het aantal aangemaakte objecten is gelijk aan de variabele *aantal_particles*.
particles = []
""" Vul lijst aan... """
for particle in range(AANTAL_PARTICLES):
    particles.append(BoringParticle(300, 300, random.uniform(-10, 10), random.uniform(-10, 10)))  # Adding initial velocities
    particles.append(Bouncingparticle(300,300, random.uniform(-10,10),random.uniform(-10,10)))


running = True
while running:
    # Maak scherm schoon.
    scherm.fill((100, 100, 100))

    # Zorg voor constante FPS. interval is de tijd tussen iedere frame (in ms)
    interval = klok.tick(FPS)

    # Controleer of quit-knop is ingeduwd.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # TODO 2: Overloop iedere particle in lijst met particles:
    #   1. Beweeg positie van ieder particle
    #   2. Reset particle wanneer ze uit het scherm zijn.
    #   3. Teken particle op scherm (deels gemaakt).
    for particle in particles:
        """ 1. Beweeg particle """
        particle.update()
        """ 2. Reset particle """
        particle.reset(BREEDTE, HOOGTE)
        colour = random.choice(colorlist)

        pygame.draw.circle(scherm, colour, (int(particle.pos_x), int(particle.pos_y)), 30)

    # Toon scherm aan gebruiker.
    pygame.display.update()

pygame.quit()
