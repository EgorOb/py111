from typing import Union, Sequence


def stairway_path(stairway: Sequence[Union[float, int]]) -> Union[float, int]:
    """
    Calculate min cost of getting to the top of stairway if agent can go on next or through one step.

    :param stairway: list of ints, where each int is a cost of appropriate step
    :return: minimal cost of getting to the top
    """
    print(stairway)
    cost = stairway.copy()
    for i in range(2, len(stairway)):
        cost[i] += min(cost[i - 1], cost[i - 2])
    return cost[-1]


def stairway_path_r(stairway: Sequence[Union[float, int]]) -> Union[float, int]:
    """
    Calculate min cost of getting to the top of stairway if agent can go on next or through one step.

    :param stairway: list of ints, where each int is a cost of appropriate step
    :return: minimal cost of getting to the top
    """
    print(stairway)
    cost = [''] * len(stairway)
    cost[0] = stairway[0]
    cost[1] = stairway[1]

    def rec(n: int) -> Union[float, int]:
        if cost[n] != '':
            return cost[n]
        if n < 2:
            return cost[n]
        cost[n] = min(rec(n - 1) + stairway[n], rec(n - 2) + stairway[n])
        return cost[n]

    return rec(len(stairway)-1)


if __name__ == '__main__':
    # print(get_fib(6))
    test_st = [1, 3, 1, 5, 2, 7, 7, 8, 9, 4, 6, 3]
    print(stairway_path(test_st))
    print(stairway_path_r(test_st))
    test_st = [1, 3, 5, 1, 7, 7, 2, 8, 9, 4, 6, 3]
    print(stairway_path(test_st))
    print(stairway_path_r(test_st))


