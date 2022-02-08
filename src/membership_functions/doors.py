"""
Membership functions for the doors attribute domain, which consists of {2, 3, 4, 5-more}.
The membership functions fuzzify the discrete domain so it can be used for calculating relations
and compositions.
"""
from .utils import triangle, right_l_function


def f_two(doors):
    """
    Membership functions for the 2 doors set. Triangle function

    :param doors: Number of doors
    :return: Membership degree to the 2 doors set
    """
    shape = (1, 2, 3)

    return triangle(doors, shape)


def f_three(doors):
    """
    Membership functions for the 3 doors set. Triangle function

    :param doors: Number of doors
    :return: Membership degree to the 3 doors set
    """
    shape = (2, 3, 4)

    return triangle(doors, shape)


def f_four(doors):
    """
    Membership functions for the 4 doors set. Triangle function

    :param doors: Number of doors
    :return: Membership degree to the 4 doors set
    """
    shape = (3, 4, 5)

    return triangle(doors, shape)


def f_five_more(doors):
    """
    Membership functions for the 5-more doors set. Right-open L-function.

    :param doors: Number of doors
    :return: Membership degree to the 2 doors set
    """
    core = 5
    base = 4

    return right_l_function(doors, base, core)
