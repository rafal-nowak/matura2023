import unittest

from matura_2021_czerwiec import Matura2021Czerwiec

class TestMatura2021Czerwiec(unittest.TestCase):
    def test_zadanie_4_1(self):
        expected_digits_in_file = 11844

        digits_in_file = Matura2021Czerwiec().zadanie_4_1()

        self.assertEqual(expected_digits_in_file, digits_in_file)

    def test_zadanie_4_2(self):
        expected_phrase = "SZYBKOROZWIAZUJEPROGRAMISTYCZNEZADANIAZINFORMATYKI"

        phrase = Matura2021Czerwiec().zadanie_4_2()

        self.assertEqual(expected_phrase, phrase)

    def test_zadanie_4_3(self):
        expected_phrase_from_middle_letters_of_palindrome = "ZADANIEMATURALNE"

        phrase_from_middle_letters_of_palindrome = Matura2021Czerwiec().zadanie_4_3()

        self.assertEqual(expected_phrase_from_middle_letters_of_palindrome, phrase_from_middle_letters_of_palindrome)

    def test_zadanie_4_4(self):
        expected_phrase_ending_with_x = "LITWOOJCZYZNOMOJATYJESTESJAKZDROWIEILECIETRZEBACENICTENTYLKOSIEDOWIEKTOCIESTRACILNATENCZASWOJSKICHWYCILNATASMIEPRZYPIETYSWOJROGBAWOLIDLUGICENTKOWANYKRETYJAKWAZBOAXXX"

        phrase_ending_with_x = Matura2021Czerwiec().zadanie_4_4()

        self.assertEqual(expected_phrase_ending_with_x, phrase_ending_with_x)

if __name__ == '__main__':
    unittest.main()