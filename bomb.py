import pygame
import random

class Bomb:
    def __init__(self, x):
        self.x=x
        self.y=0
        self.letter="b"
        self.radius=30
        self.color=(0,0,0)
        self.speed=random.randint(2,7)

    def update(self):
        self.y+=self.speed  
        if self.y>600:
            return True
        return False
    

    def draw(self,screen):

        pygame.draw.circle(screen,self.color,(self.x,self.y),self.radius)
        font=pygame.font.Font(None,40)
        letter=font.render(self.letter, True,(255,0,0))
        letter_rect=letter.get_rect(center=(self.x,self.y))
        screen.blit(letter,letter_rect)

    def is_hit(self,key):
        if key==self.letter:
            return True
        return False