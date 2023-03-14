with open('sygnaly.txt', 'r') as file:
    signals = file.read().split()


##  Zadanie 1 ##

# Naukowcy zauważyli, że po złączeniu dziesiątych liter co czterdziestego słowa
# (zaczynając od słowa czterdziestego) otrzymamy pewne przesłanie. Wypisz to przesłanie.

answer1_temp = []
for i in range(39,len(signals),40):
    answer1_temp.append(signals[i][9])
answer1 = ''.join(answer1_temp)

print("Zadanie 1\n")
print("Odpowiedź do zadania:")
print(answer1)
print("\n\n")

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

max_letter_number  = 0
max_letter_word = ''

for i in range(len(signals)):
    if counting_different_letters(signals[i]) > max_letter_number:
        max_letter_word = signals[i]
        max_letter_number = counting_different_letters(signals[i])

answer2 = "{0} {1}".format(max_letter_word, max_letter_number)

print("Zadanie 2\n")
print("Odpowiedź do zadania:")
print(answer2)
print("\n\n")


## Zadanie 3 ##

# W tym zadaniu rozważmy odległość liter w alfabecie –
# np. litery A i B są od siebie oddalone o 1,A i E o 4,F i D o 2, a każda litera od siebie samej jest oddalona o 0.
# Wypisz wszystkie słowa, w których każde dwie litery oddalone są od siebie w alfabecie co najwyżej o 10.
# Słowa wypisz w kolejności występowania w pliku sygnaly.txt, po jednym w wierszu.

def checking_if_distance_between_letters_greater_than_ten(word):
    truth = 1
    min_letter_ord = 1000
    max_letter_ord = 0

    for i in range(len(word)):
        if ord(word[i]) > max_letter_ord:
            max_letter_ord = ord(word[i])
        if ord(word[i]) < min_letter_ord:
            min_letter_ord = ord(word[i])
    if max_letter_ord - min_letter_ord > 10:
        truth = 0
    return truth


answer3_temp = []

for i in range(len(signals)):
    if checking_if_distance_between_letters_greater_than_ten(signals[i]) == 1:
        answer3_temp.append(signals[i])

answer3 = '\n'.join(answer3_temp)
print("Zadanie 3\n")
print("Odpowiedź do zadania:")
print(answer3)
print('\n\n')
print(answer3_temp)
