from tile import Tile
from player import Player
from board import Board
import random

class RummikubGame:
    def __init__(self):
        # Initialize game components here
        num_of_players = int(input("Enter how many players are playing between 2-4: "))
        while num_of_players < 2 or num_of_players > 4:
            num_of_players = int(input("Invalid player numbers, please enter a number between 2-4: "))

        self.set_of_players = []
        
        
        # Create player instances
        for i in range(num_of_players):
            player_name = input(f"Enter name for Player {i+1}: ")
            player = Player(player_name)
            self.set_of_players.append(player)

        #initializing the board
        self.board = Board()

        #initialzing tiles using the init_tile func
        self.tiles = self.init_tiles()

    def init_tiles(self):
        colors = ["Blue", "Red", "Yellow", "Black"]
        numbers = range(1, 14)  # 1 to 13

        tiles = []

        for color in colors:
            for number in numbers:
                tiles.append(Tile(color, number))
                tiles.append(Tile(color, number)) #Twice since there is 2 of each tile
        
        #Add 2 jokers (special tiles without a color or number)
        tiles.append(Tile("Joker", None))
        tiles.append(Tile("Joker", None))

        random.shuffle(tiles)        

        return tiles 
    def start_tiles(self):
        for player in self.set_of_players:
            while len(player.hand) != 14:
                player.hand.append(self.tiles.pop())

    def start_game(self):
        # Give each player their starting tiles
        self.start_tiles()

        # Game flow logic
        print("Starting the game with the following players: ")
        for player in self.set_of_players:
            print(f"Player: {player.name} \n")
            print(f"{player.name}'s hand: {player.hand} \n")
        pass

        print(f"Remaining tile pool: {self.tiles} \n")
if __name__ == "__main__":
    game = RummikubGame()
    game.start_game()
 