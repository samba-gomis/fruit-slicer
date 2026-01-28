import pygame

class Inputmanager :
    
    def __init__(self):
        pass # input manager initialization
    
    def get_pressed_letter( self, event ):

        # convert a key press into a letter
        if event.type == pygame.KEYDOWN:
            if event.unicode.isalpha():
                return event.unicode.upper()
        return None
    def handle_key(self , key , objects):
        # check if the pressed letter matches an object

        if key is None:
            return None
        for obj in objects:
            if hasattr(obj , "letter"):  # check if object has a letter
                if obj.letter == key:
                    return obj
        return None