


# Build Board
    # create an instance of the board with particular attributes
        # BOARD_SIZE
        # What types of markers are available for the board
        # Create a list of tuples for a cartesian-like grid of the
# Place Ships
  # Ask for what kind of ship or cycle through them
  # Ask if ship should be HORIZONTAL_SHIP or VERTICAL_SHIP
  # Display Ship Placement
  # Ask to Place Next Ship... If the Ship Over Laps Prompt Again
  # Once all ships are placed, Prompt the next Player to place ships
  # Roll Die to see you goes first
  # Prompt winner to go first
  # Prompt player to pick where to fire
    # Validate attack - make sure that the location has not already been fired upon
        # if attack is valid check whether or not the attack is a hit or a MISS
            #If the attack is a miss, report miss, display updated boards
            # If attack is a hit, report hit, display updated boards
        # update boards for player
    # ask if player is ready continue to next players turn if yes, clear screen
    # Display updated board with previous hit/miss info
    #



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


class Command(Board):

    def __init__(self, **kwargs):
        self.board = [[self.EMPTY]*self.BOARD_SIZE for _ in range(self.BOARD_SIZE)]
        self.print_board(self.board)

        for key, value in kwargs.items():
          setattr(self, key, value)

class Ally(Board):

    def __init__(self, **kwargs):
        self.board = [[self.EMPTY]*self.BOARD_SIZE for _ in range(self.BOARD_SIZE)]
        self.print_board(self.board)
        self.place_ships()
            # self.ship_list = [self.placement_row - 1)for i in range(0, value)

        for key, value in kwargs.items():
          setattr(self, key, value)

    def place_ships(self):
        self.ship_coordinates_dict = {"Aircraft Carrier": [], "Battleship": [], "Submarine": [], "Cruiser": [], "Patrol Boat": []}
        self.ship_coordinates = list()
        for key, value in self.SHIP_INFO:

            self.placement_row = int(input('In what row would you like to place your {}? '.format(key))) - 1
            self.placement_col = input('In what Column? ').upper()
            self.placement_col = ord(self.placement_col) - 65
            if input('[H]orizontal of [V]ertical? ').lower() == 'h':
                for i in range(0, value):
                    self.board[self.placement_row][self.placement_col + i] = self.HORIZONTAL_SHIP
                    if (self.placement_row, self.placement_col + i) in self.ship_coordinates:
                        print('Your ship placement is overlapping, please pick new coordinates.')
                        self.board = [[self.EMPTY]*self.BOARD_SIZE for _ in range(self.BOARD_SIZE)]
                        self.place_ships()
                    else:
                        self.ship_coordinates_dict[key].append((self.placement_row, self.placement_col + i))
                        self.ship_coordinates.append((self.placement_row, self.placement_col + i))
                        continue
            else:
                for i in range(0, value):
                    self.board[self.placement_row + i][self.placement_col] = self.VERTICAL_SHIP
                    if (self.placement_row + i, self.placement_col) in self.ship_coordinates:
                        print('Your ship placement is overlapping, please pick new coordinates.')
                        self.board = [[self.EMPTY]*self.BOARD_SIZE for _ in range(self.BOARD_SIZE)]
                        self.place_ships()
                    else:
                        self.ship_coordinates_dict[key].append((self.placement_row + i, self.placement_col))
                        self.ship_coordinates.append((self.placement_row + i, self.placement_col))
                        continue
            self.print_board(self.board)
            print(self.ship_coordinates)
            print(self.ship_coordinates_dict)

    # def validate(self, item):
    #     if item in validate_list
