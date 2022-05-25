from mockito import mock, verify
import unittest

from example_hello import hello_world

class HelloWorldTest(unittest.TestCase):

    def test_correct_message(self):
        out = mock()
        hello_world(out)
        verify(out).write("Hello World!\n")
