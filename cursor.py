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

# Class for managing Cursor
class Cursor:
    # initializes the image and dimensions for cursor
    def __init__(self, image_path, size_percent, WIDTH, HEIGHT):
        self.image = pygame.image.load(image_path)
        self.size = int(WIDTH * size_percent)
        self.image = pygame.transform.scale(self.image, (self.size, self.size))
        self.root = pygame.display.get_surface()
        self.x = 0
        self.y = 0
    def draw(self):
        self.root.blit(self.image, (self.x, self.y))
    
    def update(self):
        self.x = pygame.mouse.get_pos()[0] -29 #subtract to adjust sprite more accuretely over cursor
        self.y = pygame.mouse.get_pos()[1] -20