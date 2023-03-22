def to_decimal(a):
    decimal = 0
    for i in range(len(str(a))):
        number = a % 10
        a //= 10
        decimal += number * 8 ** i
    return decimal

def is_first_equal_last(string_number: str) -> bool:
    return string_number[0] == string_number[-1]

if __name__ == "__main__":
    with open('dane.txt') as file:
        self.lines = [x.rstrip() for x in file.readlines()]


    # Podaj ilość liczb, których pierwsza cyfra jest równa ostatniej

    number_of_same_digits = 0
    for number in lines:
       if is_first_equal_last(number):
           number_of_same_digits += 1

    print("##################################################")
    print(f"Pierwsza cyfra jest równa ostatniej w {number_of_same_digits} liczbach")
    print("##################################################\n\n")


    # Podaj ilość liczb, których pierwsza cyfra jest równa ostatniej w systemie dziesiętnym

    number_of_same_digits_decimal = 0
    for octal in lines:
        decimal_number = to_decimal(int(octal))
        if is_first_equal_last(str(decimal_number)):
            number_of_same_digits_decimal += 1

    print("##################################################")
    print(f"Pierwsza cyfra jest równa ostatniej w {number_of_same_digits_decimal} liczbach dziesiętnych")
    print("##################################################\n\n")


    # Ile jest liczb których cyfry ułożone są w porządku niemalejącym
    # Podaj ich liczbę, największą i najmniejszą z nich

    number_of_ascending_digits = 0
    biggest = 0
    smallest = int(lines[0])
    for number in lines:
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

    print("##################################################")
    print(f'Liczba przypadkow cyfr niemalejących: {number_of_ascending_digits}')
    print('Najwieksza z nich jest równa', biggest)
    print('Najmniejsza z nich jest równa', smallest)
    print("##################################################\n\n")