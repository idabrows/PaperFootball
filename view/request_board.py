
class RequestBoard:
    def __init__(self):
        self.lines = []
        self.point = (6, 4)
        self.last_move = []

    def __init__(self, lines, current_point, last_move):
        self.lines = lines
        self.current_point = current_point
        self.last_move = last_move
