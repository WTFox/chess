from utils import Coordinates

from .piece import Piece


class Knight(Piece):
    def __init__(self):
        self.score = 3
     
    def find_valid_positions(self, coordinates):
        return tuple(
            [
                Coordinates(coordinates.row - 2, coordinates.column + 1),
                Coordinates(coordinates.row + 2, coordinates.column - 1),
                Coordinates(coordinates.row - 1, coordinates.column + 2),
                Coordinates(coordinates.row + 1, coordinates.column - 2),
                Coordinates(coordinates.row - 1, coordinates.column - 2),
                Coordinates(coordinates.row - 2, coordinates.column - 1),
                Coordinates(coordinates.row + 1, coordinates.column + 2),
                Coordinates(coordinates.row + 2, coordinates.column + 1),
            ]
        )
