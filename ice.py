import pygame
import random
from constant import *

class Ice:
    """Represents an ice cube that freezes the game for 3 seconds if hit"""
    
    def __init__(self, x):
        """Initialize ice cube at position x"""
        self.y=0
        self.x=x
        self.size=40
        self.letter="i"
        self.speed=random.randint(ICE_SPEED, 7)
        self.radius=ICE_RADIUS
        self.color=LIGHT_BLUE
    
    def update(self):
        """Move ice cube downward, return True if out of screen"""
        self.y+=self.speed

        if self.y>600:
            return True
        return False
    
    def draw(self, screen):
        """Draw ice cube as a light blue square with letter"""
        square=pygame.Rect(self.x-self.size//2, self.y-self.size//2, self.size, self.size)
        pygame.draw.rect(screen, self.color, square)
        
        font=pygame.font.Font(None, 40)
        letter=font.render(self.letter, True, (0, 0, 255))
        letter_rect=letter.get_rect(center=(self.x, self.y))
        screen.blit(letter, letter_rect)

    def is_hit(self, key):
        """Check if pressed key matches ice cube's letter"""
        if key==self.letter:
            return True
        return False
