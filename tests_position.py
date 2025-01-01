import unittest
from position import Position


class TestPosition(unittest.TestCase):
    def test_from_string(self):
        test_cases = [
            ("",        []),
            ("1/",       [[True]]),
            ("001/011/", [[False, False, True],
                          [False, True,  True]])
        ]

        for (test_input, expected_output) in test_cases:
            self.assertEqual(Position(test_input).light_states, expected_output)

    def test_eq(self):
        test_cases = [
            (Position(""),      Position(""),      True),
            (Position("1/"),    Position("1/"),    True),
            (Position("10/11/"), Position("10/01/"), False)
        ]

        for (operand_1, operand_2, expected_output) in test_cases:
            self.assertEqual(operand_1 == operand_2, expected_output)

    def test_make_move(self):
        test_cases = [
            (Position("1/"),     0, 0, Position("0/")),
            (Position("10/11/"), 0, 1, Position("01/10/")),
            (Position("101/111/"), 1, 2, Position("100/100/"))
        ]

        for (position, row, column, expected_output) in test_cases:
            self.assertEqual(position.make_move(row, column), expected_output)

    def test_str(self):
        test_cases = [
            "",
            "1/",
            "101/111/"
        ]

        for position_str in test_cases:
            self.assertEqual(str(Position(position_str)), position_str)


if __name__ == '__main__':
    unittest.main()
