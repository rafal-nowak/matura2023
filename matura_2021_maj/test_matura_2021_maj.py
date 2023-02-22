from unittest import TestCase

from matura_2021_maj import Matura2021Maj

class TestMatura2021Maj(TestCase):
    def test_zadanie_4_1(self):
        expected_length = 517

        text_length = Matura2021Maj().zadanie4_1()

        self.assertEqual(expected_length, text_length)

    def test_zadanie_4_2(self):
        expected_type = "ZMIEN"
        expected_length = 7

        type, length = Matura2021Maj().zadanie4_2()

        self.assertEqual(expected_type, type)
        self.assertEqual(expected_length, length)

    def test_zadanie_4_3(self):
        expected_letter = "Z"
        expected_letter_additions = 37

        letter, additions = Matura2021Maj().zadanie4_3()

        self.assertEqual(expected_letter, letter)
        self.assertEqual(expected_letter_additions, additions)

    def test_zadanie_4_4(self):
        expected_word = "POZNIEJMOWIONOZECZLOWIEKTENNADSZEDLODPOLNOCYODBRAMYPOWROZNICZEJSZEDLPIESZOAOBJUCZONEGOKONIAPROWADZILZAUZDEBYLOPOZNEPOPOLUDNIEIKRAMYPOWROZNIKOWIRYMARZYBYLYJUZZAMKNIETEAULICZKAPUSTABYLOCIEPLOACZLOWIEKTENMIALNASOBIECZARNYPLASZCZNARZUCONYNARAMIONAZWRACALUWAGEZATRZYMALSIEPRZEDGOSPODASTARYNARAKORTPOSTALCHWILEPOSLUCHALGWARUGLOSOWGOSPODAJAKZWYKLEOTEJPORZEBYLAPELNALUDZINIEZNAJOMYNIEWSZEDLDOSTAREGONARAKORTUPOCIAGNALKONIADALEJWDOLULICZKITAMBYLADRUGAKARCZMAMNIEJSZANAZYWALASIEPODLISEMTUBYLOPUSTOKARCZMANIEMIALANAJLEPSZEJSLAWY"

        word = Matura2021Maj().zadanie4_4()

        self.assertEqual(expected_word, word)