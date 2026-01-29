import pygame
import random
from constant import *

class Ice:
    # Represents an ice cube that freezes the game for 3 seconds if hit
    
    def __init__(self, x,letter):
        # Initialize ice cube at position x
        self.y=SPAWN_Y
        self.x=x
        self.size=40
        self.letter=letter
        self.speed_y = -random.randint(ICE_SPEED, 7)  # negative to move upward
        self.speed_x = random.randint(SPEED_X_MIN * 10, SPEED_X_MAX * 10) / 10  # horizontal trajectory
        
        # Set ice cube size
        self.display_size=100
        self.radius=self.display_size//2
        
        # Set image and size it
        self.ice_img=pygame.image.load("ice.png").convert_alpha()
        self.ice_img = pygame.transform.scale(self.ice_img, (self.display_size,self.display_size))
    
    def update(self):
        # Move ice cube upward with horizontal trajectory, return True if out of screen
        self.y += self.speed_y
        self.x += self.speed_x
        
        # Check if out of screen (top or sides)
        if self.y + self.radius < 0 or self.x < -self.radius or self.x > SCREEN_WIDTH + self.radius:
            return True
        return False
    
    def draw(self, screen):
        # Draw ice cube as a light blue square with letter
        image_rect = self.ice_img.get_rect(center=(self.x, self.y))
        screen.blit(self.ice_img, image_rect)
        
        font=pygame.font.Font("fruit_font.ttf", 40)
        letter=font.render(self.letter, True, (0, 0, 255))
        letter_rect=letter.get_rect(center=(self.x, self.y))
        screen.blit(letter, letter_rect)

    def is_hit(self, key):
        # Check if pressed key matches ice cube's letter
        if key==self.letter:
            return True
        return False