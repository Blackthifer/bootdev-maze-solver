from window import Window
from line import Line
from point import Point
from cell import Cell
from maze import Maze

def main():
    win = Window(800, 600)
    win.delay = 0.003
    maze = Maze(Point(10, 10), Point(20, 20), 29, 39)
    win.animate_maze(maze)
    maze.break_walls(win)
    maze.reset_visited()
    if maze.solve(win):
        print("Congratulations! Maze Solved! :D")
    else:
        print("No solutions found... :C")
    win.wait_for_close()

main()