def factorial_recursive(n: int) -> int:
    """
    Calculate factorial of number n (> 0) in recursive way
    :param n: int > 0
    :return: factorial of n
    """
    print(n)
    if n < 0:
        raise ValueError
    if n == 0:
        return 1
    return factorial_recursive(n - 1) * n


def factorial_iterative(n: int) -> int:
    """
    Calculate factorial of number n (> 0) in iterative way

    :param n: int > 0
    :return: factorial of n
    """
    print(n)
    if n < 0:
        raise ValueError
    fact = 1
    for i in range(2, n + 1):
        fact *= i

    return fact


if __name__ == '__main__':
    print(factorial_recursive(5))
    print(factorial_iterative(5))
    print(factorial_recursive(-5))
    print(factorial_iterative(-5))

