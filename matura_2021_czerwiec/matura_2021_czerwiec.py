def is_palindrome(string):
    return string == string[::-1]

class Matura2021Czerwiec:
    def __init__(self):
        pass

    def zadanie_4_1(selfs):
        # Podaj łączną liczbę cyfr we wszystkich napisach z pliku napisy.txt.
        with open("napisy.txt", "r") as file:
            texts = file.read()

        digits_in_file = []

        for char in texts:
            if char.isdigit() == True:
                digits_in_file.append(char)
        
        return len(digits_in_file)
    
    def zadanie_4_2(selfs):
        # W pliku napisy.txt ukryto pewne pięćdziesięcioznakowe hasło w następujący sposób:
        # - w co dwudziestym wierszu (w wierszach o numerach 20, 40, 60, ..., 1000), ukryto dokładnie jedną literę hasła;
        # - ukryta litera w kolejnych wierszach zawsze znajduje się na innej pozycji: w 20 wierszu na pierwszej, w 40 wierszu na drugiej, w 60 wierszu na trzeciej, ..., w 1000 na pięćdziesiątej.
        # Podaj to hasło.
        with open("napisy.txt", "r") as file:
                texts = file.read()
                texts_split = texts.split()

        phrase = []

        j = 0
        for i in range(len(texts_split)):
            if (i+1)%20 == 0:
                phrase.append(texts_split[i][j])
                j += 1 
        return "".join(phrase)
    
    def zadanie_4_3(selfs):
        # Palindromem nazywamy napis, który czytany od początku lub od końca jest taki sam (np. KAJAK). Część napisów zapisanych w wierszach pliku (każdy ma 50 znaków) można w prosty sposób – przez dodanie dokładnie jednego znaku na początku lub na końcu napisu – zamienić na palindrom. Podaj hasło utworzone przez środkowe litery tak utworzonych palindromów.
        with open("napisy.txt", "r") as file:
                texts = file.read()
                texts_split = texts.split()

        phrase_from_middle_letters_of_palindrome = []

        for text in texts_split:
            if is_palindrome(text[1:]):
                phrase_from_middle_letters_of_palindrome.append(text[25])
            elif is_palindrome(text[:len(text)-1]):
                phrase_from_middle_letters_of_palindrome.append(text[24])
        return "".join(phrase_from_middle_letters_of_palindrome)

    def zadanie_4_4(selfs):
        # Ostatnie z haseł zostało ukryte w cyfrach zapisanych w pliku napisy.txt. Aby je odczytać, należy cyfry z każdego wiersza pogrupować po dwie, pomijając ostatnią, jeśli w wierszu jest nieparzysta liczba cyfr. Jeżeli liczba utworzona przez parę cyfr jest mniejsza od 65 lub większa od 90, to ją pomijamy, w przeciwnym przypadku taką liczbę zamieniamy na znak o kodzie ASCII odpowiadającym tej liczbie. Poszukiwanie hasła kończy się po otrzymaniu trzech kolejnych znaków „X”. Odczytaj z pliku tak ukryte hasło.
        with open("napisy.txt", "r") as file:
                texts = file.read()
                texts_split = texts.split()
        numbers_only = [[] for i in range(1000)]
        pairs, phrase_ending_with_x = [], []

        for i in range(len(texts_split)):
            for j in range(len(texts_split[i])):
                if texts_split[i][j].isdigit() == True:
                    numbers_only[i].append(texts_split[i][j])

        for i in range(len(numbers_only)):
            if len(numbers_only[i]) % 2 == 1:
                numbers_only[i].pop()

        for i in range(len(numbers_only)):
            for j in range(0, len(numbers_only[i]), 2):
                pairs.append(numbers_only[i][j] + numbers_only[i][j+1])
            
        for pair in pairs:
            if phrase_ending_with_x[-3:] == ["X", "X", "X"]:
                break
            pair = int(pair)
            if pair >=65 and pair <= 90:
                phrase_ending_with_x.append(chr(pair))

        return "".join(phrase_ending_with_x)
