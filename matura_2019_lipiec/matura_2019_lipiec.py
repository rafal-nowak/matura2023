class Matura2019Lipiec:
    def __init__(self):
        with open('liczby.txt', 'r') as file:
            self.numbers = [int(x.strip()) for x in file.readlines()]

        with open('pierwsze.txt', 'r') as file:
            self.prime_numbers = [int(x.strip()) for x in file.readlines()]

    def __czy_pierwsza(self, number):
        original_number = number
        factors = [1]

        while number > 1:
            for factor in range(2, number+1):
                if number % factor == 0:
                    if number not in factors: factors.append(number)
                    if factor not in factors: factors.append(factor)
                    number = number // factor
                    break
            if number == original_number:
                factors.append(original_number)
                break

        if len(factors) == 2:
            return True
        else:
            return False

    def __count_weight_of_number(self, number):
        weight = 0
        while number > 9:
            for _ in str(number):
                weight += int(_)
            number = weight
            weight = 0

        return weight

    def zadanie_4_1(self):
        # Podaj, (zachowując ich kolejność) te liczby z pliku liczby.txt,
        # które są liczbami pierwszymi z przedziału 〈100; 5000〉

        prime_numbers_between_100_and_5000 = []

        for number in self.numbers:
            if 100 <= number <= 5000:
                if self.__czy_pierwsza(number):
                    prime_numbers_between_100_and_5000.append(number)

        return prime_numbers_between_100_and_5000

    def zadanie_4_2(self):
        # Podaj, w kolejności ich występowania w pliku pierwsze.txt, wszystkie te liczby,
        # które czytane od prawej do lewej również są liczbami pierwszymi.

        prime_numbers_that_read_backwards_are_also_prime = []

        for number in self.prime_numbers:
            reversed_number = int(str(number)[::-1])
            if self.__czy_pierwsza(reversed_number):
                prime_numbers_that_read_backwards_are_also_prime.append(number)

        return prime_numbers_that_read_backwards_are_also_prime

    def zadanie_4_3(self):
        # Niech w(N) oznacza sumę cyfr liczby N. Dla danej liczby N tworzymy ciąg,
        # w którym N1 = w(N),
        # a każdy kolejny element jest sumą cyfr występujących w poprzednim elemencie:
        #       N1 = w(N)
        #       N2 = w(N1)
        #       N3 = w(N2)
        #       ...
        # Ciąg kończy się, gdy jego wyraz jest liczbą jednocyfrową.
        # Tę liczbę nazywamy wagą liczby N.
        #
        # Podaj, ile jest liczb w pliku pierwsze.txt, których waga jest równa 1.

        count_of_numbers_with_weight_equal_to_1 = 0

        for number in self.prime_numbers:
            if self.__count_weight_of_number(number) == 1:
                count_of_numbers_with_weight_equal_to_1 += 1

        return count_of_numbers_with_weight_equal_to_1
