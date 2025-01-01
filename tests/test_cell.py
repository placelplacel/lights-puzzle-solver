import unittest
from position import Cell


class TestCell(unittest.TestCase):
    def test_gt(self):
        test_cases = [
            (Cell(0, 0), Cell(0, 0), False),
            (Cell(0, 1), Cell(2, 0), True),
            (Cell(3, 2), Cell(4, 2), False),
        ]

        for (operand_1, operand_2, actual_output) in test_cases:
            self.assertEqual(operand_1 > operand_2, actual_output)

    def test_lt(self):
        test_cases = [
            (Cell(0, 0), Cell(0, 0), False),
            (Cell(0, 1), Cell(2, 0), False),
            (Cell(3, 2), Cell(4, 2), True),
        ]

        for (operand_1, operand_2, actual_output) in test_cases:
            self.assertEqual(operand_1 < operand_2, actual_output)

    def test_eq(self):
        test_cases = [
            (Cell(0, 0), Cell(0, 0), True),
            (Cell(2, 4), Cell(2, 3), False),
        ]

        for (operand_1, operand_2, actual_output) in test_cases:
            self.assertEqual(operand_1 == operand_2, actual_output)

    def test_str(self):
        test_cases = [
            (Cell(0, 0), "(0, 0)"),
        ]

        for (cell, actual_output) in test_cases:
            self.assertEqual(str(cell), actual_output)


if __name__ == '__main__':
    unittest.main()
