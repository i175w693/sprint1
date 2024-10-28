'''
Module Name: cookie.py
Purpose: Handles the drawing of the clickable cookie on the side of the screen
Inputs: None
Output: None
Additional code sources: 
Developers: Ian Wilson, Andrew Uriell, Peter Pham
Date: 10/24/2024
Last Modified: 10/26/2024
'''

from game import *

BLACK = (0, 0, 0)

# Class for managing the cookie
class Cookie:
    # initializes the image and dimensions for the clickable cookie
    def __init__(self, image_path, size_percent, WIDTH, HEIGHT):
        self.image = pygame.image.load(image_path)
        self.size = int(WIDTH * size_percent)
        self.image = pygame.transform.scale(self.image, (self.size, self.size))
        self.rect = self.image.get_rect(center=(WIDTH * 0.165, HEIGHT // 2))  # Centered in the left partition
        self.angle = 0  # Initialize rotation angle

    # renders a cookie onto the screen that rotates
    def draw(self, screen):
        rotated_image = pygame.transform.rotate(self.image, self.angle)
        new_rect = rotated_image.get_rect(center=self.rect.center)  # Center at original position
        screen.blit(rotated_image, new_rect.topleft)
        pygame.draw.rect(screen, BLACK, self.rect, 2)  # Draw rectangle around the cookie

    # updates the angle of rotation for the cookie
    def update_rotation(self):
        self.angle += 1  # Adjust the speed of rotation (1 degree per frame)
        if self.angle >= 360:  # Reset angle to keep it manageable
            self.angle = 0