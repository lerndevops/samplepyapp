import sys

"""Prints \"Hello World!\" to the given output stream."""
def hello_world(out):
    """
    Prints \"Hello World!\".
    >>> import sys
    >>> hello_world(sys.stdout)
    Hello World!\n
    """
    out.write("Hello World!\n")

"""

Below:

 > Required in order to run the documentation checker on this code.

 > The comment
     pragma: no cover
   means that this block of code will not be checked for unit test
   coverage by the `coverage` module.

"""

if __name__ == "__main__": # pragma: no cover
    import doctest
    doctest.testmod()
