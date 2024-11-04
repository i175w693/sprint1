'''
Module Name: sound.py
Purpose:
Inputs: 
Output: 
Additional code sources: 
Developers: Ian Wilson, Andrew Uriell, Peter Pham, Michael Oliver, Jack Youngquist
Date: 11/3/2024
Last Modified: 11/3/2024
'''
import pygame

class SoundManager:
    def __init__(self, assets_path='./assets/sounds'):
        # Initialize the mixer module for handling sounds
        pygame.mixer.init()
        self.sounds = {
            'click': pygame.mixer.Sound(f"{assets_path}/click.mp3"),
            'shop': pygame.mixer.Sound(f"{assets_path}/shop2.mp3"),
            'menu-click': pygame.mixer.Sound(f"{assets_path}/menu-click2.mp3"),
        }
    
    def play_sound(self, sound_name):
        """Plays the sound effect if it exists in the sounds dictionary."""
        if sound_name in self.sounds:
            self.sounds[sound_name].play()
        else:
            print(f"Sound '{sound_name}' not found in sounds dictionary.")
