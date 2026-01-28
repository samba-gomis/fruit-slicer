import pygame
from constant import *


class Menu:
    
    def __init__(self):
      
        self.font_large=pygame.font.Font("fruit_font.ttf",FONT_SIZE_LARGE)
        self.font_medium=pygame.font.Font("fruit_font.ttf",FONT_SIZE_MEDIUM)
        self.font_small=pygame.font.Font("fruit_font.ttf",FONT_SIZE_SMALL)
        self.font_tiny=pygame.font.Font("fruit_font.ttf",FONT_SIZE_TINY)

        self.background=pygame.image.load("background_menu.jpg")
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
        
        # Instructions
        instructions = [
            "HOW TO PLAY:",
            "",
            "- Type the letter on fruits to slice them",
            "- Each fruit sliced = +1 point",
            "- Slice multiple fruits at once for combos!",
            "- Miss 3 fruits = Game Over",
            "",
            "SPECIAL ITEMS:",
            "- ICE: Freezes time for 3-5 seconds",
            "- BOMB: Instant Game Over!",
            "",
        ]
        
        y_offset = 240
        for line in instructions:
            if line.startswith("HOW TO PLAY") or line.startswith("SPECIAL"):
                text = self.font_small.render(line, True, DARK_GRAY)
            else:
                text = self.font_tiny.render(line, True, BLACK)
            
            text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, y_offset))
            screen.blit(text, text_rect)
            y_offset += 30
        
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