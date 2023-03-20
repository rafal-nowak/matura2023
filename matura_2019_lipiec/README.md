Zadanie 4. Wybrane liczby
=========================

Liczby pierwsze to liczby naturalne większe od 1, które mają dokładnie dwa dzielniki: jedynkę i samą siebie.

Dane są dwa pliki: `liczby.txt` i `pierwsze.txt`. Plik `liczby.txt` zawiera 300 wierszy. W każdym wierszu tego pliku znajduje się jedna liczba całkowita dodatnia z zakresu od 1 do 100 000.

Plik `pierwsze.txt` zawiera 200 wierszy. W każdym wierszu tego pliku znajduje się jedna liczba pierwsza z zakresu od 10 do 1 300 000.

**Uwaga:** pomocnicze pliki `liczby_przyklad.txt` i `pierwsze_przyklad.txt`, zawierają dane, które możesz wykorzystać, aby sprawdzić poprawność działania swojego(-ich) programu(-ów). Każdy z nich zawiera po 50 wierszy. W każdym wierszu znajduje się jedna liczba. Odpowiedzi dla danych z tych plików są podane pod treściami zadań. 

**Napisz program(-y)**, w wyniku działania którego(-ych) otrzymasz odpowiedzi do poniższych zadań. Pliki źródłowe z rozwiązaniem zapisz pod nazwą zgodną z numerem zadania, z rozszerzeniem odpowiadającym użytemu językowi programowania.

**Uwaga:** Pamiętaj, że Twój program musi ostatecznie działać dla plików `liczby.txt` i `pierwsze.txt`.

## Zadanie 4.1. (0–4)

Podaj, (zachowując ich kolejność) te liczby z pliku `liczby.txt`, które są liczbami pierwszymi z przedziału 〈100; 5000〉.\
Odpowiedź zapisz w pliku `wyniki4_1.txt`.

Dla pliku `liczby_przyklad.txt` odpowiedzią są liczby: 103, 163, 173, 701, 1033, 2137, 3529, 4933, 977, 2143

## Zadanie 4.2. (0–4)

Podaj, w kolejności ich występowania w pliku `pierwsze.txt`, wszystkie te liczby, które czytane od prawej do lewej również są liczbami pierwszymi.\
Odpowiedź zapisz w pliku `wyniki4_2.txt`.

Przykład:\
Jeśli odczytamy liczbę pierwszą 17 od prawej do lewej, otrzymamy liczbę 71, która również jest liczbą pierwszą.

Dla pliku `pierwsze_przyklad.txt` liczbami spełniającymi warunek zadania są: 701, 709, 1033, 167, 1109, 1619, 1009, 179, 1499, 76001, 1601, 31873

## Zadanie 4.3. (0–4)

Niech w(N) oznacza sumę cyfr liczby N. Dla danej liczby N tworzymy ciąg, w którym N1 = w(N), a każdy kolejny element jest sumą cyfr występujących w poprzednim elemencie:

`	N1 = w(N)	`\
`	N2 = w(N1)	`\
`	N3 = w(N2)	`\
`	...	`\

Ciąg kończy się, gdy jego wyraz jest liczbą jednocyfrową. Tę liczbę nazywamy **wagą liczby N**.

**Przykład 1.**
Niech `N = 1109`.
`N1 = 1 + 1 + 0 + 9 = 11`\
`N2 = 1 + 1 = 2`\
Zatem waga liczby `N = 1109` jest równa 2.

**Przykład 2.**
Niech `N = 31699`.
`N1 = 3 + 1 + 6 + 9 + 9 = 28`\
`N2 = 2 + 8 = 10`\
`N3 = 1 + 0 = 1`\
Zatem waga liczby `N = 31699` jest równa 1.

Podaj, ile jest liczb w pliku `pierwsze.txt`, których waga jest równa 1.

Prawidłowa odpowiedź dla pliku `pierwsze_przyklad.txt`: 6 liczb.

Zadanie 4. Wybrane liczby - odpowiedzi
=========================

## Zadanie 4.1. (0–4)
**Zasady oceniania**\
**4 punkty** - za podanie wszystkich liczb pierwszych z przedziału, w tym:
 - 2 punkty - za podanie wszystkich liczb pierwszych z danego pliku.
 - za pominięcie jednej liczby 3p, dwóch 2p, trzech – 1punkt.

0 punktów – za odpowiedź niepoprawną albo za brak odpowiedzi.

**Rozwiązanie**\
563
2087
163
2423
3581
911
997
113
1049
1511
2467
283
3559
521
4201
877
1301
2749
4919
1213
2039
4111
3331
401
2221

## Zadanie 4.2. (0–4)
**Zasady oceniania**\
**4 punkty** - za podanie wszystkich liczb (51 sztuk), w tym:
 - za pominięcie dowolnej liczby - 1 punkt. (czyli można pominąć maksymalnie 3 liczby)
 - jeśli z powodu np. braku zmiany licznika z 300 na 200 (`plik liczby.txt` ma 300 wierszy a `pierwsze.txt` – 200 wierszy) po poprawnym zestawie liczb pojawią się liczby „nieuprawnione” – odejmujemy 1 punkt.\

**Rozwiązanie**\
31
37
101
1009
1021
113
1499
1213
1217
1229
1231
1237
1487
1223
7027
7043
3821
31873
1511
140527
151169
151189
193261
1297001
1061
100267
100271
100279
181957
13
112163
112181
3803
76001
160183
160201
160243
17
907
701
383
389
1103
1109
31721
1583
1597
1601
1619
3571
112111

## Zadanie 4.3. (0–4)
**Zasady oceniania**\
**4 punkty** - za poprawną odpowiedź, tym: 
 - 3 punkty - za odpowiedź różną (+/-1)
 - 3 punkty - za wypisanie wszystkich liczb, których waga jest równa 1 (zamiast zliczenia ich liczby)
 - 2 punkty - za obliczenie wagi wszystkich liczb
 - 1 punkt - za znalezienie przynajmniej 5 liczb z wagą 1

**Rozwiązanie**\
Odpowiedź – 27

Liczby z wagą 1:
37
1009
109
31699
31663
6733
4663
7039
66601
80191
140527
151201
440821
440893
440911
100207
100279
171253
181981
75997
80173
160183
160201
1621
2017
15787
20809 
