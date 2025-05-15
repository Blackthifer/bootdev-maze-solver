from window import Window
from line import Line
from point import Point

def main():
    win = Window(800, 600)
    win.draw_line(Line(Point(10, 10), Point(10, 20)), "black")
    win.draw_line(Line(Point(10, 20), Point(20, 20)), "black")
    win.draw_line(Line(Point(20, 20), Point(20, 10)), "black")
    win.draw_line(Line(Point(20, 10), Point(10, 10)), "black")
    win.wait_for_close()

main()