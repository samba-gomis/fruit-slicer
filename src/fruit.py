import pygame
import random
from src.constant import*

FRUIT_IMAGES = [
    pygame.image.load("./assets/images/Apricot.png"),
    pygame.image.load("./assets/images/Avocado.png"),
    pygame.image.load("./assets/images/Banana.png"),
    pygame.image.load("./assets/images/Black_Grapes.png"),
    pygame.image.load("./assets/images/Blueberry.png"),
    pygame.image.load("./assets/images/Cantaloupe.png"),
    pygame.image.load("./assets/images/Cherries.png"),
    pygame.image.load("./assets/images/Fig.png"),
    pygame.image.load("./assets/images/Kiwi.png"),
    pygame.image.load("./assets/images/Lemon.png"),
    pygame.image.load("./assets/images/Mandarin.png"),
    pygame.image.load("./assets/images/Mango.png"),
    pygame.image.load("./assets/images/Pineapple.png"),
    pygame.image.load("./assets/images/Pitaya.png"),
    pygame.image.load("./assets/images/Plum.png"),
    pygame.image.load("./assets/images/Pomegranate.png"),
    pygame.image.load("./assets/images/Prune.png"),
    pygame.image.load("./assets/images/Red_Apple.png"),
    pygame.image.load("./assets/images/Redcurrant.png"),
    pygame.image.load("./assets/images/Strawberry.png"),
    pygame.image.load("./assets/images/Watermelon.png"),
    pygame.image.load("./assets/images/Yellow_Pear.png"),
]


class Fruit :
    def __init__(self, x , letter ):
        self.x = x
        self.y = SPAWN_Y
        self.letter = letter 
        self.speed_y = -random.randint(FRUIT_SPEED, 7)  # negative to move upward
        self.speed_x = random.randint(SPEED_X_MIN * 10, SPEED_X_MAX * 10) / 10  # horizontal trajectory
        self.radius = FRUIT_RADIUS
        self.color = random.choice(FRUIT_COLORS)
        self.image =random.choice(FRUIT_IMAGES)
        self.image =pygame.transform.scale(
            self.image , (self.radius*2 ,self.radius*2)
        )
        self.rect = self.image.get_rect(center=(self.x , self.y))
    
    def update(self):
        self.y += self.speed_y
        self.x += self.speed_x
        self.rect.center = (self.x , self.y)
        # Check if out of screen (top or sides)
        if self.y + self.radius < 0 or self.x < -self.radius or self.x > SCREEN_WIDTH + self.radius:
            return True
        else:
            return False
        
    def draw( self ,screen):
        screen.blit(self.image , self.rect)
        font = pygame.font.Font("assets/fonts/fruit_font.ttf",FONT_SIZE_MEDIUM)
        texte = font.render(self.letter , True , (0,0,0))
        texte_rect = texte.get_rect(center =(self.x , self.y))
        screen.blit(texte , texte_rect)

    def is_hit(self ,key):
        if key == self.letter:
            return True
        else:
            return False