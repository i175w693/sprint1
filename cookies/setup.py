import pygame
import sys

# Initialize pygame
pygame.init()

# Set up screen
WIDTH, HEIGHT = 1500, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cookie Clicker")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Font
font = pygame.font.SysFont(None, 55)

# Game variables
cookie_count = 0
cookies_per_click = 1
upgrade_cost = 50
upgrade_multiplier = 2

# Load cookie image
cookie_image = pygame.image.load("cookie.png")
cookie_rect = cookie_image.get_rect(center=(WIDTH // 2, HEIGHT // 2))

# Function to draw text
def draw_text(text, font, color, x, y):
    text_obj = font.render(text, True, color)
    screen.blit(text_obj, (x, y))

# Main game loop
def game_loop():
    global cookie_count, cookies_per_click, upgrade_cost

    while True:
        screen.fill(WHITE)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Check for mouse clicks
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()

                # If cookie is clicked
                if cookie_rect.collidepoint(mouse_pos):
                    cookie_count += cookies_per_click

                # Check for upgrade purchase
                if upgrade_button_rect.collidepoint(mouse_pos) and cookie_count >= upgrade_cost:
                    cookie_count -= upgrade_cost
                    cookies_per_click *= upgrade_multiplier
                    upgrade_cost *= 2  # Increase the cost after each upgrade

        # Draw the cookie
        screen.blit(cookie_image, cookie_rect)

        # Draw cookie count
        draw_text(f"Cookies: {cookie_count}", font, BLACK, 20, 20)

        # Draw upgrade button
        upgrade_button_text = f"Upgrade (Cost: {upgrade_cost})"
        upgrade_button = font.render(upgrade_button_text, True, BLACK)
        upgrade_button_rect = upgrade_button.get_rect(center=(WIDTH // 2, HEIGHT - 50))
        screen.blit(upgrade_button, upgrade_button_rect)

        # Update display
        pygame.display.flip()

# Run the game
if __name__ == "__main__":
    game_loop()
