import os
import pygame
import random
from constant import *


class Fruit:
    FRUIT_IMAGES = []

    @classmethod
    def load_images(cls):
        if cls.FRUIT_IMAGES:
            return
        img_dir = FRUIT_IMAGES_DIR if 'FRUIT_IMAGES_DIR' in globals() else 'assets/images/fruits'
        if not os.path.isdir(img_dir):
            return
        for fname in os.listdir(img_dir):
            if fname.lower().endswith(('.png', '.jpg', '.jpeg')):
                path = os.path.join(img_dir, fname)
                try:
                    img = pygame.image.load(path).convert_alpha()
                    img = pygame.transform.scale(img, (FRUIT_DISPLAY_SIZE, FRUIT_DISPLAY_SIZE))
                    cls.FRUIT_IMAGES.append(img)
                except Exception:
                    # ignore individual load errors
                    pass

    def __init__(self, x, letter):
        self.x = x
        self.y = SPAWN_Y
        self.letter = letter
        self.speed_y = -random.randint(FRUIT_SPEED, 7)  # negative to move upward
        self.speed_x = random.randint(SPEED_X_MIN * 10, SPEED_X_MAX * 10) / 10  # horizontal trajectory
        self.radius = FRUIT_RADIUS
        self.color = random.choice(FRUIT_COLORS)

        # load images once and pick one if available
        Fruit.load_images()
        if Fruit.FRUIT_IMAGES:
            self.image = random.choice(Fruit.FRUIT_IMAGES)
            self.image_rect = self.image.get_rect(center=(self.x, self.y))
        else:
            self.image = None

    def update(self):
        self.y += self.speed_y
        self.x += self.speed_x
        # Update image rect if used
        if hasattr(self, 'image_rect') and self.image_rect:
            self.image_rect.center = (self.x, self.y)
        # Check if out of screen (top or sides)
        if self.y + self.radius < 0 or self.x < -self.radius or self.x > SCREEN_WIDTH + self.radius:
            return True
        else:
            return False

    def draw(self, screen):
        if self.image:
            rect = self.image.get_rect(center=(self.x, self.y))
            screen.blit(self.image, rect)
        else:
            pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
            font = pygame.font.Font("fruit_font.ttf", FONT_SIZE_MEDIUM)
            texte = font.render(self.letter, True, (0, 0, 0))
            texte_rect = texte.get_rect(center=(self.x, self.y))
            screen.blit(texte, texte_rect)

    def is_hit(self, key):
        return key == self.letter