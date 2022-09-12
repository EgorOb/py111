import sys
sys.setrecursionlimit(15000)
def calculate_paths(shape: (int, int), point: (int, int)) -> int:
    """
    Given field with size rows*cols count available paths from (0, 0) to point

    :param shape: tuple of rows and cols (each from 1 to rows/cols)
    :param point: desired point for horse
    :return: count of paths from (1, 1) to (point[0], point[1]) (numerating from 0, so (0, 0) - left bottom tile)
    """
    print(shape, point)

    table = [[0 for i in range(shape[1])] for i in range(shape[0])]
    table[1][1] = 1
    not_avaible = [[0 for i in range(shape[1])] for i in range(shape[0])]
    not_avaible[1][1] = 1

    def path_rec(i: int, j: int) -> int:

        if i < 0 or i > shape[0] - 1:
            return 0
        if j < 0 or j > shape[1] - 1:
            return 0
        if not_avaible[i][j]:
            return table[i][j]
        print((i + 1, j - 2), (i - 1, j - 2), (i - 2, j - 1), (i - 2, j + 1))
        table[i][j] += path_rec(i + 1, j - 2) + path_rec(i - 1, j - 2) + path_rec(i - 2, j - 1) + path_rec(i - 2, j + 1)
        not_avaible[i][j] = 1
            # path_rec(i - 1, j + 2) + path_rec(i + 1, j + 2) + path_rec(i + 2, j + 1) + path_rec(i + 2, j - 1)
        return table[i][j]

    return path_rec(point[0], point[1])


def calculate_paths1(shape: (int, int), point: (int, int)) -> int:
    """
    Given field with size rows*cols count available paths from (0, 0) to point

    :param shape: tuple of rows and cols (each from 1 to rows/cols)
    :param point: desired point for horse
    :return: count of paths from (1, 1) to (point[0], point[1]) (numerating from 0, so (0, 0) - left bottom tile)
    """
    print(shape, point)

    table = [[0 for i in range(shape[1])] for i in range(shape[0])]
    table[1][1] = 1
    not_avaible = [[0 for i in range(shape[1])] for i in range(shape[0])]
    not_avaible[1][1] = 1
    way = []
    ind = 0

    def path_rec(i: int, j: int) -> int:
        if way and (i, j) in way:
            return 0
        way.append((i, j))
        # ind += 1
        if i < 0 or i > shape[0] - 1:
            if way:
                # ind -= 1
                way.pop()
            return 0
        if j < 0 or j > shape[1] - 1:
            if way:
                # ind -= 1
                way.pop()
            return 0
        if not_avaible[i][j]:
            if way:
                # ind -= 1
                way.pop()
            return table[i][j]
        # print((i + 1, j - 2), (i - 1, j - 2), (i - 2, j - 1), (i - 2, j + 1))
        table[i][j] += path_rec(i + 1, j - 2) + path_rec(i - 1, j - 2) + path_rec(i - 2, j - 1) + path_rec(i - 2, j + 1) \
                       + path_rec(i - 1, j + 2) + path_rec(i + 1, j + 2) + path_rec(i + 2, j + 1) + path_rec(i + 2, j - 1)
        not_avaible[i][j] = 1
            # path_rec(i - 1, j + 2) + path_rec(i + 1, j + 2) + path_rec(i + 2, j + 1) + path_rec(i + 2, j - 1)
        way.pop()
        return table[i][j]

    return path_rec(point[0], point[1])


if __name__ == "__main__":
    print(calculate_paths1((8, 8), (7, 7)))
