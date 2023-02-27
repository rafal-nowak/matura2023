Zadanie 4. Scalanie
=================

Pliki `dane1.txt` i `dane2.txt` zawierają po 1000 wierszy. W każdym wierszu tych plików
zapisany jest uporządkowany niemalejąco ciąg dziesięciu liczb całkowitych o wartościach
z przedziału 〈0,100〉 , oddzielonych spacjami.

**Napisz program(y)**, dający(e) odpowiedzi do poniższych zadań. Odpowiedzi zapisz w plikach
o nazwach zgodnych z podanymi poniżej.

**Uwaga:** pliki przyklad1.txt oraz przyklad2.txt zawierają dane przykładowe
spełniające warunki zadania (dla tylko 5 wierszy w każdym pliku). Odpowiedzi dla danych
z przykładowych plików są podane pod poleceniami. 
## Zadanie 4.1. (0–1)

Porównaj ciągi zapisane w odpowiadających sobie wierszach w plikach `dane1.txt`
i `dane2.txt`. Podaj, w ilu wierszach zapisane są ciągi, których ostania liczba jest taka sama.

Dla danych z plików `przyklad1.txt` oraz `przyklad2.txt` wynikiem jest 3. 

## Zadanie 4.2. (0–3)

Podaj, ile jest par ciągów (w odpowiadających sobie wierszach plików `dane1.txt`
i `dane2.txt`) takich, że w jednym i drugim ciągu jest 5 liczb parzystych i 5 liczb
nieparzystych.

Dla danych z plików `przyklad1.txt` oraz `przyklad2.txt` wynikiem jest 1.

## Zadanie 4.3. (0–4)

1. Policz, ile jest par ciągów (w odpowiadających sobie wierszach plików `dane1.txt`
i `dane2.txt`), które utworzone są z takich samych liczb. Liczba powtórzeń takich samych
liczb w ciągach może być różna. 

2. Wypisz numery wierszy, w których takie pary ciągów się
znajdują.

Dla danych z plików `przyklad1.txt` oraz `przyklad2.txt` odpowiedzią jest:
2 pary ciągów
numery wierszy:
1, 5 

## Zadanie 4.4. (0–4)

Napisz program, który utworzy plik `wynik4_4.txt` zawierający w kolejnych wierszach
ciągi uporządkowane, będące wynikiem scalenia odpowiadających im co do kolejności
ciągów z plików `dane1.txt` i `dane2.txt`. Liczby w ciągach wynikowych zapisz,
rozdzielając je spacjami.

Dla danych z plików `przyklad1.txt` oraz `przyklad2.txt` wynikiem jest plik
zawierający następujące wiersze:\
3 3 9 9 12 12 12 14 14 19 19 26 26 32 32 33 33 33 36 36\
2 6 8 9 15 16 16 17 17 18 24 27 29 35 35 36 41 41 46 54\
3 9 12 12 16 21 23 25 27 29 31 33 33 38 38 46 48 48 50 54\
5 8 13 15 22 22 27 31 36 39 45 46 49 52 55 56 57 64 70 70\
1 1 2 2 8 8 8 9 9 10 10 18 18 22 22 22 32 32 34 34

Zadanie 4. Scalanie - odpowiedzi
=================

## Zadanie 4.1. (0–1)
**Schemat punktowania**\
1 p. – za podanie prawidłowej odpowiedzi.\
0 p. – za błędną odpowiedź albo za brak odpowiedzi. 

**Poprawna odpowiedź**\
32

## Zadanie 4.2. (0–3)
**Schemat punktowania**\
3 p. – za podanie prawidłowej odpowiedzi.\
0 p. – za błędną odpowiedź albo za brak odpowiedzi. \
***Uwaga: Nie przyznaje się 2 p i 1 p.***

**Poprawna odpowiedź**\
50 

## Zadanie 4.3. (0–4)
**Schemat punktowania**\
4 p. – za podanie poprawnej odpowiedzi, w tym:
- 3 p. – za podanie poprawnej liczby par ciągów,
- 1 p. – za podanie poprawnego numeru wiersza.

0 p. – za inną błędną odpowiedź albo za brak odpowiedzi.

***Uwaga: Nie przyznaje się 2 p .***

**Poprawna odpowiedź**\
Liczba par ciągów 1\
Wiersz 999

## Zadanie 4.4. (0–4)
**Schemat punktowania**
4 p. – za podanie poprawnej odpowiedzi, w tym:
- 2 p. – za prawidłowe scalenie do czasu wyczerpania elementów jednego z ciągów,
- 1 p. – za prawidłowe dopisanie pozostałych elementów, gdy ciąg z pliku dane1.txt
wyczerpie się jako pierwszy,
- 1 p. – za prawidłowe dopisanie pozostałych elementów, gdy ciąg z pliku dane2.txt
wyczerpie się jako pierwszy.

0 p. – za inną błędną odpowiedź albo za brak odpowiedzi.

**Poprawna odpowiedź**
Trzydzieści pierwszych scalonych wierszy:\
1 5 6 6 8 13 13 14 15 15 24 24 33 33 34 35 36 41 44 45\
4 8 8 14 16 17 19 22 28 28 33 38 42 43 45 45 46 46 49 49\
5 5 9 10 11 11 16 16 17 21 26 28 28 30 31 35 41 50 58 61\
5 6 13 14 17 17 19 24 26 27 29 29 36 36 38 38 44 44 51 57\
1 4 4 4 6 9 13 18 18 19 25 27 32 33 34 34 39 44 46 56\
2 2 5 9 9 13 15 20 21 24 26 27 31 32 34 37 38 42 43 49\
0 5 6 6 12 14 15 15 16 18 21 26 26 26 30 31 37 40 47 50\
5 6 6 11 12 14 17 20 21 22 29 30 35 37 39 43 46 47 56 60\
7 9 10 15 15 17 18 20 27 28 34 37 40 43 46 48 48 50 56 63\
5 8 9 9 11 15 19 19 19 27 27 27 30 34 36 38 43 45 47 47\
0 1 4 4 9 14 14 16 16 17 17 17 18 22 23 25 26 31 40 46\
3 8 8 9 9 12 14 16 23 26 28 31 36 37 41 43 43 44 52 55\
3 6 8 10 11 13 13 18 23 24 29 32 33 37 37 45 49 50 50 52\
6 7 7 10 11 16 16 16 23 25 30 30 37 38 39 43 43 43 49 50\
9 10 10 16 17 18 22 22 27 29 31 37 40 43 43 53 53 61 61 67\
6 6 6 8 14 14 16 18 21 25 26 29 34 35 36 39 42 44 52 60\
0 0 5 6 7 12 14 14 18 19 26 27 32 33 33 36 36 46 46 55\
7 9 15 17 17 21 24 27 27 28 31 35 40 41 42 45 50 50 50 54\
3 8 8 10 10 12 14 17 23 23 24 27 28 32 33 37 37 40 42 44\
2 9 9 10 14 15 18 25 25 25 26 27 34 34 37 39 39 43 52 56\
0 4 5 6 11 13 13 17 23 25 25 34 35 36 43 44 45 46 52 55\
6 6 7 9 13 19 20 23 25 25 29 30 31 32 38 39 40 41 41 50\
2 5 6 8 8 8 13 18 19 22 22 26 28 30 32 34 34 41 41 41\
4 4 7 12 14 14 22 23 24 27 27 30 36 37 37 40 47 47 54 54\
6 8 14 17 17 18 21 24 26 30 33 37 37 42 46 49 50 53 60 60\
4 6 12 15 20 24 30 30 35 36 44 46 46 51 55 56 57 60 65 67\
0 4 4 5 9 12 15 16 20 21 23 25 31 34 38 40 42 44 49 49\
2 2 3 10 13 14 15 21 23 24 25 27 28 32 34 40 41 45 51 58\
6 8 9 15 16 16 16 23 24 25 26 28 33 34 38 40 42 42 46 54\
1 8 10 11 16 16 18 19 22 24 26 28 31 33 38 42 48 58 59 62\ 
