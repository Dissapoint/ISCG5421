import pyxel
import Map
import Logging

class App:
    """Sets the starting variables"""

    def __init__(self):
        self.loading = False
        self.x = 126  # x position of player
        self.y = 90  # y position of player
        self.MapX = 0  # X position of map
        self.MapY = 0  # Y position of map
        self.Finished = 0  # If the game is Finished
        # Colour sensors
        self.Colour1 = 0  # top left
        self.Colour2 = 0  # top right
        self.Colour3 = 0  # bottom left
        self.Colour4 = 0  # bottom right
        pyxel.run(self.update, self.draw)

        """Updates the Screen"""

    def update(self):

        """ The Screen Change  """

        if self.x <= -1:  # going left
            self.x = 249
            # Labyrinth conditions
            if self.MapX == -2 and self.MapY == 0:
                self.MapX += 1
            elif self.MapX == -2 and self.MapY == -1:
                self.MapX = -1
                self.MapY = 1
            elif self.MapX == -2 and self.MapY == 1:
                self.MapY = -1
            else:
                self.MapX -= 1
        if self.x >= 250:  # going right
            self.x = 0
            if self.MapX == -1 and self.MapY == 0:
                self.MapX -= 1
            elif self.MapX == -1 and self.MapY == 1:
                self.MapX = -2
                self.MapY = -1
            elif self.MapX == -2 and self.MapY == -1:
                self.MapY = 1
            else:
                self.MapX += 1
        if self.y >= 140:  # going down
            if self.MapX == 0 and self.MapY == 1:  # Yellow castle exit
                self.y = 75
                self.MapY = 0
            elif self.MapX == -2 and self.MapY == 3:  # blue castle exit
                self.y = 75
                self.MapY -= 1
            elif self.MapX == 20 and self.MapY == 20:  # error room exit
                self.y = 72
                self.x = 122
                self.MapX = 0
                self.MapY = 0
            else:
                self.y = 1
                self.MapY -= 1
        if self.y <= -1:  # going up
            if self.MapX == 0 and self.MapY == 0:
                self.MapY = 19
                self.MapX = 20
            else:
                pass
            self.y = 139
            self.MapY += 1

        '''Castle entrance'''
        if self.MapX == 0 and self.MapY == 0:  # yellow castle gate
            if self.y <= 72 and self.x >= 108:
                if self.y >= 65 and self.x <= 141:
                    self.y = 140
                    self.MapY += 1

        if self.MapX == -2 and self.MapY == 2:  # blue castle gate
            if self.y <= 72 and self.x >= 108:
                if self.y >= 65 and self.x <= 141:
                    self.y = 140
                    self.MapY += 1

        '''collision checker -  improve if you have time future daniel'''
        if self.loading == False:
            if self.Colour1 == 10 and self.Colour2 == 10:  # up
                pass
            elif self.Colour1 == 5 and self.Colour2 == 5:
                pass
            else:
                if pyxel.btn(pyxel.KEY_W):
                    self.y -= 2
            if self.Colour3 == 10 and self.Colour4 == 10:  # down
                pass
            elif self.Colour3 == 5 and self.Colour4 == 5:
                pass
            else:
                if pyxel.btn(pyxel.KEY_S):
                    self.y += 2
            if self.Colour2 == 10 and self.Colour4 == 10:  # right
                pass
            elif self.Colour2 == 5 and self.Colour4 == 5:
                pass
            else:
                if pyxel.btn(pyxel.KEY_D):
                    self.x += 2
            if self.Colour1 == 10 and self.Colour3 == 10:  # right yellow
                pass
            elif self.Colour1 == 5 and self.Colour3 == 5:  # right blue
                pass
            else:
                if pyxel.btn(pyxel.KEY_A):
                    self.x -= 2
        else:
            pass

    """this draws onto the screen"""

    def draw(self):
        pyxel.cls(13)  # background screen
        pyxel.rect(self.x, self.y, 4, 4, 0)  # Player1

        '''This Selects what map is going to be used based on your location'''
        if self.MapX == 0 and self.MapY == 1:
            Map.World.MapLayout0_1(self)
        elif self.MapX == 0 and self.MapY == 0:
            Map.World.MapLayout0_0(self)
        elif self.MapX == 0 and self.MapY == -1:
            Map.World.MapLayout0_N1(self)
        elif self.MapX == 1 and self.MapY == -2:
            Map.World.MapLayout1_N2(self)
        elif self.MapX == -1 and self.MapY == -1:
            Map.World.MapLayoutN1_N1(self)
        elif self.MapX == -1 and self.MapY == 0:
            Map.World.MapLayoutN1_0(self)
        elif self.MapX == 1 and self.MapY == -1:
            Map.World.MapLayout1_N1(self)
        elif self.MapX == -2 and self.MapY == 0:
            Map.World.MapLayoutN2_0(self)
        elif self.MapX == -2 and self.MapY == 2:
            Map.World.MapLayoutN2_2(self)
        elif self.MapX == -1 and self.MapY == 1:
            Map.World.MapLayoutN1_1(self)
        elif self.MapX == -2 and self.MapY == 1:
            Map.World.MapLayoutN2_1(self)
        elif self.MapX == -2 and self.MapY == -1:
            Map.World.MapLayoutN2_N1(self)
        elif self.MapX == -2 and self.MapY == 3:
            Map.World.MapLayoutN2_3(self)
        else:
            Map.World.MapLayoutSecret(self)
            logging.info("Out of Map")

        '''checks if the colour has changed for collision'''
        self.Colour1 = pyxel.pget(f'{self.x - 1}', f'{self.y - 1}')  # checks the top left colour
        self.Colour2 = pyxel.pget(f'{self.x + 4}', f'{self.y - 1}')  # checks the top right colour
        self.Colour3 = pyxel.pget(f'{self.x - 1}', f'{self.y + 4}')  # checks the bottom left colour
        self.Colour4 = pyxel.pget(f'{self.x + 4}', f'{self.y + 4}')  # checks the bottom right colour
        
        '''Error with collision'''
        if self.Colour2 == 10 and self.Colour3 == 10:
            logging.warning("Problem")
        if self.Colour1 == 10 and self.Colour4 == 10:
            logging.error("Problem")
        if self.Colour2 == 5 and self.Colour3 == 5:
            logging.debug("Problem")
        if self.Colour1 == 10 and self.Colour4 == 10:
            logging.critical("Problem")
