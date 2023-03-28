from unittest import TestCase

from matura_2017_maj import Matura2017Maj

class TestMatura2017Maj(TestCase):
    def test_zadanie_6_1(self):
        expected_brightest = 221
        expected_darkest = 7

        brightest, darkest = Matura2017Maj().zadanie_6_1()

        self.assertEqual(expected_brightest, brightest)
        self.assertEqual(expected_darkest, darkest)

    def test_zadanie_6_2(self):
        expected_counter = 149

        counter = Matura2017Maj().zadanie_6_2()

        self.assertEqual(expected_counter, counter)

    def test_zadanie_6_3_1(self):
        expected_counter = 753

        counter = Matura2017Maj().zadanie_6_3_1()

        self.assertEqual(expected_counter, counter)

    def test_zadanie_6_3_2(self):
        expected_counter = 753

        counter = Matura2017Maj().zadanie_6_3_2()

        self.assertEqual(expected_counter, counter)


    def test_zadanie_6_4(self):
        expected_max_of_max_list = 5

        max_of_max_list = Matura2017Maj().zadanie_6_4()

        self.assertEqual(expected_max_of_max_list, max_of_max_list)