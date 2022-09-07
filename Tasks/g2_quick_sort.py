from typing import List


def sort(container: List[int]) -> List[int]:
    """
    Sort input container with quick sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """
    def quick_sort(container, left, right):
        if left < right:
            # This is the index after the pivot, where our lists are split
            split_index = partition(container, left, right)
            quick_sort(container, left, split_index)
            quick_sort(container, split_index + 1, right)

    quick_sort(container, 0, len(container) - 1)
    return container


def partition(container, left, right):
    val_pivot = container[(left + right) // 2]
    i = left - 1
    j = right + 1
    while True:
        i += 1
        while container[i] < val_pivot:
            i += 1

        j -= 1
        while container[j] > val_pivot:
            j -= 1

        if i >= j:
            return j

        # Если элемент с индексом i (слева от опорного) больше, чем
        # элемент с индексом j (справа от опорного), меняем их местами
        container[i], container[j] = container[j], container[i]


if __name__ == "__main__":
    data = list(range(10, -1, -1))
    print(sort(data))
