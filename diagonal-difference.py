"""
Here we solve task from here https://www.hackerrank.com/challenges/diagonal-difference
"""

def count_diagonal_diff(matrix):
    """ given matrix, returns abc diff of sum of its diagonales

    >>> count_diagonal_diff([[10, 20, 30], [20, 10, 30], [30, 15, 12]])
    38
    """

    direct_sum = sum([x[i] for (i, x) in enumerate(matrix)])
    reversed_sum = sum([x[i] for (i, x) in enumerate(reversed(matrix))])

    return abs(direct_sum - reversed_sum)

if __name__ == "__main__":
    import doctest
    doctest.testmod()

