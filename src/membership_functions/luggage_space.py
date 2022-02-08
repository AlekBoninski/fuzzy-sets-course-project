"""
Membership functions for the luggage space attribute domain, which consists of
{small, med, big}. Defines membership functions for each value in the domain.
Luggage space values are measured in litres capacity of a car's boot with seats folded up.
"""
from .utils import right_l_function, left_l_function, triangle


def f_small(lug_space):
    """
    Membership function for the small luggage space set. Left-open L-function.

    :param lug_space: Luggage space in liters
    :return: Membership degree to the small luggage space set.
    """
    core = 350
    base = 400

    return left_l_function(lug_space, base, core)


def f_med(lug_space):
    """
    Membership function for the med luggage space set. Triangle function.

    :param lug_space: Luggage space in liters
    :return: Membership degree to the med luggage space set.
    """
    shape = (350, 400, 500)

    return triangle(lug_space, shape)


def f_big(lug_space):
    """
    Membership function for the big luggage space set. Right-open L-function.

    :param lug_space: Luggage space in liters
    :return: Membership degree to the big luggage space set.
    """
    core = 500
    base = 400

    return right_l_function(lug_space, base, core)
