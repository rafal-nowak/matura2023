from unittest import TestCase

from matura_2022_maj.matura_2023_maj import Matura2023Maj


class TestMatura2023Maj(TestCase):
    def test_zadanie_4_1(self):
        expected_number_of_searched_numbers = 18
        expected_first_number_as_text = "93639"

        number_of_searched_numbers, first_number_as_text = Matura2023Maj().zadanie_4_1()

        self.assertEqual(expected_number_of_searched_numbers, number_of_searched_numbers)
        self.assertEqual(expected_first_number_as_text, first_number_as_text)

    def test_zadanie_4_2(self):
        expected_number_with_max_prime_factors = 99792
        expected_max_number_of_prime_factors = 10
        expected_number_with_max_different_prime_factors = 62790
        expected_max_number_of_different_prime_factors = 6

        number_with_max_prime_factors, \
            max_number_of_prime_factors, \
            number_with_max_different_prime_factors, \
            max_number_of_different_prime_factors = Matura2023Maj().zadanie_4_2()

        self.assertEqual(expected_number_with_max_prime_factors, number_with_max_prime_factors)
        self.assertEqual(expected_max_number_of_prime_factors, max_number_of_prime_factors)
        self.assertEqual(expected_number_with_max_different_prime_factors, number_with_max_different_prime_factors)
        self.assertEqual(expected_max_number_of_different_prime_factors, max_number_of_different_prime_factors)

    def test_zadanie_4_3(self):
        expected_numer_of_good_threes = 27
        expected_good_threes = {'797 7173 64557', '409 9816 58896', '971 6797 27188', '871 15678 62712',
                                '232 13688 27376', '2806 8418 84180', '955 8595 42975', '6797 13594 81564',
                                '2806 42090 84180', '971 6797 13594', '1403 2806 8418', '971 6797 81564',
                                '971 13594 81564', '13594 27188 81564', '1403 2806 84180', '971 13594 27188',
                                '971 27188 81564', '6797 13594 27188', '1403 8418 42090', '497 22365 89460',
                                '1403 8418 84180', '2806 8418 42090', '392 20384 61152', '8418 42090 84180',
                                '1403 42090 84180', '6797 27188 81564', '1403 2806 42090'}
        expected_numer_of_good_fives = 2
        expected_good_fives = {'1403 2806 8418 42090 84180', '971 6797 13594 27188 81564'}

        numer_of_good_threes, good_threes, numer_of_good_fives, good_fives = Matura2023Maj().zadanie_4_3()

        self.assertEqual(expected_numer_of_good_threes, numer_of_good_threes)
        self.assertEqual(expected_good_threes, good_threes)
        self.assertEqual(expected_numer_of_good_fives, numer_of_good_fives)
        self.assertEqual(expected_good_fives, good_fives)
