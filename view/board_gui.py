from view.request_board import RequestBoard
from view.board import Board
from view.board_gui_service import BoardGuiService


class BoardGui:
    def __init__(self):
        self.board = Board()
        self.board.draw_board()
        self.board.color_current_point()
        self.board.color_allowable_points()
        self.board.canvas.bind('<Button>', self.on_click)
        self.board.canvas.pack(fill="both", expand=True)
        self.board.window.geometry("400x600")
        self.board.window.mainloop()

    def on_click(self, event):
        point = self.board.get_clicked_point(event.x, event.y)
        if point:
            self.board.implement_move(point)
            response_board = BoardGuiService.get_next_move(RequestBoard(lines=self.board.lines,
                                                                        current_point=self.board.current_point,
                                                                        last_move=self.board.last_move))
            self.board.implement_move(response_board.point)


BoardGui()

