# **Zadanie 4. Liczby i ich odbicia**
W pliku <kbd>`liczby.txt`</kbd> zapisano 100 nieparzystych liczb całkowitych z przedziału [10, 9999]. Liczby w pliku mogą się powtarzać.

**Odbiciem** dodatniej nieparzystej liczby całkowitej n nazywamy taką liczbę *N*, w której zapisie 
dziesiętnym nastąpiło odwrócenie kolejności cyfr.

**Przykład**:\
Odbiciem liczby 2019 jest 9102, natomiast odbiciem liczby 12345 jest 54321.

**Napisz program** (lub kilka programów), który(-e) znajdzie(-dą) odpowiedzi na poniższe 
pytania. Każdą odpowiedź zapisz w pliku <kbd>`wyniki4.txt`</kbd> i poprzedź ją numerem 
oznaczającym zadanie.

Do dyspozycji masz również plik <kbd>`przyklad.txt`</kbd> zawierający tylko 11 nieparzystych liczb 
całkowitych z przedziału [10, 9999] – odpowiedzi dla tego pliku podane są w treściach 
zadań, możesz sprawdzać na nim działanie swojego programu. 

**Uwaga:** Pamiętaj, że Twój program (lub kilka programów) musi(-szą) ostatecznie działać dla 
100 liczb zapisanych w pliku <kbd>`liczby.txt`</kbd>.

## **Zadanie 4.1. (0–3)**
---
Wyznacz odbicia wszystkich liczb z pliku <kbd>`liczby.txt`</kbd>. Wypisz te odbicia, które są 
podzielne przez 17.

Dla pliku <kbd>`przyklad.txt`</kbd> odpowiedzią jest 51.

## **Zadanie 4.2. (0–3)**
---
Dla każdej liczby z pliku <kbd>`liczby.txt`</kbd> oblicz wartość bezwzględną różnicy tej liczby i jej 
odbicia. \
Wyznacz taką liczbę *n*, dla której wartość bezwzględna różnicy tej liczby i jej odbicia jest 
największa. Podaj tę liczbę oraz wartość bezwzględną różnicy tej liczby i jej odbicia.\
W pliku <kbd>`liczby.txt`</kbd> jest tylko jedna taka liczba.

Dla pliku <kbd>`przyklad.txt`</kbd> odpowiedzią jest 741 594.

## **Zadanie 4.3. (0–3)**
---
Wypisz wszystkie liczby pierwsze z pliku <kbd>`liczby.txt`</kbd>, których odbicia również są liczbami 
pierwszymi, każdą w oddzielnym wierszu.

Dla pliku <kbd>`przyklad.txt`</kbd> odpowiedź to:\
13\
131\
(odbiciem liczby 13 jest 31 – obie są liczbami pierwszymi, odbiciem 131 jest 131)

## **Zadanie 4.4. (0–3)**
---
Podaj:
- ile różnych liczb zapisano w pliku <kbd>`liczby.txt`</kbd>
- ile liczb powtarza się dokładnie dwa razy w pliku <kbd>`liczby.txt`</kbd>
- ile liczb powtarza się dokładnie trzy razy w pliku <kbd>`liczby.txt`</kbd>.

Dla pliku <kbd>`przyklad.txt`</kbd> odpowiedzią jest 10 1 0.

# **Zadanie 4. Liczby i ich odbicia - odpowiedzi** 
## **Zadanie 4.1. (0–3)**
---
**Zasady oceniania**\
3 pkt – za poprawną odpowiedź (przy tym 119 może być zapisana raz).\
2 pkt – w przypadku nieuwzględnienia warunku, że odbicia mają być podzielne przez 17. \
1 pkt – za wypisanie liczb podzielnych przez 17 zamiast odbić tych liczb.\
0 pkt – za odpowiedź niepoprawną albo za brak odpowiedzi.

**Rozwiązanie**\
1156\
102\
51\
765\
119\
119\
731

## **Zadanie 4.2. (0–3)**
---
**Zasady oceniania**\
3 pkt – za poprawną odpowiedź, w tym:
- 1 pkt – za największą wartość bezwzględną różnicy
- 2 pkt – za liczbę.

2 pkt – za podanie odpowiedzi bez uwzględnienia wartości bezwzględnej (6511 5355).\
0 pkt – za odpowiedź niepoprawną albo za brak odpowiedzi.

**Rozwiązanie**\
1129 8082

## **Zadanie 4.3. (0–3)**
---
**Zasady oceniania**\
3 pkt – za poprawną odpowiedź.\
2 pkt – za wypisanie wszystkich liczb, których odbicia są liczbami pierwszymi.\
1 pkt – wypisanie wszystkich liczb pierwszych.\
0 pkt – za odpowiedź niepoprawną albo za brak odpowiedzi. 

**Rozwiązanie**\
157\
31 \
347 \
929 \
941 \
761

## **Zadanie 4.4. (0–3)**
---
**Zasady oceniania**\
3 pkt – za poprawną odpowiedź, w tym:
- 1 pkt – liczbę różnych liczb w pliku
- 1 pkt – liczbę liczb, które powtarzają się 2 razy
- 1 pkt – liczbę liczb, które powtarzają się 3 razy.

0 pkt – za odpowiedź niepoprawną albo za brak odpowiedzi. 

**Rozwiązanie**\
85 (różnych)\
13 (powtarzających się 2 razy)\
1 (powtarzająca się 3 razy)