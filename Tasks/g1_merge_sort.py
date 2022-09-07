from typing import List


def sort(container: List[int]) -> List[int]:
    """
    Sort input container with merge sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """
    if len(container) == 1:
        return

    mid = len(container) // 2
    left = container[:mid]
    right = container[mid:]
    sort(left)
    sort(right)

    return merge(container, left, right)


def merge(container: List[int], left: List[int], right: List[int]) -> List[int]:

    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            container[k] = left[i]
            i += 1
        else:
            container[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        container[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        container[k] = right[j]
        j += 1
        k += 1

    return container


if __name__ == "__main__":
    data = list(range(10, -1, -1))
    print(sort(data))
