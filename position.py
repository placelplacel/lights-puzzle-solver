from cell import Cell


# Position is a List<boolean>
# interp. A puzzle position with each boolean representing the state of the light at
#         their respective index.
class Position:
    # Position -> Natural+{0}
    # Produces the number of columns in the position that is fed into it.
    #   -- TEMPLATE
    # @property
    # def num_columns(self):
    #    pass
    @property
    def num_columns(self):
        return self._num_columns

    # Position -> Natural+{0}
    # Produces the number of rows in the position that is fed into it.
    #   -- TEMPLATE
    # @property
    # def num_rows(self):
    #    pass
    @property
    def num_rows(self):
        return self._num_rows

    # Position -> Natural+{0}
    # Produces the number of cells in the position that is fed into it.
    #   -- TEMPLATE
    # @property
    # def num_cells(self):
    #    pass
    @property
    def num_cells(self):
        return self._num_rows * self._num_columns

    # Position -> List<boolean>
    # Produces a copy of the list of booleans representing the states of the lights of the
    # position that is fed into it.
    #   -- TEMPLATE
    # @property
    # def light_states(self):
    #    pass
    @property
    def light_states(self):
        return self._light_states[:]

    # Natural, Natural, Optional(String) -> Position
    # Returns a Position object representing the position being represented by the string that
    # is fed into it. The position initialized with all light states set to 0 if the string
    # does not contain any data or no argument is passed in.
    #   -- TEMPLATE
    # def __init__(self, num_rows, num_columns, pos_string):
    #     assert isinstance(num_rows, int) and num_rows >= 0, "'num_rows' is not a non-negative integer."
    #     assert isinstance(num_columns, int) and num_columns >= 0, "'num_columns' is not a non-negative integer."
    #     assert isinstance(pos_string, str), "'pos_string' is not a str."
    #     pass
    def __init__(self, num_rows=0, num_columns=0, position_str=""):
        assert isinstance(num_rows, int) and num_rows >= 0, "'num_rows' is not a non-negative integer."
        assert isinstance(num_columns, int) and num_columns >= 0, "'num_columns' is not a non-negative integer."
        assert isinstance(position_str, str), "'position_str' is not an str."

        self._light_states = []
        self._num_rows = num_rows
        self._num_columns = num_columns
        self._position_str = position_str.strip()

        if self._position_str == "":
            self._light_states = [False] * self.num_cells
            return

        row_strs = self._position_str.split("/")
        assert len(row_strs) == self._num_rows, "The number of rows is not %i." % self._num_rows

        for row_str in row_strs:
            assert len(row_str) == self._num_columns, \
                    "The row '%s' does not have exactly %i columns." % (row_str, self._num_columns)

            for state in row_str:
                if state == "1":
                    self._light_states.append(True)
                elif state == "0":
                    self._light_states.append(False)
                else:
                    raise Exception("Unknown symbol '%s' in row '%s'." % (state, row_str))

    # Position, Cell -> Position
    # Produces the position after making a move from the position that is fed into it, at the
    # coordinates of the provided cell (i.e. the position after toggling the light at that point
    # along with its neighbors). The cell must be within the position's bounds.
    #   -- TEMPLATE
    # def make_move(self, cell):
    #     assert isinstance(cell, Cell), "'cell' is not a Cell."
    #     assert cell in self, "'cell' is out of bounds."
    #     pass
    def make_move(self, cell):
        assert isinstance(cell, Cell), "'cell' is not a Cell."
        assert cell in self, "'cell' is out of bounds."

        result = self.__copy__()

        def try_toggle_light(target_cell):
            # Assumes that 'target_cell' is always a Cell.
            try:
                index = self.index_of(target_cell)
                result._light_states[index] = not result._light_states[index]
            except AssertionError:
                pass

        try_toggle_light(cell)
        try_toggle_light(cell - Cell(1, 0))
        try_toggle_light(cell + Cell(1, 0))
        try_toggle_light(cell - Cell(0, 1))
        try_toggle_light(cell + Cell(0, 1))

        result._position_str = ""
        for i in range(len(result._light_states)):
            if i % self._num_columns == 0 and not i == 0:
                result._position_str += "/"
            result._position_str += "%i" % result._light_states[i]

        return result

    # Position, Cell -> int
    # Produces the index that the cell represents based on the grid specified by provided position.
    # The cell must be in the bounds of the position.
    #   -- TEMPLATE
    # def index_of(self, cell):
    #     assert isinstance(cell, Cell), "'cell' is not a Cell."
    #     assert 0 <= cell.x < self._num_columns and 0 <= cell.get_y < self._num_rows, \
    #         "'cell' is not in the bounds of 'position'."
    #     pass
    def index_of(self, cell):
        assert isinstance(cell, Cell), "'cell' is not a Cell."
        assert 0 <= cell.x < self._num_columns and 0 <= cell.y < self._num_rows, \
            "'cell' is not in the bounds of 'position'."

        return (cell.y * self._num_columns) + cell.x

    # Position -> None
    # Prints out a 2D representation of the position's current state.
    #   -- TEMPLATE
    # def print(self):
    #     pass
    def print(self):
        for i in range(len(self._light_states)):
            if i % self._num_columns == 0:
                print()
            print(" %i" % self._light_states[i], end="")

    # Position, Position -> boolean
    # Produces True if the two positions have the same dimensions.
    #   -- TEMPLATE
    # def same_size_as(self, other):
    #     assert isinstance(other, Position), "'other' is not a Position."
    #     pass
    def same_size_as(self, other):
        assert isinstance(other, Position), "'other' is not a Position."

        return self._num_rows == other._num_rows and self._num_columns == other._num_columns

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

    # Position, Cell -> boolean
    # Produces True if the cell is in the bounds of the position that is fed into it.
    #   -- TEMPLATE
    # def __contains__(self, item):
    #     assert isinstance(item, Cell), "'item' is not a Cell."
    #     pass
    def __contains__(self, item):
        assert isinstance(item, Cell), "'item' is not a Cell."

        return 0 <= item.x < self._num_columns and 0 <= item.y < self._num_rows

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
        return Position(self._num_rows, self._num_columns, self._position_str)
