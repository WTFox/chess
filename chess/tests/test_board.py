import unittest

from chess.board import Board
from chess.pieces import Knight


class TestBoard(unittest.TestCase):
    def test_initial_board_has_default_position(self):
        board = Board()
        self.assertTrue(isinstance(board.board[0][1], Knight))
