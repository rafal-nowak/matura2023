class Matura2015Maj:
    def __init__(self):
        pass

    def zadanie4_1(self):

        # Podaj, ile liczb z pliku liczby.txt ma w swoim zapisie binarnym więcej zer niż jedynek.

        lines = open('liczby.txt', 'r').readlines()

        more_zeros_than_ones = 0

        for line in lines:
            ones = 0
            zeros = 0
            for digit in line:
                if digit == "0":
                    zeros += 1
                elif digit == "1":
                    ones += 1
            if zeros > ones:
                more_zeros_than_ones += 1

        return (more_zeros_than_ones)

    def zadanie4_2(self):

        # Podaj, ile liczb w pliku liczby.txt jest podzielnych przez 2 oraz ile liczb jest podzielnych przez 8.

        lines = open('liczby.txt', 'r').readlines()

        divisible_by_two = 0
        divisible_by_eight = 0

        for line in lines:
            number = int(line, 2)
            if number % 2 == 0:
                divisible_by_two += 1
            if number % 8 == 0:
                divisible_by_eight += 1

        return (divisible_by_two, divisible_by_eight)

    def zadanie4_3(self):

        # Znajdź najmniejszą i największą liczbę w pliku liczby.txt.
        # Jako odpowiedź podaj numery wierszy, w których się one znajdują.

        lines = open('liczby.txt', 'r').readlines()

        min_number = None
        max_number = None
        min_number_line = None
        max_number_line = None

        for i in range(len(lines)):
            number = int(lines[i], 2)
            if max_number == None or min_number == None:
                max_number, min_number = number, number
            else:
                if number > max_number:
                    max_number = number
                    max_number_line = i + 1
                if number < min_number:
                    min_number = number
                    min_number_line = i + 1

        return (min_number_line, max_number_line)
