"""
Here we solve task from here https://www.hackerrank.com/challenges/jumping-on-the-clouds
"""

import collections
import math

def countjumps(arr):
    """ given array safe (0) or unsafe (1) clouds, returns min jumps count (can jump by 1 or 2)
    >>> countjumps([0, 0, 1, 0, 0, 1, 0])
    4
    """

    return countjumpsrec(arr, 0)

def countjumpsrec(arr, prevjumps):
    if len(arr) >= 3 and arr[2] != 1:
        return countjumpsrec(arr[2:], prevjumps + 1)
    elif len(arr) >= 2 and arr[1] != 1:
        return countjumpsrec(arr[1:], prevjumps + 1)
    else:
        return prevjumps

if __name__ == "__main__":
    import doctest
    doctest.testmod()

