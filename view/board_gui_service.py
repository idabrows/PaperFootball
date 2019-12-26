

class BoardGuiService:

    @staticmethod
    def get_next_move(data):
        # załóżmy, że idzie w górę, s komputer robi ruch w prawo
        response = data
        response.point = (5, 5)
        response.last_move = [[(5, 4), (5, 5)]]
        response.lines.append([[(5, 4), (5, 5)]])
        return response

    @staticmethod
    def can_make_move(data):
        return False

    @staticmethod
    def get_allowable_points(request_board):
        return [
            (request_board.current_point[0] - 1, request_board.current_point[1] - 1), (request_board.current_point[0] - 1,
                                                                                       request_board.current_point[1]),
            (request_board.current_point[0] - 1, request_board.current_point[1] + 1),
            (request_board.current_point[0], request_board.current_point[1] - 1), (request_board.current_point[0],
                                                                                   request_board.current_point[1]),
            (request_board.current_point[0], request_board.current_point[1] + 1),
            (request_board.current_point[0] + 1, request_board.current_point[1] - 1), (request_board.current_point[0] + 1,
                                                                                       request_board.current_point[1]),
            (request_board.current_point[0] + 1, request_board.current_point[1] + 1),
        ]

    @staticmethod
    def get_positions(y, x):
        position1 = [0, 0]
        position2 = [0, 0]
        position1[1] = x
        if y % 4 == 0:
            position2[1] = x + 1
            position1[0] = int(y / 4)
            position2[0] = int(y / 4)
        elif y % 4 == 1:
            position2[1] = x
            position1[0] = int(y / 4)
            position2[0] = int(y / 4 + 1)
        elif y % 4 == 2:
            position2[1] = x + 1
            position1[0] = int(y / 4)
            position2[0] = int(y / 4) + 1
        elif y % 4 == 3:
            position2[1] = x + 1
            position1[0] = int(y / 4) + 1
            position2[0] = int(y / 4)
        return position1, position2

    @staticmethod
    def get_all_lines(board):
        lines = []
        for i in range(48):
            for j in range(8):
                if board[i, j] == 1:
                    #                     print(j,i)
                    lines.append(BoardGuiService.get_positions(i, j))
        return lines

