from point import Point

class Cell:
    def __init__(self, walls, topleft, bottomright):
        self.hasleftwall = walls[0]
        self.hastopwall = walls[1]
        self.hasrightwall = walls[2]
        self.hasbottomwall = walls[3]
        self.top = topleft.y
        self.left = topleft.x
        self.bottom = bottomright.y
        self.right = bottomright.x
        self.visited = False

    def draw(self, canvas, color):
        canvas.create_line(self.left, self.top, self.left, self.bottom, fill=color if self.hasleftwall else "#d9d9d9", width=2)
        canvas.create_line(self.right, self.top, self.right, self.bottom, fill=color if self.hasrightwall else "#d9d9d9", width=2)
        canvas.create_line(self.left, self.top, self.right, self.top, fill=color if self.hastopwall else "#d9d9d9", width=2)
        canvas.create_line(self.left, self.bottom, self.right, self.bottom, fill=color if self.hasbottomwall else "#d9d9d9", width=2)
    
    def draw_move(self, canvas, other, undo = False):
        self_center = Point((self.left + self.right) // 2, (self.top + self.bottom) // 2)
        other_center = Point((other.left + other.right) //2, (other.top + other.bottom) // 2)
        canvas.create_line(self_center.x, self_center.y, other_center.x, other_center.y, fill="grey" if undo else "red", width=2)
