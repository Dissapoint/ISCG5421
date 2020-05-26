import pyxel
import Map
class App:
    def __init__(self):
        self.x = 126 #x position of player
        self.y = 90 #y position of player
        self.MapX = 100 #X position of map
        self.MapY = 100
        self.n1 = 5
        self.Menu = True
        self.Start = 13
        self.collison = "left"
        self.Colour = 0
        self.Colour2 = 0
        pyxel.run(self.update, self.draw)


    def update(self):
        self.SSX = self.x + 3
        self.SSY = self.y + 3
        if self.Start == 0:
            if pyxel.btn(pyxel.KEY_W):
                self.y -= 2
                self.collison = "up"
            if pyxel.btn(pyxel.KEY_S):
                self.y += 2
                self.collison = "down"
            if pyxel.btn(pyxel.KEY_A):
                self.x -= 2
                self.collison = "left"
            if pyxel.btn(pyxel.KEY_D):
                self.x += 2
                self.collison = "right"
        if pyxel.btn(pyxel.KEY_ENTER):
            self.Menu = False
            self.MapX = 0
            self.MapY = 0
        if self.x <= -1: #going left
            self.x = 249
            self.MapX -= 1
        if self.x >= 250: #going right
            self.x = 0
            self.MapX += 1
        if self.y >= 140: #going down
            self.y = 0
            self.MapY -= 1
        if self.y <= -1:  #going up
            self.y = 139
            self.MapY += 1
        if self.Colour == 10:
            if self.collison == "up":
                self.y += 2
            if self.collison == "left":
                self.x += 2
        if self.Colour2 == 10:
            if self.collison == "down":
                self.y -= 2
            if self.collison == "right":
                self.x -= 2
    def draw(self):
        pyxel.cls(13)
        pyxel.rect(self.x, self.y, 4, 4, f'{self.Start}')
        pyxel.text(5, 5, f'({self.MapX}, {self.MapY})', 7)
        if self.Menu == True:
            pyxel.text(5, 30, "Main Menu", 0)
            pyxel.text(5, 40, "Press Enter to start", 0)
        if self.Menu == False:
            self.n1 -= 1
            self.Start = 0
            pyxel.text(f'{self.n1}', 30, "Main Menu", 0)
            pyxel.text(f'{self.n1}', 40, "Press Enter to start", 0)
            Map.World.MapLayout0_0(self)
        self.Colour = pyxel.pget(f'{self.x}', f'{self.y}')
        self.Colour2 = pyxel.pget(f'{self.SSX}', f'{self.SSY}')
        if self.MapX == 0 and self.MapY == 0:
            NewMapX = self.MapX
            Map.World.MapLayout0_0(self, NewMapX)
        else:
            pass
__name__ == "__main__"
