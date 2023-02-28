
import math

if __name__ == "__main__":
    with open("liczby.txt", "r") as file:
        numbers = []
        for line in file:
            numbers.append(int(line))

    reflection = []

    for number in numbers:
        number_string = str(number)
        image = ''
        for i in reversed(range(0, len(number_string))):
            image = image + number_string[i]
        reflection.append(int(image))

    divided_by_17 = []
    for j in reflection:
        if j % 17 == 0:
            divided_by_17.append(j)

    print()
    print('################################################################################')
    print('Podaj odbicia liczb z pliku liczby.txt, które sa podzielne przez 17.')
    print()
    print(f'W pliku odbicia liczb podzielne przez 17 to:  {divided_by_17}.')
    print('################################################################################')
    print()

    max_difference = 0
    max_number = 0

    for x in range(len(numbers)):
        difference = numbers[x] - reflection[x]
        if int(math.fabs(difference)) > max_difference:
            max_difference = int(math.fabs(difference))
            max_number = numbers[x]

    print()
    print('################################################################################')
    print('Wyznacz taka liczbe n, dla ktorej wartosc bezwzgledna roznicy tej liczby i jej odbicia jest najwieksza.')
    print()
    print(
        f'Najwieksza liczba to {max_number} a wartosc bezwzgledna roznicy jej i jej odbicia to {max_difference} ')
    print('################################################################################')
    print()

    prime_numbers = []
    for a in range(len(numbers)):
        value1 = 0
        for z in range(2, numbers[a] - 1):
            if numbers[a] % z == 0:
                value1 += 1
        if value1 == 0:
            value2 = 0
            for b in range(2, reflection[a]):
                if reflection[a] % b == 0:
                    value2 += 1
            if value2 == 0:
                prime_numbers.append(numbers[a])

    print()
    print('################################################################################')
    print('Wypisz wszystkie liczby pierwsze z pliku liczby.txt, ktorych odbicia rowniez sa liczbami pierwszymi.')
    print()
    print(f'Liczby pierwsze: {prime_numbers}')
    print('################################################################################')
    print()

    values = {}

    for i in numbers:
        if i in values:
            values[i] += 1
        else:
            values[i] = 1

    two_times = 0
    three_times = 0

    for x in values:
        if values[x] == 2:
            two_times += 1
        elif values[x] == 3:
            three_times += 1

    print()
    print('################################################################################')
    print('Podaj:')
    print('- ile roznych liczb zapisano w pliku liczby.txt')
    print('- ile liczb powtarza sie dokladnie dwa razy w pliku liczby.txt')
    print('- ile liczb powtarza sie dokladnie trzy razy w pliku liczby.txt')
    print()
    print(f'Ilosc roznych liczb w pliku: {len(values)}')
    print(f'Ilosc liczb powtarzajacych sie dwa razy: {two_times}')
    print(f'Ilosc liczb powtarzajacych sie trzy razy: {three_times}')
    print('################################################################################')
    print()
