import numpy as np


class GameState:
    def __init__(self, board, player_turn, current_position):
        self.board = board
        self.playerTurn = player_turn
        self.current_position = current_position

    def turn_board(self):
        board2 = np.zeros((48, 8), dtype=int)
        board2[1::4, 0] = 1
        board2[:5, :] = 1
        board2[-4:, :] = 1
        board2[1:5, [3, 4]] = 0
        board2[-5:, [3, 4]] = 0
        board2[1, 3] = 1
        board2[-3, 3] = 1
        for i in range(5,42):
            for j in range(8):
                if i%4 == 1:
                    if j == 0:
                        board2[i, j] = 1
                    else:
                        board2[i, j] = self.board[46 - i, 8 - j]
                elif i%4 == 2:
                    board2[i + 2, j] = self.board[46-i , 7-j]
                elif i%4 == 0:
                    board2[i+ 2, j] = self.board[46-i , 7-j]
                elif i%4 == 3:
                    board2[i + 4, j] = self.board[46-i , 7-j]

        board2[44,3] = self.board[4,4]
        board2[44,4] = self.board[4,3]
        board2[45,4] = self.board[1,4]
        board2[46,3] = self.board[2,4]
        board2[46,4] = self.board[2,3]
        board2[47,3] = self.board[3,4]
        board2[47,4] = self.board[3,3]

        board2[4, 4] = self.board[44,3]
        board2[4, 3] = self.board[44,4]
        board2[1, 4] = self.board[45,4]
        board2[2, 4] = self.board[46,3]
        board2[2, 3] = self.board[46,4]
        board2[3, 4] = self.board[47,3]
        board2[3, 3] = self.board[47,4]
        self.board = board2

    def _allowed_actions(self):
        neighbours = self.get_neighbours(self.current_position)
        allowed = [self.get_move(self.current_position, x) for x in neighbours]
        allowed = [x for x in allowed if self.board[x[0], x[1]] == 0]
        return allowed

    def move(self, position):
        a, b = self.get_move(self.current_position, position)
        if (a, b) in self._allowed_actions():
            self.board[a, b] = 1
            self.current_position = position
        else:
            print('Error, wrong move')

    def check_for_end_game(self):
        if len(self._allowed_actions()) == 0:
            return -1
        if self.current_position[0] == 12:
            return -1
        if self.current_position[0] == 0:
            return 1
        return 0

    def check_for_change_player(self):
        if len(self._allowed_actions()) < 7:
            return True
        return False

    @staticmethod
    def get_neighbours(position):
        neighbours = [(position[0] - 1, position[1] - 1), (position[0] - 1, position[1]),
                      (position[0], position[1] - 1),
                      (position[0] + 1, position[1] + 1), (position[0] + 1, position[1]),
                      (position[0], position[1] + 1),
                      (position[0] + 1, position[1] - 1), (position[0] - 1, position[1] + 1)]
        to_del = []
        for x in neighbours:
            if (x[0] < 0) or (x[0] > 12):
                to_del.append(x)
                continue
            elif (x[1] < 0) or (x[1] > 8):
                to_del.append(x)

        return [x for x in neighbours if x not in to_del]

    @staticmethod
    def get_move(position1, position2):
        x = min(position1[1], position2[1])
        if position1[1] == position2[1]:
            if position1[0] > position2[0]:
                y = 4 * (position1[0] - 1) + 1
            else:
                y = 4 * position1[0] + 1
        else:
            if position1[0] > position2[0]:
                if position1[1] > position2[1]:
                    y = 4 * (position1[0] - 1) + 2
                else:
                    y = 4 * (position1[0] - 1) + 3
            elif position1[0] == position2[0]:
                y = 4 * position1[0]
            else:
                if position1[1] < position2[1]:
                    y = 4 * position1[0] + 2
                else:
                    y = 4 * position1[0] + 3
        return y, x

    @staticmethod
    def get_positions(x, y):
        position1 = [0, 0]
        position2 = [0, 0]
        position1[1] = x
        if y % 4 == 0:
            position2[1] = x+1
            position1[0] = int(y/4)
            position2[0] = int(y/4)
        elif y % 4 == 1:
            position2[1] = x
            position1[0] = int(y/4)
            position2[0] = int(y/4+1)
        elif y % 4 == 2:
            position2[1] = x+1
            position1[0] = int(y/4)
            position2[0] = int(y/4)+1
        elif y % 4 == 3:
            position2[1] = x+1
            position1[0] = int(y/4)+1
            position2[0] = int(y/4)
        return position1, position2

    def get_all_lines(self):
        lines = []
        for i in range(48):
            for j in range(8):
                if self.board[i, j] == 1:
                    lines.append(self.get_positions(j, i))
        return lines
