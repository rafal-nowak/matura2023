if __name__ == '__main__':
    with open('liczby.txt') as file:
        counter_of_octal_numbers = 0

        lines = [line.rstrip() for line in file]

        for line in lines:
            if line[-1] == '8':
                counter_of_octal_numbers += 1
        print()
        print('################################################################################')
        print('Podaj, ile liczb w pliku liczby.txt zapisano w systemie ósemkowym.')
        print(f'istnieje {counter_of_octal_numbers} takich liczb')
        print('################################################################################')
        print()

    with open('liczby.txt') as file:
        good_quaternary_numbers = 0

        lines = [line.rstrip() for line in file]

        for line in lines:
            if line[-1] == '4' and line[:-1].count('0') == 0:
                good_quaternary_numbers += 1

        print()
        print('################################################################################')
        print('Podaj, ile wierszy w pliku liczby.txt zawiera liczby zapisane w systemie czwórkowym takie, że w ich zapisie nie występuje cyfra 0')
        print(f'istnieje {good_quaternary_numbers} takich wierszy')
        print('################################################################################')
        print()

    with open('liczby.txt') as file:
        good_binary_numbers = 0

        lines = [line.rstrip() for line in file]

        for line in lines:
            if line[-1] == '2' and line[-2] == '0':
                good_binary_numbers += 1
        
        print()
        print('################################################################################')
        print('Podaj, ile wierszy w pliku liczby.txt zawiera liczby parzyste zapisane w systemie dwójkowym.')
        print(f'istnieje {good_binary_numbers} takich wierszy')
        print('################################################################################')
        print()

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
        
        print()
        print('################################################################################')
        print('Podaj sumę wszystkich liczb z pliku liczby.txt, które zapisano w systemie ósemkowym. Wynik podaj w systemie dziesiętnym.')
        print(f'suma ta wynosi {sum_of_decimal_numbers}')
        print('################################################################################')
        print()

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
        
        print()
        print('################################################################################')
        print('Podaj kod największej oraz kod najmniejszej spośród liczb zakodowanych w pliku liczby.txt oraz ich wartości w systemie dziesiętnym. ')
        print(f'kod najwiekszej liczby to {lines[max_num_index]} i wynosi ona {max_num}')
        print(f'kod najmniejszej liczby to {lines[min_num_index]} i wynosi ona {min_num}')
        print('################################################################################')
        print()
