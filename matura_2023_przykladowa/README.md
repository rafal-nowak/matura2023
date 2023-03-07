Zadanie 1. Szachy
=================

**Uwaga:** do rozwiązania zadań 1.1.–1.3. nie jest potrzebna znajomość reguł gry w szachy.

W pliku `szachy.txt` znajduje się zapis partii szachów, jaką w 2020 roku rozegrali polski
arcymistrz Jan Krzysztof Duda oraz mistrz świata Magnus Carlssen. Zapis partii składa się
z opisów 125 plansz przedstawiających stany gry (położenie bierek na szachownicy) po
kolejnych posunięciach każdego z graczy. Opis każdej planszy składa się z:
- 8 wierszy tekstu po 8 znaków w każdym wierszu
- kolejne znaki w wierszach oznaczają:\
− znak '.' − puste pole\
− wielkie litery − białe bierki (czyli białe figury i pionki)\
− małe litery − czarne bierki\
− oznaczenia bierek to:\
&emsp;K/k − król, &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&ensp; H/h − hetman,\
&emsp;W/w − wieża, &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&ensp;G/g − goniec,\
&emsp;S/s − skoczek, &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;P/p − pionek.

Dla zachowania czytelności, po każdym opisie następuje pojedynczy pusty wiersz. W dalszej
części, zamiast „opis planszy”, będziemy pisać krótko „plansza”.\
\
**Przykład:**\
`wsghkgsw`\
`pppppppp`\
`........`\
`........`\
`....P...`\
`........`\
`PPPP.PPP`\
`WSGHKGSW`\
\
`wsghkgsw`\
`pp.ppppp`\
`..p.....`\
`........`\
`....P...`\
`........`\
`PPPP.PPP`\
`WSGHKGSW`

Napisz **program(-y)**, który(-e) znajdzie(-dą) odpowiedzi do poniższych zadań.
Do Twojej dyspozycji jest plik `szachy_przyklad.txt`, który zawiera 9 plansz zapisanych
w podanym wyżej formacie. Odpowiedzi dla pliku `szachy_przyklad.txt` podano w treści
poszczególnych zadań. Pamiętaj, że Twój(-e) program(-y) musi(-szą) działać dla 125 plansz.

## Zadanie 1.1. (0–3)

Podaj, na ilu planszach znajduje się przynajmniej jedna pusta kolumna, czyli taka, na polach
której nie stoi żadna bierka. Podaj także największą liczbę pustych kolumn na jednej z tych
plansz.\
\
Odpowiedź dla pliku `szachy_przyklad.txt`:\
7 5\
(7 plansz z pustymi kolumnami, największa liczba pustych kolumn na planszy − 5).

## Zadanie 1.2. (0–3)

Rozstrzygnij, ile razy w trakcie gry (inaczej: na ilu planszach zapisanych w pliku
`szachy.txt`) nastąpiła sytuacja, w której jest równowaga – jest <ins>tyle samo</ins> i <ins>takich samych</ins>
czarnych bierek, ile białych. Podaj liczbę takich plansz, a także najmniejszą liczbę bierek
(łącznie białych i czarnych) na planszy w stanie równowagi.\
\
**Przykład:**\
`A`: &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&ensp;`B`:\
`.k......` &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; `.p......`\
`........` &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; `........`\
`........` &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; `........`\
`....s...` &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; `....s...`\
`....S...` &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; `....S...`\
`........` &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; `........`\
`........` &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; `........`\
`.......K` &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; `.......K`

Plansza A jest w równowadze, a plansza B nie jest w równowadze (czarne i białe nie mają
takich samych bierek).\
\
Odpowiedź dla pliku szachy_przyklad.txt:\
6 4\
(6 plansz w równowadze, 4 − najmniejsza liczba bierek na planszy w stanie równowagi)

## Zadanie 1.3. (0–4)

Wieża szachuje króla przeciwnego gracza, jeśli znajduje się w tym samym wierszu lub w tej
samej kolumnie co król i pomiędzy nimi nie ma żadnej innej bierki.\
Oblicz i podaj, na ilu planszach biała wieża szachuje czarnego króla oraz na ilu planszach
czarna wieża szachuje białego króla.\
\
Odpowiedź dla pliku `szachy_przyklad.txt`:\
2 0\
\
(2 razy biała wieża szachuje czarnego króla, 0 razy czarna wieża szachuje białego króla).

Zadanie 1. Szachy - odpowiedzi
=================

## Zadanie 1.1. (0–3)
**Zasady oceniania**\
3 pkt – za poprawną odpowiedź, w tym:
- 1 pkt – za liczbę plansz z pustymi kolumnami
- 2 pkt – za maksymalną liczbę pustych kolumn na planszy (jeśli podana liczba
różni się o 1 od prawidłowej – 1 pkt).

0 pkt – za podanie odpowiedzi niepoprawnej lub niepełnej albo brak odpowiedzi.

**Rozwiązanie**\
36 3\
\
36 plansz z pustymi kolumnami, największa liczba pustych kolumn – 3

## Zadanie 1.2. (0–3)
**Zasady oceniania**\
3 pkt – za poprawną odpowiedź, w tym:
- 2 pkt – za liczbę plansz w stanie równowagi
- 1 pkt – za najmniejszą liczbę bierek na planszy w stanie równowagi.

0 pkt – za podanie odpowiedzi niepoprawnej lub niepełnej albo brak odpowiedzi.

**Rozwiązanie**\
22 28\
\
(22 plansze w stanie równowagi, najmniejsza liczba bierek na planszy w stanie równowagi – 28)

## Zadanie 1.3. (0–4)
**Zasady oceniania**\
4 pkt – za poprawną odpowiedź, w tym:
- 2 pkt – za liczbę plansz, na których biała wieża szachuje czarnego króla (jeśli podana
liczba różni się o 1 od prawidłowej – 1 pkt),
- 2 pkt – za liczbę plansz, na których czarna wieża szachuje białego króla (jeśli podana
liczba różni się o 1 od prawidłowej – 1 pkt).

0 pkt – za podanie odpowiedzi niepoprawnej lub niepełnej albo brak odpowiedzi.

**Rozwiązanie**\
3 1\
\
(na 3 planszach biała wieża szachuje czarnego króla, natomiast na 1 planszy czarna wieża
szachuje białego króla)
