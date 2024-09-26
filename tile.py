class Tile:
    def __init__(self, color, number):
        self.color = color #Blue, Black, Red, Yellow
        self.number = number #1-13

    def __str__(self):
        # Define how the tile should be represented as a string
        if self.color == "Joker":
            return "Joker"
        return f"{self.color} {self.number}"

    def __repr__(self):
        # Define a more detailed representation for debugging
        return self.__str__()