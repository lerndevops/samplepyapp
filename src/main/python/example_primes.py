import math
import itertools

"""Returns a list of N primes, beginning with [2, 3, 5...]."""
def first_N_primes(N):
    """
    Returns a list of N primes, beginning with [2, 3, 5...]. Returns an empty
    list if the user supplies a non-positive number. Floating point numbers
    are rounded up.
    >>> first_N_primes(0)
    []
    >>> first_N_primes(3.14)
    [2, 3, 5, 7]
    >>> first_N_primes(-42)
    []
    >>> first_N_primes(10)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    """
    if (N <= 0):
        return []

    primes = [2]
    prime  = (x for x in itertools.count(2) if not any ([x%y==0 for y in range(2, int(math.ceil(math.sqrt(x)))+1)]))

    for n in range(1, int(math.ceil(N))):
        primes.append(next(prime))

    return primes

if __name__ == "__main__": # pragma: no cover
    import doctest
    doctest.testmod()

