'''
Module Name: save_game.py
Purpose: This module is used to save the user's profile to a save file
Inputs: None
Output: None
Additional code sources: 
Developers: Peter Pham, Ian Wilson
Date: 10/26/2024
Last Modified: 10/26/2024
'''

import time

# saves the current game to the save file (currently hardcoded to save.txt)
def save(ui_manager, save_name):
    with open(save_name, 'w') as file:
        # saves the user's current balance along with any shop purchases they have made
        output = f'{time.time()}\n{ui_manager.cookie_count}\n{ui_manager.base_cookie_per_click}\n{ui_manager.click_multiplier}\n'
        for item in ui_manager.shop_items.values():
            output += f'"{item.name}":{item.purchased_count}\n'
        for upgrade in ui_manager.shop_upgrades.values():
            output += f'"{upgrade.name}":{upgrade.purchased_count}\n'
        file.write(output)
