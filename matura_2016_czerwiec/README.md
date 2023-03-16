Zadanie 6. Systemy liczbowe
===========================

W pliku `liczby.txt` zapisano 999 kodów liczb, każdy kod w osobnym wierszu. Ostatnia
cyfra kodu oznacza podstawę systemu liczbowego (od dwójkowego do dziewiątkowego),
w jakim zapisano liczbę kolejnymi cyframi kodu, od pierwszej do przedostatniej.

**Na przykład:**\
12345678 oznacza liczbę 1234567<sub>8</sub>, czyli liczbę 1234567 zapisaną w systemie ósemkowym.
Każdy kod liczby zaczyna się cyfrą większą od 0, a jego długość (wraz z cyfrą oznaczającą
system liczbowy) nie przekracza 10 cyfr.

**Uwaga:**\
Niektórych 10-cyfrowych liczb całkowitych nie da się zapisać w pojedynczej 32-bitowej
zmiennej typu całkowitoliczbowego, np. w języku C++ nie jest to możliwe w zmiennej typu
`int`, a w Pascalu – w zmiennej typu `integer`.

**Napisz program(y)**, którego(ych) wynikiem działania będą rozwiązania poniższych zadań.
Odpowiedzi do zadań zapisz odpowiednio w oddzielnych plikach `wyniki_6_1.txt`,
`wyniki_6_2.txt`, `wyniki_6_3.txt`, `wyniki_6_4.txt`, `wyniki_6_5.txt`. Pliki
źródłowe z rozwiązaniem zapisz pod nazwą zgodną z numerem zadania, z rozszerzeniem
odpowiadającym użytemu narzędziu informatycznemu.

## Zadanie 6.1. (0–1) 

Podaj, ile liczb w pliku `liczby.txt` zapisano w systemie ósemkowym.

## Zadanie 6.2. (0–2) 

Podaj, ile wierszy w pliku `liczby.txt` zawiera liczby zapisane w systemie czwórkowym
takie, że w ich zapisie nie występuje cyfra 0.

## Zadanie 6.3. (0–2)

Podaj, ile wierszy w pliku `liczby.txt` zawiera liczby parzyste zapisane w systemie
dwójkowym. 

## Zadanie 6.4. (0–3) 

Podaj sumę wszystkich liczb z pliku `liczby.txt`, które zapisano w systemie ósemkowym.
Wynik podaj w systemie dziesiętnym. 

## Zadanie 6.5. (0–4) 

Podaj kod największej oraz kod najmniejszej spośród liczb zakodowanych w pliku
`liczby.txt` oraz ich wartości w systemie dziesiętnym. 

Zadanie 6. Systemy liczbowe - odpowiedzi
===========================

## Zadanie 6.1. (0–1) 

Za podanie poprawnej liczby wystĊpujących kodów liczb
reprezentujących liczby zapisane w systemie
ósemkowym **(103) – 1 punkt**

## Zadanie 6.2. (0–2) 

Za podanie poprawnej liczby wystĊpujących kodów
reprezentujących liczby zapisane w systemie
czwórkowym, w których nie wystĊpuje cyfra 0 **(29) – 2
punkty**

## Zadanie 6.3. (0–2)

Za podanie poprawnej liczby wystĊpujących kodów
reprezentujących liczby parzyste zapisane w systemie
dwójkowym **(153) – 2 punkty**

## Zadanie 6.4. (0–3) 

Za podanie w systemie dziesiętnym poprawnej sumy
wszystkich liczb reprezentowanych przez kody zapisane
w systemie ósemkowym **(887918739) – 3 punkty**
Za podanie sumy w systemie ósemkowym
**(64731102238) – 2 punkty**

## Zadanie 6.5. (0–4) 

Za podanie poprawnej najmniejszej i największej liczby
zakodowanej i w systemie dziesiętnym – **4 punkty**\
**- najmniejsza: 100002, 16 – 2 punkty**\
**- największa: 8066218209, 347931225 – 2 punkty.**\
**Uwaga:** za kaĪdy poprawny kod i liczbĊ – po 1 punkcie 