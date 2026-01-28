import pygame
import random
from constant import*

class Fruit :
    def __init__(self, x , letter ):
        self.x = x
        self.y = SPAWN_Y
        self.letter = letter 
        self.speed = FRUIT_SPEED
        self.radius = FRUIT_RADIUS
        self.color =random.choice(FRUIT_COLORS)
    
    def update(self):
        self.y += self.speed
        if self.y - self.radius > SCREEN_HEIGHT: 
            return True
        else:
            return False
        
    def draw( self ,screen):
        pygame.draw.circle(screen, self.color,(self.x ,self.y),self.radius)
        font = pygame.font.Font(None,FONT_SIZE_MEDIUM)
        texte = font.render(self.letter , True , (0,0,0))
        texte_rect = texte.get_rect(center =(self.x , self.y))
        screen.blit(texte , texte_rect)

    def is_hit(self ,key):
        if key == self.letter:
            return True
        else:
            return False
