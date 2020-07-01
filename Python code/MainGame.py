"""imports everything thats needed"""
import pyxel
import time
import datetime
import Pong
import Adventure
import logging

"""Sets size of screen"""
pyxel.init(250, 140)

''' 
creates the main menu for the games to be selected

'''


class Mainmenu():  # the class
    def __init__(self):  # sets variables and runs the system
        self.Game = {1, 2}  # checks if the game is selected
        self.choice = 1  # checks what game is about to be selected
        pyxel.run(self.update, self.draw)  # runs the game

    '''Updates the screen '''

    def update(self):
        if len(self.Game) == 2:  # counts the number in the sets category
            if pyxel.btn(pyxel.KEY_W):  # move upwards
                self.choice -= 1
                time.sleep(0.2)
            if pyxel.btn(pyxel.KEY_S):  # moves downward
                self.choice += 1
                time.sleep(0.2)
            if pyxel.btn(pyxel.KEY_ENTER):  # selects the
                self.Game.remove(self.choice)
            if self.choice >= 3:  # sets the choice back to the 1 if goes to high
                self.choice = 1
            if self.choice <= 0:  # sets the choice back to the 2 if goes to low
                self.choice = 2
        else:  # cancels everything if choice has been made
            pass

    '''Draws onto the screen'''

    def draw(self):
        if len(self.Game) == 2:  # counts if the game hasnt changed
            pyxel.cls(7)

            ''' text on screen'''
            pyxel.text(90, 40, "Adventure", 0)
            pyxel.text(90, 60, "Pong", 0)
            pyxel.text(0, 0, f'{datetime.datetime.now()}', 0)
            if self.choice == 1:  # shows the choice the player can select
                pyxel.rectb(85, 35, 50, 15, 0)
            if self.choice == 2:  # shows the choice the player can select
                pyxel.rectb(85, 55, 50, 15, 0)
        elif self.Game == {2}:  # starts the adventure game
            Adventure.App()
            Adventure.API_find()
        elif self.Game == {1}:  # starts pong
            Pong.Start()
        else:  # error occured
            logging.FATAL("game softlocked ")
            raise Game_exception("Game doesnt equel 2 or 1")


class Game_exception(Exception):
    pass


'''entry point'''
if __name__ == "__main__":
    Mainmenu().main_proc()
