#!/usr/bin/env python3
""" Returns the sum of a mixed list as a float """

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ Returns the sum of a mixed list as a float
    Args:
        mxd_lst (List[Union[int, float]]): list of int and floats
    """
    return sum(mxd_lst)
