import pygame
import random
from constant import *

class Bomb:
    """Represents a bomb that triggers Game Over if hit"""
    
    def __init__(self, x,letter):
        """Initialize bomb at position x"""
        self.x=x
        self.y=SPAWN_Y

        self.letter=letter

        self.display_size=200
        self.radius=self.display_size//2

        self.speed=random.randint(BOMB_SPEED, 7)

        #set bomb image and size it
        self.bomb_img=pygame.image.load("bomb.png").convert_alpha()
        self.bomb_img = pygame.transform.scale(self.bomb_img, (self.display_size,self.display_size))

    def update(self):
        """Move bomb downward, return True if out of screen"""
        self.y+=self.speed  
        if self.y - self.radius > SCREEN_HEIGHT:
            return True
        return False
    
    def draw(self, screen):
        """Import bomb image and place the assigned letter"""

        image_rect = self.bomb_img.get_rect(center=(self.x, self.y))
        screen.blit(self.bomb_img, image_rect)

        font=pygame.font.Font("fruit_font.ttf", 60)
        letter=font.render(self.letter, True, BLACK)
        letter_rect=letter.get_rect(center=(self.x, self.y))
        screen.blit(letter, letter_rect)

    def is_hit(self, key):
        """Check if pressed key matches bomb's letter"""
        if key==self.letter:
            return True
        return False
