"""
Here we solve task from here https://www.hackerrank.com/challenges/repeated-string
"""

import math
import functools

def count_a_letters_in_substr(substr):
    """ counts number of a string in subsring
    >>> count_a_letters_in_substr("baba")
    2
    """
    return functools.reduce(process, substr, 0)

def process(prev_res, item):
    if item == 'a':
        return prev_res + 1
    return prev_res

def count_a_letters(substr, n):
    """ given substring and length of string made of its repeatings, returns count of letter a in resulting string
    >>> count_a_letters("baba", 9)
    4
    >>> count_a_letters("hia", 9002)
    3000
    >>> count_a_letters("hiahia", 5)
    1
    """

    if len(substr) >= n:
        return count_a_letters_in_substr(substr[:n])

    return math.floor(n / len(substr)) * count_a_letters_in_substr(substr) + count_a_letters_in_substr(substr[:n % len(substr)])

if __name__ == "__main__":
    import doctest
    doctest.testmod()

