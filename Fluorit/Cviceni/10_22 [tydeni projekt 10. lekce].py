##  5. Týždenný projekt
##
##  Napíš pythonovský skript, ktorý bude definovať tieto funkcie a jednu globálnu premennú:
##    tab = []
##    def citaj(meno_suboru):
##        ...
##    def pocet_vyskytov(slovo):
##        ...
##        return 0
##    def najcastejsie():
##        ...
##        return [...]
##    def s_poctom(n):
##        ...
##        return [...]
##    def najdlhsie():
##        ...
##        return [...]
##    def najkratsie():
##        ...
##        return [...]
##    def s_dlzkou(n):
##        ...
##        return [...]
##
##  Funkcia citaj() dostáva ako parameter meno textového súboru.
##  Funkcia tento súbor prečíta a do globálnej premennej tab
##  si nejako zaznačí počet výskytov každého slova v súbore
##  (najlepšie pre každé slovo ako dvojicu: reťazec a počet výskytov).
##  Premenná tab musí byť typu zoznam (list).
##  Slová vo vstupnom súbore sú oddelené aspoň jednou medzerou alebo znakom konca riadkov.
##  Nepoužívaj ďalšie globálne premenné ani ďalšie funkcie.
##
##  Naledovné funkcie, ktoré treba naprogramovať,
##  spracujú informácie v premennej tab a vrátia zoznam nejakých slov (možno aj prázdny):
##    • funkcia pocet_vyskytov(slovo) vráti počet, koľkokrát sa dané slovo objavilo v texte
##    • funkcia najcastejsie() vráti nticu slov (tuple),
##    ktoré boli v texte najčastejšie - buď je to ntica s jedným slovom, alebo je to ntica viacerých slov,
##    ak mali rovnaký počet výskytov (zrejme maximálny)
##    • funkcia s_poctom(n) vráti nticu slov (tuple),
##    ktoré sa v texte vyskytli presne n-krát - táto ntica môže byť aj prázdna,
##    keď v súbore nebolo ani jedno slovo s týmto počtom výskytov
##    • funkcia najdlhsie() vráti nticu slov (tuple),
##    ktoré boli v texte najdlhšie - buď je to ntica s jedným slovom, alebo je to ntica viacerých slov,
##    ak majú rovnakú maximálnu dĺžku
##    • funkcia najkratsie() vráti nticu slov (tuple),
##    ktoré boli v texte najkratšie - buď je to ntica s jedným slovom, alebo je to ntica viacerých slov,
##    ak majú rovnakú minimálnu dĺžku
##    • funkcia s_dlzkou(n) vráti nticu slov (tuple),
##    ktoré majú dĺžku presne n - táto ntica môže byť aj prázdna,
##    keď v súbore nebolo ani jedno slovo s touto dĺžkou
##
##  Žiadna z týchto funkcií nič nevypisuje, len vráti (return) nejakú nticu slov,respektíve celé číslo.
##  Funkcia citaj() nič nevracia.
##
##  Napríklad "text1.txt" sa skladá z týchto riadkov:
##    i see it i deduce it how do i know that you have been getting yourself very wet lately and that you have a most clumsy and careless servant girl
##    my dear holmes said i this is too much you would certainly have been burned had you lived a few centuries ago it is true that i had a country walk on thursday and came home in a dreadful mess but as i have changed my clothes i can't imagine how you deduce it as to mary jane she is incorrigible and my wife has given her notice but there again i fail to see how you work it out
##    he chuckled to himself and rubbed his long nervous hands together
##    it is simplicity itself said he my eyes tell me that on the inside of your left shoe just where the firelight strikes it the leather is scored by six almost parallel cuts obviously they have been caused by someone who has very carelessly scraped round the edges of the sole in order to remove crusted mud from it hence you see my double deduction that you had been out in vile weather and that you had a particularly malignant bootslitting specimen of the london slavey as to your practice if a gentleman walks into my rooms smelling of iodoform with a black mark of nitrate of silver upon his right forefinger and a bulge on the right side of his tophat to show where he has secreted his stethoscope i must be dull indeed if i do not pronounce him to be an active member of the medical profession
##
##  Tento súbor obsahuje 271 slov, pričom niektoré sa v texte opakujú. Po spustení takéhoto testu:
##    if __name__ == '__main__':
##        citaj('text1.txt')
##        print('pocet vyskytov "the":', pocet_vyskytov('the'))
##        print('najcastejsie:', najcastejsie())
##        print('najdlhsie:', najdlhsie())
##        print('najkratsie:', najkratsie())
##        print('len s poctom 5:', s_poctom(5))
##        print('len s poctom 10:', s_poctom(10))
##        print('len s dlzkou 10:', s_dlzkou(10))
##        print('pocet roznych slov =', len(tab))
##
##  program vypíše:
##    pocet vyskytov "the": 8
##    najcastejsie: ('i',)
##    najdlhsie: ('incorrigible', 'particularly', 'bootslitting')
##    najkratsie: ('i', 'a')
##    len s poctom 5: ('have', 'is')
##    len s poctom 10: ('i',)
##    len s dlzkou 10: ('simplicity', 'carelessly', 'forefinger', 'profession')
##    pocet roznych slov = 161
##
##  Vypisované ntice môžu byť aj v inom poradí.
##  Prvý riadok tohto testu if __name__ == '__main__': označuje, že telo tohto príkazu
##  (keď podmienka je pravdivá) sa vykoná jedine v prípade, že program spúšťaš pomocou Run (F5).
##  Ak tvoj program bude spúšťať testovač, tieto príkazy sa nevykonajú (testovač neobľubuje príkaz print).
##
##  Tvoj odovzdaný program s menom riesenie.py musí začínať tromi riadkami komentárov:
##  # 5. zadanie: najcastejsie
##  # autor: Janko Hraško
##  # datum: 1.11.2021
##  Projekt riesenie.py odovzdaj na úlohový server https://list.fmph.uniba.sk/ najneskôr do 23:00 5. novembra, kde ho môžeš nechať otestovať. Testovač bude spúšťať tvoje funkcie s rôznymi textovými súbormi, ktoré si môžeš stiahnuť z L.I.S.T.u. Odovzdať projekt aj ho testovať môžeš ľubovoľný počet krát. Môžeš zaň získať 5 bodov.
#1234567890123456789012345678901234567890123456789012345678901234567890123456789
                                                                               #
# 5. zadanie: najcastejsie
# autor: Dalibor Sova
# datum: 29.1.2023
                                                                               #
print('ROZBOR TEXTU')                                                           #úvodní text - nadpis
print('''Program rozebere zadaný text na jednotlivá slova,
u kterých je pak možno vyhledávat dle početu výskytů v textu
a dle počet znaků ve slově.
Pouze pro ukázku schopností programu.
Program má již zadán text v angličtině a i dotazy, na které zodpoví.''')        #úvodní text - popis programu
print()                                                                         #prázdný řádek
print()                                                                         #prázdný řádek
input('[zmáčkni [Enter] pro zobrazení výsledku]')                               #úvodní text - vyzvání vstupu do aplikace
print()                                                                         #prázdný řádek
print()                                                                         #prázdný řádek
                                                                               #
meno_suboru = '10_22.txt'                                                       #jméno souboru
                                                                               #
tab = [[], [], [], []]                                                          #seznam - pro rozbor textu
#     [0] [1] [2] [3]                                                           #[0]slova, [1]výskyt, [2]počet znaků, [3]vše
                                                                               #
def citaj(meno_suboru):                                                         #definice funkce - na přečtení a zpracování zadaného souboru
    with open(meno_suboru, 'r') as subor:                                           #otevření, načtení a zavření souboru
        cely_text = subor.read()                                                        #proměnná - pro načtení textu souboru
        slovo = ''                                                                      #proměnná - pro sestavení slov 
        for i in cely_text:                                                             #cyklus - pro každý znak textového souboru
            if i not in (' ', ',', '.', '\n'):                                              #podmínka - pokud znak není mezera, čárka, tečka, nebo znak pro nový řádek
                slovo += i                                                                      #změna - přičti znak do proměnné "slovo!
            else:                                                                           #podmínka - pokud znak není součást slova
                tab[3].append(slovo)                                                            #přičti obsah proměnné "slovo" do seznamu "tab"
                slovo = ''                                                                      #vymaž obsah proměnné "slovo"
        for slovo in tab[3]:                                                            #cyklus - pro každé slovo ze seznamu "tab[3]" a jeho index
            pocet_vyskytu = tab[3].count(slovo)                                             #proměnná - pro počet výskytů daného slova v seznamu "tab[3]"
            pocet_znaku = len(slovo)                                                        #proměnná - pro počet znaků ve slově                
            if slovo not in tab[0]:                                                         #podmínka - pokud slovo zatím není v seznamu slov
                tab[0].append(slovo)                                                            #změna - přidej do seznamu "tab[0]" slovo
                tab[1].append(pocet_vyskytu)                                                    #změna - přidej do seznamu "tab[1]" hodnotu výskytů
                tab[2].append(pocet_znaku)                                                      #změna - přidej do seznamu "tab[2]" počet znaků slova
                                                                               #
def pocet_vyskytov(slovo):                                                      #definice funkce - pro zjištění počtu výskytu zadaného slova v textu
    if slovo in tab[0]:                                                             #podmínka - pokud hledané slovo je v seznamu slov "tab[0]"
        ix = tab[0].index(slovo)                                                        #proměnná - pro index dle slova
        return tab[1][ix]                                                               #návratová hodnota - počet výskytů slova v textu
    else:                                                                           #podmínka - pokud hledané slovo není v seznamu slov "tab[0]"
        return 'Slovo se v textu nevyskytuje'                                           #návratová hodnota - vrať tento text
                                                                               #
def proved_vypocet(pocet_vyskytu, co_se_hleda, cislo_seznamu):                  #definice funkce - pro výpočet návratové hodnoty
    vysledek, ix = [], -1                                                           #proměnná - pro seznam výsledků a pro index hledané hodnoty
    for i in range(pocet_vyskytu):                                                  #cyklus - dle počtu výskytů
        ix = tab[cislo_seznamu][ix+1:].index(co_se_hleda) + ix+1                        #změna - výpočet indexu hledané hodnoty
        vysledek.append(tab[0][ix])                                                     #změna - vlož hledanou hodnotu do seznamu pro výsledek
    return vysledek                                                                 #návratová hodnota - vrať obsah seznamu pro výsledek
                                                                               #
def najcastejsie():                                                             #definice funkce - pro zjištění nejčastěji opakovaných slov
    nejvetsi_hodnota = sorted(tab[1])[-1]                                           #proměnná - pro největší hodnotu vzestupně seřazeného seznamu
    pocet_vyskytu = tab[1].count(nejvetsi_hodnota)                                  #proměnná - počet výskytů nejvyšší hodnoty
    return proved_vypocet(pocet_vyskytu, nejvetsi_hodnota, 1)                       #návratová hodnota - volání funkce pro výpočet
                                                                               #
def s_poctom(n):                                                                #definice funkce - pro zjištění slov dle počtu výskytů 
    pocet_vyskytu = tab[1].count(n)                                                 #proměnná - počet výskytů nejvyšší hodnoty
    return proved_vypocet(pocet_vyskytu, n, 1)                                      #návratová hodnota - volání funkce pro výpočet
                                                                               #
def najdlhsie():                                                                #definice funkce - pro zjištění nejdelšího slova 
    nejdelsi_slovo = sorted(tab[2])[-1]                                             #proměnná - pro největší hodnotu vzestupně seřazeného seznamu
    pocet_vyskytu = tab[2].count(nejdelsi_slovo)                                    #proměnná - počet výskytů nejvyšší hodnoty
    return proved_vypocet(pocet_vyskytu, nejdelsi_slovo, 2)                         #návratová hodnota - volání funkce pro výpočet
                                                                               #
def najkratsie():                                                               #definice funkce - pro zjištění nejkratšího slova
    nejkratsi_slovo = sorted(tab[2])[0]                                             #proměnná - pro nejmenší hodnotu vzestupně seřazeného seznamu
    pocet_vyskytu = tab[2].count(nejkratsi_slovo)                                   #proměnná - počet výskytů nejvyšší hodnoty
    return proved_vypocet(pocet_vyskytu, nejkratsi_slovo, 2)                        #návratová hodnota - volání funkce pro výpočet
                                                                               #
def s_dlzkou(n):                                                                #definice funkce - pro zjištění slov s určitou délkou
    pocet_vyskytu = tab[2].count(n)                                                 #proměnná - počet výskytů nejvyšší hodnoty
    return proved_vypocet(pocet_vyskytu, n, 2)                                      #návratová hodnota - volání funkce pro výpočet
                                                                               #
citaj(meno_suboru)                                                              #volání funkce - pro načtení a zpracování zadaného textového souboru
                                                                               #
print('jméno souboru:', meno_suboru)                                            #výstup - pro jméno souboru
print('pocet slov celkem =', len(tab[3]))                                       #výstup - pro počet slov celkem
print('pocet roznych slov =', len(tab[0]))                                      #výstup - pro počet různých slov
print('nejčastější slovo:', najcastejsie())                                          #výstup - pro nejčastější slovo
print('nejdelší slov:', najdlhsie())                                                #výstup - pro nejdelší slovo
print('nejkratší slovo:', najkratsie())                                              #výstup - pro nejkratší slovo
print('pocet vyskytov "the":', pocet_vyskytov('the'))                           #výstup - pro počet výskytů "the"
print('slova s poctom opakování 5:', s_poctom(5))                                           #výstup - pro slova s počtem opakování 5
print('slova s poctom opakování 10:', s_poctom(10))                                         #výstup - pro slova s počtem opakování 10
print('slova s délkou 10 znaků:', s_dlzkou(10))                                         #výstup - pro slova s délkou 10 znaků
print()                                                                         #prázdný řádek
print()                                                                         #prázdný řádek
input('[zmáčkni [Enter] pro ukončení programu]')                                #konečný text - vyzvání výstupu do aplikace
                                                                               #
#1234567890123456789012345678901234567890123456789012345678901234567890123456789
