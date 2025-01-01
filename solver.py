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

class SearchData:
    # SearchResult, Integer, Integer, (Integer, Integer) -> SearchData
    # Returns a SearchData object that acts as a wrapper around the position data
    # relevant to the search.

    # -- TEMPLATE
    # def __init__(self, result, depth, steps_till_end, best_move):
    #     assert isinstance(result, SearchResult), "'result' is not a SearchResult."
    #     assert isinstance(depth, int) and depth >= 0, "'depth' is not a non-negative integer."
    #     assert isinstance(steps_till_end, int) and steps_till_end >= 0, \
    #         "'steps_till_end' is not a non-negative integer."
    #     assert isinstance(best_move, tuple), "'best_move' is not a tuple."
    #     pass

    def __init__(self, result, depth, steps_till_end, best_move):
        assert isinstance(result, SearchResult), "'result' is not a SearchResult."
        assert isinstance(depth, int) and depth >= 0 or float("INF"), "'depth' is not a non-negative integer."
        assert isinstance(steps_till_end, int) and steps_till_end >= 0 or float("INF"), \
            "'steps_till_end' is not a non-negative integer."
        assert isinstance(best_move, tuple), "'best_move' is not a tuple."

        self.result = result
        self.depth = depth
        self.steps_till_end = steps_till_end
        self.best_move = best_move

    # None -> str
    # Returns a str representing the search data in a printable format.

    # -- TEMPLATE
    # def __str__(self):
    #     pass

    def __str__(self):
        return "{result: %s, depth: %f, steps_till_end: %f, best_move: %s}" % (self.result,
                                                                               self.depth,
                                                                               self.steps_till_end,
                                                                               self.best_move)


# Position, Position, Dict<str>, Integer -> SearchData
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
        return SearchData(SearchResult.PENDING_DEPTH_LIMITED, current_depth, float("INF"), UNDEFINED_MOVE)

    def update_branch_depth(position, depth):
        assert isinstance(position, Position), "'position' is not a Position."
        assert isinstance(depth, int) and depth >= 0, "'depth' is not a non-negative integer."

        # Assumes that position is a part of a known branch.
        known_search_data = known_positions[str(position)]
        known_search_data.depth = depth
        if known_search_data.best_move != UNDEFINED_MOVE:
            (row, column) = known_search_data.best_move
            update_branch_depth(position.make_move(row, column), depth + 1)

    try:
        known_search_data = known_positions[str(position)]

        if known_search_data.result == SearchResult.BAD or known_search_data.result == SearchResult.PENDING:
            return SearchData(SearchResult.BAD, current_depth, float("INF"), UNDEFINED_MOVE)
        elif known_search_data.result == SearchResult.PENDING_DEPTH_LIMITED:
            # Start another search from this position
            raise KeyError()
        else:
            if current_depth < known_search_data.depth:
                update_branch_depth(position, current_depth)
                return known_search_data
            else:
                return SearchData(SearchResult.BAD, current_depth, float("INF"), UNDEFINED_MOVE)
    except KeyError:
        best_move = UNDEFINED_MOVE
        best_search_data = SearchData(SearchResult.BAD, float("INF"), float("INF"), UNDEFINED_MOVE)
        (rows, columns) = position.size
        known_positions[str(position)] = SearchData(SearchResult.PENDING, current_depth, float("INF"),
                                                    UNDEFINED_MOVE)
        for r in range(rows):
            for c in range(columns):
                search_data = search(position.make_move(r, c), end_position, known_positions, current_depth + 1,
                                     max_depth)
                if search_data.result == SearchResult.GOOD:
                    if search_data.steps_till_end < best_search_data.steps_till_end:
                        best_move = (r, c)
                        best_search_data = search_data
                elif (search_data.result == SearchResult.PENDING_DEPTH_LIMITED
                        and not best_search_data.result == SearchResult.GOOD):
                    if search_data.depth < best_search_data.depth:
                        best_move = UNDEFINED_MOVE
                        best_search_data = search_data
        result = SearchData(best_search_data.result, current_depth, best_search_data.steps_till_end + 1, best_move)
        known_positions[str(position)] = result
        return result


def main():
    start_pos = Position("0100000/"
                         "1110000/"
                         "0101100/"
                         "0010010/"
                         "0001100/")
    end_pos = Position("0000000/"
                       "0000000/"
                       "0000000/"
                       "0000000/"
                       "0000000/")

    known_positions = {
        str(end_pos): SearchData(SearchResult.GOOD, float("INF"), 0, UNDEFINED_MOVE)
    }
    search_data = search(start_pos, end_pos, known_positions, 0, 4)

    if search_data.result == SearchResult.BAD:
        print("No sequence found.")
    elif search_data.result == SearchResult.PENDING_DEPTH_LIMITED:
        print("No sequence found in the given number of moves.")
    else:
        start_pos.print()

        next_move = search_data.best_move
        while next_move != UNDEFINED_MOVE:
            start_pos = start_pos.make_move(next_move[0], next_move[1])
            start_pos.print()

            next_move = known_positions[str(start_pos)].best_move


if __name__ == "__main__":
    main()
