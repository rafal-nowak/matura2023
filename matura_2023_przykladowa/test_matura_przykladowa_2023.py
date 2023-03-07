from unittest import TestCase

from matura_2023_przykladowa.matura_przykladowa_2023 import Matura2023Przykladowa


class TestMatura2023Maj(TestCase):
    def test_zadanie_1_1(self):
        expected_positions_with_empty_columns = 36
        expected_max_empty_columns = 3

        positions_with_empty_columns, max_empty_columns = Matura2023Przykladowa().zadanie_1_1()

        self.assertEqual(expected_positions_with_empty_columns, positions_with_empty_columns)
        self.assertEqual(expected_max_empty_columns, max_empty_columns)

    def test_zadanie_1_2(self):
        expected_equal_positions = 22
        expected_min_equal_pieces = 28

        equal_positions, min_equal_pieces = Matura2023Przykladowa().zadanie_1_2()

        self.assertEqual(expected_equal_positions, equal_positions)
        self.assertEqual(expected_min_equal_pieces, min_equal_pieces)

    def test_zadanie_1_3(self):
        expected_white_rook_checks = 3
        expected_black_rook_checks = 1

        white_rook_checks, black_rook_checks = Matura2023Przykladowa().zadanie_1_3()

        self.assertEqual(expected_white_rook_checks, white_rook_checks)
        self.assertEqual(expected_black_rook_checks, black_rook_checks)