import pygame
from constant import *

class GameOver:
    
    def __init__(self):
        self.font_large = pygame.font.Font("fruit_font.ttf", FONT_SIZE_LARGE)
        self.font_medium = pygame.font.Font("fruit_font.ttf", FONT_SIZE_MEDIUM)
        self.font_small = pygame.font.Font("fruit_font.ttf", FONT_SIZE_SMALL)
        self.font_tiny = pygame.font.Font("fruit_font.ttf", FONT_SIZE_TINY)
    
    def draw(self, screen, final_score, reason="strikes"):
    
        # Fill background
        self.background=pygame.image.load("assets/images/background_game.png")
        self.background=pygame.transform.scale(self.background,(SCREEN_WIDTH, SCREEN_HEIGHT))
        screen.blit(self.background, (0, 0))
        
        # Game Over title
        title = self.font_large.render("GAME OVER", True, RED)
        title_rect = title.get_rect(center=(SCREEN_WIDTH // 2, 120))
        screen.blit(title, title_rect)
        
        # Reason for game over
        if reason == "bomb":
            reason_text = self.font_medium.render("You hit a BOMB!", True, YELLOW)
        else:
            reason_text = self.font_medium.render("3 Strikes - You're Out!", True, ORANGE)
        
        reason_rect = reason_text.get_rect(center=(SCREEN_WIDTH // 2, 200))
        screen.blit(reason_text, reason_rect)
        
        # Final score
        score_label = self.font_small.render("Final Score:", True, WHITE)
        score_label_rect = score_label.get_rect(center=(SCREEN_WIDTH // 2, 280))
        screen.blit(score_label, score_label_rect)
        
        score_value = self.font_large.render(str(final_score), True, GREEN)
        score_value_rect = score_value.get_rect(center=(SCREEN_WIDTH // 2, 350))
        screen.blit(score_value, score_value_rect)
        
        # Statistics 
        stats_text = self.font_tiny.render(f"Fruits sliced: {final_score}", True, WHITE)
        stats_rect = stats_text.get_rect(center=(SCREEN_WIDTH // 2, 420))
        screen.blit(stats_text, stats_rect)
        
        # Restart option
        restart_text = self.font_medium.render("Press R to Restart", True, GREEN)
        restart_rect = restart_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 100))
        screen.blit(restart_text, restart_rect)
        
        # Quit option
        quit_text = self.font_tiny.render("Press Q to Quit", True, WHITE)
        quit_rect = quit_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 40))
        screen.blit(quit_text, quit_rect)
    
    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                return 'restart'
            elif event.key == pygame.K_q:
                return 'quit'
        
        return None