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

def save(ui_manager):
    with open('save.txt', 'w') as file:
        output = f'{ui_manager.cookie_count}\n'
        for item in ui_manager.shop_items.values():
            output += f'"{item.name}":{item.purchased_count}\n'
        file.write(output)