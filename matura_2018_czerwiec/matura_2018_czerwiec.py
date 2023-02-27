def is_even(number):
    if number % 2 == 0:
        return True
    return False


class Matura2018Czerwiec:
    def __init__(self):
        pass

    def zadanie_4_1(selfs):
        # Podaj, w ilu wierszach zapisane są ciągi, których ostatnia liczba jest taka sama

        number_of_equals = 0

        with open('dane1.txt', 'r') as file1, open('dane2.txt', 'r') as file2:

            lines1 = [line.rstrip() for line in file1]
            lines2 = [line.rstrip() for line in file2]

            for i in range(len(lines1)):
                line1 = lines1[i].split()
                line2 = lines2[i].split()
                if line1[len(line1) - 1] == line2[len(line2) - 1]:
                    number_of_equals += 1

            return number_of_equals

    def zadanie_4_2(selfs):
        # Podaj, ile jest par ciągów takich, że w jednym i drugim ciągu jest 5 liczb parzystych i 5 liczb nieparzystych

        number_of_strings = 0

        with open('dane1.txt', 'r') as file1, open('dane2.txt', 'r') as file2:

            lines1 = [line.rstrip() for line in file1]
            lines2 = [line.rstrip() for line in file2]

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

            return number_of_strings

    def zadanie_4_3(selfs):
        # Policz, ile jest par ciągów, które utworzone są z takich samych liczb. Liczba powtórzeń takich samych liczb w ciągach może być różna
        # Wypisz numery wierszy, w których takie prary ciągów się znajduje

        number_of_same_strings = 0
        row_of_strings = []

        with open('dane1.txt', 'r') as file1, open('dane2.txt', 'r') as file2:

            lines1 = [line.rstrip() for line in file1]
            lines2 = [line.rstrip() for line in file2]

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

            return number_of_same_strings, row_of_strings

    def zadanie_4_4(selfs):
        # Napisz program, który utworzy ciągi uporządkowane, będaące wynikiem scalenia ciągów
        # Liczby w ciągach wynikowych zapisz, rozdzielając je spacjami

        sorted_strings = ""

        with open('dane1.txt', 'r') as file1, open('dane2.txt', 'r') as file2:

            lines1 = [line.rstrip() for line in file1]
            lines2 = [line.rstrip() for line in file2]

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

            return sorted_strings
