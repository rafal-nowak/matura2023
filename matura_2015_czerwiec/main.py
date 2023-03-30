def CyfraKontrolna(N):
    Odd = 0
    Even = 0

    for i in range(0, len(N), 2):
        Odd += int(N[i])

    for i in range(1, len(N), 2):
        Even += int(N[i])
    
    return (10-((Odd+(Even*3))%10))%10

with open('kody.txt') as file:
    lines = [line.rstrip() for line in file]

    print()
    print('################################################################################')
    print('dla każdej liczby N z pliku kody.txt, dwie liczby całkowite oddzielone pojedynczym znakiem odstępu – sumę cyfr liczby N z pozycji parzystych i sumę cyfr liczby N z pozycji nieparzystych;')

    for line in lines:
        Odd = 0
        Even = 0

        for i in range(0, len(line), 2):
            Odd += int(line[i])

        for i in range(1, len(line), 2):
            Even += int(line[i])
        
        print(f'{Odd} - {Even}')

    print('################################################################################')
    print()

with open('kody.txt') as file:
    print()
    print('################################################################################')
    print('dla każdej liczby N z pliku kody.txt, cyfrę kontrolną tej liczby w systemie Standard Code 25 i po znaku odstępu odpowiadający tej cyfrze kod; ')
    
    for line in lines:
        print(f'{CyfraKontrolna(line)} {line}')

    print('################################################################################')
    print()

with open('kody.txt') as file:
    codes = {
        '0':'10101110111010',
        '1':'11101010101110',
        '2':'10111010101110',
        '3':'11101110101010',
        '4':'10101110101110',
        '5':'11101011101010',
        '6':'10111011101010',
        '7':'10101011101110',
        '8':'11101010111010',
        '9':'10111010111010'
    }

    print()
    print('################################################################################')
    print('dla każdej liczby N z pliku kody.txt, jej kod w systemie Standard Code 25. ')

    for line in lines:
        Standard25 = '11011010'

        for num in line:
            Standard25 += codes[num]
        
        Standard25 += codes[str(CyfraKontrolna(line))]
        Standard25 += '11010110'
        print(Standard25)
    
    print('################################################################################')
    print()