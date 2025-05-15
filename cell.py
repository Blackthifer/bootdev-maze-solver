class Cell:
    def __init__(self, walls, topleft, bottomright):
        self.hasleftwall = walls[0]
        self.hastopwall = walls[1]
        self.hasrightwall = walls[2]
        self.hasbottomwall = walls[3]
        self.tl = topleft
        self.br = bottomright

    def draw(self, canvas, color):
        if self.hasleftwall:
            canvas.create_line(self.tl.x, self.tl.y, self.tl.x, self.br.y, fill=color, width=2)
        if self.hasrightwall:
            canvas.create_line(self.br.x, self.tl.y, self.br.x, self.br.y, fill=color, width=2)
        if self.hastopwall:
            canvas.create_line(self.tl.x, self.tl.y, self.br.x, self.tl.y, fill=color, width=2)
        if self.hasbottomwall:
            canvas.create_line(self.tl.x, self.br.y, self.br.x, self.br.y, fill=color, width=2)