import unittest
from position import Position


class TestPosition(unittest.TestCase):
    def test_from_string(self):
        test_cases = [
            ("1",       1, 1, [True]),
            ("001/011", 2, 3, [False, False, True,
                               False, True,  True]),
        ]

        for (position_str, num_rows, num_columns, actual_output) in test_cases:
            Position.num_rows = num_rows
            Position.num_columns = num_columns
            self.assertEqual(Position(position_str).get_light_states(), actual_output)

    def test_eq(self):
        test_cases = [
            ("1",       "1",       1, 1, True),
            ("101/111", "101/011", 2, 3, False),
        ]

        for (position_str_1, position_str_2, num_rows, num_columns, actual_output) in test_cases:
            Position.num_rows = num_rows
            Position.num_columns = num_columns
            self.assertEqual(Position(position_str_1) == Position(position_str_2), actual_output)

    def test_make_move(self):
        test_cases = [
            ("1",       Position.Cell(0, 0), 1, 1, "0"),
            ("10/11",   Position.Cell(1, 0), 2, 2, "01/10"),
            ("101/111", Position.Cell(2, 1), 2, 3, "100/100"),
        ]

        for (position_str, cell, num_rows, num_columns, actual_output_str) in test_cases:
            Position.num_rows = num_rows
            Position.num_columns = num_columns
            self.assertEqual(Position(position_str).make_move(cell), Position(actual_output_str))

    def test_copy(self):
        test_cases = [
            ("1",       1, 1),
            ("101/111", 2, 3),
        ]

        for (position_str, num_rows, num_columns) in test_cases:
            Position.num_rows = num_rows
            Position.num_columns = num_columns

            position = Position(position_str)
            self.assertEqual(position.__copy__(), position)


class TestCell(unittest.TestCase):
    def test_index(self):
        test_cases = [
            (Position.Cell(0, 0), 0),
            (Position.Cell(0, 1), 8),
            (Position.Cell(3, 2), 19),
        ]

        Position.num_rows = 5
        Position.num_columns = 8

        for (cell, actual_output) in test_cases:
            self.assertEqual(int(cell), actual_output)

    def test_gt(self):
        test_cases = [
            (Position.Cell(0, 0), Position.Cell(0, 0), False),
            (Position.Cell(0, 1), Position.Cell(2, 0), True),
            (Position.Cell(3, 2), Position.Cell(4, 2), False),
        ]

        Position.num_rows = 3
        Position.num_columns = 5

        for (operand_1, operand_2, actual_output) in test_cases:
            self.assertEqual(operand_1 > operand_2, actual_output)

    def test_lt(self):
        test_cases = [
            (Position.Cell(0, 0), Position.Cell(0, 0), False),
            (Position.Cell(0, 1), Position.Cell(2, 0), False),
            (Position.Cell(3, 2), Position.Cell(4, 2), True),
        ]

        Position.num_rows = 4
        Position.num_columns = 5

        for (operand_1, operand_2, actual_output) in test_cases:
            self.assertEqual(operand_1 < operand_2, actual_output)

    def test_eq(self):
        test_cases = [
            (Position.Cell(0, 0), Position.Cell(0, 0), True),
            (Position.Cell(2, 4), Position.Cell(2, 3), False),
        ]

        for (operand_1, operand_2, actual_output) in test_cases:
            self.assertEqual(operand_1 == operand_2, actual_output)

    def test_str(self):
        test_cases = [
            (Position.Cell(0, 0), "(0, 0)"),
        ]

        for (cell, actual_output) in test_cases:
            self.assertEqual(str(cell), actual_output)


if __name__ == '__main__':
    unittest.main()
