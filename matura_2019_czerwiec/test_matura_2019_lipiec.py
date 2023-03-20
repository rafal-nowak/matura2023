import unittest

from matura_2019_lipiec import Matura2019Lipiec


class MyTestCase(unittest.TestCase):
    def test_zadanie_4_1(self):
        expected_prime_numbers_between_100_and_5000 = [563, 2087, 163, 2423, 3581, 911, 997, 113, 1049, 1511, 2467, 283,
                                                       3559, 521, 4201, 877, 1301, 2749, 4919, 1213, 2039, 4111, 3331,
                                                       401, 2221]

        prime_numbers_between_100_and_5000 = Matura2019Lipiec().zadanie_4_1()

        self.assertEqual(expected_prime_numbers_between_100_and_5000, prime_numbers_between_100_and_5000)

    def test_zadanie_4_2(self):
        expected_prime_numbers_that_read_backwards_are_also_prime = [31, 37, 101, 1009, 1021, 113, 1499, 1213, 1217,
                                                                     1229, 1231, 1237, 1487, 1223, 7027, 7043, 3821,
                                                                     31873, 1511, 140527, 151169, 151189, 193261,
                                                                     1297001, 1061, 100267, 100271, 100279, 181957, 13,
                                                                     112163, 112181, 3803, 76001, 160183, 160201,
                                                                     160243, 17, 907, 701, 383, 389, 1103, 1109, 31721,
                                                                     1583, 1597, 1601, 1619, 3571, 112111]

        prime_numbers_that_read_backwards_are_also_prime = Matura2019Lipiec().zadanie_4_2()

        self.assertEqual(expected_prime_numbers_that_read_backwards_are_also_prime,
                         prime_numbers_that_read_backwards_are_also_prime)

    def test_zadanie_4_3(self):
        expected_count_of_numbers_with_weight_equal_to_1 = 27

        count_of_numbers_with_weight_equal_to_1 = Matura2019Lipiec().zadanie_4_3()

        self.assertEqual(expected_count_of_numbers_with_weight_equal_to_1, count_of_numbers_with_weight_equal_to_1)
