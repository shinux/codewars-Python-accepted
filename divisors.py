def divisors(n):
    """
    Find the number of divisors of a positive integer n.

    Example:

        divisors(4) -> 3 -- 1, 2, 4
        divisors(5) -> 2 -- 1, 5
        divisors(12) -> 6 -- 1, 2, 3, 4, 6, 12
        divisors(30) -> 8 -- 1, 2, 3, 5, 6, 10, 15, 30
    """
    accept = 0
    for i in xrange(1, n+1):
        if n % i == 0:
            accept += 1
    return accept


if __name__ == '__main__':
    divisors(5)
