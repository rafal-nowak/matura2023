# **Zadanie 4. Luki w ciągu**

*Luką* w ciągu liczbowym nazywamy **bezwzględną wartość różnicy** między dwoma kolejnymi
elementami. <br>
Przykładowo – w czteroelementowym ciągu: <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5, 2, 7, 10 <br>
są trzy luki: <br>
− luka pomiędzy pierwszym a drugim elementem wynosi 3; <br>
− luka pomiędzy drugim a trzecim elementem wynosi 5; <br>
− luka pomiędzy trzecim a czwartym elementem wynosi 3. <br>

*Największa luka* w tym ciągu ma wartość 5.

W pliku `dane4.txt` znajduje się ciąg złożony z 1 000 dodatnich liczb całkowitych nie
większych od 2⋅10<sup>9</sup>. **Napisz program(-y)**, który(-e) da(-dzą) odpowiedzi do poniższych zadań.
Odpowiedzi zapisz w pliku `zadanie4.txt`, a każdą poprzedź numerem odpowiedniego
zadania. <br> <br>

## **Zadanie 4.1. (0–3)** <br>
Podaj wartość największej luki oraz wartość najmniejszej luki pomiędzy elementami ciągu
z pliku `dane4.txt`. <br> <br>

## **Zadanie 4.2. (0–4)** <br>
Fragment ciągu nazywamy *regularnym*, jeśli wszystkie jego luki mają tę samą wartość. <br>
Przykładowo – w ciągu: <br> <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4, 11, 4, 1, 4, 7, 11, 12, 13, 14, 7, 0, 3 <br> <br>
regularnymi są następujące fragmenty: <br> 
− 4, 11, 4 – luka między jego elementami wynosi 7; <br>
− 4, 1, 4, 7 – luka między jego elementami wynosi 3; <br>
− 7, 11 – luka między jego elementami wynosi 4; <br>
− 11, 12, 13, 14 – luka między jego elementami wynosi 1; <br>
− 14, 7, 0 – luka między jego elementami wynosi 7; <br>
− 0, 3 – luka między jego elementami wynosi 3. <br> <br>
Znajdź <ins>najdłuższy</ins> fragment regularny w ciągu z pliku `dane4.txt`. Podaj jego długość oraz
wartości (liczby) znajdujące się na początku i końcu tego fragmentu. W pliku z danymi jest
jeden taki fragment. <br> <br>
W powyższym przykładzie długość najdłuższego fragmentu regularnego jest równa 4. Takie
fragmenty w przykładzie są dwa. Jeden zaczyna się od liczby 4 i kończy liczbą 7, a drugi
zaczyna się od liczby 11 i kończy liczbą 14. <br> <br>

## **Zadanie 4.3.** (0–4) <br>
*Krotnością* luki nazywamy liczbę jej wystąpień. *Najczęstszą* luką nazywamy lukę
o największej krotności. <br> 
Przykładowo – w ciągu: <br> <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 5, 2, 7, 10 <br> <br>
luka 5 ma krotność 1, a luka 3 ma krotność 2 i wobec tego jest najczęstszą luką. <br> <br>
Podaj krotność najczęstszej luki oraz wartości wszystkich najczęstszych luk w ciągu z pliku
`dane4.txt`. <br> <br>
W przykładzie z zadania 4.2 (ciąg 4, 11, 4, 1, 4, 7, 11, 12, 13, 14, 7, 0, 3) krotność najczęstszej
luki wynosi 4. Tę krotność mają luki 7 i 3. <br> <br> <br> <br>

# **Zadanie 4. Luki w ciągu - odpowiedzi** <br> <br>

## **Zadanie 4.1** <br>
**Schemat punktowania** <br>
3 p. – za prawidłową odpowiedź, w tym: <br>
2 p. – za podanie największej luki, <br>
1 p. – za podanie najmniejszej luki. <br>
0 p. – za błędną odpowiedź albo za brak odpowiedzi. <br><br>

**Poprawna odpowiedź** <br>
Najmniejsza 1 <br>
Największa 1056392131 <br> <br>
## **Zadanie 4.2** <br>
**Schemat punktowania** <br>
4 p. – za podanie prawidłowej odpowiedzi, w tym: <br>
2 p. – za podanie długości najdłuższego regularnego fragmentu ciągu, <br>
1 p. – za podanie początku najdłuższego regularnego fragmentu ciągu, <br>
1 p. – za podanie końca najdłuższego regularnego fragmentu ciągu <br>
0 p. – za błędną odpowiedź albo za brak odpowiedzi. <br><br>
**Poprawna odpowiedź** <br>
Największa długość fragmentu regularnego: 17 <br>
Początek: 193134524 <br>
Koniec: 223545714 <br><br>

## **Zadanie 4.3** <br>
**Schemat punktowania** <br>
4 p. – za podanie prawidłowej odpowiedzi, w tym: <br>
2 p. – za podanie krotności najczęstszej luki, <br>
po 1 p. – za podanie wartości każdej z dwóch najczęstszych luk. <br>
0 p. – za błędną odpowiedź albo za brak odpowiedzi. <br><br>

**Poprawna odpowiedź** <br>
Krotność najczęstszej luki: 31 <br>
Wartości najczęstszych luk: <br>
149 <br>
11 <br>

