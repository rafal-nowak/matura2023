def to_decimal(a):
    decimal = 0
    for i in range(len(str(a))):
        number = a % 10
        a //= 10
        decimal += number * 8 ** i
    return decimal

def is_first_equal_last(string_number: str) -> bool:
    return string_number[0] == string_number[-1]

class Matura2013Maj:
    def __init__(self):
        with open('dane.txt') as file:
            self.lines = [x.rstrip() for x in file.readlines()]

    def zadanie_6_1(self) -> int:
        number_of_same_digits = 0

        for number in self.lines:
           if is_first_equal_last(number):
               number_of_same_digits += 1

        return number_of_same_digits


    def zadanie_6_2(self) -> int:
        number_of_same_digits_decimal = 0

        for octal in self.lines:
            decimal_number = to_decimal(int(octal))
            if is_first_equal_last(str(decimal_number)):
                number_of_same_digits_decimal += 1

        return number_of_same_digits_decimal


    def zadanie_6_3(self):
        number_of_ascending_digits = 0
        biggest = 0
        smallest = int(self.lines[0])

        for number in self.lines:
            is_ascending = True
            for n in range(len(number) - 1):
                if number[n] > number[n + 1]:
                    is_ascending = False
                    break
            if is_ascending:
                number_of_ascending_digits += 1
                if (number := int(number)) > biggest:
                    biggest = number
                if number < smallest:
                    smallest = number

        return number_of_ascending_digits, biggest, smallest