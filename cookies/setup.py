import pygame
import sys
import time

# Initialize pygame
pygame.init()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)  # Color for partition lines
BUTTON_COLOR = (100, 100, 255)  # Color for buttons

# Font initialization
def get_font(size):
    return pygame.font.SysFont(None, size)

# Class for Shop Items
class ShopItem:
    def __init__(self, name, cost, cps):
        self.name = name
        self.cost = cost
        self.cps = cps
        self.purchased_count = 0  # Track how many times this item has been purchased

# Class for managing the cookie
class Cookie:
    def __init__(self, image_path, size_percent):
        self.image = pygame.image.load(image_path)
        self.size = int(WIDTH * size_percent)
        self.image = pygame.transform.scale(self.image, (self.size, self.size))
        self.rect = self.image.get_rect(center=(WIDTH * 0.165, HEIGHT // 2))  # Centered in the left partition
        self.angle = 0  # Initialize rotation angle

    def draw(self, screen):
        rotated_image = pygame.transform.rotate(self.image, self.angle)
        new_rect = rotated_image.get_rect(center=self.rect.center)  # Center at original position
        screen.blit(rotated_image, new_rect.topleft)
        pygame.draw.rect(screen, BLACK, self.rect, 2)  # Draw rectangle around the cookie

    def update_rotation(self):
        self.angle += 1  # Adjust the speed of rotation (1 degree per frame)
        if self.angle >= 360:  # Reset angle to keep it manageable
            self.angle = 0

# Base class for buttons
class Button:
    def __init__(self, x, y, width, height, text, font_size):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.font = get_font(font_size)

    def draw(self, screen):
        pygame.draw.rect(screen, BUTTON_COLOR, self.rect)
        draw_text(self.text, self.font, WHITE, self.rect.x + 10, self.rect.y + 5)

    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)

# Small Button class
class SmallButton(Button):
    def __init__(self, x, y, text):
        super().__init__(x, y, int(WIDTH * 0.2), int(HEIGHT * 0.05), text, int(WIDTH * 0.03))

# Large Button class with count
class LargeButton(Button):
    def __init__(self, x, y, text, initial_count=0):
        super().__init__(x, y, int(WIDTH * 0.3), int(HEIGHT * 0.1), text, int(WIDTH * 0.04))
        self.count = initial_count  # Initialize purchase count

    def draw(self, screen):
        super().draw(screen)  # Draw the button
        count_text = f"x{self.count}"  # Display count
        draw_text(count_text, self.font, WHITE, self.rect.x + self.rect.width - 40, self.rect.y + 5)  # Position count on the right side

# UIManager class for handling all UI components
class UIManager:
    def __init__(self):
        self.cookie_count = 0
        self.cookies_per_click = 1
        self.upgrades_acquired = []
        self.shop_items = [
            ShopItem("Grandma", 100, 1),
            ShopItem("Factory", 500, 5),
        ]
        self.buttons = self.create_buttons()

    def create_buttons(self):
        buttons = []
        for idx, item in enumerate(self.shop_items):
            button = LargeButton(WIDTH - int(WIDTH * 0.25), int(HEIGHT * 0.15) + idx * int(HEIGHT * 0.1), item.name)
            buttons.append((button, item))
        return buttons

    def handle_cookie_click(self):
        self.cookie_count += self.cookies_per_click
        print(f"Cookie clicked! Total cookies: {self.cookie_count}")  # Log message for cookie clicks

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
        font_size = int(WIDTH * 0.03)  # Dynamic font size based on width
        font = get_font(font_size)
        draw_text(f"Cookies: {self.cookie_count}", font, BLACK, int(WIDTH * 0.01), int(HEIGHT * 0.01))

    def draw_upgrades(self, screen):
        font_size = int(WIDTH * 0.03)  # Dynamic font size based on width
        font = get_font(font_size)
        draw_text("Upgrades Acquired:", font, BLACK, int(WIDTH * 0.4), int(HEIGHT * 0.05))
        for idx, upgrade in enumerate(self.upgrades_acquired):
            draw_text(f"{upgrade.name} (CPS: {upgrade.cps})", font, BLACK, int(WIDTH * 0.4), int(HEIGHT * 0.15) + idx * int(HEIGHT * 0.05))

    def draw_shop(self, screen):
        font_size = int(WIDTH * 0.03)  # Dynamic font size based on width
        font = get_font(font_size)
        draw_text("Shop:", font, BLACK, int(WIDTH * 0.75), int(HEIGHT * 0.05))
        for button, _ in self.buttons:
            button.draw(screen)  # Draw each button

    def draw_partitions(self, screen):
        # Draw vertical lines to partition the screen
        pygame.draw.line(screen, GRAY, (WIDTH * 0.33, 0), (WIDTH * 0.33, HEIGHT), 2)  # Left partition
        pygame.draw.line(screen, GRAY, (WIDTH * 0.66, 0), (WIDTH * 0.66, HEIGHT), 2)  # Right partition

# Function to draw text
def draw_text(text, font, color, x, y):
    text_obj = font.render(text, True, color)
    screen.blit(text_obj, (x, y))

# Main game class
class Game:
    def __init__(self):
        self.ui_manager = UIManager()
        self.cookie = Cookie("cookie.png", 0.2)  # Increase size to 20% of the screen width
        self.last_time = time.time()  # Track time for CPS

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

                # If shop item is clicked
                self.ui_manager.handle_shop_click(mouse_pos)

            # Handle window resizing dynamically
            if event.type == pygame.VIDEORESIZE:
                global WIDTH, HEIGHT  # Access the global variables
                WIDTH, HEIGHT = event.w, event.h
                screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
                self.cookie = Cookie("cookie.png", 0.2)  # Re-initialize cookie after resizing
                self.ui_manager = UIManager()  # Re-initialize UIManager to adjust button positions

    def run(self):
        while True:
            current_time = time.time()
            if current_time - self.last_time >= 1:  # Every second
                self.ui_manager.cookie_count += self.ui_manager.cookies_per_second()
                self.last_time = current_time

            screen.fill(WHITE)
            self.handle_events()

            # Draw UI elements
            self.cookie.draw(screen)
            self.cookie.update_rotation()
            self.ui_manager.draw_stats(screen)
            self.ui_manager.draw_upgrades(screen)
            self.ui_manager.draw_shop(screen)
            self.ui_manager.draw_partitions(screen)

            # Update display
            pygame.display.flip()

# Set up screen to dynamically fetch the display's width and height
WIDTH, HEIGHT = pygame.display.Info().current_w, pygame.display.Info().current_h
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)  # Allow resizing
pygame.display.set_caption("Cookie Clicker")

# Run the game
if __name__ == "__main__":
    game = Game()
    game.run()

