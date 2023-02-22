Zadanie 4. Pary
=================

W pliku `pary.txt` znajduje się 100 wierszy. Każdy wiersz zawiera parę danych składającą się z liczby całkowitej z przedziału od 3 do 100 i słowa (ciągi znaków) złożone z małych liter alfabetu angielskiego o długości od 1 do 50 znaków. Liczba i słowo są oddzielone znakiem spacji.

**Napisz program(-my)**, dający(-e) odpowiedzi do poniższych zadań. Uzyskane odpowiedzi zapisz w pliku `wyniki4.txt`, poprzedzając każdą z nich numerem odpowiedniego zadania.

## Zadanie 4.1. (0–3)

Mocna hipoteza Goldbacha mówi, że każda parzysta liczba całkowita większa od 4 jest sumą **dwóch nieparzystych** liczb pierwszych, np. liczba 20 jest równa sumie 3 + 17 lub sumie  7 + 13. 

Każdą liczbę parzystą z pliku `pary.txt` przedstaw w postaci sumy dwóch liczb pierwszych. Wypisz tę liczbę oraz dwa składniki sumy w kolejności niemalejącej. Jeżeli istnieje więcej rozwiązań (tak jak dla liczby 20) należy wypisać składniki sumy o największej różnicy.  

Wyniki podaj w oddzielnych wierszach, w kolejności zgodnej z kolejnością danych w pliku `pary.txt`. Liczby w każdym wierszu rozdziel znakiem spacji, np. dla liczby *20* należy wypisać *20 3 17*. 

## Zadanie 4.2. (0–4)

Dla każdego słowa z pliku `pary.txt` znajdź długość najdłuższego spójnego fragmentu tego słowa złożonego z identycznych liter. Wypisz znalezione fragmenty słów i ich długości oddzielone spacją, po jednej parze w każdym wierszu. Jeżeli istnieją dwa fragmenty o takiej samej największej długości, podaj pierwszy z nich. Wyniki podaj w kolejności zgodnej  z kolejnością danych w pliku `pary.txt`.  

**Przykład:**  
dla słowa *zxyzzzz* wynikiem jest: *zzzz* 4 

natomiast dla słowa *kkkabbb* wynikiem jest: *kkk* 3 

## Zadanie 4.3. (0–4)
Para *(liczba1, słowo1)* jest mniejsza od pary *(liczba2, słowo2)*, gdy:\
    – *liczba1 < liczba2*, \
albo\
    – *liczba1 = liczba2* oraz *słowo1* jest leksykograficznie (w porządku alfabetycznym) mniejsze od *słowo2*

**Przykład:**
Para *(1, bbbb)* jest mniejsza od pary *(2, aaa)*, natomiast para *(3, aaa)* jest mniejsza od pary *(3, ab)*. 

Rozważ wszystkie pary *(liczba, słowo)* zapisane w wierszach pliku `pary.txt`, dla których **<u>liczba</u> jest równa długości <u>słowa</u>**, i wypisz spośród nich taką parę, która jest mniejsza od wszystkich pozostałych. W pliku `pary.txt` jest jedna taka para. 


Zadanie 4. Pary - odpowiedzi
=================

## Zadanie 4.1. (0–3)
**Zasady oceniania**\
3 pkt – za poprawną odpowiedź.\
2 pkt – za odpowiedź, w której jest podany dowolny poprawny rozkład na dwie liczby pierwsze dla każdej liczby parzystej\
*ALBO*\
jeśli zdający nie uwzględni warunku, że liczba, której rozkładu szukamy, musi być  parzysta, i szuka także rozkładów liczb nieparzystych (ale rozkłady dla liczb parzystych otrzymuje poprawnie)\
1 pkt – za odpowiedź zawierającą rozkłady, w których dla każdej liczby parzystej występuje przynajmniej jedna liczba
pierwsza większa od 3.\
0 pkt – za odpowiedź niepoprawną albo za brak odpowiedzi.  

## Zadanie 4.2. (0–4)
**Zasady oceniania**\
4 pkt – za poprawną odpowiedź.\
3 pkt – za odpowiedź, w której zdający: pomija pierwszą lub ostatnią literę fragmentu słowa (ale nie gubi wyników składających się z pojedynczych liter) np. dla aaab wypisze aa\
*ALBO*\
poda tylko jedną kolumnę wyniku, czyli: poprawną listę fragmentów słów, ale bez długości albo poprawne maksymalne długości, ale bez fragmentów słów\
*ALBO*\
nie uwzględni przypadku, w którym najdłuższy fragment słowa znajduje się na jego końcu i otrzymuje błędne wyniki tylko dla takich słów oraz poprawne w pozostałych przypadkach\
2 pkt – za odpowiedź, w której zdający: pomija pierwszą i ostatnią literę fragmentu słowa np. dla aaaa wypisze aa\
*ALBO*\
pomija pierwszą lub ostatnią literę fragmentu słowa oraz gubi wyniki składające się  z pojedynczych liter.\
1 pkt – za odpowiedź, w której zdający wypisze listę zawierającą poprawne (istniejące) fragmenty słów złożone z takich
samych liter, ale nie o największej długości (np. pierwsze lub ostatnie występujące); uwaga: w takim przypadku wyniki złożone  z pojedynczych liter zaliczamy tylko dla słów nie zawierających spójnych fragmentów  o długości większej niż 1 złożonych z jednakowych liter. \
0 pkt – za odpowiedź niepoprawną albo za brak odpowiedzi.  

## Zadanie 4.3. (0–4)
**Zasady oceniania**\
4 pkt – za poprawną odpowiedź.\
3 pkt – za odpowiedź: 3 ast albo 3 asq.\
2 pkt – za odpowiedź, w której zdający nie uwzględnia założenia, że para ma się składać  z liczby i słowa o długości równej danej liczbie (czyli otrzymuje w wyniku parę:  3 aaaoooooooooooooooop).\
1 pkt – za odpowiedź, w której zdający wypisze liczbę 3 w parze z dowolnym innym niż wymienione wcześniej słowem trzyliterowym\
*ALBO*\
jako wynik wypisze wszystkie dziewięć słów o długości takiej jak liczba w parze.\
0 pkt – za odpowiedź niepoprawną albo za brak odpowiedzi.
