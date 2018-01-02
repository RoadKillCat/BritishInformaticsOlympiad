class Dice:
    x = 5
    y = 5
    up = 1     #to sky
    right = 4  #to right
    top = 2    #to front (away)
    heading = "forward"
    
    def move(self):
        global grid
        v = grid[y][x]
        v = (v + self.top - 1) % 6 + 1

    def modPos(self):
        self.x = (self.x + 11) % 11
        self.y = (self.y + 11) % 11

    def leftRoll(self):
        right = 7 - self.up
        top = self.right
        self.right = right
        self.top = top
        self.x -= 1
        self.modPos()
        heading = "left"

    def rightRoll(self):
        right = self.up
        top = 7 - self.right
        self.right = right
        self.top = top
        self.x += 1
        self.modPos()
        heading = "right"

    def forwardRoll(self):
        up = 7 - self.top
        top = self.up
        self.up = up
        self.top = top
        self.y += 1
        self.modPos()
        heading = "forward"

    def backwardRoll(self):
        up = self.top
        top = 7 - self.up
        self.up = up
        self.top = top
        self.y -= 1
        self.modPos()
        heading = "backward"

grid = [[1]*11]*11
die = Dice()
