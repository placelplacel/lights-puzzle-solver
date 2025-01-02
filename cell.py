# Cell is a (Integer, Integer)
# interp. The coordinates of a cell/light.
class Cell:
    # Cell -> Integer
    # Returns the x-coordinate of the cell that is fed into it.
    #   -- TEMPLATE
    # @property
    # def x(self):
    #     pass
    @property
    def x(self):
        return self._x

    # Cell -> Integer
    # Returns the y-coordinate of the cell that is fed into it.
    #   -- TEMPLATE
    # @property
    # def y(self):
    #     pass
    @property
    def y(self):
        return self._y

    # Integer, Integer -> Cell
    # Produces a Cell object representing the cell at the given coordinates, where
    # the coordinates are of format(x, y) and +y points downwards.
    #   -- TEMPLATE
    # def __init__(self, x, y):
    #     assert isinstance(x, int), "'x' is not an integer."
    #     assert isinstance(y, int), "'y' is not an integer."
    #     pass
    def __init__(self, x=0, y=0):
        assert isinstance(x, int), "'x' is not an integer."
        assert isinstance(y, int), "'y' is not an integer."

        self._x = x
        self._y = y

    # Cell, Cell -> boolean
    # Produces True if the first cell that is fed into it comes after the second
    # when moving left-to-right top-to-down through any grid.
    #   -- TEMPLATE
    # def __gt__(self, other):
    #     assert isinstance(other, Cell), "'other' is not a Cell."
    #     pass
    def __gt__(self, other):
        assert isinstance(other, Cell), "'other' is not a Cell."

        return self._y > other._y or (self._y == other._y and self._x > other._x)

    # Cell, Cell -> boolean
    # Produces True if the first cell that is fed into it comes before the second
    # when moving left-to-right top-to-down through any grid.
    #   -- TEMPLATE
    # def __lt__(self, other):
    #     assert isinstance(other, Cell), "'other' is not a Cell."
    #     pass
    def __lt__(self, other):
        assert isinstance(other, Cell), "'other' is not a Cell."

        return self._y < other._y or (self._y == other._y and self._x < other._x)

    # Cell, Cell -> boolean
    # Produces True if the first cell that is fed into it is the same as the second.
    #   -- TEMPLATE
    # def __eq__(self, other):
    #     assert isinstance(other, Cell), "'other' is not a Cell."
    #     pass
    def __eq__(self, other):
        assert isinstance(other, Cell), "'other' is not a Cell."

        return self._x == other.x and self._y == other.y

    # Cell, Cell -> Cell
    # Produces a cell where the x-coordinate is the sum of the x-coordinates of the two
    # cells that are fed into it, and the y-coordinate is the sum of their y-coordinates.
    #   -- TEMPLATE
    # def __add__(self, other):
    #     assert isinstance(other, Cell), "'other' is not a Cell."
    #     pass
    def __add__(self, other):
        assert isinstance(other, Cell), "'other' is not a Cell."

        return Cell(self._x + other._x, self._y + other._y)

    # Cell, Cell -> Cell
    # Produces a cell where the x-coordinate is the difference of the x-coordinates
    # of the two cells that are fed into it, and the y-coordinate is the difference
    # of their y-coordinates.
    #   -- TEMPLATE
    # def __sub__(self, other):
    #     assert isinstance(other, Cell), "'other' is not a Cell."
    #     pass
    def __sub__(self, other):
        assert isinstance(other, Cell), "'other' is not a Cell."

        return Cell(self._x - other._x, self._y - other._y)

    # Cell -> String
    # Produces a string representing the move that is fed into it.
    def __str__(self):
        return "(%i, %i)" % (self._x, self._y)
