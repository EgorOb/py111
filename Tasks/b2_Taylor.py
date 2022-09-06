"""
Taylor series
"""
from typing import Union
import math as m

COUNT_SEQ = 20


def ex(x: Union[int, float]) -> float:
    """
    Calculate value of e^x with Taylor series

    :param x: x value
    :return: e^x value
    """
    print(x)

    gen = range(1, COUNT_SEQ)
    val = 1

    for idx in gen:
        val += x ** idx / m.factorial(idx)

    return val


def ex_mod(x: Union[int, float]) -> float:
    """
    Calculate value of e^x with Taylor series

    :param x: x value
    :return: e^x value
    """
    print(x)

    gen = range(1, COUNT_SEQ)
    val = 1
    fact = 1
    pow_ = 1

    for idx in gen:
        fact *= idx
        pow_ *= x
        val += pow_ / fact

    return val


def sinx(x: Union[int, float]) -> float:
    """
    Calculate sin(x) with Taylor series

    :param x: x value
    :return: sin(x) value
    """
    print(x)

    gen = range(1, COUNT_SEQ)
    val = x

    for idx in gen:
        sign = (-1) ** idx
        val += sign * x ** (2 * idx + 1) / m.factorial(2 * idx + 1)

    return val


def sinx_mod(x: Union[int, float]) -> float:
    """
    Calculate sin(x) with Taylor series

    :param x: x value
    :return: sin(x) value
    """
    print(x)

    gen = range(1, COUNT_SEQ)
    val = x
    fact = 6
    pow_ = x**3
    sign = -1

    for idx in gen:
        val += sign * pow_ / fact
        sign *= -1
        pow_ *= x**2
        fact *= 4 * idx**2 + 10 * idx + 6  # (2 * idx + 2)*(2 * idx + 3)

    return val


if __name__ == '__main__':
    import math as m

    val1 = ex(-3)
    val1_mod = ex_mod(-3)
    val2 = m.exp(-3)
    print(val1, val2, round(val1, 7) == round(val2, 7))
    print(val1, val1_mod, round(val1, 7) == round(val1_mod, 7))

    val3 = sinx(0.5)
    val3_mod = sinx_mod(0.5)
    val4 = m.sin(0.5)
    print(val3, val4, round(val3, 7) == round(val4, 7))
    print(val3, val3_mod, round(val3, 7) == round(val3_mod, 7))
