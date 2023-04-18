Zadanie 1. Kosmiczny mecz
==

Dawno temu, w odległej galaktyce, rozegrano mecz w grę, która przypominała siatkówkę.
W meczu wystąpiły dwie drużyny: drużyna A i drużyna B. Mecz składał się z 10 000 krótkich
rozgrywek. Każda rozgrywka kończyła się wygraną jednej z dwóch drużyn, za którą
zwycięska drużyna otrzymywała jeden punkt.

Plik `mecz.txt` zawiera zapis wyników kolejnych rozgrywek – jeden wiersz z napisem
złożonym z 10 000 znaków A i B. Znak A oznacza, że rozgrywkę wygrała drużyna A,
natomiast znak B – że rozgrywkę wygrała drużyna B.

**Napisz program(-y)** który(-e) znajdzie(-dą) odpowiedzi do poniższych zadań. Odpowiedzi
zapisz w pliku wyniki1.txt, a każdą z nich poprzedź numerem odpowiedniego zadania.

Do dyspozycji masz plik `mecz_przyklad.txt`, spełniający warunki zadania – odpowiedzi dla tego pliku podano w treściach zadań. Możesz sprawdzać na nim działanie swojego
programu.

## Zadanie 1.1. (0–2) 

Oblicz, ile razy nastąpiła sytuacja, w której rozgrywkę wygrała inna drużyna niż rozgrywkę poprzednią (tzn. dwa kolejne znaki A lub B w opisie meczu się różnią).

**Przykład**: Dla napisu ABBBABA odpowiedzią jest 4.\
Natomiast dla pliku `mecz_przyklad.txt` odpowiedzią jest 1798

## Zadanie 1.2. (0–3)
Pierwszy set w meczu trwa do pierwszej rozgrywki, po której któraś z drużyn ma co najmniej
1000 punktów za wygranie dotychczasowych rozgrywek, natomiast drużyna przeciwna ma
co najmniej 3 punkty mniej. Drużyna, która zdobywa w secie więcej punktów od przeciwnej,
wygrywa pierwszego seta.

**Przykład**: pierwszy set może się zakończyć wynikami: 1000:500, 997:1000, 1500:1497.\
Wyniki 900:100, 999:1000, 1500:1500 nie kończą seta.

Podaj, która drużyna *wygrała pierwszego seta* i jaki w tym momencie był wynik (liczba zwycięskich rozgrywek drużyny A i liczba zwycięskich rozgrywek drużyny B w pierwszym secie).

Dla pliku `mecz_przyklad.txt` odpowiedzią jest: A 1000:5

## Zadanie 1.3. (0–3)
Powiemy, że drużyna ma dobrą passę, jeśli wygrywa rozgrywki co najmniej 10 razy z rzędu. Każda dobra passa rozpoczyna się albo na początku meczu, albo bezpośrednio po przegranej rozgrywce. Każda dobra passa kończy się albo z końcem meczu, albo bezpośrednio przed przegraną rozgrywką.

Podaj łączną liczbę dobrych pass, które miały obie drużyny w meczu. Wyznacz długość najdłuższej dobrej passy i drużynę, która ją osiągnęła. Tylko jedna drużyna miała dobrą passę o tej długości.

**Przykład**: w meczu BBBBBBBBBBAABBAAAAAAAAAAABA mamy łącznie 2 dobre passy.\
Najdłuższą dobrą passę, o długości 11, osiągnęła drużyna A.

Dla pliku `mecz_przyklad.txt` odpowiedzią jest: 2 A 1000 (dwie dobre passy, najdłuższa
drużyny A o długości 1000).

**Do oceny oddajesz:**

- plik wyniki1.txt, zawierający odpowiedzi do zadań 1.1.–1.3.
- plik(-i) zawierający(-e) kody źródłowe Twojego(-ich) programu(-ów) o nazwie(nazwach):

(uwaga: brak tych plików jest równoznaczny z brakiem rozwiązania zadania)

\
Zadanie 2. Strzałki
==

## Zadanie 2.4. (0–3)
W pliku `pary.txt` danych jest 1000 par liczb całkowitych z przedziału [1, 100 000], po jednej parze w wierszu. Liczby w każdym wierszu są rozdzielone znakiem odstępu. Druga liczba w parze zawsze jest większa od pierwszej.

Dla N = 100 000 wykonano polecenie *rysuj(1)* dla pewnego układu *N* punktów.

**Napisz program**, który znajdzie i wypisze te pary liczb z pliku `pary.txt`, które odpowiadają numerom punktów x i y takich, że z punktu o numerze x można przejść po jednej lub wielu strzałkach (zawsze zgodnie z ich zwrotami) do punktu o numerze y.

**Przykład:**\
Przykładowo: dla *N* = 5 po strzałkach można przejść z punktu o numerze 1 do punktu o numerze 4, ale nie można przejść z punktu o numerze 3 do punktu o numerze 5.

**Do oceny oddajesz:**
- plik `wyniki2.txt`, zawierający odpowiedź do zadania 2.4.
- plik(-i) zawierający(-e) kody źródłowe Twojego(-ich) programu(-ów) o nazwie(nazwach):

(uwaga: brak tych plików jest równoznaczny z brakiem rozwiązania zadania)

\
Zadanie 3. Liczby
==

W pliku `liczby.txt` zapisanych jest 100 liczb parzystych z przedziału [4, 1 000 000], każda w oddzielnym wierszu.

**Napisz program(-y)** który(-e) znajdzie(-dą) odpowiedzi do poniższych zadań. Odpowiedzi zapisz w pliku `wyniki3.txt`, a każdą z nich poprzedź numerem odpowiedniego zadania.

Do dyspozycji masz plik `liczby_przyklad.txt`, spełniający warunki zadania – odpowiedzi dla tego pliku podano w treściach zadań. Możesz sprawdzać na nim działanie swojego programu.

## Zadanie 3.2. (0–2)
Dla każdej liczby x z pliku `liczby.txt` sprawdź, czy liczba x – 1 jest liczbą pierwszą.\
Podaj, ile liczb z pliku `liczby.txt` po pomniejszeniu o 1 daje liczbę pierwszą.

Dla pliku liczby_przyklad.txt odpowiedzią jest 94.

## Zadanie 3.3. (0–4)
*Hipoteza Goldbacha* głosi, że każda liczba parzysta większa od 2 jest sumą dwóch liczb pierwszych. Nie wiemy, czy ta hipoteza jest prawdziwa dla wszystkich liczb parzystych dodatnich, ale została potwierdzona dla wszystkich liczb „rozsądnej wielkości”, zwłaszcza dla nie przekraczających 1018. Oczywiście liczba może mieć więcej niż jeden rozkład na sumę dwóch liczb pierwszych, np. 22 = 19 + 3 = 17 + 5 = 11 + 11.\
Dla każdej z liczb z pliku `liczby.txt` rozstrzygnij, **na ile różnych sposobów** da się ją
przedstawić jako sumę dwóch liczb pierwszych.

Podaj:
- liczbę, która ma najwięcej różnych rozkładów na sumę dwóch liczb pierwszych, oraz liczbę takich rozkładów
- liczbę, która ma najmniej różnych rozkładów na sumę dwóch liczb pierwszych, oraz liczbę
takich rozkładów.

**Uwaga:** przyjmujemy, że dwa rozkłady są różne, jeśli nie zawierają takiej samej pary składników. Przykładowo: rozkłady 22 = 19 + 3 i 22 = 3 + 19 są takie same.

Dla pliku `liczby_przyklad.txt` odpowiedzią jest: 996 37 4 1 \
(liczba 996 ma 37 rozkładów, a 4 tylko jeden)

## Zadanie 3.4. (0–3)
Dla każdej liczby z pliku `liczby.txt` znajdź jej reprezentację w systemie szesnastkowym.\
Dla każdej cyfry szesnastkowej podaj, ile razy występuje ona łącznie w zapisach szesnastkowych wszystkich liczb z pliku `liczby.txt.`

Dla pliku `liczby_przyklad.txt` odpowiedzią jest\
0:2\
1:3\
2:5\
3:2\
4:94\
5:0\
6:1\
7:0\
8:2\
9:2\
A:0\
B:0\
C:1\
D:1\
E:3\
F:0

**Do oceny oddajesz:**
- plik `wyniki3.txt`, zawierający odpowiedzi do zadań 3.2.–3.4.
- plik(-i) zawierający(-e) kody źródłowe Twojego(-ich) programu(-ów) o nazwie(nazwach):

(uwaga: brak tych plików jest równoznaczny z brakiem rozwiązania zadania)

\
Zadanie 1. Kosmiczny mecz - Odpowiedzi
==

## Zadanie 1.1. (0–2)

**Zasady oceniania**\
2 pkt – odpowiedź poprawna.\
1 pkt – odpowiedź różniąca się od poprawnej o 1.\
0 pkt – inna odpowiedź niepoprawna albo brak rozwiązania.

**Rozwiązanie**\
5030

## Zadanie 1.2. (0–3) 

**Zasady oceniania**\
3 pkt – odpowiedź poprawna, w tym:
- 1 pkt – za wskazanie drużyny, która wygrywa pierwszego seta
- 2 pkt – za poprawny wynik, w tym po 1 pkt za wynik każdej z drużyn.

0 pkt – odpowiedź niepoprawna albo brak rozwiązania.

**Rozwiązanie**\
B 1001:1004

## Zadanie 1.3. (0–3) 

**Zasady oceniania**\
3 pkt – odpowiedź poprawna, w tym:
- 1 pkt – za podanie liczby wszystkich dobrych pass
- 2 pkt – za podanie drużyny, która miała najdłuższą dobrą passę i długość tej passy (po 1 punkcie za nazwę drużyny i liczbę).

0 pkt – odpowiedź niepoprawna albo brak rozwiązania.

**Rozwiązanie**\
6 B 15\
(Liczba dobrych pass: 6 Najdłuższa dobra passa: B, 15 rozgrywek)

\
Zadanie 2. Strzałki - Odpowiedzi 
==

## Zadanie 2.4. (0–3) 

**Zasady oceniania**\
3 pkt – odpowiedź poprawna.\
2 pkt – za podanie co najmniej 5 poprawnych par.\
1 pkt – za podanie co najmniej 1 poprawnej pary.\
0 pkt – odpowiedź niepoprawna albo brak rozwiązania.

**Rozwiązanie**\
47 3044\
7650 61204\
1 245\
7 63669\
9125 18250\
5 43246

\
Zadanie 3. Liczby
==

## Zadanie 3.2. (0–2) 

**Zasady oceniania**\
2 pkt – odpowiedź poprawna.\
1 pkt – odpowiedź mniejsza o 1 od poprawnej.\
0 pkt – odpowiedź niepoprawna albo brak rozwiązania.

**Rozwiązanie**\
21

## Zadanie 3.3. (0–4)

**Zasady oceniania**\
4 pkt – odpowiedź poprawna, w tym:
- 1 pkt za każdą poprawną liczbę w odpowiedzi.

0 pkt – odpowiedź niepoprawna albo brak rozwiązania.

**Rozwiązanie**\
910620 9932\
18676 195

## Zadanie 3.4. (0–3)

**Zasady oceniania**\
3 pkt – odpowiedź poprawna.\
2 pkt – odpowiedź poprawna dla przynajmniej 12 cyfr zapisu szesnastkowego.\
1 pkt – odpowiedź poprawna dla przynajmniej 5 cyfr zapisu szesnastkowego w tym co najmniej jednej litery (cyfry szesnastkowej większej niż 9).\
0 pkt – odpowiedź niepoprawna albo brak rozwiązania.

**Rozwiązanie**\
0: 32\
1: 26\
2: 37\
3: 31\
4: 43\
5: 25\
6: 28\
7: 23\
8: 38\
9: 28\
A: 45\
B: 33\
C: 29\
D: 23\
E: 44\
F: 10
