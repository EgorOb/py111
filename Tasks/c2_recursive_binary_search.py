from typing import Sequence, Optional


def binary_search(elem: int, arr: Sequence) -> Optional[int]:
    """
    Performs binary search of given element inside of array (using recursive way)

    :param elem: element to be found
    :param arr: array where element is to be found
    :return: Index of element if it's presented in the arr, None otherwise
    """
    print(elem, arr)
    left = 0
    right = len(arr) - 1

    return recursive(left, right, elem, arr)


def recursive(left: int, right: int, elem: int, arr: Sequence) -> Optional[int]:

    if arr[left] == elem:
        return left

    if left == right:
        return

    mid = (left + right) // 2
    if arr[mid] == elem:
        return mid
    elif arr[mid] < elem:
        left = min(mid + 1, len(arr))
    else:
        right = max(mid - 1, 0)

    return recursive(left, right, elem, arr)


if __name__ == '__main__':
    a = list(range(100))
    print(binary_search(-1, a))
