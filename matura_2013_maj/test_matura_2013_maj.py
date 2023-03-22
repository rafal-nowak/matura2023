import unittest
from unittest import TestCase
from matura_2013_maj import Matura2013Maj

class TestMatura2013Maj(TestCase, Matura2013Maj):
    @classmethod
    def setUpClass(self):
        with open('dane.txt') as file:
            self.lines = [x.rstrip() for x in file.readlines()]


    def test_zadanie6_1(self):
        expected_number_of_same_digits = 447

        number_of_same_digits = self.zadanie_6_1()

        self.assertEqual(expected_number_of_same_digits, number_of_same_digits)


    def test_zadanie_6_2(self):
        expected_number_of_same_digits_decimal = 324

        number_of_same_digits_decimal = self.zadanie_6_2()

        self.assertEqual(expected_number_of_same_digits_decimal, number_of_same_digits_decimal)


    def test_zadanie_6_3(self):
        expected_number_of_ascending_digits = 49
        possible_biggest = [1133357, 308975]
        possible_smallest = [24, 20]

        number_of_ascending_digits, biggest, smallest = self.zadanie_6_3()
        smallest_present, biggest_present = smallest in possible_smallest, biggest in possible_biggest

        self.assertEqual(expected_number_of_ascending_digits, number_of_ascending_digits)
        self.assertEqual(smallest_present, True)
        self.assertEqual(biggest_present, True)


if __name__ == "__main__":
    unittest.main()