"""
Membership functions for the purchase price attribute domain, which consists of
{vhigh, high, med, low}. Defines membership functions for each value in the domain.
Purchase price values are measured by the currency ($) required to purchase a vehicle.
"""
from .utils import right_l_function, left_l_function, trapezoid


def f_low(price):
    """
    Membership function for the low price set. Left-open L-function.

    :param price: Value of the price
    :return: Membership degree of price to the low price set
    """
    core = 20_000
    base = 25_000

    return left_l_function(price, base, core)


def f_med(price):
    """
    Membership function for the medium price set. Trapezoid function.

    :param price: Value of the price
    :return: Membership degree of price to the low price set
    """
    base = (20_000, 60_000)
    core = (30_000, 40_000)

    return trapezoid(price, core, base)


def f_high(price):
    """
    Membership function for the medium price set. Trapezoid function.

    :param price: Value of the price
    :return: Membership degree of price to the low price set
    """
    base = (40_000, 150_000)
    core = (60_000, 100_000)

    return trapezoid(price, core, base)


def f_vhigh(price):
    """
    Membership function for the low price set. Right-open L-function.

    :param price: Value of the price
    :return: Membership degree of price to the low price set
    """
    core = 150_000
    base = 100_000

    return right_l_function(price, base, core)
