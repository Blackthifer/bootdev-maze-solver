from cell import Cell
from point import Point

class Maze:
    def __init__(self, topleft, cell_size, num_rows, num_cols):
        self.top = topleft.y
        self.left = topleft.x
        self.cell_size = cell_size
        self.rows = num_rows
        self.cols = num_cols
        self.cells = []
        self.create_cells(cell_size, num_rows, num_cols)

    def create_cells(self, cell_size, rows, cols):
        walls = [True, True, True, True]
        for i in range(rows):
            row = []
            for j in range(cols):
                topleft = Point(self.left + j * cell_size.x, self.top + i * cell_size.y)
                bottomright = Point(self.left + (j + 1) * cell_size.x, self.top + (i + 1) * cell_size.y)
                cell = Cell(walls, topleft, bottomright)
                row += [cell]
            self.cells.append(row)

    def draw_cell(self, canvas, row, col):
        self.cells[row][col].draw(canvas, "black")
