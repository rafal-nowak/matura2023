def CyfraKontrolna(N):
    Odd = 0
    Even = 0

    for i in range(0, len(N), 2):
        Odd += int(N[i])

    for i in range(1, len(N), 2):
        Even += int(N[i])
    
    return (10-((Odd+(Even*3))%10))%10

class Matura2015Czerwiec:
    def zadanie_6_1(selfs):
        with open('kody.txt') as file:
            odds = []
            evens = []

            lines = [line.rstrip() for line in file]

            for line in lines:
                odd = 0
                even = 0

                for i in range(0, len(line), 2):
                    odd += int(line[i])

                for i in range(1, len(line), 2):
                    even += int(line[i])
                
                odds.append(odd)
                evens.append(even)
                
            return odds, evens

    def zadanie_6_2(selfs):
        with open('kody.txt') as file:
            lines = [line.rstrip() for line in file]

            control_numbers = []

            for line in lines:
                control_numbers.append(CyfraKontrolna(line))
            
            return control_numbers
    def zadanie_6_3(selfs):
        with open('kody.txt') as file:
            lines = [line.rstrip() for line in file]

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

            Standards25 = []

            for line in lines:
                Standard25 = '11011010'

                for num in line:
                    Standard25 += codes[num]
                
                Standard25 += codes[str(CyfraKontrolna(line))]
                Standard25 += '11010110'

                Standards25.append(Standard25)
            
            return Standards25

M = Matura2015Czerwiec()

print(M.zadanie_6_3())