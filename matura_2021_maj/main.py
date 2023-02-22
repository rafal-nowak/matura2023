if __name__ == '__main__':
    lines = open('instrukcje.txt', 'r').readlines()

    # Oblicz całkowitą długość napisu po wykonaniu wszystkich instrukcji z pliku instrukcje.txt

    text_length = 0

    lines = open('instrukcje.txt', 'r').readlines()

    for line in lines:
        if line.split()[0] == "DOPISZ":
            text_length += 1
        elif line.split()[0] == "USUN":
            text_length -= 1

    print()
    print('################################################################################')
    print('Oblicz całkowitą długość napisu po wykonaniu wszystkich instrukcji z pliku instrukcje.txt')
    print(f'Długość napisu to {text_length}')
    print('################################################################################')
    print()

    # Znajdź najdłuższy ciąg występujących kolejno po sobie instrukcji tego samego rodzaju.
    # Jako odpowiedź podaj rodzaj instrukcji oraz długość tego ciągu. Istnieje tylko jeden taki ciąg

    max_type = None
    max_length = 0
    length_now = 1
    last_type = None

    for line in lines:
        type = line.split()[0]
        if type == last_type:
            length_now += 1
        else:
            length_now = 1
        last_type = type
        if length_now > max_length:
            max_type = type
            max_length = length_now

    print()
    print('################################################################################')
    print('Znajdź najdłuższy ciąg występujących kolejno po sobie instrukcji tego samego rodzaju.')
    print('Jako odpowiedź podaj rodzaj instrukcji oraz długość tego ciągu. Istnieje tylko jeden taki ciąg.')
    print(f'Najdłużej występującym po sobię ciągiem instrukcji jest ciąg instrukcji {max_type}. Jego długość wynosi {max_length}')
    print('################################################################################')
    print()

    # Oblicz, która litera jest najczęściej dopisywana (najczęściej występuje w instrukcji DOPISZ).
    # Podaj tę literę oraz ile razy jest dopisywana. Istnieje tylko jedna taka litera.

    letters = {}

    for line in lines:

        type, letter = line.split()

        if type == "DOPISZ":
            if letter in letters:
                letters[letter] += 1
            else:
                letters[letter] = 1


    letter, additions = (max(letters, key=letters.get), max(letters.values()))

    print()
    print('################################################################################')
    print('Oblicz, która litera jest najczęściej dopisywana (najczęściej występuje w instrukcji DOPISZ).')
    print('Podaj tę literę oraz ile razy jest dopisywana. Istnieje tylko jedna taka litera.')
    print(f'Najczęściej dopisywaną literą jest {letter}. Jest ona dopisywana {additions} razy')
    print('################################################################################')
    print()

    # Podaj napis, który powstanie po wykonaniu wszystkich instrukcji z pliku instrukcje.txt.

    word = ""

    for line in lines:

        type, letter = line.split()

        if type == "DOPISZ":
            word += letter

        elif type == "ZMIEN":
            word = word[:-1]
            word += letter

        elif type == "USUN":
            word = word[:-1]

        elif type == "PRZESUN":
            if letter != "Z":
                word = word.replace(letter, chr(ord(letter) + 1), 1)
            else:
                word = word.replace(letter, "A", 1)

    print()
    print('################################################################################')
    print('Podaj napis, który powstanie po wykonaniu wszystkich instrukcji z pliku instrukcje.txt.')
    print(f'Ten napis to {word}.')
    print('################################################################################')
    print()