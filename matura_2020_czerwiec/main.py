def generate_sieve(limit=100):
    primes = [2]+[i for i in range(3, limit+1, 2)]
    start_index = 1

    while start_index < len(primes):
        for to_be_removed in range(primes[start_index]*2, limit+1, primes[start_index]):
            if to_be_removed in primes:
                primes.remove(to_be_removed)
        start_index += 1

    return primes


if __name__ == "__main__":
    with open("pary.txt") as file:
        data = [[int((x := line.split(' '))[0]), x[1]] for line in file.read().rstrip('\n').split('\n')]
        numbers = [line[0] for line in data]
        words = [line[1] for line in data]

    # Podaj dwie liczby pierwsze, których sumą jest podana liczba parzysta
    print()
    print("########################################")
    print("Podaj dwie liczby pierwsze, których sumą jest podana liczba parzysta")
    primes = generate_sieve()

    for number in numbers:
        if number > 4 and not number % 2:
            start_index, end_index = 0, len(primes)-1
            while primes[end_index] - primes[start_index] >= 0:
                if (sum_of_primes := primes[end_index] + primes[start_index]) == number:
                    print(f"{number} {primes[start_index]} {primes[end_index]}")
                    break
                elif sum_of_primes > number:
                    end_index -= 1
                elif sum_of_primes < number:
                    start_index += 1

    print("########################################")
    print()

    # Dla każdego słowa podaj najdłuższy spójny ciąg znaków i jego długość
    # Jeżeli występują więcej niż dwa, podaj pierwszy z nich
    print()
    print("########################################")
    print("Dla każdego słowa podaj najdłuższy spójny ciąg znaków i jego długość")

    for word in words:
        max_length, max_series, current_length, previous_letter = 0, '', 0, ''
        for letter in word:
            if letter == previous_letter:
                current_length += 1
                continue
            if current_length > max_length:
                max_length = current_length
                max_series = max_length*previous_letter
            current_length = 1
            previous_letter = letter

        if current_length > max_length: # przypadek ciągu stałego od n - len(word)
            max_length = current_length
            max_series = max_length*previous_letter
        print(max_series, max_length)

    print("########################################")
    print()

    # Wskaż pary o liczbie równej długości słowa
    # Wypisz najmniejszą z nich

    data = sorted([line for line in data if line[0] == len(line[1])])

    print()
    print("########################################")
    print("Wypisz najmniejszą z pośród par o liczbie równej długości słowa")
    print(data[0][0], data[0][1])
    print("########################################")
    print()
    