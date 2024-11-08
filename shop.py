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
    def __init__(self, name, base_cost, cps, cpc):
        self.name = name # Item Name
        self.cost = base_cost # Cost to purchase
        self.cps = cps # Cookies per second
        self.cpc = cpc # Cookies per click (multiple)
        self.purchased_count = 0  # Track how many times this item has been purchased

# Class for shop upgrades, which are one-time purchases
class ShopUpgrade:
    def __init__(self, name, base_cost, cps, cpc):
        self.name = name # Item Name
        self.cost = base_cost # Cost to purchase
        self.cps = cps # Cookies per second
        self.cpc = cpc # Cookies per click (multiple)
        self.purchased_count = 0  # Track how many times this item has been purchased

# price = base x 1.15 ^ (buildings owned)
shop_items = {
    'Extra Hands': ShopItem("Extra Hands", 10, None, 2),
    'Cursor': ShopItem("Cursor", 50, .5, None),
    'Grandma': ShopItem("Grandma", 100, 1, None),
    'Farm': ShopItem("Farm", 500, 5, None),
    'Factory': ShopItem("Factory", 1000, 10, None)
}


# These upgraeds can be renamed to whatever is necesarry to match the shop items, we can also change the cps and cpc values to whatever we want
shop_upgrades = {
    'Click Multiplier 1': ShopUpgrade("Click Multiplier 1", 200, None, 1.05),  # Can rename this to rolling pin 1
    'Click Multiplier 2': ShopUpgrade("Click Multiplier 2", 500, None, 1.15),  # Can rename this to rolling pin 2
    'Click Multiplier 3': ShopUpgrade("Click Multiplier 3", 1000, None, 1.35),  # Can rename this to rolling pin 3
    'Increase Click 1': ShopUpgrade("Increase Click 1", 300, None, 2),  # Can rename this to Reinforced Hands
    'Increase Click 2': ShopUpgrade("Increase Click 2", 600, None, 3),  # Can rename this to Strengthened Hands
    'Increase Click 3': ShopUpgrade("Increase Click 3", 1200, None, 5)  # Can rename this to Sturdy Hands
}