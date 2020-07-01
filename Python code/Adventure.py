import pyxel
import logging
import Setting
import socket

'''
This Module is used for drawing the adventure game and runs the game 

'''


'''finds request and prints the api'''
class API_find:
    response = requests.get('https://api.github.com')  # saves the api
    print(response.headers) # prints the api


class App:
    """Sets the starting variables"""

    def __init__(self):
        self.loading = False
        self.x = 126  # x position of player
        self.y = 90  # y position of player
        self.MapXY = [0, 0]  # X and Y position of map
        self.Finished = 0  # If the game is Finished
        # Colour sensors
        self.Colour = [0, 0, 0, 0]
        pyxel.run(self.update, self.draw)

        """Updates the Screen"""

    def update(self):

        Setting.gears.movement(self)  # movement

    """this draws onto the screen"""

    def draw(self):
        pyxel.cls(13)  # background screen
        pyxel.rect(self.x, self.y, 4, 4, 0)  # Player1

        '''This Selects what map is going to be used based on your location'''
        Setting.gears.map_select(self)

        '''checks if the colour has changed for collision'''
        self.Colour[0] = pyxel.pget(f'{self.x - 1}', f'{self.y - 1}')  # checks the top left colour
        self.Colour[1] = pyxel.pget(f'{self.x + 4}', f'{self.y - 1}')  # checks the top right colour
        self.Colour[2] = pyxel.pget(f'{self.x - 1}', f'{self.y + 4}')  # checks the bottom left colour
        self.Colour[3] = pyxel.pget(f'{self.x + 4}', f'{self.y + 4}')  # checks the bottom right colour

        if self.Colour[1] == 10 and self.Colour[2] == 10:
            logging.warning("Problem")
        if self.Colour[0] == 10 and self.Colour[3] == 10:
            logging.error("Problem")
        if self.Colour[1] == 5 and self.Colour[2] == 5:
            logging.debug("Problem")
        if self.Colour[0] == 10 and self.Colour[3] == 10:
            logging.critical("Problem")

    '''Developer checking test'''
    # pyxel.text(0, 0, f'({self.MapXY})', 7)
    # pyxel.text(0, 20, f'({self.x}, {self.y})', 7)
    # pyxel.rect(f'{self.x - 1}', f'{self.y - 1}',1,1,7)
    # pyxel.rect(f'{self.x + 4}', f'{self.y - 1}', 1, 1, 11)
    # pyxel.rect(f'{self.x - 1}', f'{self.y + 4}',1,1,1)
    # pyxel.rect(f'{self.x + 4}', f'{self.y +4}', 1, 1, 15
