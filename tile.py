class Tile:
    def __init__(self, color, number):
        self.tile_color = color
        self.tile_number = number

    def __str__(self):
        return f"{self.color} {self.number}"
