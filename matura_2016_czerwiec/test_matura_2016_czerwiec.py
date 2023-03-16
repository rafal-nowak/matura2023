from unittest import TestCase

from matura_2016_czerwiec import Matura2016Czerwiec


class TestMatura2016Czerwiec(TestCase):
    def test_zadanie_6_1(self):
        expected_counter_of_octal_numbers = 103

        counter_of_octal_numbers = Matura2016Czerwiec().zadanie_6_1()

        self.assertEqual(expected_counter_of_octal_numbers, counter_of_octal_numbers)

    def test_zadanie_6_2(self):
        expected_good_quaternary_numbers = 29

        good_quaternary_numbers = Matura2016Czerwiec().zadanie_6_2()

        self.assertEqual(expected_good_quaternary_numbers, good_quaternary_numbers)

    def test_zadanie_6_3(self):
        expected_good_binary_numbers = 153

        good_binary_numbers = Matura2016Czerwiec().zadanie_6_3()

        self.assertEqual(expected_good_binary_numbers, good_binary_numbers)

    def test_zadanie_6_4(self):
        expected_sum_of_decimal_numbers = 887918739

        sum_of_decimal_numbers = Matura2016Czerwiec().zadanie_6_4()

        self.assertEqual(expected_sum_of_decimal_numbers, sum_of_decimal_numbers)

    def test_zadanie_6_5(self):
        expected_max_code = '8066218209'
        expected_max_num = 347931225
        expected_min_code = '100002'
        expected_min_num = 16

        max_code, max_num, min_code, min_num = Matura2016Czerwiec().zadanie_6_5()

        self.assertEqual(expected_max_code, max_code)
        self.assertEqual(expected_max_num, max_num)
        self.assertEqual(expected_min_code, min_code)
        self.assertEqual(expected_min_num, min_num)
