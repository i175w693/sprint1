'''
Module Name: cookie.py
Purpose: Handles the drawing of the clickable cookie on the side of the screen, as well as the click animation
Inputs: None
Output: None
Additional code sources: 
Developers: Ian Wilson, Andrew Uriell, Peter Pham, Jack Youngquist
Date: 10/24/2024
Last Modified: 11/24/2024
'''

from game import *

BLACK = (0, 0, 0)
shimmer_png_path = "./assets/cookie_shimmer/cookie_shine"

# Class for managing the cookie
class Cookie:
    # initializes the image and dimensions for the clickable cookie
    def __init__(self, image_path, size_percent, WIDTH, HEIGHT):
        self.image = pygame.image.load(image_path)
        self.size = int(WIDTH * size_percent)
        self.image = pygame.transform.scale(self.image, (self.size, self.size))
        self.rect = self.image.get_rect(center=(WIDTH * 0.165, HEIGHT // 2))  # Centered in the left partition
        self.angle = 0  # Initialize rotation angle
        #load all sprites for shine animation
        self.shine_sprites = [pygame.image.load(f'{shimmer_png_path}1.png'),pygame.image.load(f'{shimmer_png_path}2.png'),pygame.image.load(f'{shimmer_png_path}3.png'),
                      pygame.image.load(f'{shimmer_png_path}4.png'),pygame.image.load(f'{shimmer_png_path}5.png'),pygame.image.load(f'{shimmer_png_path}6.png'),
                      pygame.image.load(f'{shimmer_png_path}7.png'),pygame.image.load(f'{shimmer_png_path}8.png'),pygame.image.load(f'{shimmer_png_path}9.png'),
                      pygame.image.load(f'{shimmer_png_path}10.png')]
        self.current_shine = 0 #stating point of animation
        self.image2 = pygame.transform.scale(self.shine_sprites[self.current_shine], (self.size, self.size)) #scale sprite to correct size
        self.is_animating = False #false until we want it to animate


    # renders a cookie onto the screen that rotates
    def draw(self, screen):
        rotated_image = pygame.transform.rotate(self.image, self.angle)
        new_rect = rotated_image.get_rect(center=self.rect.center)  # Center at original position
        screen.blit(rotated_image, new_rect.topleft)
        # pygame.draw.rect(screen, BLACK, self.rect, 2)  # Draw rectangle around the cookie

    # updates the angle of rotation for the cookie
    def update_rotation(self):
        self.angle += 1  # Adjust the speed of rotation (1 degree per frame)
        if self.angle >= 360:  # Reset angle to keep it manageable
            self.angle = 0

    #iterates through current_shine until its reached the last sprite
    def update_shimmer(self):
        if self.is_animating == True:
            self.current_shine += 1 #change value it increments by to change speed (0.1-1) (slowest-fastest)
            if self.current_shine >= len(self.shine_sprites): #check if we've gone past all sprites then reset
                self.current_shine = 0
                self.is_animating = False
            self.image2 = pygame.transform.scale(self.shine_sprites[int(self.current_shine)], (self.size, self.size)) #scale sprite

    def animate(self): #begin animating sprite
        self.is_animating = True
    def draw_shimmer(self, screen): #draw current sprite
        screen.blit(self.image2, self.rect)