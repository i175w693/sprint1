'''
Module Name: load_game.py
Purpose: This module is used to load the user's profile from a save file
Inputs: None
Output: None
Additional code sources: 
Developers: Peter Pham
Date: 10/26/2024
Last Modified: 10/26/2024
'''

def load(ui_manager):
    with open('save.txt', 'r') as file:
        for number, line in enumerate(file):
            if number == 0:
                ui_manager.cookie_count = int(line.strip())
            else:
                item = line.split(':')
                ui_manager.shop_items[item[0].strip('"')].purchased_count = int(item[1].strip())

