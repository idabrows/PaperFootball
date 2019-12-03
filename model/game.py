import numpy as np

from model.game_state import GameState


def empty_board():
    board = np.zeros((48, 8), dtype=int)

    # board[1::4, 0] = 2
    # board[:5, :] = 2
    # board[-5:, :] = 2

    board[1::4, 0] = 1
    board[:5, :] = 1
    board[-5:, :] = 1

    board[1:5, [3, 4]] = 0
    board[-5:0, [3, 4]] = 0

    return board


class Game:

    def __init__(self):
        self.currentPlayer = 1
        self.gameState = GameState(empty_board(), 1, (6, 4))
        self.grid_shape = (48, 8)
        self.input_shape = (2, 48, 8)
        self.name = 'paper_soccer'

    def reset(self):
        self.gameState = GameState(empty_board(), 1, (6, 4))
        self.currentPlayer = 1
        return self.gameState

    def change_turn(self):
        self.gameState.turn_board()
        self.gameState.playerTurn = -self.gameState.playerTurn
        self.currentPlayer = -self.currentPlayer

    def get_all_allowed_actions(self):
        return self.gameState.get_neighbours(self.gameState.current_position)

    def make_move(self, move):
        self.gameState.move(move)



# def get_all_allowed_moves(self):



