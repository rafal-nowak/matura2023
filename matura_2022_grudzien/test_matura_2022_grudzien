import unittest

from matura_2022_grudzien import Matura2022Grudzien

class TestMatura2022Grudzien(unittest.TestCase):
    def test_zadanie_1_1(self):
        expected_number = 5030

        number = Matura2022Grudzien().zadanie_1_1()

        self.assertEqual(expected_number, number)

    def test_zadanie_1_2(self):
        expected_match_result = "B 1001:1004"

        match_result = Matura2022Grudzien().zadanie_1_2()

        self.assertEqual(expected_match_result, match_result)    

    def test_zadanie_1_3(self):
        expected_combo_counter = 6
        expected_highest_combo_team = "B"
        expected_highest_combo = 15

        combo_counter, highest_combo_team, highest_combo = Matura2022Grudzien().zadanie_1_3()

        self.assertEqual(expected_combo_counter, combo_counter)
        self.assertEqual(expected_highest_combo_team, highest_combo_team)
        self.assertEqual(expected_highest_combo, highest_combo)

    def test_zadanie_2_4(self):
        expected_pairs = "47 3044\n7650 61204\n1 245\n7 63669\n9125 18250\n5 43246"

        pairs = Matura2022Grudzien().zadanie_2_4()

        self.assertEqual(expected_pairs, pairs)

    def test_zadanie_3_2(self):
        expected_number_count = 21

        number_count = Matura2022Grudzien().zadanie_3_2()

        self.assertEqual(expected_number_count, number_count)

    def test_zadanie_3_3(self):
        expected_most_factors_number = 910620
        expected_most_factors = 9932
        expected_least_factors_number = 18676
        expected_least_factors = 195

        most_factors_number, most_factors, least_factors_number, least_factors = Matura2022Grudzien().zadanie_3_3()

        self.assertEqual(expected_most_factors_number, most_factors_number)
        self.assertEqual(expected_most_factors, most_factors)
        self.assertEqual(expected_least_factors_number, least_factors_number)
        self.assertEqual(expected_least_factors, least_factors)

    def test_zadanie_3_4(self):
        expected_answer = "0: 32\n1: 26\n2: 37\n3: 31\n4: 43\n5: 25\n6: 28\n7: 23\n8: 38\n9: 28\nA: 45\nB: 33\nC: 29\nD: 23\nE: 44\nF: 10"

        answer = Matura2022Grudzien().zadanie_3_4()

        self.assertEqual(expected_answer, answer)

if __name__ == '__main__':
    unittest.main()