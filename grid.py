import os


class Board:

    BOARD_SIZE = 10
    V = '|'
    HZ = '-'
    EMPTY = 'O'
    MISS = '.'
    HIT = '*'
    SUNK = '#'
    SHIP_INFO = [
        ("Aircraft Carrier", 5),
        ("Battleship", 4),
        ("Submarine", 3),
        ("Cruiser", 3),
        ("Patrol Boat", 2)
                ]

    def __init__(self, **kwargs):

        for key, value in kwargs.items():
            setattr(self, key, value)

    def print_board_heading(self):
        print("   " + " ".join([
            chr(c) for c in range(ord('A'), ord('A') + self.BOARD_SIZE)]))

    def print_board(self, board):

        self.print_board_heading()

        row_num = 1
        for row in self.board:
            print(str(row_num).rjust(2) + " " + (" ".join(row)))
            row_num += 1

    def val_row(self):

        try:
            self.pr = int(input('Row Number: ')) - 1
        except ValueError:
            os.system('clear')
            print('You input an improper value.'
                  'Please enter an integer between 1 and 10.')
            self.print_board(self.board)
            self.val_row()
        else:
            if self.pr in range(10):
                return self.pr
            else:
                os.system('clear')
                print('Your input was outside the range of the possible'
                      'inputs. Please enter an integer between 1 and 10.')
                self.print_board(self.board)
                self.val_row()

    def val_col(self):
        try:
            self.pc = input('In what Column? ').upper().strip()
            self.pc = ord(self.pc) - 65
        except TypeError:
            os.system('clear')
            print('Your input was the wrong type.'
                  'Please choose a letter from A - J.')
            self.print_board(self.board)
            self.val_col()
        else:
            if self.pc in range(10):
                return self.pc
            else:
                os.system('clear')
                print('Your input was outside the range of possible inputs.'
                      'Please choose column A - J.')
                self.print_board(self.board)
                self.val_col()

    def val_or(self):

        self.orientation = input('[H]orizontal of [V]ertical? ').lower()
        # Not sure why I couldn't use an "or" statement
        if self.orientation == 'h':
            return self.orientation
        elif self.orientation == 'v':
            return self.orientation
        else:
            os.system('clear')
            print('Please choose H for Horizontal or V for Vertical.')
            self.val_or()


class Command(Board):

    def __init__(self, **kwargs):
        self.scd = {}
        self.board = [
            [self.EMPTY]*self.BOARD_SIZE for _ in range(self.BOARD_SIZE)]
        self.print_board(self.board)

        for key, value in kwargs.items():
            setattr(self, key, value)


class Ally(Board):

    def __init__(self, **kwargs):
        self.board = [
            [self.EMPTY]*self.BOARD_SIZE for _ in range(self.BOARD_SIZE)]
        self.print_board(self.board)
        self.place_ships()

        for key, value in kwargs.items():
            setattr(self, key, value)

    def place_ships(self):
        self.scd = {}
        self.ship_coordinates = list()
        for key, value in self.SHIP_INFO:
            print('In where would you like to place your {}?\n '.format(key))
            self.val_row()
            self.val_col()
            self.val_or()

            if self.orientation == 'h':
                h = 1
                v = 0
            else:
                h = 0
                v = 1

            for i in range(0, value):
                try:
                    self.board[self.pr + (v*i)][
                        self.pc + (h*i)] = (self.HZ * h) + (self.V * v)
                except IndexError:
                    os.system('clear')
                    print('Your ship placement did not fit on the board.'
                          '\n\nMake sure to pick coordinates that account'
                          'for the length of the ships.\n')
                    print(self.SHIP_INFO)
                    print('\n')
                    self.board = [[
                        self.EMPTY] * self.BOARD_SIZE for _ in range(
                        self.BOARD_SIZE)]
                    self.print_board(self.board)
                    self.place_ships()
                if (self.pr + (v*i), self.pc + (h*i)) in self.ship_coordinates:
                    print('Your ship placement is overlapping,'
                          'please pick new coordinates.')
                    self.board = [[
                        self.EMPTY] * self.BOARD_SIZE for _ in range(
                        self.BOARD_SIZE)]
                    self.print_board(self.board)
                    self.place_ships()
                else:
                    self.scd[self.pr + (v*i), self.pc + (h*i)] = key
                    self.ship_coordinates.append(
                        (self.pr + (v*i), self.pc + (h*i)))
                    continue

            self.print_board(self.board)
