'''
Module Name: game.py
Purpose: This module is the main game class for the Cookie clicker game.
Inputs: None
Output: None
Additional code sources: 
Developers: Ian Wilson, Andrew Uriell, Peter Pham
Date: 10/24/2024
Last Modified: 10/26/2024
'''

import pygame
import sys
import time

from shop import *
from cookie import Cookie

# Initialize pygame
pygame.init()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)  # Color for partition lines
BUTTON_COLOR = (100, 100, 255)  # Color for buttons

ASSETS_FILEPATH = './assets'

# Font initialization
def get_font(size):
    return pygame.font.SysFont(None, size)

from buttons import Button, SmallButton, LargeButton

# UIManager class for handling all UI components
class UIManager:
    def __init__(self):
        self.WIDTH = pygame.display.Info().current_w
        self.HEIGHT = pygame.display.Info().current_h
        self.cookie_count = 0
        self.cookies_per_click = 1
        self.upgrades_acquired = []
        self.shop_items = [
            ShopItem("Grandma", 100, 1),
            ShopItem("Factory", 500, 5),
        ]
        # Set up screen to dynamically fetch the display's width and height
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT), pygame.RESIZABLE)  # Allow resizing
        pygame.display.set_caption("Cookie Clicker")
        self.buttons = self.create_buttons()
        self.font_size = int(self.WIDTH * 0.03)  # Dynamic font size based on width
        self.font = get_font(self.font_size)

    # Function to draw text
    def draw_text(self, text, font, color, x, y):
        text_obj = font.render(text, True, color)
        self.screen.blit(text_obj, (x, y))

    def create_buttons(self):
        buttons = []
        for idx, item in enumerate(self.shop_items):
            button = LargeButton(self.screen, self.WIDTH - int(self.WIDTH * 0.25), int(self.HEIGHT * 0.15) + idx * int(self.HEIGHT * 0.1), item.name, self.WIDTH, self.HEIGHT)
            buttons.append((button, item))
        return buttons

    def handle_cookie_click(self):
        self.cookie_count += self.cookies_per_click
        # print(f"Cookie clicked! Total cookies: {self.cookie_count}")  # Log message for cookie clicks

    def handle_shop_click(self, mouse_pos):
        for button, item in self.buttons:
            if button.is_clicked(mouse_pos) and self.cookie_count >= item.cost:
                self.cookie_count -= item.cost
                item.purchased_count += 1  # Increment the count for this item
                button.count = item.purchased_count  # Update button's count display
                self.upgrades_acquired.append(item)

    def cookies_per_second(self):
        return sum(item.cps * item.purchased_count for item in self.shop_items)

    def draw_stats(self, screen):
        self.draw_text(f"Cookies: {self.cookie_count}", self.font, BLACK, int(self.WIDTH * 0.01), int(self.HEIGHT * 0.01))

    def draw_upgrades(self, screen):
        font_size = int(self.WIDTH * 0.03)  # Dynamic font size based on width
        font = get_font(font_size)
        self.draw_text("Upgrades Acquired:", font, BLACK, int(self.WIDTH * 0.4), int(self.HEIGHT * 0.05))
        for idx, upgrade in enumerate(self.upgrades_acquired):
            self.draw_text(f"{upgrade.name} (CPS: {upgrade.cps})", font, BLACK, int(self.WIDTH * 0.4), int(self.HEIGHT * 0.15) + idx * int(self.HEIGHT * 0.05))

    def draw_shop(self, screen):
        font_size = int(self.WIDTH * 0.03)  # Dynamic font size based on width
        font = get_font(font_size)
        self.draw_text("Shop:", font, BLACK, int(self.WIDTH * 0.75), int(self.HEIGHT * 0.05))
        for button, _ in self.buttons:
            button.draw(screen)  # Draw each button

    def draw_partitions(self, screen):
        # Draw vertical lines to partition the screen
        pygame.draw.line(screen, GRAY, (self.WIDTH * 0.33, 0), (self.WIDTH * 0.33, self.HEIGHT), 2)  # Left partition
        pygame.draw.line(screen, GRAY, (self.WIDTH * 0.66, 0), (self.WIDTH * 0.66, self.HEIGHT), 2)  # Right partition

# Main game class
class Game:
    def __init__(self):
        self.ui_manager = UIManager()
        self.cookie = Cookie(f"{ASSETS_FILEPATH}/cookie.png", 0.2, self.ui_manager.WIDTH, self.ui_manager.HEIGHT)  # Increase size to 20% of the screen width
        self.last_time = time.time()  # Track time for CPS
        self.clock = pygame.time.Clock() # Used to limit game to 20 ticks per second

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Check for mouse clicks
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()

                # If cookie is clicked
                if self.cookie.rect.collidepoint(mouse_pos):
                    self.ui_manager.handle_cookie_click()
                    self.ui_manager.draw_text(f"+{self.ui_manager.cookies_per_click}", self.ui_manager.font, BLACK, int(mouse_pos[0]), int(mouse_pos[1]))

                # If shop item is clicked
                self.ui_manager.handle_shop_click(mouse_pos)

            # Handle window resizing dynamically
            if event.type == pygame.VIDEORESIZE:
                self.ui_manager.WIDTH, self.ui_manager.HEIGHT = event.w, event.h
                self.ui_manager.screen = pygame.display.set_mode((self.ui_manager.WIDTH, self.ui_manager.HEIGHT), pygame.RESIZABLE)
                self.cookie = Cookie(f"{ASSETS_FILEPATH}/cookie.png", 0.2, self.ui_manager.WIDTH, self.ui_manager.HEIGHT)  # Re-initialize cookie after resizing
                self.ui_manager = UIManager()  # Re-initialize UIManager to adjust button positions

    def run(self):
        while True:
            current_time = time.time()
            if current_time - self.last_time >= 1:  # Every second
                self.ui_manager.cookie_count += self.ui_manager.cookies_per_second()
                self.last_time = current_time

            self.ui_manager.screen.fill(WHITE)
            screen = self.ui_manager.screen
            self.cookie.draw(screen)
            self.handle_events()

            # Draw UI elements
            self.cookie.update_rotation()
            self.ui_manager.draw_stats(screen)
            self.ui_manager.draw_upgrades(screen)
            self.ui_manager.draw_shop(screen)
            self.ui_manager.draw_partitions(screen)

            # Update display
            pygame.display.flip()
        
            # limits game to 20 ticks per second
            self.clock.tick(20)
