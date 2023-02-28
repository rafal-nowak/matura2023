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
                number_string = str(number)
                image = ''
                for i in reversed(range(0, len(number_string))):
                    image = image+number_string[i]
                reflection.append(int(image))

            divided_by_17 = []
            for j in reflection:
                if j % 17 == 0:
                    divided_by_17.append(j)

        return divided_by_17

    def zadanie_4_2(selfs):
        with open('liczby.txt') as file:
            numbers = []
            for line in file:
                numbers.append(int(line))

            reflection = []

            for number in numbers:
                number_string = str(number)
                image = ''
                for i in reversed(range(0, len(number_string))):
                    image = image+number_string[i]
                reflection.append(int(image))

            max_difference = 0
            max_number = 0

            for x in range(len(numbers)):
                difference = numbers[x] - reflection[x]
                if int(math.fabs(difference)) > max_difference:
                    max_difference = int(math.fabs(difference))
                    max_number = numbers[x]

        return max_difference, max_number

    def zadanie_4_3(selfs):
        with open('liczby.txt') as file:
            numbers = []
            for line in file:
                numbers.append(int(line))

            reflection = []

            for number in numbers:
                number_string = str(number)
                image = ''
                for i in reversed(range(0, len(number_string))):
                    image = image+number_string[i]
                reflection.append(int(image))

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
        return prime_numbers

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

            two_times = 0
            three_times = 0

            for x in values:
                if values[x] == 2:
                    two_times += 1
                elif values[x] == 3:
                    three_times += 1

        return len(values), two_times, three_times
