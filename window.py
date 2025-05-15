from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.root = Tk()
        self.root.title = "Maze Solver"
        self.root.protocol("WM_DELETE_WINDOW", self.close)
        self.canvas = Canvas(self.root, {"width": width, "height": height})
        self.canvas.pack()
        self.running = False

    def draw_line(self, line, color):
        line.draw(self.canvas, color)
    
    def draw_cell(self, cell, x1, y1, x2, y2, color):
        cell.draw(self.canvas, x1, y1, x2, y2, color)
    
    def redraw(self):
        self.root.update()
        self.root.update_idletasks()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()
        
    def close(self):
        self.running = False
