import sys
sys.setrecursionlimit(15000)
import matplotlib.pyplot as plt
import matplotlib.colors as clrs
import numpy as np
# import seaborn as sns


def calculate_paths(shape: (int, int), point: (int, int), start_point=(1, 1)) -> int:
    """
    Given field with size rows*cols count available paths from (0, 0) to point

    :param shape: tuple of rows and cols (each from 1 to rows/cols)
    :param point: desired point for horse
    :param start_point:
    :return: count of paths from (1, 1) to (point[0], point[1]) (numerating from 0, so (0, 0) - left bottom tile)
    """
    """
    (i + 1, j - 2)
    (i - 1, j - 2)
    (i - 2, j - 1)
    (i - 2, j + 1)
    """

    print(shape, point)
    table = [[0 for i in range(shape[1])] for i in range(shape[0])]
    table[start_point[0]][start_point[1]] = 1
    not_avaible = [[0 for i in range(shape[1])] for i in range(shape[0])]
    not_avaible[start_point[0]][start_point[1]] = 1
    d = DrawDesk(shape)

    def path_rec(i: int, j: int) -> int:

        if 0 <= i <= shape[0] - 1 and 0 <= j <= shape[1] - 1:
            if not_avaible[i][j]:
                return table[i][j]
            # print((i + 1, j - 2), (i - 1, j - 2), (i - 2, j - 1), (i - 2, j + 1))
            d.set_pos_horse(i, j)
            d.set_possible_move(get_matr_step4)
            d.show_desk()
            table[i][j] = sum((path_rec(i + 1, j - 2),
                               path_rec(i - 1, j - 2),
                               path_rec(i - 2, j - 1),
                               path_rec(i - 2, j + 1),
                               ))
            not_avaible[i][j] = 1
            return table[i][j]

        return 0

    return path_rec(*point)


def calculate_paths_all_way(shape: (int, int), point: (int, int), start_point=(1, 1)) -> int:
    """
    Given field with size rows*cols count available paths from (0, 0) to point

    :param shape: tuple of rows and cols (each from 1 to rows/cols)
    :param point: desired point for horse
    :return: count of paths from (1, 1) to (point[0], point[1]) (numerating from 0, so (0, 0) - left bottom tile)
    """
    """
        (i + 1, j - 2)
        (i - 1, j - 2)
        (i - 2, j - 1)
        (i - 2, j + 1)
        (i - 1, j + 2)
        (i + 1, j + 2)
        (i + 2, j + 1)
        (i + 2, j - 1)
        """

    print(shape, point)
    table = [[0 for i in range(shape[1])] for i in range(shape[0])]
    table[start_point[0]][start_point[1]] = 1
    not_avaible = [[0 for i in range(shape[1])] for i in range(shape[0])]
    not_avaible[start_point[0]][start_point[1]] = 1
    way = []

    def path_rec(i: int, j: int) -> int:
        if way and (i, j) in way:
            return 0
        way.append((i, j))

        if 0 <= i <= shape[0] - 1 and 0 <= j <= shape[1] - 1:
            if not_avaible[i][j]:
                way.pop()
                return table[i][j]

            table[i][j] = sum((path_rec(i + 1, j - 2),
                               path_rec(i - 1, j - 2),
                               path_rec(i - 2, j - 1),
                               path_rec(i - 2, j + 1),
                               path_rec(i - 1, j + 2),
                               path_rec(i + 1, j + 2),
                               path_rec(i + 2, j + 1),
                               path_rec(i + 2, j - 1),
                               ))
            not_avaible[i][j] = 1
            way.pop()
            return table[i][j]

        way.pop()
        return 0

    return path_rec(*point)


class DrawDesk:

    def __init__(self, shape: tuple):
        self.data = np.zeros(shape)
        # self.null_desk = self.data.copy()
        self.current_pos_horse = (0, 0)
        self.shape = shape
        self.x_data = np.ones(shape) * np.arange(0.5, shape[1] + 0.5, 1)
        self.y_data = np.transpose(self.x_data)
        self.cmap = clrs.LinearSegmentedColormap.from_list("", ["gray", "black", "blue", "yellow"])
        self.gca = None

    def set_pos_horse(self, i, j):
        self.clear_desk()
        self.data[i, j] = 1
        self.current_pos_horse = (i, j)

    def set_possible_move(self, func):
        ind = np.transpose(func(self.current_pos_horse[0],
                                self.current_pos_horse[1],
                                self.shape))
        if len(ind):
            self.data[ind[0], ind[1]] = 2

    def set_pos_current_step(self, i, j):
        self.data[i, j] = 3

    def clear_desk(self):
        self.data = np.zeros(self.shape)

    def show_desk(self):
        if self.gca is not None:
            self.clear_fig()
        self.fig = plt.imshow(self.data, cmap=self.cmap)
        self.gca = plt.gca()
        # plt.colorbar()
        self.gca.set_xticks(np.arange(0.5, 7.5, 1))
        self.gca.set_yticks(np.arange(0.5, 7.5, 1))
        # plt.xticks(range(0.5, self.shape[1], 1), list(range(self.shape[1])))
        # plt.yticks(range(0.5, self.shape[0], 1), list(range(self.shape[0])))
        # plt.axis(False)
        plt.xticks(color='w')
        plt.yticks(color='w')
        plt.grid()
        plt.show()

    def clear_fig(self):
        self.gca.clear()


def get_matr_step4(i_base, j_base, shape) -> list:

    data_border = ((i_base + 1, j_base - 2),
                   (i_base - 1, j_base - 2),
                   (i_base - 2, j_base - 1),
                   (i_base - 2, j_base + 1),
                   )
    data_step = []
    for border in data_border:
        if 0 <= border[0] <= shape[0] - 1 and 0 <= border[1] <= shape[1] - 1:
            data_step.append(border)

    return data_step


def get_matr_step8(i_base, j_base, shape) -> list:

    data_border = ((i_base + 1, j_base - 2),
                   (i_base - 1, j_base - 2),
                   (i_base - 2, j_base - 1),
                   (i_base - 2, j_base + 1),
                   (i_base - 1, j_base + 2),
                   (i_base + 1, j_base + 2),
                   (i_base + 2, j_base + 1),
                   (i_base + 2, j_base - 1),
                   )
    data_step = []
    for border in data_border:
        if 0 <= border[0] <= shape[0] - 1 and 0 <= border[1] <= shape[1] - 1:
            data_step.append(border)

    return data_step


if __name__ == "__main__":
    print(calculate_paths((8, 8), (7, 7)))
    # print(calculate_paths((7, 15), (6, 14), (0, 0)))
    # print(calculate_paths((17, 12), (16, 9), (1, 1)))
    # print(calculate_paths_all_way((4, 4), (3, 3)))
    # print(calculate_paths_all_way((7, 15), (6, 14), (1, 1)))
    # print(calculate_paths_all_way((17, 12), (16, 9), (1, 1)))
    d = DrawDesk((8, 8))
    d.set_pos_horse(2, 2)
    d.set_possible_move(get_matr_step8)
    # d.set_pos_current_step(1, 0)
    d.show_desk()

    d.clear_fig()
    print(6)
