"""
Here we solve task from here https://www.hackerrank.com/challenges/counting-valleys
"""

import collections
import functools

def count_valleys(arr):
    """ given array altitide changes, returns valleys count.

    >>> count_valleys([-1, -1, 1, 1, 1, -1, -1, -1, 1])
    2

    >>> count_valleys([-1, -1, -1, 1, 1, 1, -1, -1, -1, 1, -1, -1])
    2
    """

    return functools.reduce(process, arr, {'valleysCount': 0, 'abcAlt': 0 })['valleysCount']

def process(prevRes, item):
    prevAlt = prevRes['abcAlt']
    prevRes['abcAlt'] = prevRes['abcAlt'] + item

    if prevAlt >= 0 and prevRes['abcAlt'] < 0:
        prevRes['valleysCount'] = prevRes['valleysCount'] + 1

    return prevRes

if __name__ == "__main__":
    import doctest
    doctest.testmod()

