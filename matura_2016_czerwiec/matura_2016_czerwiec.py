class Matura2016Czerwiec:
    def __init__(self):
        pass

    def zadanie_6_1(selfs):
        with open('liczby.txt') as file:
            counter_of_octal_numbers = 0

            lines = [line.rstrip() for line in file]

            for line in lines:
                if line[-1] == '8':
                    counter_of_octal_numbers += 1

            return counter_of_octal_numbers
    
    def zadanie_6_2(selfs):
        with open('liczby.txt') as file:
            good_quaternary_numbers = 0

            lines = [line.rstrip() for line in file]

            for line in lines:
                if line[-1] == '4' and line[:-1].count('0') == 0:
                    good_quaternary_numbers += 1

            return good_quaternary_numbers

    def zadanie_6_3(selfs):
        with open('liczby.txt') as file:
            good_binary_numbers = 0

            lines = [line.rstrip() for line in file]

            for line in lines:
                if line[-1] == '2' and line[-2] == '0':
                    good_binary_numbers += 1
            
            return good_binary_numbers

    def zadanie_6_4(selfs):
        with open('liczby.txt') as file:
            sum_of_decimal_numbers = 0
            decimal_numbers = []

            lines = [line.rstrip() for line in file]

            for line in lines:
                if line[-1] == '8':
                    decimal = 0
                    for i in range(len(line[:-1])):
                        a = int(line[len(line)-2-i])
                        for j in range(i):
                            a*=8
                        decimal += a
                    decimal_numbers.append(decimal)
            
            sum_of_decimal_numbers = sum(decimal_numbers)

            return sum_of_decimal_numbers

    def zadanie_6_5(selfs):
        with open('liczby.txt') as file:
            decimal_numbers = []

            lines = [line.rstrip() for line in file]

            for line in lines:
                decimal = 0
                for i in range(len(line[:-1])):
                    a = int(line[len(line)-2-i])
                    for j in range(i):
                        a*=int(line[-1])
                    decimal += a
                decimal_numbers.append(decimal)

            min_num = decimal_numbers[0]
            min_num_index = 0
            max_num = decimal_numbers[0]
            max_num_index = 0

            for i in range(len(decimal_numbers)):
                if decimal_numbers[i] < min_num:
                    min_num = decimal_numbers[i]
                    min_num_index = i
                if decimal_numbers[i] > max_num:
                    max_num = decimal_numbers[i]
                    max_num_index = i
            
            return lines[max_num_index], max_num, lines[min_num_index], min_num