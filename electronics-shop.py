"""
Here we solve task from here https://www.hackerrank.com/challenges/electronics-shop
"""

import collections
import math

def count_max_purch(budget, arr1, arr2):
    """ given budget and 2 arrays of prices, returns max sum of 1 item from 1st arr and 1 item from 2nd arr, that is <= budget

    >>> count_max_purch(11, [2, 3, 5], [6, 1, 3])
    11
    >>> count_max_purch(8, [2, 3], [6, 1, 3])
    6
    """

    return [x + y for x in reversed(sorted(arr1))
                  for y in reversed(sorted(arr2)) if x + y <= budget][0]

if __name__ == "__main__":
    import doctest
    doctest.testmod()

