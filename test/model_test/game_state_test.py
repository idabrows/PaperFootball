import unittest
import numpy as np

from model.game import Game


class GameStateTest(unittest.TestCase):

    def test_turn_empty_board(self):
        game = Game()
        board = game.gameState.turn_board(game.gameState.board)
        self.assertEqual(game.gameState.board.tolist(), board.tolist())
        board[0, 0] = 0
        self.assertNotEqual(game.gameState.board.tolist(), board.tolist())

    def test_turn_full_board(self):
        game = Game()
        board = np.zeros((48, 8), dtype=int)
        board[:48, :8] = 1
        print(board)
        self.assertEqual(game.gameState.turn_board(board).tolist(), board.tolist())

    def test_turn_board_with_lines(self):
        game = Game()
        board = game.gameState.board.copy()
        game.gameState.board[18, 5] = 1
        game.gameState.board[28, 6] = 1
        board[30, 2] = 1
        board[20, 1] = 1
        self.assertEqual(game.gameState.turn_board(game.gameState.board).tolist(), board.tolist())

    def test_turn_board_with_broad_lines(self):
        game = Game()
        board = game.gameState.board.copy()
        game.gameState.board[4, 0] = 1
        game.gameState.board[42, 0] = 1
        game.gameState.board[6, 7] = 1
        board[44, 7] = 1
        board[6, 7] = 1
        board[42, 0] = 1

        self.assertEqual(game.gameState.turn_board(game.gameState.board).tolist(), board.tolist())

