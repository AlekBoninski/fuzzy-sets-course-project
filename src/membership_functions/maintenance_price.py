"""
Membership functions for the maintenance price attribute domain, which consists of
{vhigh, high, med, low}. Defines membership functions for each value in the domain.
Maintenance price values are measured by currency ($) required per month to keep a vehicle
operational.
"""
from .utils import right_l_function, left_l_function, trapezoid


def f_low(price):
    """
    Membership function for the low price set. Left-open L-function.

    :param price: Value of the price
    :return: Membership degree of price to the low price set
    """
    core = 50
    base = 100

    return left_l_function(price, base, core)


def f_med(price):
    """
    Membership function for the medium price set. Trapezoid function.

    :param price: Value of the price
    :return: Membership degree of price to the low price set
    """
    base = (50, 250)
    core = (75, 150)

    return trapezoid(price, core, base)


def f_high(price):
    """
    Membership function for the medium price set. Trapezoid function.

    :param price: Value of the price
    :return: Membership degree of price to the low price set
    """
    base = (150, 500)
    core = (250, 300)

    return trapezoid(price, core, base)


def f_vhigh(price):
    """
    Membership function for the low price set. Right-open L-function.

    :param price: Value of the price
    :return: Membership degree of price to the low price set
    """
    core = 500
    base = 300

    return right_l_function(price, base, core)
