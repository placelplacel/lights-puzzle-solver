from enum import Enum
from position import Position

UNDEFINED_MOVE = -1, -1


class SearchResult(Enum):
    PENDING_DEPTH_LIMITED = -2,
    PENDING = -1,
    BAD = 0,
    GOOD = 1,


# PositionSearchData is [SearchResult, Integer, Integer, (Integer, Integer)]
# interp. data about the position relevant during the search.
# data_example_1 = SearchResult.GOOD, 10, 0, (-1, -1)
# data_example_2 = SearchResult.BAD, 5, 8, (0, 3)
# -- TEMPLATE
# def fn_for_position_search_data(self, data):
#     assert isinstance(data, list), "'data' is not a list."
#     pass


# Position, Position, Dict<str>, Integer -> PositionData
# Produces the PositionData for the first position that is fed into it, which is relevant
# to the search for the best moves to get to the second position.

# -- TEMPLATE
# def search(position, end_position, known_positions, current_depth):
#     assert isinstance(position, Position), "'position' is not a Position."
#     assert isinstance(end_position, Position), "'end_position' is not a Position."
#     assert isinstance(known_positions, dict), "'known_positions' is not a dict."
#     pass

def search(position, end_position, known_positions, current_depth, max_depth):
    assert isinstance(position, Position), "'position' is not a Position."
    assert isinstance(end_position, Position), "'end_position' is not a Position."
    assert isinstance(known_positions, dict), "'known_positions' is not a dict."
    assert isinstance(current_depth, int) and current_depth >= 0, "'current_depth' is not a non-negative integer."
    assert isinstance(max_depth, int) and max_depth >= 0, "'max_depth' is not a non-negative integer."

    # FIXME: The program shits itself if it reaches a "critical" position in solving a problem
    #        on or near the recursion depth limit. Because it automatically gets classified as
    #        bad, it discards the move as worthless even if it is the only move that solves the
    #        problem.
    if current_depth >= max_depth:
        return [SearchResult.BAD, current_depth, float("NaN"), UNDEFINED_MOVE]

    def update_branch_depth(position, depth):
        assert isinstance(position, Position), "'position' is not a Position."
        assert isinstance(depth, int) and depth >= 0, "'depth' is not a non-negative integer."

        # Assumes that position is a part of a known branch.
        known_search_data = known_positions[str(position)]
        known_search_data[1] = depth
        if known_search_data[2] != UNDEFINED_MOVE:
            (row, column) = known_search_data[2]
            update_branch_depth(position.make_move(row, column), depth + 1)

    if position == end_position:
        return [SearchResult.GOOD, current_depth, 0, UNDEFINED_MOVE]

    try:
        known_search_data = known_positions[str(position)]

        if known_search_data[0] == SearchResult.BAD or known_search_data[0] == SearchResult.PENDING:
            return [SearchResult.BAD, current_depth, float("NaN"), UNDEFINED_MOVE]
        else:
            if current_depth < known_search_data[1]:
                update_branch_depth(position, current_depth)
                return known_search_data
            else:
                return [SearchResult.BAD, current_depth, float("NaN"), UNDEFINED_MOVE]
    except KeyError:
        best_move = UNDEFINED_MOVE
        best_search_data = [SearchResult.BAD, float("INF"), float("NaN"), UNDEFINED_MOVE]
        (rows, columns) = position.size
        for r in range(rows):
            for c in range(columns):
                known_positions[str(position)] = [SearchResult.PENDING, current_depth, float("NaN"), UNDEFINED_MOVE]
                search_data = search(position.make_move(r, c),
                                     end_position,
                                     known_positions,
                                     current_depth + 1,
                                     max_depth)
                known_positions[str(position)] = search_data
                if search_data[0] == SearchResult.GOOD:
                    if search_data[1] < best_search_data[1]:
                        best_move = (r, c)
                        best_search_data = search_data
        result = [best_search_data[0], current_depth, best_search_data[2] + 1, best_move]
        known_positions[str(position)] = result
        return result


def main():
    start_pos = Position("0000000/"
                         "0000100/"
                         "0001110/"
                         "0000100/"
                         "0000000/")
    end_pos = Position("0000000/"
                       "0000000/"
                       "0000000/"
                       "0000000/"
                       "0000000/")

    known_positions = {
        str(end_pos): [SearchResult.GOOD, float("INF"), 0, UNDEFINED_MOVE]
    }
    search_data = search(start_pos, end_pos, known_positions, 0, 4)

    next_move = search_data[3]
    while start_pos != end_pos:
        start_pos.print()
        print()
        start_pos = start_pos.make_move(next_move[0], next_move[1])
        next_move = known_positions[str(start_pos)][3]

    start_pos.print()
    print()


if __name__ == "__main__":
    main()
