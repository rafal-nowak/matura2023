import unittest

from matura_czerwiec_22 import Matura2022Czerwiec


class TestMatura2022Czerwiec(unittest.TestCase):
    def test_zadanie_4_1(self):
        expected_divided_by_17 = [1156, 102, 51, 765, 119, 119, 731]

        divided_by_17 = Matura2022Czerwiec().zadanie_4_1()

        self.assertEqual(expected_divided_by_17, divided_by_17)

    def test_zadanie_4_2(self):
        expected_max_difference = 8082
        expected_max_number = 1129
        max_difference, max_number = Matura2022Czerwiec().zadanie_4_2()

        self.assertEqual(expected_max_difference, max_difference)
        self.assertEqual(expected_max_number, max_number,)

    def test_zadanie_4_3(self):
        expected_prime_numbers = [157, 31, 347, 929, 941, 761]

        prime_numbers = Matura2022Czerwiec().zadanie_4_3()

        self.assertEqual(expected_prime_numbers, prime_numbers)

    def test_zadanie_4_4(self):
        expected_values = 85
        values, two_times, three_times = Matura2022Czerwiec().zadanie_4_4()

        expected_two_times = 13

        expected_three_times = 1

        self.assertEqual(expected_values, values)
        self.assertEqual(expected_two_times, two_times)
        self.assertEqual(expected_three_times, three_times)


if __name__ == '__main__':
    unittest.main()
