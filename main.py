from window import Window
from line import Line
from point import Point
from cell import Cell
from maze import Maze

def main():
    win = Window(800, 600)
    maze = Maze(Point(20, 20), Point(40, 40), 14, 19, 5)
    win.animate_maze(maze)
    maze.break_entrance_and_exit(win.canvas)
    maze.break_walls(0, 0)
    win.animate_maze(maze)
    win.wait_for_close()

main()