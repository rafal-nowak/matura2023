def is_even(number):
    if number % 2 == 0:
        return True
    return False


if __name__ == '__main__':
    with open('dane1.txt', 'r') as file1, open('dane2.txt', 'r') as file2:

        lines1 = [line.rstrip() for line in file1]
        lines2 = [line.rstrip() for line in file2]
        print(lines1)
        print(lines2)

        # Podaj, w ilu wierszach zapisane są ciągi, których ostatnia liczba jest taka sama

        number_of_equals = 0
        for i in range(len(lines1)):
            line1 = lines1[i].split()
            line2 = lines2[i].split()
            if line1[len(line1) - 1] == line2[len(line2) - 1]:
                number_of_equals += 1

        print()
        print('################################################################################')
        print('Podaj, w ilu wierszach zapisane są ciągi, których ostatnia liczba jest taka sama')
        print(f'Liczba wierszy to {number_of_equals}')
        print('################################################################################')
        print()

        # Podaj, ile jest par ciągów takich, że w jednym i drugim ciągu jest 5 liczb parzystych i 5 liczb nieparzystych

        number_of_strings = 0

        for i in range(len(lines1)):
            number_of_odds_line1 = 0
            number_of_even_line1 = 0
            number_of_odds_line2 = 0
            number_of_even_line2 = 0
            line1 = lines1[i].split()
            line2 = lines2[i].split()
            for number in line1:
                if is_even(int(number)):
                    number_of_even_line1 += 1
                else:
                    number_of_odds_line1 += 1
            for number in line2:
                if is_even(int(number)):
                    number_of_even_line2 += 1
                else:
                    number_of_odds_line2 += 1
            if number_of_even_line1 == 5 and number_of_odds_line1 == 5 and number_of_even_line2 == 5 and number_of_odds_line2 == 5:
                number_of_strings += 1

        print()
        print('################################################################################')
        print(
            'Podaj, ile jest par ciągów takich, że w jednym i drugim ciągu jest 5 liczb parzystych i 5 liczb nieparzystych')
        print(f'Liczba takich par to {number_of_strings}')
        print('################################################################################')
        print()

        # Policz, ile jest par ciągów, które utworzone są z takich samych liczb. Liczba powtórzeń takich samych liczb w ciągach może być różna
        # Wypisz numery wierszy, w których takie prary ciągów się znajduje

        number_of_same_strings = 0
        row_of_strings = []

        for i in range(len(lines1)):
            numbers1 = lines1[i].split()
            numbers2 = lines2[i].split()
            numbers_in_line1 = set()
            numbers_in_line2 = set()
            for number in numbers1:
                numbers_in_line1.add(number)
            for number in numbers2:
                numbers_in_line2.add(number)
            if numbers_in_line1 == numbers_in_line2:
                number_of_same_strings += 1
                row_of_strings.append(i + 1)

        print()
        print('################################################################################')
        print(
            'Policz, ile jest par ciągów, które utworzone są z takich samych liczb. Liczba powtórzeń takich samych liczb w ciągach może być różna')
        print('Wypisz numery wierszy, w których takie prary ciągów się znajduje')
        print(f'Istnieje {number_of_same_strings} takich par ciągów')
        print(f'Numery tych wierszy to {row_of_strings}')
        print('################################################################################')
        print()

        # Napisz program, który utworzy ciągi uporządkowane, będaące wynikiem scalenia ciągów
        # Liczby w ciągach wynikowych zapisz, rozdzielając je spacjami
        sorted_strings = ""
        for i in range(len(lines1)):
            sorted_string = ""
            numbers1 = lines1[i].split()
            numbers2 = lines2[i].split()
            position_in_numbers1 = 0
            position_in_numbers2 = 0
            while True:
                if numbers1[0] <= numbers2[0]:
                    sorted_string += f'{numbers1[0]} '
                    position_in_numbers1 += 1
                    numbers1.pop(0)
                elif numbers1[0] > numbers2[0]:
                    sorted_string += (f'{numbers2[0]} ')
                    position_in_numbers2 += 1
                    numbers2.pop(0)
                if position_in_numbers1 > (len(numbers1)):
                    for number in numbers2:
                        sorted_string += (f'{number} ')
                    break
                elif position_in_numbers2 > (len(numbers2)):
                    for number in numbers1:
                        sorted_string += (f'{number} ')
                    break
            sorted_strings += (f'{sorted_string}\n')

        print()
        print('################################################################################')
        print('Napisz program, który utworzy ciągi uporządkowane, będaące wynikiem scalenia ciągów')
        print('Liczby w ciągach wynikowych zapisz, rozdzielając je spacjami')
        print(f'{sorted_strings}')
        print('################################################################################')
        print()
