"""
Membership functions for the persons attribute domain, which consists of {2, 4, more}.
The membership functions fuzzify the discrete domain so it can be used for calculating relations
and compositions.
"""
from .utils import triangle, right_l_function


def f_two(persons):
    """
    Membership functions for the 2 persons set. Triangle function.

    :param persons: Number of passengers that can be seated
    :return: Membership degree to the 2 persons set.
    """
    shape = (1, 2, 3)

    return triangle(persons, shape)


def f_four(persons):
    """
    Membership functions for the 4 persons set. Triangle function.

    :param persons: Number of passengers that can be seated
    :return: Membership degree to the 4 persons set.
    """
    shape = (3, 4, 5)

    return triangle(persons, shape)


def f_more(persons):
    """
    Membership functions for the more persons set. Right-open L-function.

    :param persons: Number of passengers that can be seated
    :return: Membership degree to the more persons set.
    """
    core = 5
    base = 4

    return right_l_function(persons, base, core)
