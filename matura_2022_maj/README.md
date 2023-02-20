Zadanie 4. Liczby
=================

W pliku `liczby.txt` danych jest 200 różnych liczb całkowitych z zakresu [10, 100000]. 
Każda z tych liczb zapisana jest w osobnym wierszu.

**Napisz program** (lub kilka programów), który(-e) znajdzie(-dą) odpowiedzi do poniższych zadań. 
Odpowiedzi zapisz w pliku `wyniki4.txt`. Każdą odpowiedź poprzedź numerem oznaczającym zadanie.

Do dyspozycji masz plik `przyklad.txt`, który także zawiera 200 liczb – odpowiedzi dla tego pliku podano w treściach zadań. 
Możesz sprawdzać na nim działanie swojego programu.

**Uwaga:** Pamiętaj, że Twój program musi ostatecznie działać dla pliku `liczby.txt`.

## Zadanie 4.1. (0–4)

Podaj, ile jest w pliku `liczby.txt` takich liczb, których cyfry pierwsza i ostatnia są takie same. 
Zapisz tę z nich, która występuje w pliku `liczby.txt` jako pierwsza.\
W pliku z danymi jest co najmniej jedna taka liczba.

Odpowiedź dla danych z pliku `przyklad.txt`: 26 626\
(26 takich liczb, które mają pierwszą i ostatnią cyfrę taką samą; pierwszą z nich w pliku przykładowym jest 626)

## Zadanie 4.2. (0–4)

Znajdź w pliku `liczby.txt`:

- liczbę, która ma w rozkładzie najwięcej czynników pierwszych (podaj tę liczbę oraz liczbę jej czynników pierwszych)
- liczbę, która ma w rozkładzie najwięcej <u>różnych</u> czynników pierwszych (podaj tę liczbę oraz liczbę jej <u>różnych</u> czynników pierwszych).

**Przykład**: liczba 420=2·2·3·5·7 ma w rozkładzie 5 czynników pierwszych, w tym 4 różne czynniki pierwsze (2, 3, 5, 7).

Odpowiedź dla danych z pliku `przyklad.txt`: 144 6 210 4
(Liczba 144 ma najwięcej czynników pierwszych; liczba czynników pierwszych liczby 144
wynosi 6. Liczba 210 ma najwięcej <u>różnych</u> czynników pierwszych; liczba <u>różnych</u> czynników pierwszych liczby 210 wynosi 4).

## Zadanie 4.3. (0–4)

Trójka (x, y, z) jest dobra, jeśli y jest wielokrotnością x, natomiast z jest wielokrotnością y (czyli x dzieli y, a y dzieli z) oraz x, y, z są różne.

**Przykład**: trójka (2, 6, 12) jest dobra, ponieważ 2 dzieli 6, a 6 dzieli 12. Trójka (2, 10, 12) nie jest dobra, ponieważ 10 nie dzieli 12.

Analogicznie możemy zdefiniować dobrą piątkę liczb – piątka (u, w, x, y, z) jest dobra, jeśli każda z liczb, poza pierwszą, jest podzielna przez poprzednią liczbę z piątki (u dzieli w,
w dzieli x, x dzieli y oraz y dzieli z) oraz wszystkie liczby z piątki są różne.

1. Podaj, ile jest dobrych trójek wśród liczb występujących w pliku `liczby.txt`. 
Zapisz wszystkie dobre trójki do pliku `trojki.txt`, każdą w osobnym wierszu.\
**Uwaga**: Liczby z trójki nie muszą występować w pliku `liczby.txt` w kolejnych wierszach, a ich kolejność w tym pliku może być dowolna.
2. Podaj, ile jest dobrych piątek wśród liczb występujących w pliku `liczby.txt`.

Odpowiedzi dla danych z pliku przyklad.txt: 
1. 10
2. 1\
(10 dobrych trójek i jedna dobra piątka)

Zawartość pliku trojki.txt dla danych z pliku przyklad.txt:\
13 104 208\
13 52 104\
13 52 208\
13 26 104\
13 26 52\
13 26 208\
52 104 208\
26 104 208\
26 52 104\
26 52 208


Zadanie 4. Liczby - odpowiedzi
=================

## Zadanie 4.1. (0–4)
**Zasady oceniania**\
4 pkt – za poprawną odpowiedź, w tym:
- 2 pkt – za prawidłowe policzenie liczb (w przypadku podania liczby różniącej się o 1 – 1 punkt)
- 2 pkt – za prawidłową pierwszą liczbę (w przypadku podania ostatniej liczby 64386 – 1 punkt)

0 pkt – za odpowiedź niepoprawną albo za brak odpowiedzi.

**Rozwiązanie**\
Liczb z pierwszą cyfrą równą ostatniej: 18.\
Pierwsza taka liczba: 93639.

## Zadanie 4.2. (0–4)
**Zasady oceniania**\
4 pkt – za poprawną odpowiedź, w tym:
- 1 pkt – za liczbę czynników pierwszych
- 1 pkt – za liczbę różnych czynników pierwszych
- 1 pkt – za liczbę, która ma najwięcej czynników pierwszych\
(99792 lub 20992 lub 56064)
- 1 pkt – za liczbę, która ma najwięcej różnych czynników pierwszych.

0 pkt – za odpowiedź niepoprawną albo za brak odpowiedzi.

**Rozwiązanie**\
Najwięcej czynników: 10 dla 99792, 20992, 56064\
Najwięcej różnych: 6 dla 62790

## Zadanie 4.3. (0–4)
**Zasady oceniania**\
4 pkt – za poprawną odpowiedź, w tym:
- 3 pkt – za wyznaczanie dobrych trójek, w tym:
> 2 pkt – za liczbę dobrych trójek\
> 1 pkt – za plik zawierający wszystkie dobre trójki,
(ALBO: w przypadku wyznaczenia co najmniej pięciu dobrych trójek i zapisania
ich, i tylko ich, w pliku – 2 pkt)\
- 1 pkt – za liczbę dobrych piątek.

0 pkt – za odpowiedź niepoprawną albo za brak odpowiedzi.

**Rozwiązanie**\
27 (trójki)\
2 (piątki)

Dobre trójki:\
955 8595 42975\
232 13688 27376\
13594 27188 81564\
971 13594 81564\
971 13594 27188\
971 27188 81564\
971 6797 81564\
971 6797 13594\
971 6797 27188\
797 7173 64557\
1403 42090 84180\
1403 2806 42090\
1403 2806 84180\
1403 2806 8418\
1403 8418 42090\
1403 8418 84180\
871 15678 62712\
497 22365 89460\
2806 42090 84180\
2806 8418 42090\
2806 8418 84180\
392 20384 61152\
409 9816 58896\
8418 42090 84180\
6797 13594 81564\
6797 13594 27188\
6797 27188 81564