class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
    
    def put_down_group(self, group):
        #insert logic for placing group from hand on board
        return 0
    
    def draw_from_pool(self,tile):
        self.hand.append(tile)