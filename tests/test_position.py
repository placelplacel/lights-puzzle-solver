import unittest
from position import Cell, Position


class TestPosition(unittest.TestCase):
    def test_num_cells(self):
        test_cases = [
            (Position(0, 0), 0),
            (Position(3, 4), 12),
            (Position(0, 1), 0)
        ]

        for (position, actual_output) in test_cases:
            self.assertEqual(position.num_cells, actual_output)

    def test_from_str(self):
        test_cases = [
            (1, 1, "1",       [True]),
            (2, 3, "001/011", [False, False, True,
                               False, True,  True]),
        ]

        for (num_rows, num_columns, position_str, actual_output) in test_cases:
            self.assertEqual(Position(num_rows, num_columns, position_str).light_states, actual_output)

    def test_make_move(self):
        test_cases = [
            (1, 1, "1",           Cell(0, 0), "0"),
            (2, 2, "10/11",       Cell(1, 0), "01/10"),
            (2, 3, "101/111",     Cell(2, 1), "100/100"),
            (3, 3, "101/000/101", Cell(1, 1), "111/111/111")
        ]

        for (num_rows, num_columns, position_str, cell, actual_output_str) in test_cases:
            self.assertEqual(Position(num_rows, num_columns, position_str).make_move(cell),
                             Position(num_rows, num_columns, actual_output_str))

    def test_index_of(self):
        test_cases = [
            (Cell(0, 0), 0),
            (Cell(0, 1), 8),
            (Cell(3, 2), 19),
        ]

        position = Position(3, 8)
        for (cell, actual_output) in test_cases:
            self.assertEqual(position.index_of(cell), actual_output)

    def test_same_size_as(self):
        test_cases = [
            (Position(1, 1, "1"),       Position(1, 1, "0"),        True),
            (Position(2, 3, "101/111"), Position(2, 2, "10/10"),    False),
            (Position(2, 3, "101/111"), Position(1, 3, "100"),      False),
            (Position(1, 1, "1"),       Position(3, 2, "10/10/01"), False),
        ]

        for (operand_1, operand_2, actual_output) in test_cases:
            self.assertEqual(operand_1.same_size_as(operand_2), actual_output)

    def test_copy(self):
        test_cases = [
            (1, 1, "1"),
            (2, 3, "101/111"),
        ]

        for (num_rows, num_columns, position_str) in test_cases:
            position = Position(num_rows, num_columns, position_str)
            self.assertEqual(position.__copy__(), position)

    def test_eq(self):
        test_cases = [
            (1, 1, "1",       "1",       True),
            (2, 3, "101/111", "101/011", False),
        ]

        for (num_rows, num_columns, position_str_1, position_str_2, actual_output) in test_cases:
            self.assertEqual(Position(num_rows, num_columns, position_str_1)
                             == Position(num_rows, num_columns, position_str_2), actual_output)


if __name__ == '__main__':
    unittest.main()
