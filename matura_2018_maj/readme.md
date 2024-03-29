# Zadanie 4 - WEGA

W ramach projektu WEGA naukowcom udało się odczytać sygnały radiowe pochodzące z przestrzeni kosmicznej. Po wstępnej obróbce zapisali je do pliku `sygnaly.txt`.

W pliku `sygnaly.txt` znajduje się 1000 wierszy. Każdy wiersz zawiera jedno niepuste słowo złożone z wielkich liter alfabetu angielskiego. Długość jednego słowa nie przekracza 100 znaków.

Napisz **program(y)**, który(e) da(dzą) odpowiedzi do poniższych zadań. Odpowiedzi zapisz w pliku `wyniki4.txt`, a każdą odpowiedź poprzedź numerem oznaczającym odpowiednie zadanie.

**Uwaga**: Plik przyklad.txt zawiera dane przykładowe spełniające warunki zadania. Odpowiedzi dla danych z pliku `przyklad.txt` są podane pod pytaniami.


## Zadanie 4.1. (0–3)

Naukowcy zauważyli, że po złączeniu dziesiątych liter co czterdziestego słowa (zaczynając od słowa czterdziestego) otrzymamy pewne przesłanie. Wypisz to przesłanie.

**Uwaga**: Każde co czterdzieste słowo ma co najmniej 10 znaków. Dla danych z pliku `przyklad.txt` wynikiem jest:\
`NIECHCIMATURAPROSTABEDZIE`


## Zadanie 4.2. (0–4)

Znajdź słowo, w którym występuje największa liczba różnych liter. Wypisz to słowo i liczbę występujących w nim różnych liter. Jeśli słów o największej liczbie różnych liter jest więcej niż jedno, wypisz pierwsze z nich pojawiające się w pliku z danymi.

Dla danych z pliku `przyklad.txt` wynikiem jest:\
`AKLMNOPRSTWZA 12`

## Zadanie 4.3. (0–4)


W tym zadaniu rozważmy odległość liter w alfabecie – np. litery `A` i `B` są od siebie oddalone o 1, `A` i `E` o 4,`F` i `D` o 2, a każda litera od siebie samej jest oddalona o 0. Wypisz wszystkie słowa, w których każde dwie litery oddalone są od siebie w alfabecie co najwyżej o 10. Słowa wypisz w kolejności występowania w pliku `sygnaly.txt`, po jednym w wierszu.

Na przykład `CGECF` jest takim słowem, ale `ABEZA` nie jest (odległość `A` – `Z` wynosi 25).

Dla danych z pliku `przyklad.txt` wynikiem jest :

`AAAAAAAAAI`\
`AAAAAAAAAE`\
`AAAAAAAAAC`\
`AAAAAAAAAH`\
`AAAAAAAAAC`\
`AAAAAAAAAI`\
`AAAAAAAAAA`\
`BB`\
`AAAAAAAAAA`\
`AAAAAAAAAA`\
`AAAAAAAAAB`\
`AAAAAAAAAE`\
`AAAAAAAAAD`\
`AAAAAAAAAI`\
`AAAAAAAAAE`

# Zadanie 4 - odpowiedzi

## Zadanie 4.1
**Schemat punktowania**

3 p. – *za prawidłową odpowiedź.*
- 1 p. – *za podanie wynikowego słowa z jednym błędem.*

0 p. – *za błędną odpowiedź albo za brak odpowiedzi.*

*Uwaga: Nie przyznaje się 2 p.*

**Poprawna odpowiedź:**\
``ZAPISZODPOWIEDZIWPLIKUTXT``

## Zadanie 4.2
Schemat punktowania

4 p. – *za podanie prawidłowego słowa i liczby liter.* 
- 2 p. – *za podanie tylko prawidłowego słowa.*

0 p. – *za błędną odpowiedź albo za brak odpowiedzi.*

*Uwaga: Nie przyznaje się 3 p i 1 p.*

**Poprawna odpowiedź:**\
`26`\
`SUOLDQWISCDRFLRWHZBNTMIAPHALMNCWHVGMXOZSQNXWXSFELZVTUTI LXWKCTYBQYSUAKNYJKRXDJQYHXAQGWN`

## Zadanie 4.3
Schemat punktowania

4 p. – *za podanie prawidłowej listy słów, w których każde dwie litery są oddalone co najwyżej 10*
- 2 p. – *za podanie listy słów powstałej przez porównanie odległości tylko sąsiadujących liter (jest 207 takich słów).*

0 p. – *za inną błędną odpowiedź albo za brak odpowiedzi.*

*Uwaga: Nie przyznaje się 3 p i 1 p.*

**Poprawna odpowiedź**\
Lista słów:\
`QQMLKKQNOHPKKPJOLHIPJKLKQIIHQHPNKNQPHNKLKQNIMLQPNLPMHNNIPNJJONQOHKKQO IHOHHJMOJPMNIPIKION PTPNTOLNOPOSKLQOQKNTQTPLPNLNRRSTNNSMRNNMLPNLKORTSMNKRTLLLLNRKKOLKTR QOQOQONKTKRSPTTORMKQTRNOKKQ JONLNPOJRPKPMMSQOLPLNNMKLJKOPRKRKNSJMSOJQPLOOLSOJQSOLLOQKSOJJMNRKMJMJP QKJRSMJQ TWUSWQTTOUXUTVTWWUTSXUWXWXRPSXOTQQUPPXUPRUOSURVQWSWSOUQSXOSQQXTW SWTW  
IICEGIFCCGBEBCKDBIGIH FAAEEDBACDGEDCEBGEEFAAGBCFEFCCDFEGGGACFBBAGGEADGAAGEE PNMTNQSOQOSTQLPTPTRNPMMQKTQNKPTROORQSTTSTKKTKLTTMNMQQSQKLKROSONOTNR OONOPTQPPKMRTKMROPKTLTLRKQQKMOM  
OO  
FH  
AE
VSQRYRRWQYQWXWXUUXPVWWUTSXYPXQVPSVXWYRXXRSPPYUVYWQUVSSPQTWXPTQPQ TYSUSWTYRPXUX DAACAEDDABDBBCADAEDDCABABDDDBCEBCDEAEBCEDAEADDABBEBBAAADBDDCCCECBE ABBBBCBEBCABA FDEEBCDBDBFFFCCFCADBCBEEFAFFCEAEDDFCFCDDACEFCEBFDFCCFBFCCCBDDEADCACBD BBB
DCCDEBCHCHADBHFBFHBCGCAAFBHBHDEGCCFFGAHEGCCHHECDAFCECFEEBEEFEE OPQPHIHQQIQLQPPMNIJPIPLON  
EEL
SRMQOLLOLTSPUMRUMRTNPRRLSUSRTRT OJQMKJOPQKKQOORKKOMNJQKKMNKQRNNQOLJKNNMSKLMSSMSRLNPRSNO HBDHIFAGHAJHADDCECACFHDHCHJJFDIGEFGBBGEICDJGJAJFDGAHGCBCEAFDEJADGJAHIJGD EDBIDECAJBEI
NMFEN  
CCHHGEHEHBGAEDCGHCECHFFHECDEDCHECABFHDGDECBGFAH XWYYYXWTTXTYWWUWYUXWVTVXTYYTYYTTXVVVYWXTUTXXWXYYUUTXTXT EFCHGGIJKFDBFKFCEGHHFFGGHGFHKEEGKHIFBJBKDGFGCFKIIEHGICGFJH RQSRQSRSRRLPNNLQTTQMOSRTQPQLPLPLPMRMNM SSQRTSNOUPOSVQUOQVSPOQRSNORUUTSNSSWRRPPVOUQOUU EABEGFBFAGDEECGEBFBBFFAECDGGFCBCFDCEABDGBGEBEEFFGCGDDAAGFDBG JFKKFMJFMIILOLFOMOMGNFNLKHKHNGLOJJIOIOJLLKLFIJIHOJFLLKLGIGGIILNNJMOLIGGHLFI NOOOJ VVXUVSUUTWSWTXYTYUVTTWTYSWXUSWYTTXTYXVSWUSVSYUSYTUUTXUSWTSUYVTXY UXTYXVYUWVSVWWVUUTSTXUWS JHJKDFGHHFGFHEJGGGIDCEHFLFCFDJDLDJHGGCGILCLKJHLKDFGICL OGHFKHFKHONHFFIHHFNKINIOFHKIONMONNOGLMFOGOJKNFHGILOHHOIHFIHNFGGHJGGHIF INMNFNHFLMOIMLOMNMLJIHOGNJHN OJMNHMJMJKPKPKLPPIHNMMMPNHKMQNIJJNOLQKHKIPQQPQMIKNIHHIOJONKOJJLOOOMKL OQKKHNJJHPJJKMJHO DJJBHGFGGDKIKCHKGKBFEKFEFJEGEHCHIFBDBGKJKCDGDCIDIBEBDGCGFKCGFFCHJJEJBJCIH KKBHIEGKDG YWUUSRXWSQTYVXVVUTRXWWVVUQQVTSXUWWVXUXTSTSSRWTTWXWUYURVYTWTXXV YVUUWURQUYUU  
MOQIPPOMHJMJJLNKKOIJLIJMMQPIPJMNMMQ TXTUVUWWUUUWUWUXWYWXXTTXWWYWUVXXXVYWYWYVUYYUYTXVUXUTTUYTYUTX YWXWTVVYXTYWUWWWUYUVTUXVTVWYXWVYWV  
EEEEB
WUYTXVXUXVWXVTUVTUUTUTWVVVTUXXUVTXUVYVYXXUUYWVUUUVYYYUXTUUUTWU VYXWVYTYUTYYTTWUUVXXUVYXTUXTWTYYVT WXVUYUXYUUVYXTWVVTXVYYVXXWWUTUXXUVXWUYWTWTWWUWXVUYXYUYVTTXUU W  
WVSSQSSXRUUPVQXVTPYSTYURWTSURYVRVPPWXVXUVWQUXQSWWUWTXTSU DEBDBDCDECCABAAEBBDEDBCCADA  
QQ  
GIDIHFGKLLKE  
TQYQTWRPXTQSWSYVSYSWVYRWSRPTSXVXPT VOSVQOSQQTUOOTXUTSVXUSWWRXWPXVVUSWURSWTWPSOWWXXPUTXVVXRTURSWTSXQ WXWUTSOPTTPSPWQUPVXQXPVXSSOQOUXV UVWUYYYYXWUWXYVVWXVXVYWYWYYVUXUYUXUVWWYXWXWUVWWVUWXWUXYUYU WWYUWXVVWVWWVUYUVXXVYUWWUWXVXW GGAGFAHGGDGEHDEGDHDGHHFDFGDGBCDACCCCDHAFDFEECEAGFDHA EABDAADFECFAEEBBADBCBAEAADADEADBADAFEBDFEFDDBCCBBBCACBADEDEADFFEFEBF EABBDFCFBBBFCCFEFCCD EIFEACGHGGGBDBGCCBFDCGCICHDHDEEACIAHCBAHAHHIDIDGHIBIBABECGEHDCGFEFFEHB EGHBIIFIEBBCBDAEDFEADHHFFEDGIA  
UYYSRSXUWWXTXYSVVRWRTQTXXWSYVRTUW  
BFFH  
IKCHJKBJFFEFGGFFBGGGIHFIFFHBBGCHGBGFBGJFJIDGDCCECGJBBCKEDGBBGG IJJBGAJBGDFJFHJIGJDDBFAIAGFCDAHEBEIGBCIIJBFIDEEFHDAIFJDEGAAIBHCDBCFDCGJIBD TRRPOURNVTRWWOWOURNQTVTRTVWOWVTOSPWOTSORTNR DEHDDEAHFBBCEBDFCGHDDFEHHDBCDDFECDFADAGFDGEBEFCBFADHEHAEBACGFCDDECA G
QNUSNNUWSOQQRVWQRTNSPNNQTQUUTUPSOWSUTSNQTUTWSRWQTNRQRVTUNOSNUQUVN ORONSRSUWPPPNRRSWQNSSWNSNUSUOOVWQ  
BEFEC QRTWTPPURPUXWWRWOPOVXTVPXTWTOTUOOPROTOPXVUOWWWTOPOTWPTQOSWOVRPQT UTVVTSVUSRWSS PSMUQPPSSPTQNTNVTMNUVSUPNRNVNOOTVRSQPSNNVUPPPVTSMRUTUVMRNRMQTQQVMSS MOSRTRT
UU XVXXUUWUYTYVVWWSUWSUSSUSTYTVYWVTYTTSWSVYYYVTXYSYWSUYWXTUXVSWWW VTWYWXUSUWVXWSYUVWUXYSWTTSYVYVVTYYYVXX AAHEGCCGGBCECGBDBIADEDCIEICEFGBGAGA GLICJLIIKKKDILKEDEJEFFLGECLFFIFGFHIGIJGKDFGEHGKLKDEDLCFFICGJHIJEHJFDFLDHGIDL KEEJLEDEECIJGIIGJKCCJDJF ABBDCAEEEBBCDAABBCDBACCCBECCBCDECEEBACEECAAEBBAEEBDEEBDABBCECBBABDA AAADEDCEDBBBCDECCCBEBECAACABBCDBA  
GDEKFJKKLLLEJGK JJGHLMMMFMIFHONHGOINFIJKIJGJMJOIKHNOIGHKMMGNMJJMFMHNHFOLOMMOMFIGLLNHH IKLGOIIMNFLLFFOKHNONLMNMMONMLJ UVVUXVUXWWXVXUWXXYWYWUVYYXYVXXVYXWUUXWWWYWVVWUYVUWXXYXUXYY WWWYUUXYUVWXYYUYXUUUVXXYXWUXXXUUWVUVWWYU`
