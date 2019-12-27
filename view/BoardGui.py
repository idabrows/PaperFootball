import tkinter as tk
from view.Point import Point
from view.Line import Line


class BoardGui:
    def __init__(self):
        self.window = tk.Tk()
        self.canvas = tk.Canvas(self.window)
        self.square_size = 50
        self.point_radius = 2
        self.points_gui = []
        self.current_point = Point(0, 0)
        self.line_enter = 0


    def draw_board(self):
        for i in range(3, 5):
            self.canvas.create_rectangle(self.square_size * i, 0, self.square_size * i +

                                         self.square_size, self.square_size, fill='green')
        for i in range(8):
            for j in range(1, 11):
                self.canvas.create_rectangle(self.square_size * i, self.square_size * j,
                                             self.square_size * i + self.square_size,
                                             self.square_size * j + self.square_size, fill='green')
        for i in range(3, 5):
            self.canvas.create_rectangle(self.square_size * i, self.square_size * 11, self.square_size * i +
                                         self.square_size,
                                         self.square_size * 11 + self.square_size, fill='green')


        self.points_gui.append([])
        for j in range(0, 3):
            self.points_gui[0].append(self.canvas.create_oval(self.square_size * j, 0,
                                                           self.square_size * j, 0, fill='white'))

        for j in range(3, 6):
            self.points_gui[0].append( self.canvas.create_oval(self.square_size * j - self.point_radius, -self.point_radius, self.square_size * j +
                                    self.point_radius
                                    , self.point_radius, fill='black') )
        for j in range(6, 9):
            self.points_gui[0].append(self.canvas.create_oval(self.square_size * j, 0,
                                                           self.square_size * j, 0, fill='white'))

        for i in range(1, 12):
            self.points_gui.append([])
            for j in range(0, 9):
                 self.points_gui[i].append( self.canvas.create_oval(self.square_size * j - self.point_radius, self.square_size * i -
                                        self.point_radius,
                                        self.square_size * j + self.point_radius,
                                        self.square_size * i + self.point_radius,
                                        fill="black") )

        self.points_gui.append([])

        for j in range(0, 3):
            self.points_gui[12].append(self.canvas.create_oval(self.square_size * j, self.square_size * 12,
                                    self.square_size * j, self.square_size * 12,
                                    fill="white"))

        for j in range(3, 6):
            self.points_gui[12].append(self.canvas.create_oval(self.square_size * j - self.point_radius, self.square_size * 12 - self.point_radius,
                                    self.square_size * j + self.point_radius, self.square_size * 12 + self.point_radius,
                                    fill="black"))

        for j in range(6, 9):
            self.points_gui[12].append(self.canvas.create_oval(self.square_size * j, self.square_size * 12,
                                                               self.square_size * j, self.square_size * 12,
                                                               fill="white"))
        self.canvas.create_oval(self.square_size * 4 - 5, self.square_size * 6 -5,
                                self.square_size * 4 + 5, self.square_size * 6 + 5,
                                fill="blue")

    def draw_lines(self, lines):
        for i in range(0, lines.__len__()):
            self.canvas.create_line(50 * lines[i].point1.y, 50 * lines[i].point1.x, 50 * lines[i].point2.y,
                                    50 * lines[i].point2.x,
                                    width=3, fill='red')

    def draw_lines(self, lines):
        for i in range(0, lines.__len__()):
            self.canvas.create_line(50 * lines[i][0][1], 50 * lines[i][0][0], 50 * lines[i][1][1],
                                    50 * lines[i][1][0],
                                    width=3, fill='red')


   # def draw_lines(self, points):
   #     for i in range(0, points.__len__()-1):
   #         self.canvas.create_line(50 * points[i].y, 50 * points[i].x, 50 * points[i+1].y,
   #                                 50 * points[i+1].x,
   #                                 width=3, fill='red')

    def draw_line(self, line):
        self.line_enter = self.canvas.create_line(50 * line.point1.x, 50 * line.point1.x, 50 * line.point2.y, 50 * line.point2.x, width=3, fill='red')

    def delete_line(self):
        self.canvas.delete(self.line_enter)

    def on_click(self, event):
        # self.draw_line(Line(Point(1, 1), Point(4, 5)))
        self.draw_lines([Point(1, 1), Point(2, 1), Point(2, 2), Point(3, 3)])

    def mouseEnter(self, event, point_to):
        self.draw_line(Line(self.current_point, point_to))

    def mouseLeave(self, event):
        self.delete_line()


def main():
    board = BoardGui()
    board.draw_board()
    board.draw_lines(

[([0, 0], [0, 1]),
 ([0, 1], [0, 2]),
 ([0, 2], [0, 3]),
 ([0, 3], [0, 4]),
 ([0, 4], [0, 5]),
 ([0, 5], [0, 6]),
 ([0, 6], [0, 7]),
 ([0, 7], [0, 8]),
 ([0, 0], [1, 0]),
 ([0, 1], [1, 1]),
 ([0, 2], [1, 2]),
 ([0, 3], [1, 3]),
 ([0, 5], [1, 5]),
 ([0, 6], [1, 6]),
 ([0, 7], [1, 7]),
 ([0, 0], [1, 1]),
 ([0, 1], [1, 2]),
 ([0, 2], [1, 3]),
 ([0, 5], [1, 6]),
 ([0, 6], [1, 7]),
 ([0, 7], [1, 8]),
 ([1, 0], [0, 1]),
 ([1, 1], [0, 2]),
 ([1, 2], [0, 3]),
 ([1, 5], [0, 6]),
 ([1, 6], [0, 7]),
 ([1, 7], [0, 8]),
 ([1, 0], [1, 1]),
 ([1, 1], [1, 2]),
 ([1, 2], [1, 3]),
 ([1, 5], [1, 6]),
 ([1, 6], [1, 7]),
 ([1, 7], [1, 8]),
 ([1, 0], [2, 0]),
 ([2, 0], [3, 0]),
 ([3, 0], [4, 0]),
 ([4, 0], [5, 0]),
 ([4, 1], [5, 2]),
 ([5, 0], [4, 1]),
 ([5, 0], [5, 1]),
 ([5, 0], [6, 0]),
 ([5, 2], [6, 3]),
 ([6, 3], [6, 4]),
 ([6, 0], [7, 0]),
 ([7, 0], [8, 0]),
 ([8, 0], [9, 0]),
 ([9, 0], [10, 0]),
 ([10, 0], [11, 0]),
 ([11, 0], [11, 1]),
 ([11, 1], [11, 2]),
 ([11, 2], [11, 3]),
 ([11, 5], [11, 6]),
 ([11, 6], [11, 7]),
 ([11, 7], [11, 8]),
 ([11, 0], [12, 0]),
 ([11, 1], [12, 1]),
 ([11, 2], [12, 2]),
 ([11, 3], [12, 3]),
 ([11, 5], [12, 5]),
 ([11, 6], [12, 6]),
 ([11, 7], [12, 7]),
 ([11, 0], [12, 1]),
 ([11, 1], [12, 2]),
 ([11, 2], [12, 3]),
 ([11, 5], [12, 6]),
 ([11, 6], [12, 7]),
 ([11, 7], [12, 8]),
 ([12, 0], [11, 1]),
 ([12, 1], [11, 2]),
 ([12, 2], [11, 3]),
 ([12, 5], [11, 6]),
 ([12, 6], [11, 7]),
 ([12, 7], [11, 8])]
)
    #board.canvas.bind('<Button>', board.on_click)
    #board.canvas.tag_bind(board.points_gui[1][1], "<Any-Enter>", functools.partial(board.mouseEnter, point_to=Point(1, 1)))
    #board.canvas.tag_bind(board.points_gui[1][1], "<Any-Leave>", board.mouseLeave)


#     board.canvas.pack(fill="both", expand=True)
#     board.window.geometry("400x600")
#     board.window.mainloop()
#     print(board.points_gui)
#
# main()
