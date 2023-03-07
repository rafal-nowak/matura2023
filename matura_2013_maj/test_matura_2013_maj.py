import unittest
from unittest import TestCase
from matura_2013_maj import Matura2013Maj

class TestMatura2013Maj(TestCase):
    def test_zadanie6_1(self):
        expected_output = 1
        output = Matura2013Maj().zadanie6_1()
        self.assertEqual(expected_output, output)
        # TODO: make variables
        # TODO: make test
        pass

    # TODO: make functions

unittest.main()