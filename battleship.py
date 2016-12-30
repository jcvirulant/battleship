from grid import Board
from character1 import Player
import sys
import os


class Game:

    SHIP_DICT = {"Aircraft Carrier": 5,
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
        self.player1 = Player()
        self.player2 = Player()

        # Game loop
        while True:

          self.player1_turn()
          self.cleanup()
          self.player2_turn()
          self.cleanup()


    def validate_attack_row(self):

        try:
            self.attack_row = int(input('Row Number: ')) - 1
        except ValueError:
            os.system('cls')
            print('You input an improper value. Please enter an integer between 1 and 10.')
            self.validate_attack_row()
        else:
            if self.attack_row in range(10):
                return self.attack_row
            else:
                os.system('cls')
                print('Your input was outside the range of the possible inputs. Please enter an integer between 1 and 10.')
                self.validate_attack_row()

    def validate_attack_col(self):
        try:
            self.attack_col = input('In what Column? ').upper()
            self.attack_col = ord(self.attack_col) - 65
        except TypeError:
            os.system('cls')
            print('Your input was the wrong type. Please choose a letter from A - J')
            self.validate_attack_col()
        else:
            if self.attack_col in range(10):
                return self.attack_col
            else:
                os.system('cls')
                print('Your input was outside the range of the possible inputs. Please choose column A - J.')
                self.validate_attack_col()

    def cleanup(self):
        # test if all ships have been destroyed - requires both instances of player
        if self.player1.command.ship_coordinates_dict == self.player2.ally.ship_coordinates_dict:
            print("Commander {} WINS!\n".format(self.player1.name))
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
            print("Commander {} WINS!\n".format(self.player2.name))
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
        # prompt player for coordinates - requires only one instance of player
         print("\n"+"="*20)
         print('You are up Commander {}! Try to sink your opponents ships!'.format(self.player1.name))
         print('\n')
        # Display command board
        print("Commander {}, your Command Center\n".format(self.player1.name))
        self.player1.command.print_board(self.player1.command.board)
        print("Commander {}, your ALLY WATERS\n".format(self.player1.name))
        self.player1.ally.print_board(self.player1.ally.board)
        print('\n\nCommander {}, where would you like to attack?'.format(self.player1.name))
        self.validate_attack_row()
        self.validate_attack_col()
        # validate against previous attacks

        if (self.attack_row, self.attack_col) in self.player1.attack_list:
            print("Commander {}, you have already attacked these coordinates.".format(self.player1.name))
            self.player1_turn()
        else:
            # validate coordinates against opponent ship dict - requires both instances of player (ships)
            if ((self.attack_row, self.attack_col)) in self.player2.ally.ship_coordinates_dict:
                # report to player the outcome of the attack and record for further reference
                print("Commander {}, you hit {}'s ship!".format(self.player1.name, self.player2.name))
                # update command ship coordinates for cleanup
                self.player1.command.ship_coordinates_dict[(self.attack_row, self.attack_col)] = self.player2.ally.ship_coordinates_dict[self.attack_row, self.attack_col]
                # update command board
                self.player1.command.board[self.attack_row][self.attack_col] = self.player1.command.HIT
                # update opponent ally board
                self.player2.ally.board[self.attack_row][self.attack_col] = self.player2.ally.HIT
                # print command board
                self.player1.command.print_board(self.player1.command.board)
                # allow other player to get in front of screen
                pause = input("Continue?: press Enter: ")
                os.system('cls')
                # new player prompt
                if sum(1 for self.player2.ally.ship_coordinates_dict[self.attack_row, self.attack_col] in self.player1.command.ship_coordinates_dict.values()) == self.SHIP_DICT[self.player2.ally.ship_coordinates_dict[self.attack_row, self.attack_col]]:
                    pause = input("Commander {}, the Pirate {} SUNK your {}!\nPress Enter to coninue.".format(self.player2.name, self.player1.name, self.player2.ally.ship_coordinates_dict[self.attack_row, self.attack_col]))
                else:
                    pause = input("Commander {}, the Pirate {} hit your {}!\nPress Enter to coninue.".format(self.player2.name, self.player1.name, self.player2.ally.ship_coordinates_dict[self.attack_row, self.attack_col]))
            else:
                print("Commander {}, your attack missed!\n".format(self.player1.name))
                self.player1.command.board[self.attack_row][self.attack_col] = self.player1.command.MISS
                self.player2.ally.board[self.attack_row][self.attack_col] = self.player2.ally.MISS
                self.player1.command.print_board(self.player1.command.board)
                pause = input("Continue?: press Enter: ")
                os.system('cls')
                pause = input("Commander {}, the Pirate {} missed!\nPress Enter to coninue.".format(self.player2.name, self.player1.name))
            # record attack for validation against future attacks
            self.player1.attack_list.append((self.attack_row, self.attack_col))


    def player2_turn(self):
        # prompt player for coordinates
         print("\n"+"="*20)
         print('You are up Commander {}! Try to sink your opponents ships!'.format(self.player2.name))
         print('\n')
        # Display command board
        print("Commander {}, your Command Center\n".format(self.player2.name))
        self.player2.command.print_board(self.player2.command.board)
        print("Commander {}, your ALLY WATERS\n".format(self.player2.name))
        self.player2.ally.print_board(self.player2.ally.board)
        print('\n\nCommander {}, where would you like to attack?'.format(self.player2.name))
        self.validate_attack_row()
        self.validate_attack_col()
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
                # # print command board
                self.player2.command.print_board(self.player2.command.board)
                pause = input("Continue?: press Enter: ")
                os.system('cls')
                # new player prompt - validating whether or not the ship was sunk
                if sum(1 for self.player1.ally.ship_coordinates_dict[self.attack_row, self.attack_col] in self.player2.command.ship_coordinates_dict.values()) == self.SHIP_DICT[self.player1.ally.ship_coordinates_dict[self.attack_row, self.attack_col]]:
                    pause = input("Commander {}, the Pirate {} SUNK your {}!\nPress Enter to coninue.".format(self.player1.name, self.player2.name, self.player1.ally.ship_coordinates_dict[self.attack_row, self.attack_col]))
                else:
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

