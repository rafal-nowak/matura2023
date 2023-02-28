import unittest

from matura_czerwiec_22 import Matura2022Czerwiec


class TestMatura2022Czerwiec(unittest.TestCase):
    def test_zadanie_4_1(self):
        expected_dividedby17 = [1156, 102, 51, 765, 119, 119, 731]

        dividedby17 = Matura2022Czerwiec().zadanie_4_1()

        self.assertEqual(expected_dividedby17, dividedby17)

    def test_zadanie_4_2(self):
        expected_maxdifference = 8082
        expected_maxnumber = 1129
        maxdifference, maxnumber = Matura2022Czerwiec().zadanie_4_2()

        self.assertEqual(expected_maxdifference, maxdifference)
        self.assertEqual(expected_maxnumber, maxnumber,)

    def test_zadanie_4_3(self):
        expected_primeNumbers = [157, 31, 347, 929, 941, 761]

        primeNumbers = Matura2022Czerwiec().zadanie_4_3()

        self.assertEqual(expected_primeNumbers, primeNumbers)

    def test_zadanie_4_4(self):
        expected_values = 85
        values, twoTimes, threeTimes = Matura2022Czerwiec().zadanie_4_4()

        expected_twoTimes = 13

        expected_threeTimes = 1

        self.assertEqual(expected_values, values)
        self.assertEqual(expected_twoTimes, twoTimes)
        self.assertEqual(expected_threeTimes, threeTimes)


if __name__ == '__main__':
    unittest.main()
