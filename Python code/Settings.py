import logging
import Map
import pyxel
class gears:
    def map_select(self):
        if self.MapXY == [0,1]:
            Map.World.MapLayout0_1(self)
        elif self.MapXY == [0,0]:
            Map.World.MapLayout0_0(self)
        elif self.MapXY == [0,-1]:
            Map.World.MapLayout0_N1(self)
        elif self.MapXY ==  [1,-2]:
            Map.World.MapLayout1_N2(self)
        elif self.MapXY ==  [-1,-1]:
            Map.World.MapLayoutN1_N1(self)
        elif self.MapXY ==  [-1,0]:
            Map.World.MapLayoutN1_0(self)
        elif self.MapXY ==  [1,-1]:
            Map.World.MapLayout1_N1(self)
        elif self.MapXY ==  [-2,0]:
            Map.World.MapLayoutN2_0(self)
        elif self.MapXY ==  [-2,2]:
            Map.World.MapLayoutN2_2(self)
        elif self.MapXY ==  [-1,1]:
            Map.World.MapLayoutN1_1(self)
        elif self.MapXY ==  [-2,1]:
            Map.World.MapLayoutN2_1(self)
        elif self.MapXY ==  [-2,-1]:
            Map.World.MapLayoutN2_N1(self)
        elif self.MapXY ==  [-2,3]:
            Map.World.MapLayoutN2_3(self)
        else:
            Map.World.MapLayoutSecret(self)
            logging.info("Out of Map")
    def movement(self):
        if self.x <= -1:  # going left
            self.x = 249
            # Labyrinth conditions
            if self.MapXY == [-2, 0]:
                self.MapXY[1] += 1
            elif self.MapXY == [-2, -1]:
                self.MapXY = [-1, 1]
            elif self.MapXY == [-2, 1]:
                self.MapXY[1] = -1
            else:
                self.MapXY[0] -= 1
        if self.x >= 250:  # going right
            self.x = 0
            if self.MapXY == [-1, 0]:
                self.MapXY[0] -= 1
            elif self.MapXY == [-1, -1]:
                self.MapXY = [-2, -1]
            elif self.MapXY == [-2, -1]:
                self.MapXY[1] = 1
            else:
                self.MapXY[0] += 1
        if self.y >= 140:  # going down
            if self.MapXY == [0, 1]:  # Yellow castle exit
                self.y = 75
                self.MapXY[1] = 0
            elif self.MapXY == [-2, 3]:  # blue castle exit
                self.y = 75
                self.MapXY[1] -= 1
            elif self.MapXY == [20, 20]:  # error room exit
                self.y = 72
                self.x = 122
                self.MapXY = [0, 0]
            else:
                self.y = 1
                self.MapXY[1] -= 1
        if self.y <= -1:  # going up
            if self.MapXY == [0, 0]:
                self.MapXY[1] = 19
                self.MapXY[0] = 20
            else:
                pass
            self.y = 139
            self.MapXY[1] += 1

        '''Castle entrance'''
        if self.MapXY == [0,0]: # yellow castle gate
            if self.y <= 72 and self.x >= 108:
                if self.y >= 65 and self.x <= 141:
                    self.y = 140
                    self.MapXY[1] += 1

        if self.MapXY == [-2,2]:# blue castle gate
            if self.y <= 72 and self.x >= 108:
                if self.y >= 65 and self.x <= 141:
                    self.y = 140
                    self.MapXY[1] += 1

        '''collison with the wall'''
        if self.loading == False:
            if self.Colour[0] == 10 and self.Colour[1] == 10:  # up
                pass
            elif self.Colour[0] == 5 and self.Colour[1] == 5:
                pass
            else:
                if pyxel.btn(pyxel.KEY_W):
                    self.y -= 2
            if self.Colour[2] == 10 and self.Colour[3] == 10:  # down
                pass
            elif self.Colour[2] == 5 and self.Colour[3] == 5:
                pass
            else:
                if pyxel.btn(pyxel.KEY_S):
                    self.y += 2
            if self.Colour[1] == 10 and self.Colour[3] == 10:  # right
                pass
            elif self.Colour[1] == 5 and self.Colour[3] == 5:
                pass
            else:
                if pyxel.btn(pyxel.KEY_D):
                    self.x += 2
            if self.Colour[0] == 10 and self.Colour[2] == 10:  # right yellow
                pass
            elif self.Colour[0] == 5 and self.Colour[2] == 5:  # right blue
                pass
            else:
                if pyxel.btn(pyxel.KEY_A):
                    self.x -= 2
        else:
            pass

'''Unit tests'''

def test_going_up():
    results = MapXY(0,0)
    assert results == (0,1)

def test_going_down():
    results = MapXY(0,0)
    assert results == (0,-1)

def test_going_left():
    results = MapXY(0,0)
    assert results == (-1,0)

def test_going_right():
    results = MapXY(0,0)
    assert results == (1,0)

def test_moveing_up():
    results = x(0)
    assert results == (2)

def test_Movement_notstop(): # no problem should be dectected
    results = Colour(0,0,0,0)
    assert results == ("")

def test_Movement_stop_left(): # should stop going left
    results = Colour(10,0,10,0) or Colour(5,0,5,0)
    assert results == ("")

def test_Movement_stop_right(): # should stop going right
    results = Colour(0,10,0,10) or Colour(0,5,0,5)
    assert results == ("")


def test_Movement_stop_down():  # should stop going down
    results = Colour(0, 0, 10, 10) or Colour(0, 0, 5, 5)
    assert results == ("")


def test_Movement_stop_up():  # should stop going right
    results = Colour(10, 10, 0, 0) or Colour(5, 5, 0, 0)
    assert results == ("")
