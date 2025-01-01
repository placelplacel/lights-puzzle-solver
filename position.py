# Position is a List<boolean>
# interp. A puzzle position with each boolean representing the state of the light at
#         their respective index.
class Position:
    # Cell is a (Natural+{0}, Natural+{0})
    # interp. The coordinates of a cell/light.
    class Cell:
        # Cell -> Natural+{0}
        # Returns the x-coordinate of the cell that is fed into it.
        #   -- TEMPLATE
        # def get_x(self):
        #     pass
        def get_x(self):
            return self._x

        # Cell -> Natural+{0}
        # Returns the y-coordinate of the cell that is fed into it.
        #   -- TEMPLATE
        # def get_y(self):
        #     pass
        def get_y(self):
            return self._y

        # Natural+{0}, Natural+{0} -> Cell
        # Produces a Cell object representing the cell at the given coordinates, where
        # the coordinates are of format(x, y) and +y points downwards.
        #   -- TEMPLATE
        # def __init__(self, x, y):
        #     assert isinstance(x, int) and x >= 0, "'x' is not a non-negative integer."
        #     assert isinstance(y, int) and y >= 0, "'y' is not a non-negative integer."
        #     pass
        def __init__(self, x=0, y=0):
            assert isinstance(x, int) and x >= 0, "'x' is not a non-negative integer."
            assert isinstance(y, int) and y >= 0, "'y' is not a non-negative integer."

            self._x = x
            self._y = y

        # Cell -> int
        # Produces the index that the cell represents based on the grid specified by
        # Position.num_rows and Position.num_columns.
        #   -- TEMPLATE
        # def __index__(self):
        #     pass
        def __index__(self):
            return (self._y * Position.num_columns) + self._x

        # Cell, Cell -> boolean
        # Produces True if the first cell that is fed into it comes after the second
        # when moving left-to-right top-to-down through the grid.
        #   -- TEMPLATE
        # def __gt__(self, other):
        #     assert isinstance(other, Position.Cell), "'other' is not a Cell."
        #     pass
        def __gt__(self, other):
            assert isinstance(other, Position.Cell), "'other' is not a Cell."

            return int(self) > int(other)

        # Cell, Cell -> boolean
        # Produces True if the first cell that is fed into it comes before the second
        # when moving left-to-right top-to-down through the grid.
        #   -- TEMPLATE
        # def __lt__(self, other):
        #     assert isinstance(other, Position.Cell), "'other' is not a Cell."
        #     pass
        def __lt__(self, other):
            assert isinstance(other, Position.Cell), "'other' is not a Cell."

            return int(self) < int(other)

        # Cell, Cell -> boolean
        # Produces True if the first cell that is fed into it is the same as the second.
        #   -- TEMPLATE
        # def __eq__(self, other):
        #     assert isinstance(other, Position.Cell), "'other' is not a Cell."
        #     pass
        def __eq__(self, other):
            assert isinstance(other, Position.Cell), "'other' is not a Cell."

            return self._x == other.get_x() and self._y == other.get_y()

        # Cell -> String
        # Produces a string representing the move that is fed into it.
        def __str__(self):
            return "(%i, %i)" % (self._x, self._y)

    num_rows = 5
    num_columns = 7

    # None -> (Natural+{0}, Natural+{0})
    # Produces a tuple representing the dimensions of the position.
    #   -- TEMPLATE
    # def get_size():
    #    pass
    @staticmethod
    def get_size():
        return Position.num_columns, Position.num_rows

    # Position -> List<boolean>
    # Produces a copy of the list of booleans representing the states of the lights of the
    # position that is fed into it.
    #   -- TEMPLATE
    # def get_light_states(self):
    #    pass
    def get_light_states(self):
        return self._light_states[:]

    # Optional(String) -> Position
    # Returns a Position object representing the position being represented by the string that
    # is fed into it. The position initialized with all light states set to 0 if the string
    # does not contain any data or no argument is passed in.
    #   -- TEMPLATE
    # def __init__(self, pos_string):
    #     assert isinstance(pos_string, str), "'pos_string' is not a str."
    #     pass
    def __init__(self, position_str=""):
        assert isinstance(position_str, str), "'position_str' is not an str."

        self._light_states = []
        self._position_str = position_str.strip()

        if self._position_str == "":
            self._light_states = [0] * (Position.num_rows * Position.num_columns)
            return

        row_strs = self._position_str.split("/")
        assert len(row_strs) == Position.num_rows, "The number of rows is not %i." % Position.num_rows

        for row_str in row_strs:
            assert len(row_str) == Position.num_columns, \
                    "The row '%s' does not have exactly %i columns." % (row_str, Position.num_columns)

            for state in row_str:
                if state == "1":
                    self._light_states.append(True)
                elif state == "0":
                    self._light_states.append(False)
                else:
                    raise Exception("Unknown symbol '%s' in row '%s'." % (state, row_str))

    # Position, Position -> boolean
    # Produces True if the light states of the two operand Positions are the same and False
    # otherwise.
    #   -- TEMPLATE
    # def __eq__(self, other):
    #     assert isinstance(other, Position), "'other' is not a Position."
    #     pass
    def __eq__(self, other):
        assert isinstance(other, Position), "'other' is not a Position."

        return self._light_states == other._light_states

    # Position, Cell -> Position
    # Produces the position after making a move from the position that is fed into it, at the
    # coordinates of the provided cell (i.e. the position after toggling the light at that point
    # along with its neighbors).
    #   -- TEMPLATE
    # def make_move(self, cell):
    #     assert isinstance(cell, Position.Cell), "'cell' is not a Cell."
    #     pass
    def make_move(self, cell):
        assert isinstance(cell, Position.Cell), "'cell' is not a Cell."

        result = Position(self._position_str)

        def try_toggle_light(x, y):
            # Assumes that 'x' and 'y' are always integers.
            if 0 <= x < Position.num_columns and 0 <= y < Position.num_rows:
                index = int(Position.Cell(x, y))
                result._light_states[index] = not result._light_states[index]

        try_toggle_light(cell.get_x(),     cell.get_y())
        try_toggle_light(cell.get_x() - 1, cell.get_y())
        try_toggle_light(cell.get_x() + 1, cell.get_y())
        try_toggle_light(cell.get_x(),     cell.get_y() - 1)
        try_toggle_light(cell.get_x(),     cell.get_y() + 1)

        result._position_str = ""
        for i in range(len(result._light_states)):
            if i % Position.num_columns == 0 and not i == 0:
                result._position_str += "/"
            result._position_str += "%i" % result._light_states[i]

        return result

    # Position -> None
    # Prints out a 2D representation of the position's current state.
    #   -- TEMPLATE
    # def print(self):
    #     pass
    def print(self):
        for i in range(len(self._light_states)):
            if i % Position.num_columns == 0:
                print()
            print(" %i" % self._light_states[i], end="")

    # Position -> String
    # Produces a string representing the position that is fed into it.
    #   -- TEMPLATE
    # def __str__(self):
    #     pass
    def __str__(self):
        return self._position_str

    # Position -> Position
    # Produces a copy of the position that is fed into it.
    #   -- TEMPLATE
    # def __copy__(self):
    #     pass
    def __copy__(self):
        return Position(self._position_str)
