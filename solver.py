from position import Cell, Position


class Solver:
    # Position, Position, Cell, tuple(Cell), Natural+{0}, Natural+{0} -> tuple(Cell)
    # Produces a tuple containing the moves that must be made to get from the first position
    # that is fed into it to the second.
    #   -- TEMPLATE
    # def solve(start_position, end_position, past_move, past_moves, current_depth, max_depth):
    #     assert isinstance(start_position, Position), "'start_position' is not a Position."
    #     assert isinstance(end_position, Position), "'end_position' is not a Position."
    #     assert isinstance(past_move, Cell), "'past_move' is not a Cell."
    #     assert isinstance(past_moves, tuple), "'past_moves' is not a tuple."
    #     assert isinstance(current_depth, int) and current_depth >= 0, "'current_depth' is not a non-negative integer."
    #     assert isinstance(max_depth, int) and max_depth >= 0, "'max_depth' is not a non-negative integer."
    #     pass
    @staticmethod
    def solve(start_position, end_position, past_move, past_moves=(), current_depth=0, max_depth=36):
        assert isinstance(start_position, Position), "'start_position' is not a Position."
        assert isinstance(end_position, Position), "'end_position' is not a Position."
        assert isinstance(past_move, Cell), "'past_move' is not a Cell."
        assert isinstance(past_moves, tuple), "'past_moves' is not a tuple."
        assert isinstance(current_depth, int) and current_depth >= 0, "'current_depth' is not a non-negative integer."
        assert isinstance(max_depth, int) and max_depth >= 0, "'max_depth' is not a non-negative integer."

        if (not start_position.num_columns == end_position.num_columns
                or not start_position.num_rows == end_position.num_rows) or current_depth >= max_depth:
            return ()

        if start_position == end_position:
            return past_moves

        move_x = past_move.x
        move_y = past_move.y
        for i in range(start_position.index_of(past_move), start_position.num_rows * start_position.num_columns):
            move = Cell(move_x, move_y)
            result = Solver.solve(start_position.make_move(move), end_position, move, past_moves + (move,),
                                  current_depth + 1, max_depth)
            if len(result) > 0:
                return result

            move_x = (move_x + 1) % start_position.num_columns
            if move_x == 0:
                move_y += 1

        return ()
