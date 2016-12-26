from grid import Board
from character1 import Player
import random
import sys
import os


class Game:

    def __init__(self):
        self.setup()

    def setup(self):
        print("\n"+"_" * 40)
        print("\n")
        print("Welcome to BATTLESHIP!!\n")
        self.player1 = Player()
        self.player2 = Player()

        while True:
          print("\n"+"="*20)
          print('You are up Commander {}! Try to sink your opponents ships!'.format(self.player1.name))
          print('\n')
          self.player1_turn()
          self.cleanup()
          self.player2_turn()
          self.cleanup()


    def cleanup(self):
        if self.player1.command.ship_coordinates_dict == self.player2.ally.ship_coordinates_dict:
            print("Commander {}, has sunk all ships of Commander {}!\n".format(self.player1.name, self.player2.name))
            print("Commander {}'s Command Center\n".format(self.player1.name))
            self.player1.command.print_board(self.player1.command.board)
            print("Commander {}'s ALLY WATERS\n".format(self.player1.name))
            self.player1.ally.print_board(self.player1.ally.board)
            print("Commander {}'s Command Center\n".format(self.player2.name))
            self.player2.command.print_board(self.player2.command.board)
            print("Commander {}'s ALLY WATERS\n".format(self.player2.name))
            self.player2.ally.print_board(self.player2.ally.board)
            print("Thanks for playing!")
            sys.exit()
        elif self.player2.command.ship_coordinates_dict == self.player1.ally.ship_coordinates_dict:
            print("Commander {}, has sunk all ships of Commander {}!\n".format(self.player2.name, self.player1.name))
            print("Commander {}'s Command Center\n".format(self.player2.name))
            self.player2.command.print_board(self.player2.command.board)
            print("Commander {}'s ALLY WATERS\n".format(self.player2.name))
            self.player2.ally.print_board(self.player2.ally.board)
            print("Commander {}'s Command Center\n".format(self.player1.name))
            self.player1.command.print_board(self.player1.command.board)
            print("Commander {}'s ALLY WATERS\n".format(self.player1.name))
            self.player1.ally.print_board(self.player1.ally.board)
            print("Thanks for playing!")
            sys.exit()
            

    def player1_turn(self):
        # prompt player for coordinates
        print('Ready to Fire Commander {}'.format(self.player1.name))
        # Display command board
        print("Commander {}, your Command Center\n".format(self.player1.name))
        self.player1.command.print_board(self.player1.command.board)
        print("Commander {}, your ALLY WATERS\n".format(self.player1.name))
        self.player1.ally.print_board(self.player1.ally.board)
        self.attack_row = int(input('{}, in what row would you like to attack?'.format(self.player1.name))) - 1
        self.attack_col = input('{}, in what column would you like to attack?'.format(self.player1.name)).upper()
        self.attack_col = ord(self.attack_col) - 65
        # validate against previous attacks
        if (self.attack_row, self.attack_col) in self.player1.attack_list:
            print("Commander {}, you have already attacked these coordinates.".format(self.player1.name))
            self.player1_turn()
        else:
            # validate coordinates against opponent ship dict
            if ((self.attack_row, self.attack_col)) in self.player2.ally.ship_coordinates_dict:
                # report to player the outcome of the attack
                print("Commander {}, you hit {}'s ship!".format(self.player1.name, self.player2.name))
                self.player1.command.ship_coordinates_dict[(self.attack_row, self.attack_col)] = self.player2.ally.ship_coordinates_dict[self.attack_row, self.attack_col]
                self.player1.command.board[self.attack_row][self.attack_col] = self.player1.command.HIT
                self.player2.ally.board[self.attack_row][self.attack_col] = self.player2.ally.HIT
                self.player1.command.print_board(self.player1.command.board)
                pause = input("Continue?: press Enter: ")
                os.system('cls')
                pause = input("Commander {}, the Pirate {} hit your {}!\nPress Enter to coninue.".format(self.player2.name, self.player1.name, self.player2.ally.ship_coordinates_dict[self.attack_row, self.attack_col]))
            else:
                print("Commander {}, your attack missed!\n".format(self.player1.name))
                self.player1.command.board[self.attack_row][self.attack_col] = self.player1.command.MISS
                self.player2.ally.board[self.attack_row][self.attack_col] = self.player2.ally.MISS
                self.player1.command.print_board(self.player1.command.board)
                pause = input("Continue?: press Enter: ")
                os.system('cls')
                pause = input("Commander {}, the Pirate {} missed!\nPress Enter to coninue.".format(self.player2.name, self.player1.name))

            self.player1.attack_list.append((self.attack_row, self.attack_col))


    def player2_turn(self):
        # prompt player for coordinates
        print('Ready to Fire Commander {}'.format(self.player2.name))
        # Display command board
        print("Commander {}, your Command Center\n".format(self.player2.name))
        self.player2.command.print_board(self.player2.command.board)
        print("Commander {}, your ALLY WATERS\n".format(self.player2.name))
        self.player2.ally.print_board(self.player2.ally.board)
        self.attack_row = int(input('{}, in what row would you like to attack?'.format(self.player2.name))) - 1
        self.attack_col = input('{}, in what column would you like to attack?'.format(self.player2.name)).upper()
        self.attack_col = ord(self.attack_col) - 65
        # validate against previous attacks
        if (self.attack_row, self.attack_col) in self.player2.attack_list:
            print("Commander {}, you have already attacked these coordinates.".format(self.player2.name))
            self.player2_turn()
        else:
            # validate coordinates against opponent ship dict
            if ((self.attack_row, self.attack_col)) in self.player1.ally.ship_coordinates_dict:
                # report to player the outcome of the attack
                print("Commander {}, you hit {}'s ship!".format(self.player2.name, self.player1.name))
                # record hit coordinates of ships with ship types (for cleanup)
                self.player2.command.ship_coordinates_dict[(self.attack_row, self.attack_col)] = self.player1.ally.ship_coordinates_dict[self.attack_row, self.attack_col]
                # record hit/miss on command board
                self.player2.command.board[self.attack_row][self.attack_col] = self.player2.command.HIT
                self.player1.ally.board[self.attack_row][self.attack_col] = self.player1.ally.HIT
                # print command board
                self.player2.command.print_board(self.player2.command.board)
                pause = input("Continue?: press Enter: ")
                os.system('cls')
                pause = input("Commander {}, the Pirate {} hit your {}!\nPress Enter to coninue.".format(self.player1.name, self.player2.name, self.player1.ally.ship_coordinates_dict[self.attack_row, self.attack_col]))
            else:
                print("Commander {}, your attack missed!\n".format(self.player2.name))
                self.player2.command.board[self.attack_row][self.attack_col] = self.player2.command.MISS
                self.player1.ally.board[self.attack_row][self.attack_col] = self.player1.ally.MISS
                self.player2.command.print_board(self.player2.command.board)
                print('\n Your ALLY WATERS Board\n')
                self.player2.ally.print_board(self.player2.ally.board)
                pause = input("Continue?: press Enter: ")
                os.system('cls')
                pause = input("Commander {}, the Pirate {} missed!\nPress Enter to coninue.".format(self.player1.name, self.player2.name))
            self.player2.attack_list.append((self.attack_row, self.attack_col))

Game()

