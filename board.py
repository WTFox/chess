class Board:
    LOWER_BOUNDS = 0
    UPPER_BOUNDS = 8

    def __init__(self):
        self.board = self.build_board()

    def get_piece(self, coordinates):
        return self.board[coordinates.row][coordinates.column]

    def set_piece(self, coordinates, piece):
        self.board[coordinates.row][coordinates.column] = piece

    def build_board(self):
        return [[None] * self.UPPER_BOUNDS for n in range(self.UPPER_BOUNDS)]

    def pprint_board(self, board):
        for row in board:
            print(row)

    def filter_to_valid_bounds(self, coordinate_list):
        return tuple(
            [
                coords
                for coords in coordinate_list
                if (
                    (coords.row < self.UPPER_BOUNDS and coords.row >= self.LOWER_BOUNDS)
                    and (
                        coords.column < self.UPPER_BOUNDS
                        and coords.column >= self.LOWER_BOUNDS
                    )
                )
            ]
        )

    def find_available_moves_to_highlight(self, coordinates):
        piece = self.get_piece(coordinates)
        piece_moves = piece.find_valid_positions(coordinates)
        piece_moves = self.filter_to_valid_bounds(piece_moves)
        # filter out positions that are taken by another piece
        return piece_moves
