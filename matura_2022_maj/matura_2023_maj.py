def is_first_and_last_digit_same(number_as_text):
    if number_as_text[0] == number_as_text[-1]:
        return True
    return False


def prime_factorization(n):
    factors = []
    k = 2
    while n != 1:
        while n % k == 0:
            n //= k
            factors.append(k)
        k += 1

    return factors


class Matura2023Maj:
    def __init__(self):
        pass

    def zadanie_4_1(selfs):
        # Podaj, ile jest w pliku takich liczb, ktorych cyfry pierwsza i ostatnia sa takie same
        # Zapisz te z nich, ktora wystepuje w pliku jako pierwsza

        number_of_searched_numbers = 0
        first_number_as_text = ""

        with open("liczby.txt") as file:

            lines = [line.rstrip() for line in file]

            for line in lines:
                if is_first_and_last_digit_same(line):
                    number_of_searched_numbers += 1
                    if first_number_as_text == "":
                        first_number_as_text = line

        return number_of_searched_numbers, first_number_as_text

    def zadanie_4_2(selfs):
        # Znajdz w pliku liczbe, ktora ma w rozkladzie najwiecej czynnikow pierwszych
        # (podaj te liczbe oraz liczbe jej czynnikow pierwszych)
        # Znajdz w pliku liczbe, ktora ma w rozkladzie najwiecej roznych czynnikow pierwszych
        # (podaj te liczbe oraz liczbe jej roznych czynnikow pierwszych)

        max_number_of_prime_factors = 0
        max_number_of_different_prime_factors = 0
        number_with_max_prime_factors = 0
        number_with_max_different_prime_factors = 0

        with open("liczby.txt") as file:

            lines = [line.rstrip() for line in file]
            for line in lines:
                number = int(line)
                prime_factors = prime_factorization(number)
                different_prime_factors = set(prime_factors)
                if len(prime_factors) > max_number_of_prime_factors:
                    max_number_of_prime_factors = len(prime_factors)
                    number_with_max_prime_factors = number
                if len(different_prime_factors) > max_number_of_different_prime_factors:
                    max_number_of_different_prime_factors = len(different_prime_factors)
                    number_with_max_different_prime_factors = number

        return number_with_max_prime_factors, max_number_of_prime_factors, number_with_max_different_prime_factors, max_number_of_different_prime_factors

    def zadanie_4_3(selfs):
        # Podaj, ile jest dobrych trójek wśród liczb występujących w pliku `liczby.txt`.
        # Zapisz wszystkie dobre trójki do pliku `trojki.txt`
        # Podaj, ile jest dobrych piątek wśród liczb występujących w pliku `liczby.txt`.

        # Dobre trojki
        numer_of_good_threes = 0
        good_threes = set()
        # Dobre piatki
        numer_of_good_fives = 0
        good_fives = set()

        with open("liczby.txt") as file:

            lines = [line.rstrip() for line in file]


            numbers = set()
            for line in lines:
                numbers.add(int(line))

            numbers = sorted(numbers)
            print(numbers)

            for number in numbers:
                for i in range(number + 1, max(numbers) + 1):
                    if i % number == 0 and i in numbers:
                        for j in range(i + 1, max(numbers) + 1):
                            if j % i == 0 and j in numbers:
                                numer_of_good_threes += 1
                                good_threes.add(f'{number} {i} {j}')
                                for k in range(j + 1, max(numbers) + 1):
                                    if k % j == 0 and k in numbers:
                                        for l in range(k + 1, max(numbers) + 1):
                                            if l % k == 0 and l in numbers:
                                                numer_of_good_fives += 1
                                                good_fives.add(f'{number} {i} {j} {k} {l}')

        return numer_of_good_threes, good_threes, numer_of_good_fives, good_fives
