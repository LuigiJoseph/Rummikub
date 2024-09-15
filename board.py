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
            if tile.color != first_tile_color:
                return False
        
        #extract numbers from group and sort them
        numbers = [tile.number for tile in group]
        numbers.sort()

        #check if they are consecutive
        for i in range(1, len(numbers)):
            if numbers[i] != numbers[i - 1] + 1: #current number with its previous number
                return False
            
        return True

    def is_valid_set(self, group):
        if len(group) < 3:
            return False

        #Check if all tiles have the same number
        first_tile_number = group[0].number
        for tile in group:
            if tile.number != first_tile_number:
                return False
        
        #Check there are no same colors
        seen_colors = set()
        for tile in group:
            if tile.color in seen_colors:
                return False #Duplicate color
            seen_colors.add(tile.color)
        
        return True

    def is_valid_group(self, group):
        if (self.is_valid_group(self.group) or self.is_valid_run(self,group)) == True:
            return True
        return False
