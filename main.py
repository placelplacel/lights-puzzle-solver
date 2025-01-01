from solver import Solver, Cell, Position


def main():
    solution = Solver.solve(Position(5, 7,
                                     "0000000/"
                                     "0010100/"
                                     "0010100/"
                                     "1100010/"
                                     "0100001"),
                            Position(5, 7,
                                     "0000000/"
                                     "0000000/"
                                     "0000000/"
                                     "0000000/"
                                     "0000000"),
                            Cell(0, 0))

    for move in solution:
        print(move)


if __name__ == "__main__":
    main()
