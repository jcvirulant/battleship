from grid import Board
from character1 import Player
import sys
import os


class Game:

    def setup(self):
        print("\n"+"_" * 40)
        print("\n")
        print("Welcome to BATTLESHIP!!\n")
        self.player1 = Player()
        self.player2 = Player()

        while True:
          print("\n"+"="*20)
          print('You are up {}! Try to sink your opponents ships!'.format(self.player1.name))
          self.player_turn(self.player1)
          os.system('cls')
          if input('Continue? ') != 'x':
              sys.exit()


    def __init__(self):
        self.setup()

    def player_turn(self, player):
        print('Ready to Fire Commander {}'.format(self.name))
        self.attack_row = int(input('{}, in what row would you like to attack?')) - 1
        self.attack_col = int(input('{}, in what column would you like to attack?'))
        self.attack_col = ord(self.attack_col) - 65
        if (self.attack_row, self.attack_col) == self.player.ally.ship_coordinates_dict:
            print('Target hit!')



    # if self.player1.ship_total:
    #   print("{} Wins!".format(self.player1.name))
    #   sys.exit()
    # elif self.player2.ship_total:
    #   print("{} Wins!".format(self.player2.name))
    #   sys.exit()

Game()
