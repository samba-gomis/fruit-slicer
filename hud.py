import pygame
from constant import *

class hud:
    def __init__(self):
        self.font_large=pygame.font.Font(None, FONT_SIZE_LARGE)
        self.font_medium=pygame.font.Font(None, FONT_SIZE_MEDIUM)
        self.font_small=pygame.font.Font(None, FONT_SIZE_SMALL)

        self.combo_display_time=0
        self.combo_count=0

    def draw_score(self, screen, score):
        """Display current score in top-left corner"""
        txt_score=self.font_medium.render(f"Score: {score}", True, BLACK)
        screen.blit(txt_score, (SCORE_POSITION))

    def draw_strikes(self, screen, strikes, max_strikes):
        """Display remaining lives/hearts in top-right corner"""
        x_start=SCREEN_WIDTH-200 
        y=10
        
        for i in range(max_strikes):
            if i<strikes:
                txt_strike=self.font_medium.render("cross", True, RED)
            else:
                txt_strike=self.font_medium.render("heart", True, RED)

            screen.blit(txt_strike,(x_start+i*50,y))

    def draw_combo(self, screen, combo_count):
        """Display combo message for 1 second when activated"""
        current_time=pygame.time.get_ticks()

        if combo_count>self.combo_count:
            self.combo_count=combo_count
            self.combo_display_time=current_time+1000 

        if current_time<self.combo_display_time:
            combo_text=self.font_large.render(f"COMBO X{combo_count}!", True, BLACK)
            screen.blit(combo_text, (COMBO_POSITION))
        else:
            self.combo_count=0      

    def draw_freeze_timer(self, screen, time_left):
        """Display remaining freeze time in seconds"""
        if time_left>0:
            seconds=time_left/1000

            txt_freeze=self.font_medium.render(f"FREEZE:{seconds:.1f}s", True, WHITE)
            screen.blit(txt_freeze, (10, 10))

    def draw_all(self, screen, score, strikes, max_strikes, combo_count=0, freeze_time=0):
        """Draw all HUD elements at once"""
        self.draw_score(screen, score)
        self.draw_strikes(screen, strikes, max_strikes)
        self.draw_combo(screen, combo_count)
        
        if freeze_time>0:
<<<<<<< HEAD
            self.draw_freeze_timer(screen,freeze_time)
=======
            self.draw_freeze_timer(screen, freeze_time)
>>>>>>> feature/hud
