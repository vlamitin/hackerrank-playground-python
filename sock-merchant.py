"""
Here we solve task from here https://www.hackerrank.com/challenges/sock-merchant
"""

import collections
import math

def countpairs(arr):
    """ given array of socks of different colors, returns pairs count.

    >>> countpairs([10, 20, 30, 20, 10, 30, 30])
    3

    """

    keys_to_count = collections.defaultdict(lambda: 0)

    for i in arr:
        keys_to_count[i] = keys_to_count[i] + 1

    pairs_count = 0

    for p in [keys_to_count[x] for x in keys_to_count]:
        pairs_count = pairs_count + math.floor(p / 2)

    return pairs_count

if __name__ == "__main__":
    import doctest
    doctest.testmod()

