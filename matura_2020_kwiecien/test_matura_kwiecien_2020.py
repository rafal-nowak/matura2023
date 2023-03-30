import unittest
from unittest import TestCase
from matura_kwiecien_2020 import matura_kwiecien_2020

class TestMaturaKwiecien2020(TestCase):


    def test_zadanie_4_1(self):
        min_gap, max_gap = matura_kwiecien_2020().zadanie_4_1()
        self.assertEqual(min_gap, 1)
        self.assertEqual(max_gap, 1056392131)

    def test_zadanie_4_2(self):
        length, start, end = matura_kwiecien_2020().zadanie_4_2()
        self.assertEqual(length, 17)
        self.assertEqual(start, 193134524)
        self.assertEqual(end, 223545714)

    def test_zadanie_4_3(self):
        max_count, most_frequent_gaps = matura_kwiecien_2020().zadanie_4_3()
        self.assertEqual(max_count, 31)
        self.assertEqual(most_frequent_gaps, [149, 11])

if __name__ == '__main__':
    unittest.main()




