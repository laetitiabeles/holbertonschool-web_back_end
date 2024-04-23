#!/usr/bin/env python3
""" Returns the sum of a list of floats as a float """

from typing import List


def sum_list(input_list: List[float]) -> float:
    """ Returns the sum of a list of floats as a float
    Args:
        input_list (List(float)): list of floats
    """
    return sum(input_list)
