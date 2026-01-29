import pygame
import sys
from src.constant import SCREEN_WIDTH, SCREEN_HEIGHT, FPS
from src.game import Game

def main():
    
    # Initialize pygame
    pygame.init()
    
    # Create the game window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Fruit Ninja Typing Game")
    
    # Create clock for FPS control
    clock = pygame.time.Clock()
    
    # Create game instance
    game = Game(screen, clock)
    
    # Run the game
    game.run()
    
    # Quit pygame properly
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()