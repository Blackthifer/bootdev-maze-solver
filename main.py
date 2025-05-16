from window import Window
from line import Line
from point import Point
from cell import Cell
from maze import Maze

def main():
    win = Window(800, 600)
    win.delay = 0.005
    maze = Maze(Point(20, 20), Point(20, 20), 28, 38)
    win.animate_maze(maze)
    maze.break_walls(0, 0, win)
    maze.reset_visited()
    if maze.solve(win, 0, 0):
        print("Congratulations! Maze Solved! :D")
    else:
        print("No solutions found... :C")
    win.wait_for_close()

main()