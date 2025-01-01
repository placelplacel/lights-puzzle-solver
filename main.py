from solver import Solver, Position


def main():
    Position.num_rows = 5
    Position.num_columns = 7

    solution = Solver.solve(Position("0000000/"
                                     "0010100/"
                                     "0010100/"
                                     "1100010/"
                                     "0100001"),
                            Position("0000000/"
                                     "0000000/"
                                     "0000000/"
                                     "0000000/"
                                     "0000000"),
                            Position.Cell(0, 0))

    for move in solution:
        print(move)


if __name__ == "__main__":
    main()
