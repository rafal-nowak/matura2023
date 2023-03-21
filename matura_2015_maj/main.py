if __name__ == '__main__':
    lines = open('liczby.txt', 'r').readlines()

    # Podaj, ile liczb z pliku liczby.txt ma w swoim zapisie binarnym więcej zer niż jedynek.

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

    print()
    print('################################################################################')
    print('Podaj, ile liczb ma w swoim zapisie binarnym więcej zer niż jedynek ')
    print(f'Liczb, które w zapisie mają więcej zer niż jedynek jest {more_zeros_than_ones}')
    print('################################################################################')
    print()

    # Podaj, ile liczb w pliku liczby.txt jest podzielnych przez 2 oraz ile liczb jest podzielnych przez 8.

    divisible_by_two = 0
    divisible_by_eight = 0

    for line in lines:
        number = int(line, 2)
        if number % 2 == 0:
            divisible_by_two += 1
        if number % 8 == 0:
            divisible_by_eight += 1

    print()
    print('################################################################################')
    print('Podaj, ile liczb w pliku liczby.txt jest podzielnych przez 2 oraz ile liczb jest podzielnych przez 8.')
    print(f'Przez 2 podzielnych jest {divisible_by_two} liczb, a przez 8 podzielnych jest {divisible_by_eight} liczb')
    print('################################################################################')
    print()

    # Znajdź najmniejszą i największą liczbę w pliku liczby.txt.
    # Jako odpowiedź podaj numery wierszy, w których się one znajdują.

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

    print()
    print('################################################################################')
    print('Znajdź najmniejszą i największą liczbę w pliku liczby.txt.')
    print('Jako odpowiedź podaj numery wierszy, w których się one znajdują.')
    print(f'Najmniejsza liczba znajduje się w wierszu numer {min_number_line}, a największa w wierszu numer {max_number_line}')
    print('################################################################################')
    print()
