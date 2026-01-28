import pygame
import random
from constant import *
from fruit import Fruit
from bomb import Bomb
from ice import Ice

class SpawnManager:
    def __init__(self):
       self.spawn_delay=SPAWN_DELAY  
       self.spawn_min=SPAWN_X_MIN
       self.spawn_max=SPAWN_X_MAX 
       self.spawn_y=SPAWN_Y
       self.last_spawn_time=pygame.time.get_ticks()
       
    def should_spawn(self):    
        current_time=pygame.time.get_ticks()
        time_elapsed=(current_time-self.last_spawn_time)
        if time_elapsed>=self.spawn_delay:
            self.last_spawn_time=current_time
            return True
        return False

    def spawn_object(self):
        x=random.randint(self.spawn_min,self.spawn_max)
        letter=random.choice(LETTERS)
        rand=random.randint(0,99)

        if rand<FRUIT_SPAWN_CHANCE:
            return Fruit(x,letter)
        elif rand<FRUIT_SPAWN_CHANCE+rand<BOMB_SPAWN_CHANCE:
            return Bomb(x,"b")
        else:
            return Ice(x,"i")
        

    def increase_difficulty(self,score):
        difficulty_level=score//DIFFICULTY_INCREASE_SCORE
        self.spawn_delay=max(MIN_SPAWN_DELAY,SPAWN_DELAY-(difficulty_level*SPAWN_DELAY_DECREASE))