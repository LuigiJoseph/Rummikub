from tile import Tile


class Board:
    def __init__(self):
        self.played_groups = [] #Groups = sets or runs

    #insert logic for validating run
    def is_valid_run(self, group):
        if len(group) < 3:
            return False
        
        #Check if all tiles have the same color
        first_tile_color = group[0].color
        for tile in group:
            if tile.color == "Joker":
                continue
            if tile.color != first_tile_color:
                return False
        
        #extract numbers from group and sort them
        numbers = [tile.number for tile in group if tile.number != 0]  # Non-joker tiles
        jokers = [tile for tile in group if tile.number == 0]  # Jokers

        numbers.sort()

        joker_count = len(jokers)

        #Check if the remaining non-joker numbers are consecutive or can be made consecutive using jokers

        for i in range(1, len(numbers)): #start at index 1
            gap = numbers[i] - numbers[i - 1]  # Calculate the gap between consecutive numbers
            if gap > 1:
            # Check if we can fill the gap using jokers
                    needed_jokers = gap - 1
            if needed_jokers > joker_count:  # If the gap is too large for the number of jokers
                return False
            joker_count -= needed_jokers  # Use jokers to fill the gap
        return True

    def is_valid_set(self, group):
        if len(group) < 3:
            return False

        #Check if all tiles have the same number
        first_tile_number = group[0].number
        for tile in group:
            if tile.number == 0: #Joker case
                continue 
            if tile.number != first_tile_number:
                return False
        
        #Check there are no same colors
        seen_colors = set()
        for tile in group:
            if tile.color == "Joker":  # Allow jokers to have duplicate color
                continue
            if tile.color in seen_colors:
                return False #Duplicate color
            seen_colors.add(tile.color)
        
        return True

    def is_valid_group(self, group):
        if (self.is_valid_group(self.group) or self.is_valid_run(self,group)) == True:
            return True
        return False
