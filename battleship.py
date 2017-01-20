from grid import Board
from character1 import Player
from collections import Counter
import sys
import os


# scd = ship_coordinates_dict - This is used to keep track of the ship names and where th
# ar/ac = attack_row/column
# pr/pc = placement_row/column

class Game:

    index = 0

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
        self.players = [Player(), Player()]
        index = 0
        # Game loop
        while True:

            self.players[index].turn()
            self.val_attack(index)
            self.cleanup(index)

            if index == 0:
                index = 1
            else:
                index = 0

    def cleanup(self, index):
        p1 = self.players[index]
        p2 = self.players[index - 1]
        # test if all ships have been destroyed
        if p1.com.scd == p2.ally.scd:
            print("Commander {} WINS!\n".format(p1.name))
            print("Commander {}'s Command Center\n".format(p1.name))
            p1.com.print_board(p1.com.board)
            print("Commander {}'s ALLY WATERS\n".format(p1.name))
            p1.ally.print_board(p1.ally.board)
            print("Commander {}'s Command Center\n".format(p2.name))
            p2.com.print_board(p2.com.board)
            print("Commander {}'s ALLY WATERS\n".format(p2.name))
            p2.ally.print_board(p2.ally.board)
            print("Thanks for playing!")
            sys.exit()

    def val_attack(self, index):
        p1 = self.players[index]
        p2 = self.players[index - 1]

        # val coordinates against opponent ship dict
        # - requires both instances of player (ships)
        if ((p1.ar, p1.ac)) in p2.ally.scd:
            # report to player the outcome of the attack and record for further reference
            print("Commander {}, you hit {}'s ship!".format(p1.name, p2.name))
            # update com ship coordinates for cleanup
            p1.com.scd[(p1.ar, p1.ac)] = p2.ally.scd[(p1.ar, p1.ac)]
            # update com board
            p1.com.board[p1.ar][p1.ac] = p1.com.HIT
            # update opponent ally board
            p2.ally.board[p1.ar][p1.ac] = p2.ally.HIT
            # print com board
            p1.com.print_board(p1.com.board)
            # allow other player to get in front of screen
            pause = input("Continue?: press Enter: ")
            os.system('clear')
            # new player prompt
            c = Counter(p1.com.scd.values())
            if c[p1.com.scd[(p1.ar, p1.ac)]] == self.SHIP_DICT[p1.com.scd[p1.ar, p1.ac]]:
                for key, value in p1.com.scd.items():
                    if value == p1.com.scd[(p1.ar, p1.ac)]:
                        p1.com.board[key[0]][key[1]] = p1.com.SUNK
                        p2.ally.board[key[0]][key[1]] = p1.com.SUNK
                pause = input("Commander {}, the Pirate {} SUNK your"
                " {}!\nPress Enter to coninue.".format(p2.name, p1.name, p2.ally.scd[p1.ar, p1.ac]))
            else:
                pause = input("Commander {}, the Pirate {} hit your {}!\nPress Enter to coninue.".format(p2.name, p1.name, p2.ally.scd[p1.ar, p1.ac]))
        else:
            print("Commander {}, your attack missed!\n".format(p1.name))
            p1.com.board[p1.ar][p1.ac] = p1.com.MISS
            p2.ally.board[p1.ar][p1.ac] = p2.ally.MISS
            p1.com.print_board(p1.com.board)
            pause = input("Continue?: press Enter: ")
            os.system('clear')
            pause = input("Commander {}, the Pirate {} missed!\nPress Enter to coninue.".format(p2.name, p1.name))
        # record attack for validation against future attacks
        p1.attack_list.append((p1.ar, p1.ac))


Game()
