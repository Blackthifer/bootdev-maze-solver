from window import Window
from line import Line
from point import Point
from cell import Cell

def main():
    win = Window(800, 600)
    points = []
    for i in range(16):
        points += [Point((i + 1) * 10, (i + 1) * 10)]
    cells = [
        Cell([True, True, True, True], points[0], points[1]),
        Cell([True, True, True, False], points[1], points[2]),
        Cell([True, True, False, True], points[2], points[3]),
        Cell([True, False, True, True], points[3], points[4]),
        Cell([False, True, True, True], points[4], points[5]),
        Cell([True, True, False, False], points[5], points[6]),
        Cell([True, False, True, False], points[6], points[7]),
        Cell([True, False, False, True], points[7], points[8]),
        Cell([False, True, True, False], points[8], points[9]),
        Cell([False, True, False, True], points[9], points[10]),
        Cell([False, False, True, True], points[10], points[11]),
        Cell([True, False, False, False], points[11], points[12]),
        Cell([False, True, False, False], points[12], points[13]),
        Cell([False, False, True, False], points[13], points[14]),
        Cell([False, False, False, True], points[14], points[15])
        ]
    for cell in cells:
        win.draw_cell(cell, "black")
    for i in range(len(cells) - 1):
        win.connect_cells(cells[i], cells[i + 1], i % 2 == 0)
    win.wait_for_close()

main()