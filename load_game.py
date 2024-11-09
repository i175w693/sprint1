'''
Module Name: load_game.py
Purpose: This module is used to load the user's profile from a save file
Inputs: None
Output: Returns None if a save file does not exist
Additional code sources: 
Developers: Peter Pham, Jack youngquist, Ian Wilson
Date: 10/26/2024
Last Modified: 10/26/2024
'''

import time

# function to load the user's save file (currently hardcoded to save.txt)
def load(ui_manager):
    try:
        with open('save.txt', 'r') as file:
            for number, line in enumerate(file):
                if number == 0:
                    time_diff = time.time() - float(line.strip())
                elif number == 1:
                    ui_manager.cookie_count = float(line.strip())
                elif number == 2:
                    ui_manager.base_cookie_per_click = float(line.strip())
                elif number == 3:
                    ui_manager.click_multiplier = float(line.strip())
                else:
                    item = line.split(':')
                    item_name = item[0].strip('"')
                    purchased_count = int(item[1].strip())
                    
                     # Determine if the item is in shop_items or shop_upgrades
                    if item_name in ui_manager.shop_items:
                        shop_item = ui_manager.shop_items[item_name]
                        shop_item.purchased_count = purchased_count
                        if purchased_count > 0:
                            ui_manager.upgrades_acquired.append(shop_item)

                    elif item_name in ui_manager.shop_upgrades:
                        shop_upgrade = ui_manager.shop_upgrades[item_name]
                        shop_upgrade.purchased_count = purchased_count
                        if purchased_count > 0:
                            ui_manager.upgrades_acquired.append(shop_upgrade)

            bonus_cookies = time_diff / 100
            ui_manager.cookie_count += round(bonus_cookies * ui_manager.cookies_per_second())
            ui_manager.cookie_per_click =  ui_manager.base_cookie_per_click * ui_manager.click_multiplier
            return True
    # if not save file exists, return and start a new game
    except FileNotFoundError:
        print(f'Save file not found!')
        return None
    

                # if current_time - self.last_time >= 1:
                #     self.ui_manager.cookie_count += self.ui_manager.cookies_per_second()
                #     self.last_time = current_time
