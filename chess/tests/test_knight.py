import unittest

from chess.board import Board
from chess.pieces import Knight
from chess.utils import Coordinates


class TestKnightFindValidPositions(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.knight = Knight()

    def test_lower_left_corner_location_filters_out_of_bounds(self):
        knight_pos = Coordinates(7, 0)
        self.board.set_piece(knight_pos, self.knight)
        results = self.board.find_available_moves_to_highlight(knight_pos)

        expected = (Coordinates(5, 1), Coordinates(6, 2))
        self.assertEqual(results, expected)

    def test_lower_right_corner_location_filters_out_of_bounds(self):
        knight_pos = Coordinates(7, 7)
        self.board.set_piece(knight_pos, self.knight)
        results = self.board.find_available_moves_to_highlight(knight_pos)

        expected = (Coordinates(6, 5), Coordinates(5, 6))
        self.assertEqual(results, expected)

    def test_upper_left_corner_location_filters_out_of_bounds(self):
        knight_pos = Coordinates(0, 0)
        self.board.set_piece(knight_pos, self.knight)
        results = self.board.find_available_moves_to_highlight(knight_pos)

        expected = (Coordinates(1, 2), Coordinates(2, 1))
        self.assertEqual(results, expected)

    def test_upper_right_corner_location_filters_out_of_bounds(self):
        knight_pos = Coordinates(0, 7)
        self.board.set_piece(knight_pos, self.knight)
        results = self.board.find_available_moves_to_highlight(knight_pos)

        expected = (Coordinates(2, 6), Coordinates(1, 5))
        self.assertEqual(results, expected)

    def test_central_location_filters_out_of_bounds(self):
        knight_pos = Coordinates(3, 3)
        self.board.set_piece(knight_pos, self.knight)
        results = self.board.find_available_moves_to_highlight(knight_pos)

        expected = (
            Coordinates(1, 2),
            Coordinates(2, 5),
            Coordinates(2, 1),
            Coordinates(5, 2),
            Coordinates(1, 4),
            Coordinates(4, 1),
            Coordinates(5, 4),
            Coordinates(4, 5),
        )

        for coord in expected:
            self.assertIn(coord, results)
    
    def test_filter_out_location_other_same_color_pieces(self):
        # TODO: write this
        pass


if __name__ == "__main__":
    unittest.main()
