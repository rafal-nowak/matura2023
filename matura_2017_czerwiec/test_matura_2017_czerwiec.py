import unittest
from Matura_2017_czerwiec import Matura2017Czerwiec

class TestMatura2015Maj(unittest.TestCase):
    def test_zadanie_4_1(self):
        expected_PrimeNum = 18

        PrimeNum= Matura2017Czerwiec().zadanie_4_1()

        self.assertEqual( expected_PrimeNum, PrimeNum)

    def test_zadanie_4_2(self):
        expected_n = 5

        n = Matura2017Czerwiec().zadanie_4_2()

        self.assertEqual(expected_n, n)

    def test_zadanie_4_3(self):
        expected_lenght = 13347
        expected_xa = 9901
        expected_ya = 593
        expected_xb = 35
        expected_yb = 9583

        lenght, XA, YA, XB, YB = Matura2017Czerwiec().zadanie_4_3()

        self.assertEqual(  expected_lenght, lenght)
        self.assertEqual(  expected_xa, XA)
        self.assertEqual(  expected_ya, YA)
        self.assertEqual(  expected_xb, XB)
        self.assertEqual(  expected_yb, YB)

    def test_zadanie_4_4(self):
        expected_outside = 749
        expected_inside = 249
        expected_edge = 2

        outside,inside, edge = Matura2017Czerwiec().zadanie_4_4()

        self.assertEqual(  expected_outside, outside)
        self.assertEqual(  expected_inside, inside)
        self.assertEqual(  expected_edge, edge)

if __name__ == '__main__':
    unittest.main()