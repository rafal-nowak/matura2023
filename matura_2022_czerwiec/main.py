
import math

if __name__ == "__main__":
    with open("liczby.txt", "r") as file:
        numbers = []
        for line in file:
            numbers.append(int(line))

    reflection = []

    for number in numbers:
        numberString = str(number)
        image = ''
        for i in reversed(range(0, len(numberString))):
            image = image+numberString[i]
        reflection.append(int(image))

    dividedby17 = []
    for j in reflection:
        if j % 17 == 0:
            dividedby17.append(j)

    print()
    print('################################################################################')
    print('Podaj odbicia liczb z pliku liczby.txt, które sa podzielne przez 17.')
    print()
    print(f'W pliku odbicia liczb podzielne przez 17 to:  {dividedby17}.')
    print('################################################################################')
    print()

    maxdifference = 0
    maxnumber = 0

    for x in range(len(numbers)):
        difference = numbers[x] - reflection[x]
        if int(math.fabs(difference)) > maxdifference:
            maxdifference = int(math.fabs(difference))
            maxnumber = numbers[x]

    print()
    print('################################################################################')
    print('Wyznacz taka liczbe n, dla ktorej wartosc bezwzgledna roznicy tej liczby i jej odbicia jest najwieksza.')
    print()
    print(
        f'Najwieksza liczba to {maxnumber} a wartosc bezwzgledna roznicy jej i jej odbicia to {maxdifference} ')
    print('################################################################################')
    print()

    primeNumbers = []
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
                primeNumbers.append(numbers[a])

    print()
    print('################################################################################')
    print('Wypisz wszystkie liczby pierwsze z pliku liczby.txt, ktorych odbicia rowniez sa liczbami pierwszymi.')
    print()
    print(f'Liczby pierwsze: {primeNumbers}')
    print('################################################################################')
    print()

    values = {}

    for i in numbers:
        if i in values:
            values[i] += 1
        else:
            values[i] = 1

    twoTimes = 0
    threeTimes = 0

    for x in values:
        if values[x] == 2:
            twoTimes += 1
        elif values[x] == 3:
            threeTimes += 1

    print()
    print('################################################################################')
    print('Podaj:')
    print('- ile roznych liczb zapisano w pliku liczby.txt')
    print('- ile liczb powtarza sie dokladnie dwa razy w pliku liczby.txt')
    print('- ile liczb powtarza sie dokladnie trzy razy w pliku liczby.txt')
    print()
    print(f'Ilosc roznych liczb w pliku: {len(values)}')
    print(f'Ilosc liczb powtarzajacych sie dwa razy: {twoTimes}')
    print(f'Ilosc liczb powtarzajacych sie trzy razy: {threeTimes}')
    print('################################################################################')
    print()
