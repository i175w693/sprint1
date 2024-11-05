'''
Module Name: save_game.py
Purpose: This module is used to save the user's profile to a save file
Inputs: None
Output: None
Additional code sources: 
Developers: Peter Pham
Date: 10/26/2024
Last Modified: 10/26/2024
'''

import time

# saves the current game to the save file (currently hardcoded to save.txt)
def save(ui_manager):
    with open('save.txt', 'w') as file:
        # saves the user's current balance along with any shop purchases they have made
        output = f'{time.time()}\n{ui_manager.cookie_count}\n'
        for item in ui_manager.shop_items.values():
            output += f'"{item.name}":{item.purchased_count}\n'
        file.write(output)