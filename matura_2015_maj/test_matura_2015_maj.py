from unittest import TestCase

from matura_2015_maj import Matura2015Maj


class TestMatura2015Maj(TestCase):
    def test_zadanie_4_1(self):
        expected_more_zeros = 422

        more_zeros_than_ones = Matura2015Maj().zadanie4_1()

        self.assertEqual(expected_more_zeros, more_zeros_than_ones)

    def test_zadanie_4_2(self):
        expected_divisible_by_two = 500
        expected_divisible_by_eight = 123

        divisible_by_two, divisible_by_eight = Matura2015Maj().zadanie4_2()

        self.assertEqual(expected_divisible_by_two, divisible_by_two)
        self.assertEqual(expected_divisible_by_eight, divisible_by_eight)

    def test_zadanie_4_3(self):
        expected_min_number_line = 859
        expected_max_number_line = 925

        min_number_line, max_number_line = Matura2015Maj().zadanie4_3()

        self.assertEqual(expected_min_number_line, min_number_line)
        self.assertEqual(expected_max_number_line, max_number_line)
