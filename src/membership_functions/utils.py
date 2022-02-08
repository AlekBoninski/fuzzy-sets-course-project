"""
Utilities containing base membership functions which can be reused.
"""


def trapezoid(x, core, base):
    core_left, core_right = core
    base_left, base_right = base

    if x < base_left or x > base_right:
        return 0
    if base_left <= x < core_left:
        return (x - base_left) / (core_left - base_left)
    if core_left <= x < core_right:
        return 1
    if core_right <= x <= base_right:
        return (base_right - x) / (base_right - core_right)
    
    pass


def triangle(x, shape):
    base_left, tip, base_right = shape

    if x < base_left or x > base_right:
        return 0
    if base_left <= x < tip:
        return (x - base_left) / (tip - base_left)
    if tip <= x <= base_right:
        return (base_right - x) / (base_right - tip)


def left_l_function(x, base, core):
    if x < core:
        return 1
    if core <= x <= base:
        return (base - x) / (base - core)
    if x > base:
        return 0


def right_l_function(x, base, core):
    if x < base:
        return 0
    if base <= x <= core:
        return (x - base) / (core - base)
    if x > core:
        return 1
