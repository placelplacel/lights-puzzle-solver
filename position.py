# Position is a List<List<boolean>>
# interp. a puzzle position with each boolean representing the state of
#         the light at that position.

class Position:
    @property
    def size(self):
        return self._rows, self._columns

    @property
    def light_states(self):
        return self._light_states[:]

    # String -> Position
    # Returns a Position object representing the position being represented by the string
    # that is fed into it.
    # -- TEMPLATE
    # def __init__(self, pos_string):
    #     assert isinstance(pos_string, str), "'pos_string' is not a str."
    #     pass
    def __init__(self, position_str):
        assert isinstance(position_str, str), "'position_str' is not an str."

        self._light_states = []
        self._rows = 0
        self._columns = 0
        self._position_str = position_str

        row = []
        for state in self._position_str.strip():
            if state == "1":
                row.append(True)
            elif state == "0":
                row.append(False)
            elif state == "/":
                if self._columns != len(row):
                    if self._columns > 0:
                        raise Exception("The number of columns is not the same for every row.")
                    else:
                        self._columns = len(row)
                self._light_states.append(row)
                row = []
                self._rows += 1
            else:
                raise Exception("Unknown symbol '%s' in 'position_str'." % state)

    # Position, Position -> boolean
    # Produces True if the light states of the two operand Positions are the same and False
    # otherwise.

    # -- TEMPLATE
    # def __eq__(self, other):
    #     assert isinstance(other, Position), "'other' is not a Position."
    #     pass

    def __eq__(self, other):
        assert isinstance(other, Position), "'other' is not a Position."

        return self._light_states == other._light_states

    # (Integer, Integer) -> Position
    # Produces the position after making a move at the provided coordinates (i.e. the position
    # after toggling the light at that point along with its neighbors).
    # -- TEMPLATE
    # def make_move(self, row, column):
    #     assert isinstance(row, int) and row >= 0, "'row' is not a non-negative integer."
    #     assert isinstance(column, int) and column >= 0, "'column' is not a non-negative integer."
    #     pass
    def make_move(self, row, column):
        assert isinstance(row, int) and 0 <= row < self._rows, "'row' is out of bounds."
        assert isinstance(column, int) and 0 <= column < self._columns, "'column' is out of bounds."

        result = Position(self._position_str)

        def try_toggle_light(_row, _column):
            if 0 <= _row < self._rows and 0 <= _column < self._columns:
                result._light_states[_row][_column] = not result._light_states[_row][_column]

        try_toggle_light(row,     column)
        try_toggle_light(row - 1, column)
        try_toggle_light(row + 1, column)
        try_toggle_light(row,     column - 1)
        try_toggle_light(row,     column + 1)

        result._position_str = ""
        for row in result._light_states:
            for state in row:
                result._position_str += "%i" % state
            result._position_str += "/"

        return result

    # None -> None
    # Prints out a 2D representation of the position's current state.
    # -- TEMPLATE
    # def print(self):
    #     pass
    def print(self):
        for row in self._light_states:
            for state in row:
                print(" %i" % state, end="")
            print()

    # None -> String
    # Returns a string representing the position.
    # -- TEMPLATE
    # def __str__(self):
    #     pass
    def __str__(self):
        return self._position_str
