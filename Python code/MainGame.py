"""imports everything thats needed"""
import pyxel
import time
import datetime
import Pong
import Adventure
pyxel.init(250, 140)
class Mainmenu():
    def __init__(self): #sets variables and runs the system
        self.Game = 0
        self.choice = 1
        pyxel.run(self.update, self.draw)

    def update(self):
        if self.Game == 0:
            if pyxel.btn(pyxel.KEY_W):
                self.choice -= 1
                time.sleep(0.2)
            if pyxel.btn(pyxel.KEY_S):
                self.choice += 1
                time.sleep(0.2)
            if pyxel.btn(pyxel.KEY_ENTER):
                self.Game = self.choice
            if self.choice >= 3:
                self.choice = 1
            if self.choice <= 0:
                self.choice = 2
    def draw(self):
        if self.Game == 0:
            pyxel.cls(7)
            pyxel.text(90,40,"Adventure",0)
            pyxel.text(90,60,"Pong", 0)
            pyxel.text(0, 0, f'{datetime.datetime.now()}', 0)
            if self.choice == 1:
                pyxel.rectb(85, 35, 50, 15, 0)
            if self.choice == 2:
                pyxel.rectb(85, 55, 50, 15, 0)
        elif self.Game == 1:
            Adventure.App()
        elif self.Game == 2:
            Pong.Start()
        else:
            pass
Mainmenu()
