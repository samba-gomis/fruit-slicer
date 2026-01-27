import pygame

class Bomb:
    def __init__(self, vitesse, gravite, x, y):
        self.x=y
        self.y=y
        self.vitesse=vitesse
        self.gravite=gravite
        self.image=pygame.image.load("image.png").convert_alpha()
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y