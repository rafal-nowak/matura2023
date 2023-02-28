import math


class Matura2022Czerwiec:
    def __init__(self):
        pass

    def zadanie_4_1(selfs):
        with open('liczby.txt') as file:
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

        return dividedby17

    def zadanie_4_2(selfs):
        with open('liczby.txt') as file:
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

            maxdifference = 0
            maxnumber = 0

            for x in range(len(numbers)):
                difference = numbers[x] - reflection[x]
                if int(math.fabs(difference)) > maxdifference:
                    maxdifference = int(math.fabs(difference))
                    maxnumber = numbers[x]

        return maxdifference, maxnumber

    def zadanie_4_3(selfs):
        with open('liczby.txt') as file:
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
        return primeNumbers

    def zadanie_4_4(selfs):
        with open('liczby.txt') as file:
            numbers = []
            for line in file:
                numbers.append(int(line))

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

        return len(values), twoTimes, threeTimes
