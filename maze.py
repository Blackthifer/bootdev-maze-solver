from cell import Cell
from point import Point
import random as rand

class Maze:
    def __init__(self, topleft, cell_size, num_rows, num_cols, seed = None):
        if seed:
            rand.seed(seed)
        self.top = topleft.y
        self.left = topleft.x
        self.cell_size = cell_size
        self.rows = num_rows
        self.cols = num_cols
        self.cells = []
        self.create_cells()
        self.entry = None
        self.exit = None

    def create_cells(self):
        walls = [True, True, True, True]
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                topleft = Point(self.left + j * self.cell_size.x, self.top + i * self.cell_size.y)
                bottomright = Point(self.left + (j + 1) * self.cell_size.x, self.top + (i + 1) * self.cell_size.y)
                cell = Cell(walls, topleft, bottomright)
                row += [cell]
            self.cells.append(row)
    
    def choose_entrance_and_exit(self, canvas):
        self.entry = Point(0, 0)
        self.draw_cell(canvas, 0, 0)
        self.exit = Point(self.rows - 1, self.cols - 1)
        self.draw_cell(canvas, self.rows - 1, self.cols - 1)
    
    def break_walls(self, row, col, window):
        if not self.entry and not self.exit:
            self.choose_entrance_and_exit(window.canvas)
        self.draw_cell(window.canvas, row, col)
        self.cells[row][col].visited = True
        window.animate()
        breakable = self.get_breakable_walls(row, col)
        while len(breakable) > 0:
            to_break = rand.choice(breakable)
            match to_break:
                case "left":
                    self.cells[row][col].hasleftwall = False
                    self.cells[row][col - 1].hasrightwall = False
                    self.break_walls(row, col - 1, window)
                case "top":
                    self.cells[row][col].hastopwall = False
                    self.cells[row - 1][col].hasbottomwall = False
                    self.break_walls(row - 1, col, window)
                case "right":
                    self.cells[row][col].hasrightwall = False
                    self.cells[row][col + 1].hasleftwall = False
                    self.break_walls(row, col + 1, window)
                case "bottom":
                    self.cells[row][col].hasbottomwall = False
                    self.cells[row + 1][col].hastopwall = False
                    self.break_walls(row + 1, col, window)
            breakable = self.get_breakable_walls(row, col)
        if row == 0 and col == 0:
            self.draw_endpoints(window.canvas)
            window.animate()
    
    def get_breakable_walls(self, row, col):
        breakable = []
        if col > 0 and not self.cells[row][col - 1].visited:
            breakable += ["left"]
        if row > 0 and not self.cells[row - 1][col].visited:
            breakable += ["top"]
        if col < self.cols - 1 and not self.cells[row][col + 1].visited:
            breakable += ["right"]
        if row < self.rows - 1 and not self.cells[row + 1][col].visited:
            breakable += ["bottom"]
        return breakable
    
    def reset_visited(self):
        for row in self.cells:
            for cell in row:
                cell.visited = False
    
    def solve(self, window, row = -1, col = -1):
        window.animate()
        if row < 0 and col < 0 and not self.entry:
            return False
        if row == -1:
            row = self.entry.x
        if col == -1:
            col = self.entry.y
        if self.is_exit(row, col):
            return True
        self.cells[row][col].visited = True
        options = self.get_open_walls(row, col)
        for option in options:
            match option:
                case "left":
                    self.cells[row][col].draw_move(window.canvas, self.cells[row][col - 1])
                    if self.solve(window, row, col - 1):
                        return True
                    self.cells[row][col].draw_move(window.canvas, self.cells[row][col - 1], True)
                case "top":
                    self.cells[row][col].draw_move(window.canvas, self.cells[row - 1][col])
                    if self.solve(window, row - 1, col):
                        return True
                    self.cells[row][col].draw_move(window.canvas, self.cells[row - 1][col], True)
                case "right":
                    self.cells[row][col].draw_move(window.canvas, self.cells[row][col + 1])
                    if self.solve(window, row, col + 1):
                        return True
                    self.cells[row][col].draw_move(window.canvas, self.cells[row][col + 1], True)
                case "bottom":
                    self.cells[row][col].draw_move(window.canvas, self.cells[row + 1][col])
                    if self.solve(window, row + 1, col):
                        return True
                    self.cells[row][col].draw_move(window.canvas, self.cells[row + 1][col], True)
    
    def get_open_walls(self, row, col):
        broken = []
        if not self.cells[row][col].hasleftwall and not self.cells[row][col - 1].visited:
            broken += ["left"]
        if not self.cells[row][col].hastopwall and not self.cells[row - 1][col].visited:
            broken += ["top"]
        if not self.cells[row][col].hasrightwall and not self.cells[row][col + 1].visited:
            broken += ["right"]
        if not self.cells[row][col].hasbottomwall and not self.cells[row + 1][col].visited:
            broken += ["bottom"]
        return broken

    def draw_cell(self, canvas, row, col):
        color = "black"
        if self.is_entry(row, col):
            color = "red"
        elif self.is_exit(row, col):
            color = "blue"
        self.cells[row][col].draw(canvas, color)
    
    def draw_endpoints(self, canvas):
        if self.entry:
            self.draw_cell(canvas, self.entry.x, self.entry.y)
        if self.exit:
            self.draw_cell(canvas, self.exit.x, self.exit.y)

    def is_entry(self, row, col):
        if self.entry:
            return row == self.entry.x and col == self.entry.y
        return False
    
    def is_exit(self, row, col):
        if self.exit:
            return row == self.exit.x and col == self.exit.y
        return False
