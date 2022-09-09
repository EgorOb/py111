from typing import Union, Sequence


def stairway_path(stairway: Sequence[Union[float, int]]) -> Union[float, int]:
    """
    Calculate min cost of getting to the top of stairway if agent can go on next or through one step.

    :param stairway: list of ints, where each int is a cost of appropriate step
    :return: minimal cost of getting to the top
    """
    print(stairway)
    # cost = stairway.copy()
    for i in range(2, len(stairway)):
        stairway[i] += min(stairway[i - 1], stairway[i - 2])
    return stairway[-1]


fib = [1] * 10


def get_fib(i):
    if (i <= 2):  # Начальные значения
        return 1
    if (fib[i] != -1):  # Ленивость
        return fib[i]
    fib[i] = get_fib(i - 1) + get_fib(i - 2)  # Пересчёт
    return fib[i]

if __name__ == '__main__':
    # print(get_fib(6))
    test_st = [1, 3, 1, 5, 2, 7, 7, 8, 9, 4, 6, 3]
    print(stairway_path(test_st))

