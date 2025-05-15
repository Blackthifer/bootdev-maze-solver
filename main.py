from window import Window
from line import Line
from point import Point
from cell import Cell

def main():
    win = Window(800, 600)
    cells = [
        Cell(True, True, True, True),
        Cell(True, True, True, False),
        Cell(True, True, False, True),
        Cell(True, False, True, True),
        Cell(False, True, True, True),
        Cell(True, True, False, False),
        Cell(True, False, True, False),
        Cell(True, False, False, True),
        Cell(False, True, True, False),
        Cell(False, True, False, True),
        Cell(False, False, True, True),
        Cell(True, False, False, False),
        Cell(False, True, False, False),
        Cell(False, False, True, False),
        Cell(False, False, False, True)
        ]
    for i in range(len(cells)):
        win.draw_cell(cells[i], 10 * (i + 1), 10 * (i + 1), 10 * (i + 2), 10 * (i + 2), "black")
    win.wait_for_close()

main()