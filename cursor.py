'''
Module Name: cursor.py
Purpose: Handles the drawing of custom cursor
Inputs: None
Output: None
Additional code sources: 
Developers: Jack Youngquist
Date: 11/04/2024
Last Modified: 11/04/2024
'''

from game import *
sprites_png_path = "./assets/cursor/cursor"

# Class for managing Cursor
class Cursor:
    # initializes the image and dimensions for cursor
    def __init__(self, image_path, size_percent, WIDTH, HEIGHT):
        self.image = pygame.image.load(image_path)
        self.size = int(WIDTH * size_percent)
        self.root = pygame.display.get_surface()
        self.x = 0
        self.y = 0
        #list with all cursor sprites for animation
        self.sprites = [pygame.image.load(f'{sprites_png_path}1.png'), pygame.image.load(f'{sprites_png_path}2.png'),pygame.image.load(f'{sprites_png_path}3.png'),
                        pygame.image.load(f'{sprites_png_path}4.png'),pygame.image.load(f'{sprites_png_path}5.png')]
        self.current_sprite = 0
        self.image = pygame.transform.scale(self.sprites[self.current_sprite], (self.size, self.size))
        self.is_animating = False

    def draw(self):
        self.root.blit(self.image, (self.x, self.y))
    
    def update(self): #keeps cursor location updated
        self.x = pygame.mouse.get_pos()[0] -29 #subtract to adjust sprite more accuretely over cursor
        self.y = pygame.mouse.get_pos()[1] -20

    def update_sprite(self): #update to next sprite in animation if animating
        if self.is_animating == True:
            self.current_sprite += 1
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False
            self.image = pygame.transform.scale(self.sprites[int(self.current_sprite)], (self.size, self.size))

    def animate(self): #set is_animating to true
        self.is_animating = True