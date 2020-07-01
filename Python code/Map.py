import pyxel

'''This module creates the maps'''


class World:
    '''the design for the maps'''
    def MapLayout0_0(self):
        pyxel.rect(0, 0, 10, 130, 10)#right side
        pyxel.rect(0, 0, 70, 10, 10)#top left side
        pyxel.rect(180, 0, 250, 10, 10)#top right side
        pyxel.rect(240, 0, 10, 130, 10)#right side
        pyxel.rect(65, 10, 35, 40, 10)#tower left block
        pyxel.rect(150, 10, 35, 40, 10)#tower right block
        pyxel.rect(140, 50, 35, 50, 10)#tower bottom right block
        pyxel.rect(75, 50, 35, 50, 10)#tower bottom left block
        pyxel.rect(75, 40, 100, 30, 10)#Middle tower
        pyxel.rect(0, 130, 90, 10, 10)#bottom left block
        pyxel.rect(160, 130, 90, 10, 10)#bottom right block
        #Tower points
        for t in (75, 85, 95, 150, 160, 170):
            pyxel.rect(t, 0, 5, 10, 10)
    def MapLayout0_1(self):
        pyxel.rect(0, 130, 110, 10, 10)#bottom left block
        pyxel.rect(140, 130, 100, 10, 10)#bottom right block
        pyxel.rect(0, 0, 10, 140, 10)#leftwall
        pyxel.rect(240, 0, 10, 140, 10)#rightwall
        pyxel.rect(0, 0, 250, 10, 10)#bottomblock
    def MapLayout0_N1(self):
        pyxel.rect(0, 0, 90, 10, 10)#top left block
        pyxel.rect(160, 0, 90, 10, 10)#top right block
        pyxel.rect(0, 130, 250, 10, 10)#bottomblock
    def MapLayoutN1_N1(self):
        pyxel.rect(0, 0, 90, 10, 10)#top left block
        pyxel.rect(160, 0, 90, 10, 10)#top right block
        pyxel.rect(0, 130, 250, 10, 10)#bottomblock
        pyxel.rect(40, 0, 2, 140, 10)# wall
    def MapLayoutN1_0(self):
        pyxel.rect(0, 130, 91, 10, 5)#bottom left block
        pyxel.rect(160, 130, 90, 10, 5)#bottom right block
        pyxel.rect(0, 0, 50, 10, 5) #top left block
        pyxel.rect(200, 0, 50, 10, 5) #top right block
        pyxel.rect(40, 0, 10, 90, 5) #left side block
        pyxel.rect(80, 0, 10, 40, 5) #middle left block
        pyxel.rect(160, 0, 10, 40, 5) #middle right block
        pyxel.rect(110, 0, 30, 10, 5) #middle left block
        pyxel.rect(60, 0, 10, 90, 5) #middle left side block
        pyxel.rect(180, 0, 10, 90, 5) #right side block
        pyxel.rect(200, 0, 10, 90, 5) #right side block
        pyxel.rect(0, 40, 20, 20, 5) #left side small block
        pyxel.rect(80, 40, 90, 20, 5) #bottom small block
        pyxel.rect(230, 40, 20, 20, 5) #right side small block
        pyxel.rect(0, 90, 50, 20, 5) #left bottom side block
        pyxel.rect(60, 90, 130, 20, 5) #bottom block
        pyxel.rect(200, 90, 50, 20, 5) #left bottom side block

    def MapLayout1_N1(self):
        pyxel.rect(0, 130, 90, 10, 10)#bottom left block
        pyxel.rect(160, 130, 90, 10, 10)#bottom right block
        pyxel.rect(0, 0, 250, 10, 10)#bottomblock
        pyxel.rect(210, 0, 2, 140, 10)# wall
    def MapLayoutSecret(self):
        pyxel.rect(0, 130, 110, 10, 5)#bottom left block
        pyxel.rect(140, 130, 100, 10, 5)#bottom right block
        pyxel.rect(0, 0, 10, 140, 5)#leftwall
        pyxel.rect(240, 0, 10, 140, 5)#rightwall
        pyxel.rect(0, 0, 250, 10, 5)#bottomblock
        pyxel.text(80,60,"How did you get in here",7)
    def MapLayoutN2_0(self):
        pyxel.rect(100, 0, 10, 90, 5)  # left middle block
        pyxel.rect(0, 0, 20, 10, 5)  #top left block
        pyxel.rect(50, 0, 40, 10, 5)  #2nd left block
        pyxel.rect(0, 40, 70, 20, 5)  # top left block
        pyxel.rect(0, 90, 20, 20, 5)  #top left block
        pyxel.rect(30, 0, 10, 40, 5)  #top left block
        pyxel.rect(90, 0, 20, 10, 5)  #top left block
        pyxel.rect(90, 40, 10, 40, 5)  #top left block
        pyxel.rect(70, 40, 10, 120, 5)  #top left block
        pyxel.rect(90, 0, 10, 140, 5)  #top left block
        pyxel.rect(0, 130, 40, 10, 5)  #top left block
        pyxel.rect(40, 90, 10, 50, 5)  #top left block
        #mirror for right side
        pyxel.rect(140, 0, 10, 90, 5)  # left middle block
        pyxel.rect(230, 0, 20, 10, 5)  #top left block
        pyxel.rect(160, 0, 40, 10, 5)  #2nd left block
        pyxel.rect(180, 40, 70, 20, 5)  # top left block
        pyxel.rect(230, 90, 20, 20, 5)  #top left block
        pyxel.rect(210, 0, 10, 40, 5)  #top left block
        pyxel.rect(140, 0, 20, 10, 5)  #top left block
        pyxel.rect(150, 40, 10, 40, 5)  #top left block
        pyxel.rect(170, 40, 10, 120, 5)  #top left block
        pyxel.rect(150, 0, 10, 140, 5)  #top left block
        pyxel.rect(210, 130, 40, 10, 5)  #top left block
        pyxel.rect(200, 90, 10, 50, 5)  #top left block
    def MapLayoutN2_1(self):
        pyxel.rect(0, 0, 90, 10, 5)#top left block
        pyxel.rect(100, 80, 10, 90, 5)  # left middle block
        pyxel.rect(100, 40, 10, 20, 5)  # left middle block
        pyxel.rect(90, 0, 10, 60, 5)  # left middle block
        pyxel.rect(0, 40, 20, 60, 5)  # left middle block
        pyxel.rect(60, 0, 10, 90, 5)  # left middle block
        pyxel.rect(0, 80, 100, 20, 5)  # left middle block
        pyxel.rect(0, 130, 20, 10, 5)  #top left block
        pyxel.rect(50, 130, 50, 10, 5)  #2nd left block
        pyxel.rect(30, 100, 10, 40, 5)  #top left block
        #Mirror
        pyxel.rect(160, 0, 90, 10, 5)#top left block
        pyxel.rect(140, 80, 10, 90, 5)  # left middle block
        pyxel.rect(140, 40, 10, 20, 5)  # left middle block
        pyxel.rect(150, 0, 10, 60, 5)  # left middle block
        pyxel.rect(230, 40, 20, 60, 5)  # left middle block
        pyxel.rect(180, 0, 10, 90, 5)  # left middle block
        pyxel.rect(150, 80, 100, 20, 5)  # left middle block
        pyxel.rect(230, 130, 20, 10, 5)  #top left block
        pyxel.rect(150, 130, 50, 10, 5)  #2nd left block
        pyxel.rect(210, 100, 10, 40, 5)  #top left block
    def MapLayoutN2_2(self):
        pyxel.rect(0, 0, 10, 130, 5)#right side
        pyxel.rect(0, 0, 70, 10, 5)#top left side
        pyxel.rect(180, 0, 250, 10, 5)#top right side
        pyxel.rect(240, 0, 10, 130, 5)#right side
        pyxel.rect(65, 10, 35, 40, 5)#tower left block
        pyxel.rect(150, 10, 35, 40, 5)#tower right block
        pyxel.rect(140, 50, 35, 50, 5)#tower bottom right block
        pyxel.rect(75, 50, 35, 50, 5)#tower bottom left block
        pyxel.rect(75, 40, 100, 30, 5)#Middle tower
        pyxel.rect(0, 130, 90, 10, 5)#bottom left block
        pyxel.rect(160, 130, 90, 10, 5)#bottom right block
        #Tower points
        for t in (75, 85, 95, 150, 160, 170):
            pyxel.rect(t, 0, 5, 10, 5)
    def MapLayoutN1_1(self):
        pyxel.rect(0,0,250,10,5)
        pyxel.rect(110, 40, 30, 110, 5) #middle block
        pyxel.rect(60, 40, 130, 20, 5)
        pyxel.rect(0, 40, 50, 20, 5)
        pyxel.rect(200, 40, 50, 20, 5)
        pyxel.rect(0, 40, 20, 60, 5)
        pyxel.rect(230, 40, 20, 60, 5)
        pyxel.rect(0, 130, 30, 10, 5)
        pyxel.rect(220, 130, 30, 10, 5)
        pyxel.rect(40, 80, 10, 60, 5)
        pyxel.rect(200, 80, 10, 60, 5)
        pyxel.rect(40, 80, 50, 20, 5)
        pyxel.rect(80, 80, 10, 60, 5)
        pyxel.rect(160, 80, 50, 20, 5)
        pyxel.rect(160, 80, 10, 60, 5)
        pyxel.rect(60, 130, 10, 10, 5)
        pyxel.rect(180, 130, 10, 10,5)
    def MapLayoutN2_N1(self):
        pyxel.rect(0, 130, 250, 10, 5)
        #left side
        pyxel.rect(40, 90, 10, 50, 5)
        pyxel.rect(40, 0, 10, 50, 5)
        pyxel.rect(0, 0, 40, 10, 5)
        pyxel.rect(70, 0, 10, 10, 5)
        pyxel.rect(90, 0, 10, 50, 5)
        pyxel.rect(0, 40, 20, 60, 5)
        pyxel.rect(0, 80, 50, 20, 5)
        pyxel.rect(40, 40, 60, 20, 5)
        #right side
        pyxel.rect(200, 90, 10, 50, 5)
        pyxel.rect(200, 0, 10, 50, 5)
        pyxel.rect(210, 0, 40, 10, 5)
        pyxel.rect(170, 0, 10, 10, 5)
        pyxel.rect(150, 0, 10, 50, 5)
        pyxel.rect(230, 40, 20, 60, 5)
        pyxel.rect(200, 80, 50, 20, 5)
        pyxel.rect(150, 40, 60, 20, 5)
    def MapLayout1_N2(self):
        pyxel.rect(0, 0, 90, 10, 10)#bottom left block
        pyxel.rect(160, 0, 100, 10, 10)#bottom right block
        pyxel.rect(0, 0, 10, 140, 10)#leftwall
        pyxel.rect(240, 0, 10, 140, 10)#rightwall
        pyxel.rect(0, 130, 250, 10, 10)#bottomblock
    def MapLayoutN2_3(self):
        pyxel.rect(0, 130, 110, 10, 5)#bottom left block
        pyxel.rect(140, 130, 100, 10, 5)#bottom right block
        pyxel.rect(0, 0, 10, 140, 5)#leftwall
        pyxel.rect(240, 0, 10, 140, 5)#rightwall
        pyxel.rect(0, 0, 250, 10, 5)#bottomblock
