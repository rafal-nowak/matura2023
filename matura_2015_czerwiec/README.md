# Zadanie 6. Kody kreskowe
*Standard Code 25* jest sposobem kodowania stosowanym do oznaczania towarów spożywczych i przemysłowych. *Standard Code 25* pozwala na zapisywanie liczby o dowolnej liczbie cyfr.

Struktura napisu w *Standard Code 25* wygląda następująco:
- Znak **START** kodowany jako: 11011010
- Kolejne cyfry kodowane są zgodnie z poniższą tabelą (zapisaną również w dostarczonym pliku cyfra_kodkreskowy.txt)
- Cyfra Kod kreskowy
 - **0**  - 10101110111010
 - **1**   - 11101010101110
 - **2**  - 10111010101110
 - **3**  - 11101110101010
 - **4**  - 10101110101110
 - **5**  - 11101011101010
 - **6**  - 10111011101010
 - **7**  - 10101011101110
 - **8**  - 11101010111010
 - **9**  - 10111010111010
- Kod cyfry kontrolnej. Cyfra ta powstaje poprzez:
 - zsumowanie cyfr kodowanej liczby występujących na pozycjach parzystych, przy czym najmniej znacząca cyfra (cyfra jednostek) występuje na pozycji 0, cyfra dziesiątek – na pozycji 1, itd.
 - zsumowanie cyfr kodowanej liczby występujących na pozycjach nieparzystych,
 - dodanie potrojonej pierwszej z tych sum do drugiej sumy,
 - wyliczenie reszty modulo 10 z tak otrzymanego wyniku, odjęciu jej od 10 i ponownemu policzeniu reszty modulo 10.
- Znak **STOP** kodowany jako: 11010110.


Przykład:
Zakodujemy liczbę: 764321
Znak **START** kodowany jest jako: **11011010** Cyfra **7** kodowana jest jako: **10101011101110** Cyfra **6** kodowana jest jako: **10111011101010** Cyfra **4** kodowana jest jako: **10101110101110** Cyfra **3** kodowana jest jako: **11101110101010**
Cyfra **2** kodowana jest jako: **10111010101110** Cyfra **1** kodowana jest jako: **11101010101110**

Teraz obliczmy sumę kontrolną:
Suma cyfr liczby **764321** z pozycji parzystych pomnożona przez 3: **(1 + 3 + 6) * 3 = 30**
Suma cyfr liczby **764321** z pozycji nieparzystych: **(2 + 4 + 7) = 13**
Dodajemy obie sumy: **30 + 13 = 43**
Znajdujemy resztę z dzielenia przez 10: **43 mod 10 = 3**
Odejmujemy wynik od 10: **10 – 3 = 7**
Obliczamy resztę z dzielenia przez 10: 7 mod 10 = 7, czyli jako cyfry kontrolnej użyjemy **7**, która kodowana jest jako: **10101011101110**
Znak **STOP** kodowany jako: **11010110**

| Start  | 7  | 6  | 4  | 3  | 2  | 1  | Cyfra kontrolna (7 w tym wypadku)| stop  |
| ------------ | ------------ | ------------ | ------------ | ------------ | ------------ | ------------ | ------------ | ------------ |
| 11011010  | 10101011101110   | 10111011101010  |  10101110101110 |   11101110101010 | 10111010101110  |   11101010101110| 10101011101110  |   11010110|


W pliku ***kody.txt*** znajduje się 500 sześciocyfrowych liczb naturalnych, po jednej w każdym wierszu. W wybranym przez siebie języku programowania napisz program, który w kolejnych wierszach plików tekstowych *kody1.txt*, *kody2.txt*, *kody3.txt*, czyli w wierszach odpowiadających kolejnym wierszom kliku ***kody.txt***, zapisze odpowiednio:

### Zadanie 6.1
Dla każdej liczby **N** z pliku *kody.txt*, dwie liczby całkowite oddzielone pojedynczym znakiem odstępu – sumę cyfr liczby **N** z pozycji parzystych i sumę cyfr liczby **N** z pozycji nieparzystych;

### Zadanie 6.2
Dla każdej liczby **N** z pliku *kody.txt*, cyfrę kontrolną tej liczby w systemie *Standard Code 25* i po znaku odstępu odpowiadający tej cyfrze kod;

### Zadanie 6.3
Dla każdej liczby **N** z pliku *kody.txt*, jej kod w systemie *Standard Code 25*. Wszystkie pliki wynikowe do tego zadania powinny mieć po 500 wierszy.


# Opowiedzi:
### Zadanie 6.1
- Za podanie dla każdej liczby poprawnej wartości sumy cyfr na pozycjach parzystych – **2 pkt.**
- Za podanie dla każdej liczby poprawnej wartości sumy cyfr na pozycjach nieparzystych – **2 pkt.**
- Zmiana kolejności kolumn bez straty punktów.

Odp:
> 123


### Zadanie 6.2
- Za podanie dla każdej liczby poprawnej wartości sumy cyfry kontrolnej w systemie dziesiętnym – **3 pkt.**
- Za podanie dla każdej liczby poprawnego kodu kreskowego odpowiadającego cyfrze kontrolnej – **2 pkt**
- Zmiana kolejności kolumn bez straty punktów.

Odp:
>123

### Zadanie 6.3
- Za poprawne połączenie kodów startu, kodu cyfry, kodu cyfry kontrolnej (nawet nieprawidłowo obliczonej) i kodu stopu – **3 pkt**
- Zmiana kolejności kolumn bez straty punktów.

Odp:
>1232

