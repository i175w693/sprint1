'''
Module Name: prestige.py
Purpose: This module handles all gameplay aspects related to the prestige mechanism
Inputs: None
Output: None
Additional code sources: 
Developers: Peter Pham
Date: 12/1/2024
Last Modified: 12/1/2024
'''

class Prestige:
    def __init__(self, ui_manager):
        self.prestige_count = 0
        self.golden_cookies = 0
        self.ui_manager = ui_manager

    def prestige_check(self):
        if self.ui_manager.cookie_count > 10000000:
            return True
        else:
            return False

    def prestige(self):
        if self.prestige_check():
            self.ui_manager.cookie_count = 0
            self.ui_manager.upgrades_acquired = []

    def draw_prestige_menu(self):
        pass


class Prestige_Shop:
    def __init__(self):
        pass