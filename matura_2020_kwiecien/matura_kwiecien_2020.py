
class matura_kwiecien_2020:
    def __init__(self):
        pass
# Podaj wartość największej luki oraz wartość najmniejszej luki pomiędzy elementami ciągu

    def zadanie_4_1(selfs):
        with open("dane4.txt", "r") as f:
            string = [int(x) for x in f.read().split()]

        min_gap = float('inf')
        max_gap = 0

        for i in range(1, len(string)):
            gap = abs(string[i] - string[i-1])
            if gap < min_gap:
                min_gap = gap
            if gap > max_gap:
                max_gap = gap

        return min_gap, max_gap


    # Znajdź najdłuższy fragment regularny w ciągu
    # Podaj jego długość oraz wartości (liczby) znajdujące się na początku i końcu tego fragmentu.

    def zadanie_4_2(selfs):
        with open("dane4.txt") as f:
            string = [int(x) for x in f.read().split()]

        n = len(string)

        result = []
        for i in range(n-1):
            regular = [string[i], string[i+1]]
            gap = abs(string[i+1] - string[i])
            for j in range(i+1, n-1):
                if abs(string[j+1] - string[j]) != gap:
                    break
                regular.append(string[j+1])
            if len(regular) > len(result):
                result = regular

        return len(result), result[0], result[-1]

    # Podaj krotność najczęstszej luki oraz wartości wszystkich najczęstszych luk w ciągu

    def zadanie_4_3(self):
        with open("dane4.txt", "r") as f:
            numbers = [int(x) for x in f.read().split()]

        gaps = []
        for i in range(1, len(numbers)):
            gaps.append(abs(numbers[i] - numbers[i-1]))
        gaps_count = {}
        for gap in gaps:
            if gap in gaps_count:
                gaps_count[gap] += 1
            else:
                gaps_count[gap] = 1
        max_count = max(gaps_count.values())
        most_frequent_gaps = [gap for gap, count in gaps_count.items() if count == max_count]
        return max_count, most_frequent_gaps




