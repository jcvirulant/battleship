from grid import Ally
from grid import Board
from grid import Command
import os

class Player:
    ship_total = 17

    def __init__(self):
        # prompt for Names
        self.name = input('Name: ')
        print("{}, Welcome to your ALLY WATERS! Here your will place your ships and record your opponents attacks.".format(self.name))
        self.ally = Ally()
        pause = input("Continue?: press any key: ")
        print("{}, this is your command center. Here you will order your ships to attack ENEMY WATERS.\nUnfortunately, your opponent has jammed your radar and you must use logic and cunning to defeat your enemy".format(self.name))
        self.command = Command()
        pause = input("Is your opponent ready? press any key: ")
        os.system('cls')
