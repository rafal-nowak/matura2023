def get_from_x_to_y(x, y):
    steps_from_x, steps_from_y = [], []

    if x == 1 or y == 1:
        return True

    while x != 1:
        steps_from_x.append(x)
        x = x // 2

    while y != 1:
        steps_from_y.append(y)
        y = y // 2

    for step in steps_from_x:
        if step not in steps_from_y:
            return False
    return True

def is_prime(x):
    if x > 1:
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                return False
        return True
    return False

class Matura2022Grudzien:
    def __init__(self):
        pass

    def zadanie_1_1(selfs):
        # Oblicz, ile razy nastąpiła sytuacja, w której rozgrywkę wygrała inna drużyna niż rozgrywkę poprzednią (tzn. dwa kolejne znaki A lub B w opisie meczu się różnią).
        with open("mecz.txt", "r") as file:
            wins = [char for char in file.read()][:-1]

        counter = 0

        for i in range(len(wins) - 1):
            if wins[i+1] != wins[i]:
                counter += 1

        return counter
    
    def zadanie_1_2(selfs):
        # Podaj, która drużyna *wygrała pierwszego seta* i jaki w tym momencie był wynik (liczba zwycięskich rozgrywek drużyny A i liczba zwycięskich rozgrywek drużyny B w pierwszym secie).
        with open("mecz.txt", "r") as file:
            wins = [char for char in file.read()][:-1]

        counter_a, counter_b, winner = 0, 0, ""

        for char in wins:
            if char == "A":
                counter_a += 1
            else:
                counter_b += 1
            if counter_a >= 1000 and counter_a - counter_b >= 3:
                winner = "A"
                break
            elif counter_b >= 1000 and counter_b - counter_a >= 3:
                winner = "B"
                break

        return f"{winner} {counter_a}:{counter_b}"
    
    def zadanie_1_3(selfs):
        # Podaj łączną liczbę dobrych pass, które miały obie drużyny w meczu. Wyznacz długość najdłuższej dobrej passy i drużynę, która ją osiągnęła. Tylko jedna drużyna miała dobrą passę o tej długości.
        with open("mecz.txt", "r") as file:
            wins = [char for char in file.read()][:-1]

        highest_combo = 1
        highest_combo_team = wins[0]
        combo_counter = 0
        combo_a, combo_b = 0, 0

        if wins[0] == "A":
            combo_a += 1
        else:
            combo_b += 1

        for i in range(1, len(wins)):
            if wins[i] == "A":
                combo_a += 1
            else:
                combo_b += 1

            if wins[i] != wins[i-1]:
                if wins[i-1] == "A":
                    if combo_a >= 10:
                        combo_counter += 1
                        if combo_a >= highest_combo:
                            highest_combo = combo_a
                            highest_combo_team = "A"
                    combo_a = 0

                else:
                    if combo_b >= 10:
                        combo_counter += 1
                        if combo_b >= highest_combo:
                            highest_combo = combo_b
                            highest_combo_team = "B"
                    combo_b = 0

        return combo_counter, highest_combo_team, highest_combo
    
    def zadanie_2_4(selfs):
        # Napisz program, który znajdzie i wypisze te pary liczb z pliku `pary.txt`, które odpowiadają numerom punktów x i y takich, że z punktu o numerze x można przejść po jednej lub wielu strzałkach (zawsze zgodnie z ich zwrotami) do punktu o numerze y.
        with open("pary.txt", "r") as file:
            numbers = list(map(int, file.read().split()))

        pairs = []

        for i in range(len(numbers) // 2):
            if get_from_x_to_y(numbers[i*2], numbers[i*2+1]):
                pairs.append(f"{numbers[i*2]} {numbers[i*2+1]}")

        return "\n".join(pairs)
    
    def zadanie_3_2(selfs):
        # Podaj, ile liczb z pliku liczby.txt po pomniejszeniu o 1 daje liczbę pierwszą.
        with open("liczby.txt", "r") as file:
            numbers = list(map(int, file.read().split()))

        counter = 0

        for number in numbers:
            if is_prime(number - 1) == True:
                counter += 1

        return counter
    
    def zadanie_3_3(selfs):
        # Podaj:
        # - liczbę, która ma najwięcej różnych rozkładów na sumę dwóch liczb pierwszych, oraz liczbę takich rozkładów
        # - liczbę, która ma najmniej różnych rozkładów na sumę dwóch liczb pierwszych, oraz liczbę takich rozkładów.
        with open("liczby.txt", "r") as file:
            numbers = list(map(int, file.read().split()))

        primes = []
        for i in range(max(numbers)):
            if is_prime(i) == True:
                primes.append(i)

        sum_of_two_primes = {}

        for number in numbers:
            temp = 0
            for prime in primes:
                if prime >= (number // 2) + 1:
                    break
                if is_prime(number - prime) == True:
                    temp += 1
            sum_of_two_primes[number] = temp

        return max(sum_of_two_primes, key=sum_of_two_primes.get), sum_of_two_primes[max(sum_of_two_primes, key=sum_of_two_primes.get)], min(sum_of_two_primes, key=sum_of_two_primes.get), sum_of_two_primes[min(sum_of_two_primes, key=sum_of_two_primes.get)]
    
    def zadanie_3_4(selfs):
        # Dla każdej cyfry szesnastkowej podaj, ile razy występuje ona łącznie w zapisach szesnastkowych wszystkich liczb z pliku liczby.txt.")
        with open("liczby.txt") as file:
            numbers = [x[2:] for x in list(map(hex, list(map(int, file.read().split()))))]

        hex_chars = {
            "0" : 0, "1" : 0, "2" : 0, "3" : 0,
            "4" : 0, "5" : 0, "6" : 0, "7" : 0,
            "8" : 0, "9" : 0, "A" : 0, "B" : 0,
            "C" : 0, "D" : 0, "E" : 0, "F" : 0
        }

        chars, answer = [], []
        for number in numbers:
            for char in number:
                chars.append(char)

        for char in chars:
            for hex_char in hex_chars:
                if char.upper() == hex_char:
                    hex_chars[hex_char] += 1

        for key, value in hex_chars.items():
            answer.append(f"{key}: {value}")

        return "\n".join(answer)