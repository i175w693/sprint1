'''
Module Name: buttons.py
Purpose: This module handles the drawing of all of the buttons for the game
Inputs: None
Output: None
Additional code sources: 
Developers: Ian Wilson, Andrew Uriell, Peter Pham
Date: 10/24/2024
Last Modified: 10/26/2024
'''

import pygame
from game import get_font, WHITE, BUTTON_COLOR

# Base class for buttons
class Button:
    # initializes the button's dimensions, text, and font
    def __init__(self, x, y, width, height, text, font_size, image_file):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.font = get_font(font_size)
        self.image_file = image_file
        self.x = x
        self.y = y

    # Function to draw text
    def draw_text(self, text, font, color, x, y, screen):
        text_obj = font.render(text, True, color)
        screen.blit(text_obj, (x, y))

    # Function to draw the rectangle
    def draw(self, screen):
        if self.image_file != None:
            IMAGE = pygame.transform.scale(pygame.image.load(self.image_file).convert_alpha(), (self.rect.width, self.rect.height))
            screen.blit(IMAGE, self.rect)
        else:
            pygame.draw.rect(screen, BUTTON_COLOR, self.rect)
            self.draw_text(self.text, self.font, WHITE, self.rect.x + 10, self.rect.y + 5, screen)

    # Function to detect if the cookie has been clicked
    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)


# Small Button class
class SmallButton(Button):
    def __init__(self, x, y, text, image_file = None):
        width = int(pygame.display.Info().current_w * 0.2)  # Define width dynamically if needed
        height = int(pygame.display.Info().current_h * 0.05)  # Define height dynamically if needed
        super().__init__(x, y, width, height, text, int(height * 0.5), image_file)  # Call to the parent constructor


# Large Button class
class LargeButton(Button):
    def __init__(self, screen, x, y, text, width, height, image_file = None):
        self.screen = screen  # Store screen reference
        self.x = x
        self.y = y  # Ensure y is stored
        super().__init__(x, y, width, height, text, int(height * 0.5), image_file)  # Initialize the base class

    def draw(self, screen):
        super().draw(self.screen)  # Use the stored screen for drawing



