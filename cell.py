class Cell:
    def __init__(self, left, right, top, bottom):
        self.hasleftwall = left
        self.hasrightwall = right
        self.hastopwall = top
        self.hasbottomwall = bottom

    def draw(self, canvas, top, left, bottom, right, color):
        if self.hasleftwall:
            canvas.create_line(left, top, left, bottom, fill=color, width=2)
        if self.hasrightwall:
            canvas.create_line(right, top, right, bottom, fill=color, width=2)
        if self.hastopwall:
            canvas.create_line(left, top, right, top, fill=color, width=2)
        if self.hasbottomwall:
            canvas.create_line(left, bottom, right, bottom, fill=color, width=2)