class Board:

    BOARD_SIZE = 10
    VERTICAL_SHIP = '|'
    HORIZONTAL_SHIP = '-'
    EMPTY = 'O'
    MISS = '.'
    HIT = '*'
    SUNK = '#'
    SHIP_INFO = [("Aircraft Carrier", 5),
                ("Battleship", 4),
                ("Submarine", 3),
                ("Cruiser", 3),
                ("Patrol Boat", 2)
                ]


    def __init__(self, **kwargs):

        for key, value in kwargs.items():
          setattr(self, key, value)

    def print_board_heading(self):
        print("   " + " ".join([chr(c) for c in range(ord('A'), ord('A') + self.BOARD_SIZE)]))

    def print_board(self, board):

        self.print_board_heading()

        row_num = 1
        for row in self.board:
            print(str(row_num).rjust(2) + " " + (" ".join(row)))
            row_num += 1

    def validate_row(self):

        try:
            self.placement_row = int(input('Row Number: ')) - 1
        except ValueError:
            os.system('cls')
            print('You input an improper value. Please enter an integer between 1 and 10.')
            self.validate_row()
        else:
            if self.placement_row in range(10):
                return self.placement_row
            else:
                os.system('cls')
                print('Your input was outside the range of the possible inputs. Please enter an integer between 1 and 10.')
                self.validate_row()

    def validate_col(self):
        try:
            self.placement_col = input('In what Column? ').upper()
            self.placement_col = ord(self.placement_col) - 65
        except TypeError:
            os.system('cls')
            print('Your input was the wrong type. Please choose a letter from A - J.')
            self.validate_col()
        else:
            if self.placement_col in range(10):
                return self.placement_col
            else:
                os.system('cls')
                print('Your input was outside the range of the possible inputs. Please choose column A - J.')
                self.validate_col()

    def validate_or(self):

        self.orientation = input('[H]orizontal of [V]ertical? ').lower()

        if self.orientation == 'h': # Not sure why I couldn't use an "or" statement
            return self.orientation
        elif self.orientation == 'v':
            return self.orientation
        else:
            os.system('cls')
            print('Please choose H for Horizontal or V for Vertical.')
            self.validate_or()

class Command(Board):


    def __init__(self, **kwargs):
        self.ship_coordinates_dict = {}
        self.board = [[self.EMPTY]*self.BOARD_SIZE for _ in range(self.BOARD_SIZE)]
        self.print_board(self.board)

        for key, value in kwargs.items():
          setattr(self, key, value)

class Ally(Board):

    def __init__(self, **kwargs):
        self.board = [[self.EMPTY]*self.BOARD_SIZE for _ in range(self.BOARD_SIZE)]
        self.print_board(self.board)
        self.place_ships()


        for key, value in kwargs.items():
          setattr(self, key, value)

    def place_ships(self):

        self.ship_coordinates_dict = {}
        self.ship_coordinates = list()

        for key, value in self.SHIP_INFO:
            print('In where would you like to place your {}?\n '.format(key))
            self.validate_row()
            self.validate_col()
            self.validate_or()

            if self.orientation == 'h':
                h = 1
                v = 0
            else:
                h = 0
                v = 1

            for i in range(0, value):
                try:
                    self.board[self.placement_row + (v*i)][self.placement_col + (h*i)] = (self.HORIZONTAL_SHIP * h) + (self.VERTICAL_SHIP * v)
                except IndexError:
                    print('Make sure to pick coordinates that account for the length of the ships.\n')
                    print(self.SHIP_INFO)
                    self.place_ships()
                if (self.placement_row + (v*i), self.placement_col + (h*i)) in self.ship_coordinates:
                    print('Your ship placement is overlapping, please pick new coordinates.')
                    self.board = [[self.EMPTY]*self.BOARD_SIZE for _ in range(self.BOARD_SIZE)]
                    self.place_ships()
                else:
                    self.ship_coordinates_dict[self.placement_row + (v*i), self.placement_col + (h*i)] = key
                    self.ship_coordinates.append((self.placement_row + (v*i), self.placement_col + (h*i)))
                    continue

            self.print_board(self.board)

