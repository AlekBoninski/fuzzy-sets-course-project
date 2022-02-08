"""
Membership functions for the safety attribute domain, which consists of
{low, med, high}. Defines membership functions for each value in the domain.
Safety values are measured by Euro NCAP results of a vehicle which ranges from 0 to 5 stars.
"""
from .utils import right_l_function, left_l_function, triangle


def f_low(safety_rating):
    """
    Membership function for the low safety set. Left-open L-function.

    :param safety_rating: Euro NCAP rating
    :return: Membership degree to the low safety set.
    """
    core = 2
    base = 3

    return left_l_function(safety_rating, base, core)


def f_med(safety_rating):
    """
    Membership function for the med safety set. Triangle function.

    :param safety_rating: Euro NCAP rating
    :return: Membership degree to the med safety set.
    """
    shape = (2, 3, 4)

    return triangle(safety_rating, shape)


def f_high(safety_rating):
    """
    Membership function for the high safety set. Right-open L-function.

    :param safety_rating: Euro NCAP rating
    :return: Membership degree to the high safety set.
    """
    core = 4
    base = 3

    return right_l_function(safety_rating, base, core)
