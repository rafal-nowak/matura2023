from math import sqrt

class Matura2017Czerwiec :
    def __init__(self):
        pass

    def zadanie_4_1(selfs):

        # Ile jest punktów, których obie współrzędne są liczbami pierwszymi?

        f = open("punkty.txt", "r").readlines()

        PrimeNum = 0

        for line in f:
            num = line.split()
            prime_flagA = 0
            prime_flagB = 0
            for i in range(2, int(sqrt(int(num[0]))) + 1):
                if (int(num[0]) % i == 0):
                    prime_flagA = 1
                    break
            for i in range(2, int(sqrt(int(num[1]))) + 1):
                if (int(num[1]) % i == 0):
                    prime_flagB = 1
                    break
            if prime_flagA == 0 and prime_flagB == 0:
                PrimeNum += 1

        return PrimeNum

    def zadanie_4_2(selfs):

        # Dwie liczby są cyfropodobne, jeżeli do zapisania każdej z nich wykorzystujemy takie same
        # cyfry dziesiętne.
        # Podaj ile jest punktów, których współrzędne są cyfropodobne.
        f = open("punkty.txt", "r").readlines()

        n = 0
        for line in f:
            num = line.split()
            digitsA = []
            digitsB = []
            for x in num[0]:
                digitsA.append(x)
            for x in num[1]:
                digitsB.append(x)
            good = True
            for x in num[1]:
                if x not in digitsA:
                    good = False
                    break
            if good == True:
                for x in num[0]:
                    if x not in digitsB:
                        good = False
                        break
                if good == True:
                    n += 1

        return n

    def zadanie_4_3(selfs):

        # Znajdź najbardziej oddalone od siebie punkty. Podaj współrzędne znalezionych punktów oraz
        # odległość między nimi zaokrągloną do liczby całkowitej.

        f = open("punkty.txt", "r").readlines()

        answer = 0

        for line in f:
            num = line.split()
            x = int(num[0])
            y = int(num[1])
            for lineb in f:
                numb = lineb.split()
                x2 = int(numb[0])
                y2 = int(numb[1])
                lenght = int(sqrt((x - x2) * (x - x2) + (y - y2) * (y - y2)))
                if lenght > answer:
                    answer = lenght
                    XA = x
                    YA = y
                    XB = x2
                    YB = y2

        return answer, XA, YA, XB, YB,

    def zadanie_4_4(selfs):

        # Długość boku kwadratu K równa się 10000. Środek symetrii tego kwadratu znajduje się
        # w początku układu współrzędnych XY, a jego boki są równoległe do osi układu. Podaj liczbę
        # punktów, które leżą odpowiednio:
            # a. wewnątrz kwadratu K (bez jego boków),
            # b. na bokach kwadratu K,
            # c. na zewnątrz kwadratu K (bez jego boków).

        f = open("punkty.txt", "r").readlines()

        inside = 0
        edge = 0
        outside = 0

        for line in f:
            num = line.split()
            x = int(num[0])
            y = int(num[1])
            if x > 5000 or y > 5000:
                outside += 1
            elif x == 5000 and y < 5000 or y == 5000 and x < 5000:
                edge += 1
            else:
                inside += 1

        return inside, outside, edge

