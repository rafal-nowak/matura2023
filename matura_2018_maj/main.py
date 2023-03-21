if __name__ == '__main__':
    with open('sygnaly.txt', 'r') as file:
        signals = file.read().split()


    ##  Zadanie 1 ##

    # Naukowcy zauważyli, że po złączeniu dziesiątych liter co czterdziestego słowa
    # (zaczynając od słowa czterdziestego) otrzymamy pewne przesłanie. Wypisz to przesłanie.

    message_temp = []
    for i in range(39,len(signals),40):
        message_temp.append(signals[i][9])
    message = ''.join(message_temp)

    print()
    print('################################################################################')
    print('Naukowcy zauważyli, że po złączeniu dziesiątych liter co czterdziestego słowa (zaczynając od słowa czterdziestego) otrzymamy pewne przesłanie. Wypisz to przesłanie.')
    print(f'To przesłanie to {message}')
    print('################################################################################')
    print()

    ## Zadanie 2 ##

    # Znajdź słowo, w którym występuje największa liczba różnych liter.
    # Wypisz to słowo i liczbę występujących w nim różnych liter.
    # Jeśli słów o największej liczbie różnych liter jest więcej niż jedno,
    # wypisz pierwsze z nich pojawiające się w pliku z danymi

    def counting_different_letters(word):
        letter_set = set()
        for i in range(len(word)):
            letter_set.add(word[i])
        return len(letter_set)

    max_letter_number = 0
    max_letter_word = ''

    for i in range(len(signals)):
        if counting_different_letters(signals[i]) > max_letter_number:
            max_letter_word = signals[i]
            max_letter_number = counting_different_letters(signals[i])

    print()
    print('################################################################################')
    print('Znajdź słowo, w którym występuje największa liczba różnych liter.')
    print('Wypisz to słowo i liczbę występujących w nim różnych liter.')
    print('Jeśli słów o największej liczbie różnych liter jest więcej niż jedno, wypisz pierwsze z nich pojawiające się w pliku z danymi')
    print(f'To słowo to {max_letter_word}. Występuje w nim {max_letter_number} różnych liter')
    print('################################################################################')
    print()


    ## Zadanie 3 ##

    # W tym zadaniu rozważmy odległość liter w alfabecie –
    # np. litery A i B są od siebie oddalone o 1,A i E o 4,F i D o 2, a każda litera od siebie samej jest oddalona o 0.
    # Wypisz wszystkie słowa, w których każde dwie litery oddalone są od siebie w alfabecie co najwyżej o 10.
    # Słowa wypisz w kolejności występowania w pliku sygnaly.txt, po jednym w wierszu.

    def checking_if_distance_between_letters_greater_than_ten(word):
        min_letter_ord = 1000
        max_letter_ord = 0

        for i in range(len(word)):
            if ord(word[i]) > max_letter_ord:
                max_letter_ord = ord(word[i])
            if ord(word[i]) < min_letter_ord:
                min_letter_ord = ord(word[i])
        if max_letter_ord - min_letter_ord > 10:
            return False
        return True


    words = []

    for i in range(len(signals)):
        if checking_if_distance_between_letters_greater_than_ten(signals[i]) == True:
            words.append(signals[i])

    words = '\n'.join(words)

    print()
    print('################################################################################')
    print('Wypisz wszystkie słowa, w których każde dwie litery oddalone są od siebie w alfabecie co najwyżej o 10.')
    print('Słowa wypisz w kolejności występowania w pliku sygnaly.txt, po jednym w wierszu.')
    print(f'Te słowa to {words}')
    print('################################################################################')
    print()
