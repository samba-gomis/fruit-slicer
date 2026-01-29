import pygame

class SoundManager:
    def __init__(self):
        #Initialize sound
        pygame.mixer.init()
        
        #import sounds files
        self.slice_sound=pygame.mixer.Sound("slice.mp3")
        self.bomb_sound=pygame.mixer.Sound("bomb.wav")
        self.ice_sound=pygame.mixer.Sound("ice.wav")
        self.combo_sound=pygame.mixer.Sound("combo.mp3")
        self.strike_sound=pygame.mixer.Sound("miss.wav")
        self.game_over_sound=pygame.mixer.Sound("game_over.wav")

        #set sounds volumes
        self.slice_sound.set_volume(1)
        self.bomb_sound.set_volume(1)
        self.ice_sound.set_volume(1)
        self.combo_sound.set_volume(1)
        self.strike_sound.set_volume(1)
        self.game_over_sound.set_volume(1)

        #set background loop music
        self.menu_music=("background_sound_menu.wav")
        self.game_music=("background_sound_game.wav")
        self.current_music=None

    #play each sounds
    def sound_slice(self):
        if self.slice_sound:
            self.slice_sound.play()
    
    def sound_bomb(self):
        if self.bomb_sound:
            self.bomb_sound.play()
    
    def sound_ice(self):
        if self.ice_sound:
            self.ice_sound.play()
    
    def sound_combo(self):
        if self.combo_sound:
            self.combo_sound.play()
    
    def sound_strike(self):
        if self.strike_sound:
            self.strike_sound.play()
    
    def sound_game_over(self):
        if self.game_over_sound:
            self.game_over_sound.play()

    #music management, play, stop and volume
    def play_menu_music(self):
        if self.current_music!="menu":
            pygame.mixer.music.load(self.menu_music)
            pygame.mixer.music.set_volume(0.1)
            pygame.mixer.music.play(-1)
            self.current_music="menu"

    def play_game_music(self):
         if self.current_music!="game":
            pygame.mixer.music.load(self.game_music)
            pygame.mixer.music.set_volume(0.1)
            pygame.mixer.music.play(-1)
            self.current_music="game"
    
    def stop_music(self):
        pygame.mixer.music.stop()
        self.current_music=None
    
    def music_volume(self):
        pygame.mixer.music.set_volume(0.2)
