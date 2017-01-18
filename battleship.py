from grid import Board
from character1 import Player
import sys
import os


# scd = ship_coordinates_dict
# ar/ac = attack_row/column
# pr/pc = placement_row/column

class Game:

    SHIP_DICT = {
        "Aircraft Carrier": 5,
        "Battleship": 4,
        "Submarine": 3,
        "Cruiser": 3,
        "Patrol Boat": 2}

    def __init__(self):
        self.setup()

    def setup(self):
        print("\n"+"_" * 40)
        print("\n")
        print("Welcome to BATTLESHIP!!\n")
        # Create two players for Game
        self.p1 = Player()
        self.p2 = Player()

        # Game loop
        while True:

            self.p1_turn()
            self.cleanup()
            self.p2_turn()
            self.cleanup()

    def val_ar(self):
        try:
            self.ar = int(input('Row Number: ')) - 1
        except ValueError:
            os.system('clear')
            print('You input an improper value.'
                  'Please enter an integer between 1 and 10.')
            self.val_ar()
        else:
            if self.ar in range(10):
                return self.ar
            else:
                os.system('clear')
                print('Your input was outside the range of the possible'
                      'inputs. Please enter an integer between 1 and 10.')
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

    def cleanup(self):
        # test if all ships have been destroyed
        # - requires both instances of player
        if self.p1.com.scd == self.p2.ally.scd:
            print("Commander {} WINS!\n".format(self.p1.name))
            print("Commander {}'s Command Center\n".format(self.p1.name))
            self.p1.com.print_board(self.p1.com.board)
            print("Commander {}'s ALLY WATERS\n".format(self.p1.name))
            self.p1.ally.print_board(self.p1.ally.board)
            print("Commander {}'s Command Center\n".format(self.p2.name))
            self.p2.com.print_board(self.p2.com.board)
            print("Commander {}'s ALLY WATERS\n".format(self.p2.name))
            self.p2.ally.print_board(self.p2.ally.board)
            print("Thanks for playing!")
            sys.exit()
        elif self.p2.com.scd == self.p1.ally.scd:
            print("Commander {} WINS!\n".format(self.p2.name))
            print("Commander {}'s Command Center\n".format(self.p2.name))
            self.p2.com.print_board(self.p2.com.board)
            print("Commander {}'s ALLY WATERS\n".format(self.p2.name))
            self.p2.ally.print_board(self.p2.ally.board)
            print("Commander {}'s Command Center\n".format(self.p1.name))
            self.p1.com.print_board(self.p1.com.board)
            print("Commander {}'s ALLY WATERS\n".format(self.p1.name))
            self.p1.ally.print_board(self.p1.ally.board)
            print("Thanks for playing!")
            sys.exit()

    def p1_turn(self):
        # prompt player for coordinates - requires only one instance of player
        print("\n"+"="*20)
        print('You are up Commander {}!'
              'Try to sink your opponents ships!'.format(self.p1.name))
        print('\n')
        # Display com board
        print("Commander {}, your Command Center\n".format(self.p1.name))
        self.p1.com.print_board(self.p1.com.board)
        print("Commander {}, your ALLY WATERS\n".format(self.p1.name))
        self.p1.ally.print_board(self.p1.ally.board)
        print('\n\nCommander {},'
              'where would you like to attack?'.format(self.p1.name))
        self.val_ar()
        self.val_ac()
        # val against previous attacks

        if (self.ar, self.ac) in self.p1.attack_list:
            print("Commander {},you have already attacked"
                  "these coordinates.".format(self.p1.name))
            self.p1_turn()
        else:
            # val coordinates against opponent ship dict
            # - requires both instances of player (ships)
            if ((self.ar, self.ac)) in self.p2.ally.scd:
                # report to player the outcome of the attack and record for further reference
                print("Commander {}, you hit {}'s ship!".format(self.p1.name, self.p2.name))
                # update com ship coordinates for cleanup
                self.p1.com.scd[(self.ar, self.ac)] = self.p2.ally.scd[self.ar, self.ac]
                # update com board
                self.p1.com.board[self.ar][self.ac] = self.p1.com.HIT
                # update opponent ally board
                self.p2.ally.board[self.ar][self.ac] = self.p2.ally.HIT
                # print com board
                self.p1.com.print_board(self.p1.com.board)
                # allow other player to get in front of screen
                pause = input("Continue?: press Enter: ")
                os.system('clear')
                # new player prompt
                if sum(1 for self.p2.ally.scd[self.ar, self.ac] in self.p1.com.scd.values()) == self.SHIP_DICT[self.p2.ally.scd[self.ar, self.ac]]:
                    pause = input("Commander {}, the Pirate {} SUNK your {}!\nPress Enter to coninue.".format(self.p2.name, self.p1.name, self.p2.ally.scd[self.ar, self.ac]))
                else:
                    pause = input("Commander {}, the Pirate {} hit your {}!\nPress Enter to coninue.".format(self.p2.name, self.p1.name, self.p2.ally.scd[self.ar, self.ac]))
            else:
                print("Commander {}, your attack missed!\n".format(self.p1.name))
                self.p1.com.board[self.ar][self.ac] = self.p1.com.MISS
                self.p2.ally.board[self.ar][self.ac] = self.p2.ally.MISS
                self.p1.com.print_board(self.p1.com.board)
                pause = input("Continue?: press Enter: ")
                os.system('clear')
                pause = input("Commander {}, the Pirate {} missed!\nPress Enter to coninue.".format(self.p2.name, self.p1.name))
            # record attack for validation against future attacks
            self.p1.attack_list.append((self.ar, self.ac))

    def p2_turn(self):
        # prompt player for coordinates
        print("\n"+"="*20)
        print('You are up Commander {}! Try to sink your opponents ships!'.format(self.p2.name))
        print('\n')
        # Display com board
        print("Commander {}, your Command Center\n".format(self.p2.name))
        self.p2.com.print_board(self.p2.com.board)
        print("Commander {}, your ALLY WATERS\n".format(self.p2.name))
        self.p2.ally.print_board(self.p2.ally.board)
        print('\n\nCommander {}, where would you like to attack?'.format(self.p2.name))
        self.val_ar()
        self.val_ac()
        # val against previous attacks
        if (self.ar, self.ac) in self.p2.attack_list:
            print("Commander {}, you have already attacked these coordinates.".format(self.p2.name))
            self.p2_turn()
        else:
            # val coordinates against opponent ship dict
            if ((self.ar, self.ac)) in self.p1.ally.scd:
                # report to player the outcome of the attack
                print("Commander {}, you hit {}'s ship!".format(self.p2.name, self.p1.name))
                # record hit coordinates of ships with ship types (for cleanup)
                self.p2.com.scd[(self.ar, self.ac)] = self.p1.ally.scd[self.ar, self.ac]
                # record hit/miss on com board
                self.p2.com.board[self.ar][self.ac] = self.p2.com.HIT
                self.p1.ally.board[self.ar][self.ac] = self.p1.ally.HIT
                # # print com board
                self.p2.com.print_board(self.p2.com.board)
                pause = input("Continue?: press Enter: ")
                os.system('clear')
                # new player prompt - validating whether or not the ship was sunk
                if sum(1 for self.p1.ally.scd[self.ar, self.ac] in self.p2.com.scd.values()) == self.SHIP_DICT[self.p1.ally.scd[self.ar, self.ac]]:
                    pause = input("Commander {}, the Pirate {} SUNK your {}!\nPress Enter to coninue.".format(self.p1.name, self.p2.name, self.p1.ally.scd[self.ar, self.ac]))
                else:
                    pause = input("Commander {}, the Pirate {} hit your {}!\nPress Enter to coninue.".format(self.p1.name, self.p2.name, self.p1.ally.scd[self.ar, self.ac]))
            else:
                print("Commander {}, your attack missed!\n".format(self.p2.name))
                self.p2.com.board[self.ar][self.ac] = self.p2.com.MISS
                self.p1.ally.board[self.ar][self.ac] = self.p1.ally.MISS
                self.p2.com.print_board(self.p2.com.board)
                print('\n Your ALLY WATERS Board\n')
                self.p2.ally.print_board(self.p2.ally.board)
                pause = input("Continue?: press Enter: ")
                os.system('clear')
                pause = input("Commander {}, the Pirate {} missed!\nPress Enter to coninue.".format(self.p1.name, self.p2.name))
            self.p2.attack_list.append((self.ar, self.ac))

Game()
