import random


class BoringParticle():

    def __init__(self, pos_x, pos_y, speedx, speedy):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.speedx = speedx
        self.speedy = speedy

    def update(self):
        self.pos_y += self.speedy
        self.pos_x += self.speedx

    def reset(self, BREEDTE, HOOGTE):
        if self.pos_x < 0 or self.pos_x > BREEDTE:
            self.speedx *= -1
        if self.pos_y < 0 or self.pos_y > HOOGTE:
            self.speedy *= -1


class Bouncingparticle():

    def __init__(self, pos_x, pos_y, speedx, speedy):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.speedx = speedx
        self.speedy = speedy

    def update(self):
        self.pos_y += self.speedy
        self.pos_x += self.speedx

    def reset(self, BREEDTE, HOOGTE):
        if self.pos_x < 0 or self.pos_x > BREEDTE:
            self.speedx *= -1
        if self.pos_y < 0 or self.pos_y > HOOGTE:
            self.speedy *= -1
