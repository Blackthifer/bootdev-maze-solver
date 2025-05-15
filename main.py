from window import Window
from line import Line
from point import Point
from cell import Cell
from maze import Maze

def main():
    win = Window(800, 600)
    maze = Maze(Point(20, 20), Point(20, 20), 28, 38)
    win.animate_maze(maze)
    win.wait_for_close()

main()