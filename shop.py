'''
Module Name: shop.py
Purpose: This module handles the shop mechanic of the game
Inputs: None
Output: None
Additional code sources: 
Developers: Ian Wilson, Andrew Uriell, Peter Pham
Date: 10/26/2024
Last Modified: 10/26/2024
'''

# Class for Shop Items
class ShopItem:
    def __init__(self, name, cost, cps, cpc):
        self.name = name # Item Name
        self.cost = cost # Cost to purchase
        self.cps = cps # Cookies per second
        self.cpc = cpc # Cookies per click (multiple)
        self.purchased_count = 0  # Track how many times this item has been purchased