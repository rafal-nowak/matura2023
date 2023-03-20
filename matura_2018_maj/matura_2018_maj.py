class Matura2018Maj:
    def __init__(self):
        pass

    def zadanie_4_1(selfs):
        # Naukowcy zauważyli, że po złączeniu dziesiątych liter co czterdziestego słowa
        # (zaczynając od słowa czterdziestego) otrzymamy pewne przesłanie. Wypisz to przesłanie.

        with open('sygnaly.txt', 'r') as file:
            signals = file.read().split()

        message_temp = []
        for i in range(39, len(signals), 40):
            message_temp.append(signals[i][9])
        message = ''.join(message_temp)

        return message

    def zadanie_4_2(selfs):
        # Znajdź słowo, w którym występuje największa liczba różnych liter.
        # Wypisz to słowo i liczbę występujących w nim różnych liter.
        # Jeśli słów o największej liczbie różnych liter jest więcej niż jedno,
        # wypisz pierwsze z nich pojawiające się w pliku z danymi

        with open('sygnaly.txt', 'r') as file:
            signals = file.read().split()

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

        return max_letter_word, max_letter_number

    def zadanie_4_3(selfs):
        # W tym zadaniu rozważmy odległość liter w alfabecie –
        # np. litery A i B są od siebie oddalone o 1,A i E o 4,F i D o 2, a każda litera od siebie samej jest oddalona o 0.
        # Wypisz wszystkie słowa, w których każde dwie litery oddalone są od siebie w alfabecie co najwyżej o 10.
        # Słowa wypisz w kolejności występowania w pliku sygnaly.txt, po jednym w wierszu.

        with open('sygnaly.txt', 'r') as file:
            signals = file.read().split()

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
            if checking_if_distance_between_letters_greater_than_ten(signals[i]):
                words.append(signals[i])

        return words
