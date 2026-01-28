import pygame
import sys
from constant import FREEZE_DURATION_MAX
from constant import *
from menu import Menu
from game_over import GameOver
from spawn_manager import *
from hud import *


class Game:
    
    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.running = True
        
        # Game state
        self.state = STATE_MENU
        self.menu = Menu()
        self.game_over_screen = GameOver()
        
        # Game variables
        self.score = 0
        self.strikes = 0
        self.game_over_reason = "strikes"
        self.hud=hud()
        
        # Game objects lists
        self.fruits = []
        self.bombs = []
        self.ices = []
        
        # Freeze mechanic
        self.is_frozen = False
        self.freeze_end_time = 0
        
        # Spawn control
        self.last_spawn_time = 0
        self.current_spawn_delay = SPAWN_DELAY
        
        # Combo system
        self.last_hit_times = []
        self.combo_display_time = 0
        self.current_combo = 0
    
    
    def reset_game(self):
        self.score = 0
        self.strikes = 0
        self.game_over_reason = "strikes"
        self.fruits = []
        self.bombs = []
        self.ices = []
        self.is_frozen = False
        self.freeze_end_time = 0
        self.last_spawn_time = pygame.time.get_ticks()
        self.current_spawn_delay = SPAWN_DELAY
        self.last_hit_times = []
        self.combo_display_time = 0
        self.current_combo = 0
    
    def run(self):
        while self.running:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                
                # Handle input based on game state
                if self.state == STATE_MENU:
                    action = self.menu.handle_input(event)
                    if action == 'start':
                        self.reset_game()
                        self.state = STATE_PLAYING
                    elif action == 'quit':
                        self.running = False
                
                elif self.state == STATE_PLAYING:
                    if event.type == pygame.KEYDOWN:
                        self.handle_key_press(event)
                
                elif self.state == STATE_GAME_OVER:
                    action = self.game_over_screen.handle_input(event)
                    if action == 'restart':
                        self.reset_game()
                        self.state = STATE_PLAYING
                    elif action == 'quit':
                        self.running = False
            
            # Update and draw based on state
            if self.state == STATE_MENU:
                self.menu.draw(self.screen)
            
            elif self.state == STATE_PLAYING:
                self.update()
                self.draw()
            
            elif self.state == STATE_GAME_OVER:
                self.game_over_screen.draw(self.screen, self.score, self.game_over_reason)
            
            # Update display and tick
            pygame.display.flip()
            self.clock.tick(FPS)
    
    def update(self):
        """Update game logic"""
        current_time = pygame.time.get_ticks()
        
        # Check freeze status
        if self.is_frozen and current_time >= self.freeze_end_time:
            self.is_frozen = False
        
        # Only update if not frozen
        if not self.is_frozen:
            # Update all fruits
            for fruit in self.fruits[:]:
                if fruit.update():
                    # Fruit went off screen - missed!
                    self.fruits.remove(fruit)
                    self.add_strike()
            
            # Update all bombs
            for bomb in self.bombs[:]:
                if bomb.update():
                    self.bombs.remove(bomb)
            
            # Update all ice objects
            for ice in self.ices[:]:
                if ice.update():
                    self.ices.remove(ice)
            
            # Spawn new objects
            self.spawn_objects()
        
        # Update combo display timer
        if self.combo_display_time > 0:
            self.combo_display_time -= 1
    
    def draw(self):
        self.screen.fill(WHITE)
        
        # Draw all objects
        for fruit in self.fruits:
            fruit.draw(self.screen)
        
        for bomb in self.bombs:
            bomb.draw(self.screen)
        
        for ice in self.ices:
            ice.draw(self.screen)
        
        # Draw freeze indicator if active
        freeze_time=0

        if self.is_frozen:
           freeze_time=self.freeze_end_time-pygame.time.get_ticks()

        # Draw score, strikes and combo
        self.hud.draw_all(self.screen, self.score, self.strikes, MAX_STRIKES, self.current_combo, freeze_time)

    def handle_key_press(self, event):
        # Get the letter pressed (convert to uppercase)
        if event.unicode.isalpha():
            letter = event.unicode.upper()
            
            # Check all objects for matching letter
            hit_object = None
            object_type = None
            
            # Check fruits
            for fruit in self.fruits:
                if fruit.is_hit(letter):
                    hit_object = fruit
                    object_type = 'fruit'
                    self.fruits.remove(fruit)
                    break
            
            # Check bomb
            if not hit_object:
                for bomb in self.bombs:
                    if bomb.letter == letter:
                        hit_object = bomb
                        object_type = 'bomb'
                        self.bombs.remove(bomb)
                        break
            
            # Check ice
            if not hit_object:
                for ice in self.ices:
                    if ice.letter == letter:
                        hit_object = ice
                        object_type = 'ice'
                        self.ices.remove(ice)
                        break
            
            # Process the hit
            if hit_object:
                if object_type == 'fruit':
                    self.add_score()
                elif object_type == 'bomb':
                    self.trigger_bomb()
                elif object_type == 'ice':
                    self.trigger_freeze()
    
    def spawn_objects(self):
        """Spawn new objects based on timer"""
        if not hasattr(self, "spawn_manager"):
            self.spawn_manager=SpawnManager()
        
        if self.spawn_manager.should_spawn():
            obj=self.spawn_manager.spawn_object()

            if obj.__class__.__name__=="Fruit":
                self.fruits.append(obj)
            elif obj.__class__.__name__=="Bomb":
                self.bombs.append(obj)
            elif obj.__class__.__name__=="Ice":
                self.ices.append(obj)

        self.spawn_manager.increase_difficulty(self.score)
    

    
    def add_score(self):
        current_time = pygame.time.get_ticks()
        
        # Add to hit times for combo detection
        self.last_hit_times.append(current_time)
        
        # Remove old hits outside combo window
        self.last_hit_times = [t for t in self.last_hit_times 
                               if current_time - t <= COMBO_TIME_WINDOW]
        
        # Check for combo
        if len(self.last_hit_times) >= 2:
            combo_count = len(self.last_hit_times)
            bonus = combo_count - 1
            self.score += bonus
            self.current_combo = combo_count
            self.combo_display_time = 60  # Display for 1 second at 60 FPS
        
        # Always add base point
        self.score += 1
    
    def add_strike(self):
        """Add a strike for missing a fruit"""
        self.strikes += 1
        
        # Check for game over
        if self.strikes >= MAX_STRIKES:
            self.game_over_reason = "strikes"
            self.state = STATE_GAME_OVER
    
    def trigger_bomb(self):
        """Handle bomb hit - instant game over"""
        self.game_over_reason = "bomb"
        self.state = STATE_GAME_OVER
    
    def trigger_freeze(self):
        """Handle ice hit - freeze time"""
        import random
        freeze_duration = random.randint(FREEZE_DURATION_MIN, FREEZE_DURATION_MAX)
        self.is_frozen = True
        self.freeze_end_time = pygame.time.get_ticks() + (freeze_duration * 1000)