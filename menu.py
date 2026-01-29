import pygame
from constant import *

class Menu:
    
    def __init__(self):
      
        self.font_large=pygame.font.Font("fruit_font.ttf",FONT_SIZE_LARGE)
        self.font_medium=pygame.font.Font("fruit_font.ttf",FONT_SIZE_MEDIUM)
        self.font_small=pygame.font.Font("fruit_font.ttf",FONT_SIZE_SMALL)
        self.font_tiny=pygame.font.Font("fruit_font.ttf",FONT_SIZE_TINY)

        self.background=pygame.image.load("assets/images/background_menu.jpg")
        self.background=pygame.transform.scale(self.background,(SCREEN_WIDTH, SCREEN_HEIGHT))
    
    def draw(self, screen):
        screen.blit(self.background,(0,0))

        # Title
        title = self.font_large.render("FRUIT NINJA", True, RED)
        title_rect = title.get_rect(center=(SCREEN_WIDTH // 2, 100))
        screen.blit(title, title_rect)
        
        # Subtitle
        subtitle = self.font_medium.render("Typing Game", True, ORANGE)
        subtitle_rect = subtitle.get_rect(center=(SCREEN_WIDTH // 2, 170))
        screen.blit(subtitle, subtitle_rect)
        
        start_text = self.font_medium.render("Press SPACE to Start", True, GREEN)
        start_rect = start_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 80))
        screen.blit(start_text, start_rect)
        
        quit_text = self.font_tiny.render("Press Q to Quit", True, DARK_GRAY)
        quit_rect = quit_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 30))
        screen.blit(quit_text, quit_rect)
    
    def handle_input(self, event):
       
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                return 'start'
            elif event.key == pygame.K_q:
                return 'quit'
        
        return None