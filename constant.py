# Window settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Colors (RGB format)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 100, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
PURPLE = (128, 0, 128)
LIGHT_BLUE = (173, 216, 230)
DARK_GRAY = (50, 50, 50)

# Fruit colors (random selection)
FRUIT_COLORS = [RED, GREEN, ORANGE, PURPLE]

# Game objects settings
FRUIT_RADIUS = 30
BOMB_RADIUS = 30
ICE_RADIUS = 30
# Fruit image settings
FRUIT_DISPLAY_SIZE = 64  # pixel size to scale fruit images to
FRUIT_IMAGES_DIR = "assets/images/fruits"  # folder to place fruit PNG/JPG files

# Speed settings
FRUIT_SPEED = 3
BOMB_SPEED = 3
ICE_SPEED = 3

# Spawn settings
SPAWN_DELAY = 1500  # milliseconds between spawns
SPAWN_X_MIN = 50  # minimum X position for spawn
SPAWN_X_MAX = SCREEN_WIDTH - 50  # maximum X position for spawn
SPAWN_Y = SCREEN_HEIGHT + 50  # spawn below screen
SPEED_X_MIN = -2  # minimum horizontal speed
SPEED_X_MAX = 2  # maximum horizontal speed

# Spawn probabilities (must sum to 100)
FRUIT_SPAWN_CHANCE = 70  # 70% chance
BOMB_SPAWN_CHANCE = 15   # 15% chance
ICE_SPAWN_CHANCE = 15    # 15% chance

# Game rules
MAX_STRIKES = 3
FREEZE_DURATION_MIN = 3  # seconds
FREEZE_DURATION_MAX = 5  # seconds
COMBO_TIME_WINDOW = 500  # milliseconds to detect combo

# Available letters for objects
LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Font sizes
FONT_SIZE_LARGE = 72
FONT_SIZE_MEDIUM = 48
FONT_SIZE_SMALL = 36
FONT_SIZE_TINY = 24

# positions
SCORE_POSITION = (10, 10)
STRIKES_POSITION = (SCREEN_WIDTH - 150, 10)
COMBO_POSITION = (SCREEN_WIDTH // 2 - 100, 100)
FREEZE_POSITION = (SCREEN_WIDTH // 2 - 100, 100)
# Game states
STATE_MENU = "menu"
STATE_PLAYING = "playing"
STATE_GAME_OVER = "game_over"

# Difficulty progression
DIFFICULTY_INCREASE_SCORE = 10  # increase difficulty every 10 points
SPEED_INCREASE = 0.5  # speed added per difficulty level
SPAWN_DELAY_DECREASE = 100  # milliseconds reduced per difficulty level
MIN_SPAWN_DELAY = 500  # minimum spawn delay