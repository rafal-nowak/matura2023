# Zadanie 4. Galerie handlowe
Firma *Igloo* planuje w wybranych miastach Europy wybudować galerie handlowe. W każdej
z planowanych galerii może znajdować się różna liczba lokali handlowych. Wszystkie lokale
handlowe będą miały kształt prostokąta.

W pliku `galerie.txt` zapisanych jest 50 wierszy z informacjami dotyczącymi planowanych
galerii. Każdy wiersz w pliku to informacja o jednej galerii. Dane oddzielone są spacją
i zawierają odpowiednio:
- kod kraju;
- nazwę miasta (nazwy miast nie powtarzają się);
- 70 par liczb (140 liczb) określających wymiary (długość i szerokość w metrach) lokali
handlowych, które znajdować się będą w danej galerii. Jeżeli liczba lokali w galerii jest
mniejsza niż 70, to wiersz uzupełniony jest zerami.

**Przykład:**
NL Amsterdam 8 4 5 12 7 5 5 11 9 4 7 6 … 0 0 0 0 0 0\
Do Twojej dyspozycji jest pomocniczy plik `galerie_przyklad.txt`, zawierający
10 wierszy, który możesz wykorzystać, aby sprawdzić poprawność działania swojego(-ich)
programu(-ów).\
**Napisz program(-y)**, w wyniku działania którego(-ych) otrzymasz odpowiedzi do podanych
zadań. Pliki źródłowe z rozwiązaniem zapisz pod nazwą zgodną z numerem zadania,
z rozszerzeniem odpowiadającym użytemu narzędziu informatycznemu.

## Zadanie 4.1. (0−4)
Dla każdego kraju z pliku `galerie.txt` wyznacz liczbę miast, w których powstaną galerie.
W każdym wierszu pliku powinny znajdować się: kod
państwa oraz informacja o liczbie miast.\
Dla danych z pliku `galerie_przyklad.txt` prawidłowa odpowiedź to:\
H 1\
I 2\
F 1\
GB 1\
D 3\
NL 1\
DK 1

## Zadanie 4.2. (0−4)
**a.** Oblicz całkowitą powierzchnię handlową każdej galerii (jako sumę powierzchni wszystkich
lokali w danej galerii) oraz liczbę lokali. W każdym wierszu pliku wynikowego powinny
się znaleźć: nazwa miasta, powierzchnia galerii znajdującej się w danym mieście oraz
liczba lokali, rozdzielone znakiem spacji.

Dla danych z pliku `galerie_przyklad.txt` prawidłowa odpowiedź to:\
Budapeszt 3598 64\
Neapol 3352 48\
Marsylia 3444 56\
Leeds 2952 44\
Frankfurt 3515 57\
Genua 3386 56\
Dortmund 3697 57\
Rotterdam 3184 49\
Dusseldorf 3737 63\
Kopenhaga 3765 60

**b.** Podaj nazwę miasta z galerią o największej powierzchni całkowitej oraz nazwę miasta
z galerią o najmniejszej powierzchni całkowitej. Jest dokładnie jedno miasto z galerią
o największej powierzchni i jedno z galerią o najmniejszej powierzchni. W pliku wynikowym powinny znaleźć się nazwy
miast wraz z powierzchniami galerii.

Prawidłowa odpowiedź dla danych pliku `galerie_przyklad.txt`:\
Kopenhaga 3765\
Leeds 2952

## Zadanie 4.3. (0−4)
Powiemy, że dwa lokale są tego samego rodzaju, jeżeli ich powierzchnia jest taka sama.
W którym mieście powstanie galeria z największą liczbą różnych rodzajów lokali (jest jedno
takie miasto), a w którym powstanie galeria z najmniejszą liczbą różnych rodzajów lokali (jest
jedno takie miasto)? Podaj te miasta oraz liczby różnych rodzajów lokali w tych miastach.
W każdym z dwóch wierszy pliku powinny znajdować się nazwa miasta oraz liczba różnych rodzajów lokali w tym mieście.

Prawidłowa odpowiedź dla danych pliku `galerie_przyklad.txt`:\
Dusseldorf 34\
Genua 23

# Zadanie 4 - ocenianie

## Zadanie 4.1
**Zasady oceniania**\
4 pkt – za poprawną odpowiedź, w tym:\
2 pkt – za wygenerowanie listy kodów krajów bez powtórzeń,\
2 pkt – za wyznaczenie liczby miast w danym państwie.\
1 pkt – za wygenerowanie listy kodów krajów (z powtórzeniami).\
0 pkt – za odpowiedź niepoprawną albo za brak odpowiedzi.


**Rozwiązanie**\
GB 5\
D 15\
E 6\
I 6\
F 2\
RO 1\
A 1\
H 1\
BG 1\
CZ 1\
B 1\
S 1\
HR 1\
NL 2\
LV 1\
GR 1\
LT 1\
FIN 1\
DK 1\
IRL 1

## Zadanie 4.2
**Zasady oceniania**\
4 pkt – za poprawną odpowiedź, w tym:\
3 pkt – za podanie listy galerii wraz z powierzchniami całkowitymi i liczbą lokali,\
(w przypadku listy zawierającej tylko powierzchnie lub tylko liczbę lokali – 2 pkt),\
1 pkt – za podanie miasta z największą galerią i miasta z najmniejszą galerią.\
0 pkt – za odpowiedź niepoprawną albo za brak odpowiedzi.

**Rozwiązanie**

**a**
Londyn 3628 58\
Berlin 3777 59\
Madryt 2217 34\
Rzym 3678 51\
Paryz 3889 62\
Bukareszt 1957 33\
Wieden 2694 42\
Hamburg 3518 52\
Budapeszt 3598 64\
Barcelona 4059 60

...

Brema 2948 44\
Sheffield 2324 36\
Hanower 3532 53\
Lipsk 1871 29\
Kopenhaga 3765 60\
Drezno 1900 26\
Dublin 1986 31\
Norymberga 4178 69\
Duisburg 3948 61

**b**\
Essen 4760\
Wilno 1620

## Zadanie 4.3
**Zasady oceniania**\
2 pkt – za poprawną odpowiedź.\
1 pkt – za numery telefonów bez liczby połączeń.\
0 pkt – za odpowiedź niepoprawną albo za brak odpowiedzi.

**Rozwiązanie**\
4546455 8\
3505978 7\
4657345 6
