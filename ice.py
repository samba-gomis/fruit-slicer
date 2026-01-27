import pygame
import random

class Ice:
    def __init__(self,x):
       self.y=0
       self.x=x
       self.size=40
       self.letter="i"
       self.speed=random.randint(2,7)
       self.radius=30
       self.color(173, 216, 230)
    
    def update(self):
        self.y+=self.speed

        if self.y>600:
            return True
        return False
    
    def draw(self,screen):
         square=pygame.Rect(self.x-self.size//2,self.y-self.size//2,self.size,self.size)
         pygame.draw.rect(screen,self.color,square)
        
         font=pygame.font.Font(None, 40)
         letter=font.render(self.letter, True, (0, 0, 255))
         letter_rect=letter.get_rect(center=(self.x, self.y))
         screen.blit(letter, letter_rect)

    def is_hit(self,key):
        if key==self.letter:
            return True
        return False
    
    
      