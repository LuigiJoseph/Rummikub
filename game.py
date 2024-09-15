from tile import Tile
from player import Player
from board import Board

class RummikubGame:
    def __init__(self):
        # Initialize game components here
        num_of_players = input("Enter how many players are playing. 2-4")
        self.set_of_players = []
        
        # Create player instances
        for i in range(num_of_players):
            player_name = input(f"Enter name for Player {i+1}: ")
            player = Player(player_name)
            self.set_of_players.append(player)


    def start_game(self):
        # Game flow logic
        pass

if __name__ == "__main__":
    game = RummikubGame()
    game.start_game()
 