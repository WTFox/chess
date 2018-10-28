from typing import Tuple


class Piece:
    # is_active == incase that piece has been taken.
    def find_valid_positions(self, coordinates: 'Coordinate') -> Tuple['Coordinate']:
        """
        Given the current position's coordinates, 
        return a tuple of valid moves for the type 
        of piece. This method does not account for 
        the bounds of the board or the location of 
        other pieces.
        """
        raise NotImplementedError()
