from grid import Ally
from grid import Board
from grid import Command
import os


class Player:

    def __init__(self):
        self.attack_list = list()
        # prompt for Names
        self.name = input('Name: ')
        print("{}, Welcome to your ally waters! Here you will place your "
              "ships and record your opponents attacks.".format(self.name)
              )
        self.ally = Ally()
        pause = input("Continue?: press Enter: ")
        os.system('clear')
        print("{}, this is your command center. Here you will order your ships"
              " to attack enemy waters.\nUnfortunately, your opponent has"
              " jammed your radar and you must use logic and cunning to defeat"
              " your enemy\n".format(self.name)
              )
        self.com = Command()
        pause = input("Is your opponent ready? press Enter: ")
        os.system('clear')

    def val_ar(self):
        try:
            self.ar = int(input('Row Number: ')) - 1
        except ValueError:
            os.system('clear')
            print('You input an improper value.'
                  'Please enter an integer between 1 and 10.\n')
            self.com.print_board(self.com.board)
            self.val_ar()
        else:
            if self.ar in range(10):
                return self.ar
            else:
                os.system('clear')
                print('Your input was outside the range of the possible'
                      'inputs. Please enter an integer between 1 and 10.\n')
                self.com.print_board(self.com.board)
                self.val_ar()

    def val_ac(self):
        try:
            self.ac = input('In what Column? ').upper()
            self.ac = ord(self.ac) - 65
        except TypeError:
            os.system('clear')
            print('Your input was the wrong type. '
                  'Please choose a letter from A - J')
            self.val_ac()
        else:
            if self.ac in range(10):
                return self.ac
            else:
                os.system('clear')
                print('Your input was outside the range of the possible'
                      'inputs. Please choose column A - J.')
                self.val_ac()

    def turn(self):
        name = self.name
        # prompt player for coordinates
        print("\n"+"="*20)
        print('You are up Commander {}! '
              'Try to sink your opponents ships!'.format(name))
        print('\n')
        # Display com board
        print("Commander {}, your Command Center\n".format(name))
        self.com.print_board(self.com.board)
        print("\nCommander {}, your ALLY WATERS\n".format(name))
        self.ally.print_board(self.ally.board)
        print('\n\nCommander {},'
              ' where would you like to attack?'.format(name))
        self.val_ar()
        self.val_ac()
        # val against previous attacks

        if (self.ar, self.ac) in self.attack_list:
            print("Commander {},you have already attacked"
                  " these coordinates.".format(name))
            self.turn()
        else:
            return self.ar
            return self.ac
