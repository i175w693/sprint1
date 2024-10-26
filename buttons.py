'''
Module Name: buttons.py
Purpose: This module handles drawing all of the buttons for the game
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
    def __init__(self, x, y, width, height, text, font_size):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.font = get_font(font_size)

    # Function to draw text
    def draw_text(self, text, font, color, x, y):
        text_obj = font.render(text, True, color)
        self.screen.blit(text_obj, (x, y))

    def draw(self, screen):
        pygame.draw.rect(screen, BUTTON_COLOR, self.rect)
        self.draw_text(self.text, self.font, WHITE, self.rect.x + 10, self.rect.y + 5)

    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)

# Small Button class
class SmallButton(Button):
    def __init__(self, x, y, text):
        super().__init__(x, y, int(WIDTH * 0.2), int(HEIGHT * 0.05), text, int(WIDTH * 0.03))

# Large Button class with count
class LargeButton(Button):
    def __init__(self, screen, x, y, text, WIDTH, HEIGHT, initial_count=0):
        super().__init__(x, y, int(WIDTH * 0.3), int(HEIGHT * 0.1), text, int(WIDTH * 0.04))
        self.count = initial_count  # Initialize purchase count
        self.screen = screen

    # Function to draw text
    def draw_text(self, text, font, color, x, y):
        text_obj = font.render(text, True, color)
        self.screen.blit(text_obj, (x, y))

    def draw(self, screen):
        super().draw(screen)  # Draw the button
        count_text = f"x{self.count}"  # Display count
        self.draw_text(count_text, self.font, WHITE, self.rect.x + self.rect.width - 40, self.rect.y + 5)  # Position count on the right side
