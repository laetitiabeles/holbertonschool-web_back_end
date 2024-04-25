#!/usr/bin/env python3
""" Convert a string and int or float to a tuple """

from typing import Union
from typing import Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ Convert a string and int or float to a tuple
    Args:
        k (str): key of the tuple
        v (Union[int, float]): value of the tuple
    """
    return (k, v * v)
