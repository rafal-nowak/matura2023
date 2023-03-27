
# Zadanie 6. Piksele
W pliku dane.txt znajduje się 200 wierszy. Każdy wiersz zawiera 320 liczb naturalnych
z przedziału od 0 do 255, oddzielonych znakami pojedynczego odstępu (spacjami).
Przedstawiają one jasności kolejnych pikseli czarno-białego obrazu o wymiarach 320 na 200
pikseli (od 0 – czarny do 255 – biały).

Napisz program(y), który(e) da(dzą) odpowiedzi do poniższych zadań. Odpowiedzi zapisz
w pliku wyniki6.txt, a każdą odpowiedź poprzedź numerem oznaczającym odpowiednie
zadanie.

Uwaga: plik przyklad.txt zawiera dane przykładowe spełniające warunki zadania (obraz
ma takie same rozmiary). Odpowiedzi dla danych z pliku przyklad.txt są podane pod
poleceniami.

# Zadanie 6.1. (0–2)
Podaj jasność najjaśniejszego i jasność najciemniejszego piksela.
Dla danych z pliku przyklad.txt wynikiem jest 255 (najjaśniejszy) i 0 (najciemniejszy).
# Zadanie 6.2. (0–2)
Podaj, ile wynosi najmniejsza liczba wierszy, które należy usunąć, żeby obraz miał pionową oś
symetrii. Obraz ma pionową oś symetrii, jeśli w każdym wierszu i-ty piksel od lewej strony
przyjmuje tę samą wartość, co i-ty piksel od prawej strony, dla dowolnego 1 ≤ i ≤ 320.
Dla danych z pliku przyklad.txt wynikiem jest 3.
# Zadanie 6.3. (0–3)
Sąsiednie piksele to takie, które leżą obok siebie w tym samym wierszu lub w tej samej
kolumnie. Dwa sąsiednie piksele nazywamy kontrastującymi, jeśli ich wartości różnią się
o więcej niż 128. Podaj liczbę wszystkich takich pikseli, dla których istnieje przynajmniej jeden
kontrastujący z nim sąsiedni piksel.
Dla danych z pliku przyklad.txt wynikiem jest 5.
# Zadanie 6.4. (0–4)
Podaj długość najdłuższej linii pionowej (czyli ciągu kolejnych pikseli w tej samej kolumnie
obrazka), złożonej z pikseli tej samej jasności.
Dla danych z pliku przyklad.txt wynikiem jest 198. 

# ___________________________________________________________________________

# # Zadanie 6. Piksele - odpowiedzi

# Zadanie 6.1. (0–2)

## Schemat punktowania
#### 2p. – za prawidłową odpowiedź, w tym
#### 1 p. – za podanie wartości najjaśniejszego piksela.
#### 1 p. – za podanie wartości najciemniejszego piksela.
#### 0 p. – za odpowiedź błędną albo za brak odpowiedzi.
## Poprawna odpowiedź
### Wartość najjaśniejszego piksela 221.
### Wartość najciemniejszego piksela 7.


# Zadanie 6.2. (0–2)

## Schemat punktowania
#### 2 p. – za poprawną odpowiedź.
#### 0 p. – za odpowiedź błędną albo za brak odpowiedzi.
#### Uwaga: Nie przyznaje się 1 p.
## Poprawna odpowiedź
### 149

# Zadanie 6.3. (0–3)

## Schemat punktowania:
#### 3 p. – za prawidłową odpowiedź.
#### 2 p. – za odpowiedź, w której różnica wartości miedzy pikselami jest większa lub równa 128 (768)
#### 1 p. – za odpowiedź do otrzymania, której nie wykorzystano wartości bezwzględnej przy obliczaniu różnicy (166 lub 587).
#### 1 p. – za odpowiedź, którą otrzymano w wyniku wielokrotnego zliczania sąsiedztwa z kontrastującym pikselem (1226).
#### 1 p. – za odpowiedź, która nie uwzględnia brzegowych pikseli (747 lub 750 lub 752)
#### 0 p. – za inną błędną odpowiedź albo za brak odpowiedzi.
## Poprawna odpowiedź
### 753

# Zadanie 6.4. (0–4)

## Schemat punktowania:
#### 4 p. – za prawidłową odpowiedź.
#### 2 p. – za podanie odpowiedzi (4) lub (6).
#### 0 p. – za inną błędną odpowiedź albo za brak odpowiedzi.
#### Uwaga: Nie przyznaje się 3 p. i 1 p.
## Poprawna odpowiedź
### 5