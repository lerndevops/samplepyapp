import unittest

from example_primes import first_N_primes

class FirstNPrimesTest(unittest.TestCase):

    """ test negative float input """
    def test_negFloatInput(self):
        self.assertEqual(first_N_primes(-14.3), [])

    """ test positive integer input """
    def test_posIntInput(self):
        self.assertEqual(first_N_primes(6), [2, 3, 5, 7, 11, 13])
