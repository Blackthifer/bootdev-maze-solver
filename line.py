class Line:
    def __init__(self, p1, p2):
        self.a = p1
        self.b = p2

    def draw(self, canvas, color):
        canvas.create_line(self.a.x, self.a.y, self.b.x, self.b.y, fill = color, width = 2)