'''
Module Name: load_game.py
Purpose: This module is used to load the user's profile from a save file
Inputs: None
Output: Returns None if a save file does not exist
Additional code sources: 
Developers: Peter Pham, Jack youngquist
Date: 10/26/2024
Last Modified: 10/26/2024
'''

# function to load the user's save file (currently hardcoded to save.txt)
def load(ui_manager):
    try:
        with open('save.txt', 'r') as file:
            for number, line in enumerate(file):
                if number == 0:
                    ui_manager.cookie_count = int(line.strip())
                else:
                    item = line.split(':')
                    item_name = item[0].strip('"')
                    purchased_count = int(item[1].strip())
                    
                    shop_item = ui_manager.shop_items[item_name]
                    shop_item.purchased_count = purchased_count
                    
                    ui_manager.upgrades_acquired.append(shop_item)
                    return True
    # if not save file exists, return and start a new game
    except FileNotFoundError:
        print(f'Save file not found!')
        return None