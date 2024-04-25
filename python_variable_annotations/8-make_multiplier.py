#!/usr/bin/env python3
""" Returns a fonction that multiplies a float by multiplier """

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Returns a function that multiplies a float by multiplier
    Args:
        multiplier (float): multiplier to multiply by
    Returns:
        Callable[[float], float]: funct that multiplies a float by multiplier
    """
    def multiply_func(number: float) -> float:
        """ Multiplies a float by multiplier
        Args:
            number (float): number to multiply
        """
        return number * multiplier

    return multiply_func
