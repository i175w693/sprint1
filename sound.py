'''
Module Name: sound.py
Purpose:
Inputs: 
Output: 
Additional code sources: 
Developers: Ian Wilson, Andrew Uriell, Peter Pham, Michael Oliver, Jack Youngquist
Date: 11/3/2024
Last Modified: 11/8/2024
'''
import pygame

# Global variable to control the sound state (True = sound on, False = sound off)
sound_enabled = True

class SoundManager:
    def __init__(self, assets_path='./assets/sounds'):
        # Initialize the mixer module for handling sounds
        pygame.mixer.init()
        self.toggle_music = False
        self.music_playing = True
        self.sounds = {
            'click': pygame.mixer.Sound(f"{assets_path}/click.mp3"),
            'shop': pygame.mixer.Sound(f"{assets_path}/shop2.mp3"),
            'menu-click': pygame.mixer.Sound(f"{assets_path}/menu-click2.mp3"),
        }
    
    def play_sound(self, sound_name):
        """Plays the sound effect if it exists in the sounds dictionary and sound is enabled."""
        global sound_enabled  # Use the global variable to check sound state
        if sound_enabled and sound_name in self.sounds:
            self.sounds[sound_name].play()
        elif not sound_enabled:
            print("Sound is disabled. No sound will play.")
        else:
            print(f"Sound '{sound_name}' not found in sounds dictionary.")
    
    def toggle_sound(self):
        """Toggles the global sound state and manages background music playback."""
        global sound_enabled
        sound_enabled = not sound_enabled  # Toggle sound state

        if sound_enabled:
            # Resume background music if enabled
            if not pygame.mixer.music.get_busy():  # Check if music is already playing
                self.play_music()
        else:
            # Stop background music if disabled
            pygame.mixer.music.stop()

        print("Sound Enabled:", sound_enabled)
       
    def play_music(self, assets_path='./assets/sounds'):
        """Plays the background music on loop if sound is enabled."""
        if self.music_playing:
            pygame.mixer.music.load(f"{assets_path}/smooth-coffee.mp3")
            pygame.mixer.music.play(loops=-1)  # Loop forever
            print("Background music started.")
        else:
            pygame.mixer.music.stop()  # Stop the music
            print("Sound is disabled. Background music will not play.")


