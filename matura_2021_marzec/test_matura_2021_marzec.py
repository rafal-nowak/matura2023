import unittest
from unittest import TestCase
from matura_2021_marzec import Matura2021Marzec

class TestMatura2021Marzec(TestCase, Matura2021Marzec):
    @classmethod
    def setUpClass(self):
        self.galeries = []
        with open('galerie.txt') as file:
            for line in file.read().rstrip().split('\n'):
                self.galeries.append({"code": (data := line.split(' '))[0], 
                                      "city": data[1], "stores": [int(x) for x in data[2:] if int(x)]})


    def test_zadanie_4_1(self):
        expected_country_and_number = [('GB', 5), ('D', 15), ('E', 6), ('I', 6), ('F', 2), ('RO', 1), ('A', 1), 
                                       ('H', 1), ('BG', 1), ('CZ', 1), ('B', 1), ('S', 1), ('HR', 1), ('NL', 2), 
                                       ('LV', 1), ('GR', 1), ('LT', 1), ('FIN', 1), ('DK', 1), ('IRL', 1)]
        country_and_number = self.zadanie_4_1()

        self.assertEqual(expected_country_and_number, country_and_number)


    def test_zadanie_4_2(self):
        expected_areas_and_locals = [('Londyn', 3628, 58), ('Berlin', 3777, 59), ('Madryt', 2217, 34), 
                                     ('Rzym', 3678, 51), ('Paryz', 3889, 62), ('Bukareszt', 1957, 33), 
                                     ('Wieden', 2694, 42), ('Hamburg', 3518, 52), ('Budapeszt', 3598, 64), 
                                     ('Barcelona', 4059, 60), ('Monachium', 1734, 31), ('Mediolan', 1958, 35), 
                                     ('Sofia', 3631, 59), ('Praga', 2622, 40), ('Bruksela', 4316, 64), 
                                     ('Birmingham', 1826, 25), ('Kolonia', 2104, 31), ('Neapol', 3352, 48), 
                                     ('Turyn', 2646, 39), ('Marsylia', 3444, 56), ('Sztokholm', 2133, 33), 
                                     ('Walencja', 3981, 68), ('Zagrzeb', 2177, 31), ('Leeds', 2952, 44), 
                                     ('Amsterdam', 3371, 60), ('Sewilla', 4305, 70), ('Ryga', 1745, 30), 
                                     ('Frankfurt', 3515, 57), ('Palermo', 2733, 43), ('Ateny', 4435, 65), 
                                     ('Saragossa', 3480, 50), ('Genua', 3386, 56), ('Stuttgart', 1718, 32), 
                                     ('Dortmund', 3697, 57), ('Rotterdam', 3184, 49), ('Essen', 4760, 67), 
                                     ('Glasgow', 3731, 68), ('Dusseldorf', 3737, 63), ('Wilno', 1620, 28), 
                                     ('Helsinki', 3597, 56), ('Malaga', 3757, 57), ('Brema', 2948, 44), 
                                     ('Sheffield', 2324, 36), ('Hanower', 3532, 53), ('Lipsk', 1871, 29), 
                                     ('Kopenhaga', 3765, 60), ('Drezno', 1900, 26), ('Dublin', 1986, 31), 
                                     ('Norymberga', 4178, 69), ('Duisburg', 3948, 61)]
        expected_min_city, expected_min_area = 'Wilno', 1620
        expected_max_city, expected_max_area = 'Essen', 4760

        areas_and_locals, min_city, min_area, max_city, max_area = self.zadanie_4_2()

        self.assertEqual(expected_areas_and_locals, areas_and_locals)
        self.assertEqual(expected_min_city, min_city)
        self.assertEqual(expected_max_city, max_city)
        self.assertEqual(expected_min_area, min_area)
        self.assertEqual(expected_max_area, max_area)

    def test_zadanie_4_3(self):
        expected_min_city, expected_min_number = 'Kolonia', 18
        expected_max_city, expected_max_number = 'Berlin', 35

        min_city, min_number, max_city, max_number = self.zadanie_4_3()

        self.assertEqual(expected_min_city, min_city)
        self.assertEqual(expected_max_city, max_city)
        self.assertEqual(expected_min_number, min_number)
        self.assertEqual(expected_max_number, max_number)


if __name__ == "__main__":
    unittest.main()