"""
Here we solve task from here https://www.hackerrank.com/challenges/plus-minus
"""

def count_plus_minus(arr):
    """ given list, returns tuple with proportions of its plus, minus and zeros

    >>> count_plus_minus([-1, 1, 0, 2, 34234, -1234, 5, -2, 0])
    (0.4444444444444444, 0.3333333333333333, 0.2222222222222222)

    """
    pluses_count = len([x for x in arr if x > 0])
    minuses_count = len([x for x in arr if x < 0])
    zeros_count = len([x for x in arr if x == 0])

    return (pluses_count / len(arr), minuses_count / len(arr), zeros_count / len(arr))

if __name__ == "__main__":
    import doctest
    doctest.testmod()

