from math import sqrt


if __name__ == '__main__':
    f = open("punkty.txt", "r").readlines()

    # Ile jest punktów, których obie współrzędne są liczbami pierwszymi?

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

    print()
    print("1.")
    print(f'Jest {PrimeNum} par liczb pierwszych')
    print()

    # Dwie liczby są cyfropodobne, jeżeli do zapisania każdej z nich wykorzystujemy takie same
    # cyfry dziesiętne.
    # Podaj ile jest punktów, których współrzędne są cyfropodobne.

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

    print()
    print("2")
    print(f'Jest {n} par liczb cyfropodobnych')
    print()


    # Znajdź najbardziej oddalone od siebie punkty. Podaj współrzędne znalezionych punktów oraz
    # odległość między nimi zaokrągloną do liczby całkowitej.

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

    print()
    print("3.")
    print(f'Największa odległość między punktami to {lenght}')
    print(f'Współrzędne pierwszego punktu to ({XA},{YA})')
    print(f'Współrzędne drugiego punktu to ({XB},{YB})')
    print()


    # Długość boku kwadratu K równa się 10000. Środek symetrii tego kwadratu znajduje się
    # w początku układu współrzędnych XY, a jego boki są równoległe do osi układu. Podaj liczbę
    # punktów, które leżą odpowiednio:
    # a. wewnątrz kwadratu K (bez jego boków),
    # b. na bokach kwadratu K,
    # c. na zewnątrz kwadratu K (bez jego boków).

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

    print()
    print("4")
    print(f'Na zewnątrz kwadratu znajduje się {outside} punktów')
    print(f'W środku kwadratu znajduje się {inside} punktów')
    print(f'Na boku kwadratu leżą {edge} punkty')
    print()
