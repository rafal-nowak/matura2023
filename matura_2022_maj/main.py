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


if __name__ == '__main__':
    with open("liczby.txt") as file:

        lines = [line.rstrip() for line in file]
        print(lines)

        # Podaj, ile jest w pliku takich liczb, ktorych cyfry pierwsza i ostatnia sa takie same
        # Zapisz te z nich, ktora wystepuje w pliku jako pierwsza

        number_of_searched_numbers = 0
        first_number_as_text = ""
        for line in lines:
            if is_first_and_last_digit_same(line):
                number_of_searched_numbers += 1
                if first_number_as_text == "":
                    first_number_as_text = line

        print()
        print('################################################################################')
        print('Podaj, ile jest w pliku takich liczb, ktorych cyfry pierwsza i ostatnia sa takie same')
        print('Zapisz te z nich, ktora wystepuje w pliku jako pierwsza')
        print(f'Istnieje {number_of_searched_numbers} takich liczb')
        print(f'Pierwsza z nich to {first_number_as_text}')
        print('################################################################################')
        print()

        # Znajdz w pliku liczbe, ktora ma w rozkladzie najwiecej czynnikow pierwszych (podaj te liczbe oraz liczbe jej czynnikow pierwszych)
        # Znajdz w pliku liczbe, ktora ma w rozkladzie najwiecej roznych czynnikow pierwszych (podaj te liczbe oraz liczbe jej roznych czynnikow pierwszych)

        max_number_of_prime_factors = 0
        max_number_of_different_prime_factors = 0
        number_with_max_prime_factors = 0
        number_with_max_different_prime_factors = 0

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

        print()
        print('################################################################################')
        print(f'Liczba, ktora ma w rozkladzie najwiecej czynnikow pierwszych to {number_with_max_prime_factors},')
        print(f'Liczba tych czynnikow to {max_number_of_prime_factors}')
        print(f'Liczba, ktora ma w rozkladzie najwiecej roznych czynnikow pierwszych to {number_with_max_different_prime_factors},')
        print(f'Liczba tych czynnikow to {max_number_of_different_prime_factors}')
        print('################################################################################')
        print()

        # Podaj, ile jest dobrych trójek wśród liczb występujących w pliku `liczby.txt`.
        # Zapisz wszystkie dobre trójki do pliku `trojki.txt`
        # Podaj, ile jest dobrych piątek wśród liczb występujących w pliku `liczby.txt`.

        numer_of_good_threes = 0
        numer_of_good_fives = 0
        good_threes = set()
        good_fives = set()

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

        print()
        print('################################################################################')
        print(f'W pliku wystepuje {numer_of_good_threes} dobrych trojek')
        print(f'W pliku wystepuje {numer_of_good_fives} dobrych piatek')
        print(f'Oto dobre trojki {good_threes}')
        print(f'Oto dobre piatki {good_fives}')
        print('################################################################################')
        print()
