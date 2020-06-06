import pyxel
import threading
import time

"""Threading"""
class myThread(threading.Thread):
    def run(self):
        print("Starting Threading")
        time.sleep(5)
        print("Done")


P2Thread1 = myThread()
P2Thread2 = myThread()
P2Thread3 = myThread()

class Start:
    thread1 = myThread()
    """Sets the starting variables"""
    def __init__(self):  # variables we will use in this pong
        self.P1Y = 90  # Player 1 Y position
        self.P2Y = 90  # Player 2 Y position
        self.GameStart = True  # If the Game has started
        self.BallX = 125  # The Balls X position
        self.BallY = 90  # The Balls Y position
        self.P1Y2 = 130  # The other end of the Players 1 Y position
        self.P2Y2 = 130  # The other end of the Players 2 Y position
        self.DirectionX = 1  # The X direction that the ball is going either left or right
        self.DirectionY = 1  # The Y direction that the ball is going either up or down
        self.Colour = 10
        self.P1Score = 0
        self.P2Score = 0
        pyxel.run(self.update, self.draw)  # runs the application

    def update(self):  # updates the screen
        if pyxel.btn(pyxel.KEY_W):
            if self.P1Y <= 20:
                pass
            else:
                self.P1Y -= 2
        if pyxel.btn(pyxel.KEY_S):
            if self.P1Y >= 100:
                pass
            else:
                self.P1Y += 2
        if self.GameStart == True:
            if self.DirectionX == 1:
                self.BallX -= 1
            if self.DirectionX == 2:
                self.BallX += 1
            if self.DirectionY == 1:
                self.BallY -= 1
            if self.DirectionY == 2:
                self.BallY += 1
            if self.BallY >= 130:
                self.DirectionY = 1
            if self.BallY <= 20:
                self.DirectionY = 2
            # player 1 Ball Bounces back
            if self.Colour == 0 and self.DirectionX == 1:
                self.DirectionX = 2
                self.BallX += 2
            elif self.Colour == 0 and self.DirectionX == 2:
                self.DirectionX = 1
                self.BallX -= 4
            else:
                pass
            # Player 2 follows ball
            if self.BallY >= 41 and self.P2Y != 20:
                if self.BallY >= (self.P2Y + 20):
                    if self.BallY <= (self.P2Y - 20):
                        pass
                    else:
                        self.P2Y += 1
                else:
                    self.P2Y -= 1
            else:
                pass


    def draw(self):
        pyxel.cls(7)
        pyxel.rect(f'{self.BallX}', f'{self.BallY}', 4, 4, 10)  # Draws The ball
        pyxel.rect(20, f'{self.P1Y}', 10, 40, 0)  # draws player 1
        pyxel.rect(220, f'{self.P2Y}', 10, 40, 0)  # draws player 2
        self.Colour = pyxel.pget(f'{self.BallX} ', f'{self.BallY}')
        pyxel.rect(0, 0, 250, 20, 0)  # draws player 2
        pyxel.text(120, 10, f'{self.P1Score}', 7)
        pyxel.text(140, 10, f'{self.P2Score}', 7)

        if self.BallX <= 10:
            self.P1Score += 1
            self.DirectionX = 2
            self.BallX = 125
            self.BallY = 90
            if self.P1Score == 1:
                P2Thread1.start()
            if self.P1Score == 2:
                P2Thread2.start()
            if self.P1Score == 3:
                P2Thread3.start()
