import pygame
import random
from src.constant import*

class Fruit :
    def __init__(self, x , letter ):
        self.x = x
        self.y = SPAWN_Y
        self.letter = letter 
        self.speed_y = -random.randint(FRUIT_SPEED, 7)  # negative to move upward
        self.speed_x = random.randint(SPEED_X_MIN * 10, SPEED_X_MAX * 10) / 10  # horizontal trajectory
        self.radius = FRUIT_RADIUS
        self.color = random.choice(FRUIT_COLORS)
    
    def update(self):
        self.y += self.speed_y
        self.x += self.speed_x
        # Check if out of screen (top or sides)
        if self.y + self.radius < 0 or self.x < -self.radius or self.x > SCREEN_WIDTH + self.radius:
            return True
        else:
            return False
        
    def draw( self ,screen):
        pygame.draw.circle(screen, self.color,(self.x ,self.y),self.radius)
        font = pygame.font.Font("assets/fonts/fruit_font.ttf",FONT_SIZE_MEDIUM)
        texte = font.render(self.letter , True , (0,0,0))
        texte_rect = texte.get_rect(center =(self.x , self.y))
        screen.blit(texte , texte_rect)

    def is_hit(self ,key):
        if key == self.letter:
            return True
        else:
            return False