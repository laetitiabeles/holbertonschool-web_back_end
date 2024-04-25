#!/usr/bin/env python3
""" Returns a list of typles """

from typing import List
from typing import Iterable
from typing import Tuple
from typing import Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Returns a list of tuples
    Args:
       lst (List[str]): inputt iterable of sequences
    Returns:
       List[Tuple[str, int]]: list of tuples where each tuple
           contains a sequence from the input iterable
           and its corresponding length
    """
    return [(i, len(i)) for i in lst]
