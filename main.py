'''
Module Name: main.py
Purpose: Serves as the entrypoint into the game
Inputs: None
Output: None
Additional code sources: 
Developers: Peter Pham
Date: 10/26/2024
Last Modified: 10/26/2024
'''

from game import Game

# runs the game
def main():
    game = Game()
    game.run()

if __name__ == '__main__':
    main()