# Author: Joshua White
# Git Username: Keonu94
# Date: 03/10/2022
# Description: Program allows two people to play battleship. Each player will get a 10x10 grid, and place their ships
# on their respective grids. Once ships have been placed, players will take turns firing torpedo's at each other's
# grids/ships until all opponent's ships have been sunk (S = Ship, T = Torpedo that missed, X = Ship that was hit)

class ShipGame:
    """Represents a battleship game that allows two players to place ships and fire torpedo's on their opponent's
    ships. Once a player sinks all of their enemy's ships, they will be declared the winner. Moves(placing ships and
    firing torpedo's) are validated and will return True if valid, and False otherwise"""

    def __init__(self):
        """Takes no parameters and initializes all private data members for current state,
         battle grid(list of dictionaries), first player ships, second
          player ships and player's turn"""
        self._current_state = "UNFINISHED"
        self._grid_1 = [{"A": ["", "", "", "", "", "", "", "", "", ""]}, {"B": ["", "", "", "", "", "", "", "", "", ""]},
                       {"C": ["", "", "", "", "", "", "", "", "", ""]}, {"D": ["", "", "", "", "", "", "", "", "", ""]},
                       {"E": ["", "", "", "", "", "", "", "", "", ""]}, {"F": ["", "", "", "", "", "", "", "", "", ""]},
                       {"G": ["", "", "", "", "", "", "", "", "", ""]}, {"H": ["", "", "", "", "", "", "", "", "", ""]},
                       {"I": ["", "", "", "", "", "", "", "", "", ""]}, {"J": ["", "", "", "", "", "", "", "", "", ""]}]
        self._grid_2 = [{"A": ["", "", "", "", "", "", "", "", "", ""]}, {"B": ["", "", "", "", "", "", "", "", "", ""]},
                       {"C": ["", "", "", "", "", "", "", "", "", ""]}, {"D": ["", "", "", "", "", "", "", "", "", ""]},
                       {"E": ["", "", "", "", "", "", "", "", "", ""]}, {"F": ["", "", "", "", "", "", "", "", "", ""]},
                       {"G": ["", "", "", "", "", "", "", "", "", ""]}, {"H": ["", "", "", "", "", "", "", "", "", ""]},
                       {"I": ["", "", "", "", "", "", "", "", "", ""]}, {"J": ["", "", "", "", "", "", "", "", "", ""]}]
        self._first_ship_coordinates = []     # Stores exact coordinates for first player ships
        self._first_num_of_ships = []         # Each index of list will represent a ship for first player
        self._second_ship_coordinates = []    # Stores exact coordinates for second player ships
        self._second_num_of_ships = []        # Each index of list will represent a ship for second player
        self._player_turn = 'first'

    def place_ship(self, player, length, coordinates, orientation):
        """Takes as arguments the 'first' or 'second', length of the ship, coordinates of the ship,
         and the ship's orientation. Returns False if the ship being placed is too large for the grid, overlaps
         another ship, or the length of the ship is less than 2. Returns True otherwise."""
        letter_coordinates = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        add_coordinate = 0          # Variable is used to keep track of additional coordinates from length/orientation

        # Validate player, length is at least 2, letter coordinate is within grid, and number coordinate is less than 11
        if player == 'first' and length >= 2 and coordinates[0] in letter_coordinates and int(coordinates[1:]) <= 10:
            # Validates that initial coordinate is empty
            for column in self._grid_1:
                if coordinates[0] in column.keys():
                    for row in column.values():
                        if row[int(coordinates[1:]) - 1] == "S":
                            return False
            if orientation == 'C':
                for column in range(len(self._grid_1)):
                    if coordinates[0] in self._grid_1[column].keys():
                        if column + length < len(self._grid_1) + 1:     # Validates next coordinates are within grid
                            while add_coordinate != length - 1:
                                next = column + (length - add_coordinate - 1)
                                # Call column_coordinates method to correctly store coordinates in player's coord list
                                self.column_coordinates('first', str(self._grid_1[next].keys()), coordinates[1])
                                for row in self._grid_1[next].values():
                                    if row[int(coordinates[1:]) - 1] == "":
                                        row[int(coordinates[1:]) - 1] = "S"
                                        add_coordinate += 1
                                    else:
                                        return False
                        else:
                            return False
                # Adds final/initial coordinate for whole ship
                for column in self._grid_1:
                    if coordinates[0] in column.keys():
                        for row in column.values():
                            row[int(coordinates[1:]) - 1] = "S"
                            # Adds coordinates to player's coord list and new ship to player's num of ships
                            self._first_ship_coordinates.append(coordinates)
                            self._first_num_of_ships.append(length)
                            return True

            elif orientation == 'R':
                for column in self._grid_1:
                    if coordinates[0] in column.keys():
                        if length + int(coordinates[1:]) <= 11:   # Validates next coordinates are within grid
                            while add_coordinate != length - 1:
                                for row in column.values():
                                    next = (length + int(coordinates[1])) - add_coordinate - 1
                                    # Adds additional coordinates to player's coord list
                                    self._first_ship_coordinates.append(str(coordinates[0] + str(next)))
                                    if row[next - 1] == "":         # Validates coordinate is empty
                                        row[next - 1] = "S"
                                        add_coordinate += 1
                                    else:
                                        return False
                        else:
                            return False
                # Adds final/initial coordinate for whole ship
                for column in self._grid_1:
                    if coordinates[0] in column.keys():
                        for row in column.values():
                            row[int(coordinates[1:]) - 1] = "S"
                            # Adds coordinates to player's coord list and new ship to player's num of ships
                            self._first_ship_coordinates.append(coordinates)
                            self._first_num_of_ships.append(length)
                            return True

        # Validate player, length is at least 2, letter coordinate is within grid, and number coordinate is less than 11
        elif player == 'second' and length >= 2 and coordinates[0] in letter_coordinates and int(coordinates[1:]) <= 10:
            # Validates that initial coordinate is empty
            for column in self._grid_2:
                if coordinates[0] in column.keys():
                    for row in column.values():
                        if row[int(coordinates[1:]) - 1] == "S":
                            return False
            if orientation == 'C':
                for column in range(len(self._grid_2)):
                    if coordinates[0] in self._grid_2[column].keys():
                        if column + length < len(self._grid_2) + 1:
                            while add_coordinate != length - 1:     # Validates next coordinates are within grid
                                next = column + (length - add_coordinate - 1)
                                # Call column_coordinates method to correctly store coordinates in player's coord list
                                self.column_coordinates('second', str(self._grid_2[next].keys()), coordinates[1])
                                for row in self._grid_2[next].values():
                                    if row[int(coordinates[1:]) - 1] == "":      # Validates coordinate is empty
                                        row[int(coordinates[1:]) - 1] = "S"
                                        add_coordinate += 1
                                    else:
                                        return False
                        else:
                            return False
                # Adds final/initial coordinate for whole ship
                for column in self._grid_2:
                        if coordinates[0] in column.keys():
                            for row in column.values():
                                row[int(coordinates[1:]) - 1] = "S"
                                # Adds coordinates to player's coord list and new ship to player's num of ships
                                self._second_ship_coordinates.append(coordinates)
                                self._second_num_of_ships.append(length)
                                return True

            elif orientation == 'R':
                for column in self._grid_2:
                    if coordinates[0] in column.keys():
                        if length + int(coordinates[1:]) <= 11:      # Validates next coordinates are within grid
                            while add_coordinate != length - 1:
                                for row in column.values():
                                    next = (length + int(coordinates[1])) - add_coordinate - 1
                                    # Adds additional coordinates to player's coord list
                                    self._second_ship_coordinates.append(str(coordinates[0] + str(next)))
                                    if row[next - 1] == "":        # Validates coordinate is empty
                                        row[next - 1] = "S"
                                        add_coordinate += 1
                                    else:
                                        return False
                        else:
                            return False
                # Adds final/initial coordinate for whole ship
                for column in self._grid_2:
                        if coordinates[0] in column.keys():
                            for row in column.values():
                                row[int(coordinates[1:]) - 1] = "S"
                                # Adds coordinates to player's coord list and new ship to player's num of ships
                                self._second_ship_coordinates.append(coordinates)
                                self._second_num_of_ships.append(length)
                                return True
        else:
            return False

    def get_current_state(self):
        """Returns the current state of the game"""
        return self._current_state

    def fire_torpedo(self, player, coordinates):
        """Takes as arguments 'first' or 'second' and coordinates of the target. Returns False if it's not the player's
        turn or if the game has already been won. Otherwise, it will record the move, update player's turn, update the
         current state and return True"""
        if player == self._player_turn and self._current_state == 'UNFINISHED':     # Validates player and game state
            if player == 'first':
                for column in self._grid_2:
                    if coordinates[0] in column.keys():
                        for row in column.values():
                            # If grid location is linked to an empty space ("") or torpedo miss (T), update/retain T
                            if row[int(coordinates[1]) - 1] == "" or row[int(coordinates[1]) - 1] == "T":
                                row[int(coordinates[1]) - 1] = "T"
                            # If grid location is linked to a ship (S) or damaged ship (X), update/retain X
                            elif row[int(coordinates[1]) - 1] == "S" or row[int(coordinates[1]) - 1] == "X":
                                row[int(coordinates[1]) - 1] = "X"
                            self._player_turn = 'second'             # Changes player turn
                            self.ship_status('second', coordinates)  # Call ship status method to update player list
                            return True

            if player == 'second':
                for column in self._grid_1:
                    if coordinates[0] in column.keys():
                        for row in column.values():
                            # If grid location is linked to an empty space ("") or torpedo miss (T), update/retain T
                            if row[int(coordinates[1]) - 1] == "" or row[int(coordinates[1]) - 1] == "T":
                                row[int(coordinates[1]) - 1] = "T"
                            # If grid location is linked to a ship (S) or damaged ship (X), update/retain X
                            elif row[int(coordinates[1]) - 1] == "S" or row[int(coordinates[1]) - 1] == "X":
                                row[int(coordinates[1]) - 1] = "X"
                            self._player_turn = 'first'             # Changes player turn
                            self.ship_status('first', coordinates)  # Call ship status method to update player list
                            return True
        else:
            return False

    def get_num_ships_remaining(self, player):
        """Takes as an argument 'first' or 'second' and returns how many ships the specified player
        has left"""
        if player == "first":
            return len(self._first_num_of_ships)

        elif player == "second":
            return len(self._second_num_of_ships)

    def ship_status(self, player, coordinates):
        """Takes as an argument coordinates that were hit. Updates the player ship lists
        after each valid hit. If a player's coordinate list becomes empty, the current_state data member
        will be updated with a winner. Returns nothing"""
        if player == 'first':
            # Removes ship coordinate from player's list of coordinates if ship was damaged
            if coordinates in self._first_ship_coordinates:
                self._first_ship_coordinates.remove(coordinates)

            # Updates player's num of ships list as each ship is sunk
            ship_size = sum(self._first_num_of_ships) - len(self._first_ship_coordinates)
            if ship_size > min(self._first_num_of_ships):
                remove_ship = min(self._first_num_of_ships)
                self._first_num_of_ships.remove(remove_ship)

            # Checks to see if player still has ships, and updates game state if all ships are sunk
            if len(self._first_ship_coordinates) == 0:
                self._current_state = 'SECOND_WON'

        elif player == 'second':
            # Removes ship coordinate from player's list of coordinates if ship was damaged
            if coordinates in self._second_ship_coordinates:
                self._second_ship_coordinates.remove(coordinates)

            # Updates player's num of ships list as each ship is sunk
            ship_size = sum(self._second_num_of_ships) - len(self._second_ship_coordinates)
            if ship_size > min(self._second_num_of_ships):
                remove_ship = min(self._second_num_of_ships)
                self._second_num_of_ships.remove(remove_ship)

            # Checks to see if player still has ships, and updates game state if all ships are sunk
            if len(self._second_ship_coordinates) == 0:
                self._current_state = 'FIRST_WON'

    def column_coordinates(self, player, letter, num):
        """Takes as an argument, player, letter, num and stores additional
        column coordinates (Ships) for each player"""
        new_coordinate = letter[12] + num           # Splices the letter coordinate to the num coordinate
        if player == 'first':
            self._first_ship_coordinates.append(new_coordinate)

        elif player == 'second':
            self._second_ship_coordinates.append(new_coordinate)

