##8. Týždenný projekt
##L.I.S.T.
##•	riešenie odovzdaj na úlohový server https://list.fmph.uniba.sk/
##
##Veľký štvorec môžeme rozdeliť na 4 kvadranty takto: (viz. obrázek v zadání)
## 
##Úplne rovnako môžeme každý kvadrant rozdeliť na menšie kvadranty,
##napríklad 2. kvadrant takto: (viz. obrázek v zadání)
## 
##Môžeš vidieť, že tieto menšie kvadranty v 2 sú očíslované ako 21, 22, 23, 24.
##Ľubovoľný kvadrant môžeš rozdeliť na 4 menšie.
##Napríklad, rozdelením kvadrantu 23 dostaneš: (viz. obrázek v zadání)
## 
##Takýmto delením môžeš ísť do nejakej danej hĺbky n,
##kým neprídeš na elementárny štvorček, ktorý sa už deliť nedá.
##Napríklad, hĺbka n=1 znamená, že plocha sa skladá z 2x2 elementárnych štvorčekov
##a deliť ju môžeš maximálne raz na 4 základné kvadranty.
##Hĺbka n=4 označuje 16x16 elementárnych štvorčekov,
##ktorú môžeš deliť maximálne 4-krát.
##Potom, napríklad kvadrant 2 je veľký 8x8 elementárnych štvorčekov,
##kvadrant 23 zaberá 4x4 štvorčekov,
##kvadrant 234 zaberá 2x2 štvorčeky a zrejme 2343 už len jeden.
##Teda pre dané n poradové číslo kvadrantu má zmysel s maximálnym počtom cifier n.
##Čím má číselné označenie kvadrantu menej cifier,
##tým je kvadrant väčší (napríklad 0-ciferné číslo kvadrantu označuje celý štvorec).
##Napíš pythonovský modul, ktorý bude obsahovať
##jedinú triedu Stvorce a žiadne iné globálne premenné:
##class Stvorce:
##    def __init__(self, n):
##        ...
##
##    def urob(self, index):
##        ...
##
##    def pocet(self):
##        ...
##
##    def vypis(self):
##        ...
##Metódy majú fungovať takto:
##•	inicializácia __init__(self, n) vyhradí takú dvojrozmernú tabuľku,
##aby sa dali deliť kvadranty do hĺbky n;
##každý elementárny štvorček môže obsahovať 0 alebo 1,
##pri inicializácii budú všade 0
##•	metóda urob(self, index) dostáva číslo kvadrantu ako znakový reťazec
##(môže byť aj prázdny) a pre zadaný kvadrant vyznačí všetky elementárne štvorčeky tak,
##že hodnoty 0 nahradí 1 a hodnoty 1 nahradí 0
##•	metóda pocet(self) vráti dvojicu celých čísel:
##počet núl a počet jednotiek v dvojrozmernej tabuľke
##•	metóda vypis(self) vypíše (pomocou print()) momentálny obsah dvojrozmernej tabuľky,
##pričom namiesto 0 použije znak '-' a namiesto 1 znak 'X'
##Napríklad:
##>>> stv = Stvorce(2)
##>>> stv.pocet()
##    (16, 0)
##>>> stv.urob('23')
##>>> stv.vypis()
##    ----
##    --X-
##    ----
##    ----
##>>> stv.pocet()
##    (15, 1)
##>>> stv.urob('2')
##>>> stv.urob('3')
##>>> stv.pocet()
##    (9, 7)
##>>> stv.vypis()
##    --XX
##    ---X
##    XX--
##    XX--
##Pre inšpiráciu môžeš otestovať tieto postupnosti indexov:
##['1', '11', '131', '1314', '143', '12', '1233', '1234', '1243', '1244', '23', '234',
##'2133', '2134', '2143', '2144', '24', '242', '2423', '31', '313', '3132', '32', '324',
##'3232', '3411', '3412', '3421', '3422', '4', '44', '424', '4241', '413', '4141', '43',
##'4311', '4312', '4321', '4322']
##----------------
##----------------
##----------------
##----XXXXXXXX----
##--XXXXXXXXXXXX--
##-XXXXXXXXXXXXXX-
##XXXX--XXXX--XXXX
##XXXX--XXXX--XXXX
##XXXXXXXXXXXXXXXX
##XXXXXXXXXXXXXXXX
##-XXXX------XXXX-
##--XXXX----XXXX--
##----XXXXXXXX----
##----------------
##----------------
##----------------
##['14', '141','1412','1431','124', '1241', '2', '21', '22', '24', '213', '2113',
##'2143', '2324', '2433', '3', '31', '3142', '3211', '343', '3441', '3443', '33',
##'332', '3321', '41', '4213', '4231', '4232', '43', '434', '441', '4423']
##----------------
##--------X-------
##-------XXX------
##------XXXXX-----
##-----XXXXXXX----
##------XXXXX-----
##-----XXXXXXX----
##----XXXXXXXXX---
##-----XXXXXXX----
##----XXXXXXXXX---
##---XXXXXXXXXXX--
##----XXXXXXXX----
##---XXXXXXXXXXX--
##--XXXXXXXXXXXXX-
##-------XXX------
##-------XXX------
##['2', '23224', '2411', '24123', '24131', '24132', '2422', '24223', '2444', '24441',
##'212', '21412', '21421', '21422', '211', '2113', '21132', '21143', '22', '2233',
##'2234', '22342', '14', '14111', '14113', '1433', '14332', '132', '1322', '13223',
##'134', '1344', '13441', '1312', '13142', '13144', '13322', '13324', '1334', '1134',
##'11341', '11333', '11334', '11433', '1224', '12243', '12344', '124', '1241', '12421',
##'12423', '12431', '3112', '31123', '31111', '31112', '31211', '32122', '322', '3223',
##'32213', '3224', '32242', '411', '412', '4124', '41241', '41234', '4211', '42121',
##'42122', '42211', '4131', '413114', '41321']
##--------------------------------
##--------------------------------
##--------------XXX---------------
##---------------XXXX-------------
##---------------XXXXXX-----------
##---------------XXXXXXXXX--------
##---X---------XXXXXXXXXXXXXX-----
##XXXXX------XXXXXXXXXXXXXXXXX----
##--XXXX---XXXXXXXXXXXXXXX--XXXX--
##--XXXXX--XXXXXXXXXXXXXX----XXXX-
##---XXXXXXXXXXXXXXXXXXXXX--XXXXXX
##---XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
##---XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
##---XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
##--XXXXX--XXXXXXXXXXXXXXXXXXXXXX-
##--XXXX----XXXXXXXXXXXXXXXXXXXX--
##XXXXX------XXXXXXXXXXXXXXXXXX---
##---X---------XXXXXXXXXXXXX------
##---------------XXXXXXXX---------
##----------------XXXXX-----------
##----------------XXX-------------
##----------------XX--------------
##--------------------------------
##--------------------------------
##--------------------------------
##--------------------------------
##--------------------------------
##--------------------------------
##--------------------------------
##--------------------------------
##--------------------------------
##--------------------------------
##Tvoj odovzdaný program s menom riesenie.py musí začínať tromi riadkami komentárov:
### 8. zadanie: stvorce
### autor: Janko Hraško
### datum: 3.12.2021
##Projekt riesenie.py odovzdaj na úlohový server https://list.fmph.uniba.sk/
##najneskôr do 23:00 3. decembra. Môžeš zaň získať 5 bodov.
#123456789#123456789#123456789#123456789#123456789#123456789#123456789#123#75
                                                                            #
#8. zadanie: stvorce
#autor: Dalibor Sova
#datum: 5.4.2023


#úvodní a prázdný řádek:                                                  
print('TÝDENÍ PROJEKT 15 LEKCE')                              
print('''
Program obsahuje třídu Stvorce, kteráobsahuje následující metody:
dle hodnoty zanoření, vytvoří dvojrozměrnou tabulku vyplněnou nulama.
Následně dle indexů rozdělení čtverce, projde tuto tabulku a 
Třída Obdelnik obsahuje následující funkce:

1) inicializační funkce __init__(n)
    očekávající 1 parametr:
        n = hloubka zanoření
    inicializační funkce vytvoří dle této hodnoty dvojrozměrnou
    tabulku vyplněnou nulama

2) metoda urob(index)
    očekávající 1 parametr:
        index = číslo ve formátu textového řetězce
    metoda postupně projde všechny hodnoty čísla
    a dle klíče postupného vnořování a dělení čtverců
    na 4 části změní obsah tabulky na opačnou hodnotu
    (hodnoty jsou 0 a 1)

3) metoda pocet(),
    bez parametru
    metoda vypíše počet 0 a 1 v celé tabulce

4) metoda vypis(), 
    bez parametru
    metoda vypíše tabulku po řádcích
    '0' nahradí při výpisu za znak '-'
    '1' nahradí při výpisu za znak 'X'
''')


#definice třídy:
class Stvorce:  
    def __init__(self, n):                                              #inicializační metody - vyžaduje údaj hodnoty zanoření
        self.hloubka_tab = n                                                #vytvoření atributu pro hloubku zanoření tabulky
        self.velikost_tab  = 2**n                                           #vytvoření atrubutu pro velikost tabulky
        self.tabulka = []                                                   #vytvoření atributu pro tabulku

        for radek in range(self.velikost_tab):                              #cyklus pro tvorbu řádků dle velikosti tabulky
            self.tabulka.append([])                                             #přidání prázdného seznamu na konec tabulky
            for sloupec in range(self.velikost_tab):                            #cyklus pro tvorbu sloupců dle velikosti tabulky
                self.tabulka[-1].append(0)                                          #přidání nuly do seznamu


    def urob(self, index):                                              #metoda urob - vyžaduje údaj indexu oblasti
        sloupce = list(range(self.velikost_tab))                            #lokální proměnná pro seznam indexů sloupců (dle velikosti tabulky)
        radky = list(range(self.velikost_tab))                              #lokální proměnná pro seznam indexů řádků (dle velikosti tabulky)

        for cislo in index:                                                 #cyklus pro každé jednotlivé číslo indexu
            if int(cislo) in (1, 2):                                            #podmínka - pokud je číslo 1 nebo 2
                sloupce = sloupce[:len(sloupce)//2]                                 #ponech pouze první půlku tabulky pro sloupce
            else:                                                               #podmínka - pokud je číslo 3 nebo 4
                sloupce = sloupce[len(sloupce)//2:]                                 #ponech pouze druhou půlku tabulky pro sloupce
            if int(cislo) in (1, 3):                                            #podmínka - pokud je číslo 1 nebo 3
                radky = radky[:len(radky)//2]                                       #ponech pouze první půlku tabulky pro řádky
            else:                                                               #podmínka - pokud je číslo 2 nebo 4
                radky = radky[len(radky)//2:]                                       #ponech pouze druhou půlku tabulky pro řádky

        for sloupec in sloupce:                                             #cyklus dle hodnot seznamu sloupce
            for radek in radky:                                                 #cyklus dle hodnot seznamu radky
                if self.tabulka[sloupec][radek] == 0:                               #podmínka - pokud tabulka obsahuje hodnotu 0
                    self.tabulka[sloupec][radek] = 1                                    #změň tuto hodnotu na hodnotu 1
                else:                                                               #podmínka - pokud tabulka obsahuje hodnotu 1
                    self.tabulka[sloupec][radek] = 0                                    #změň tuto hodnotu na hodnotu 0
                    

    def pocet(self):                                                    #metoda pocet, nevyžadující žádný údaj
        nuly = jednicky = 0                                                 #nastavení lokálních proměnných 'nuly' a 'jednicky' na hodnotu 0
        for radek in self.tabulka:                                          #cyklus pro řádek tabulky
            nuly += radek.count(0)                                              #přípočet počtu 0 v řádku k celkovému počtu
            jednicky += radek.count(1)                                          #přípočet počtu 1 v řádku k celkovému počtu
        print('nuly: ', nuly, ', jedničky = ', jednicky)                                             #výpis nul a jedniček


    def vypis(self):                                                    #metoda vypis,  nevyžadující žádný údaj
        for radek in self.tabulka:                                          #cyklus pro každý řádek tabulky
            for sloupec in radek:                                               #cyklus pro každý sloupec tabulky
                if sloupec == 0:                                                    #podmínka - když je hodnota 0
                    print('-', end='')                                                  #vypiš znak '-'
                else:                                                               #podmínka - když je hodnota 1
                    print('X', end='')                                                  #vypiš znak 'X'
            print()                                                             #oddělení dalšího řádku
                    

print('Ukázka správné funkčnosti programu:')
input('''
Zmáčkni [enter] pro vytvoření tabulky s hodnotou zanoření 2
pomocí příkazu stv = Stvorce(2)
a výpisu počtu nula jedniček pomocí příkazu stv.pocet()
''')
stv = Stvorce(2)
stv.pocet()

input('''
Zmáčkni [enter] pro zakreslení pozice dle indexu 23
pomocí příkazu stv.urob('23'),
výpisu počtu nula jedniček pomocí příkazu stv.pocet()
a výpis tabulky pomocí příkazu stv.vypis()
''')
stv.urob('23')
stv.pocet()
stv.vypis()


input('''
Zmáčkni [enter] pro zakreslení pozice dle indexu 2 a 3
pomocí příkazu stv.urob('2'); stv.urob('3')
výpisu počtu nula jedniček pomocí příkazu stv.pocet()
a výpis tabulky pomocí příkazu stv.vypis()
''')
stv.urob('2')
stv.urob('3')
stv.pocet()
stv.vypis()


input('''
Zmáčkni [enter] pro vykreslení tabulky s hloubkou zanoření 4
a následujícími indexy:
['1', '11', '131', '1314', '143', '12', '1233', '1234', '1243', '1244', 
'23', '234', '2133', '2134', '2143', '2144', '24', '242', '2423', '31', 
'313', '3132', '32', '324', '3232', '3411', '3412', '3421', '3422', '4',
'44', '424', '4241', '413', '4141', '43', '4311', '4312', '4321', '4322']
''')
stv_x1 = Stvorce(4)
x1 = ['1', '11', '131', '1314', '143', '12', '1233', '1234', '1243', '1244', '23', '234',
'2133', '2134', '2143', '2144', '24', '242', '2423', '31', '313', '3132', '32', '324',
'3232', '3411', '3412', '3421', '3422', '4', '44', '424', '4241', '413', '4141', '43',
'4311', '4312', '4321', '4322']
for i in x1:
    stv_x1.urob(i)
stv_x1.pocet()
stv_x1.vypis()


input('''
Zmáčkni [enter] pro vykreslení tabulky s hloubkou zanoření 4
a následujícími indexy:
['14', '141','1412','1431','124', '1241', '2', '21', '22', '24', '213', 
'2113', '2143', '2324', '2433', '3', '31', '3142', '3211', '343', '3441',
 '3443', '33', '332', '3321', '41', '4213', '4231', '4232', '43', '434', 
'441', '4423']
''')
stv_x2 = Stvorce(4)
x2 = ['14', '141','1412','1431','124', '1241', '2', '21', '22', '24', '213', '2113',
'2143', '2324', '2433', '3', '31', '3142', '3211', '343', '3441', '3443', '33',
'332', '3321', '41', '4213', '4231', '4232', '43', '434', '441', '4423']
for i in x2:
    stv_x2.urob(i)
stv_x2.pocet()
stv_x2.vypis()
    

input('''
Zmáčkni [enter] pro vykreslení tabulky s hloubkou zanoření 5
a následujícími indexy:
['2', '23224', '2411', '24123', '24131', '24132', '2422', '24223', '2444', 
'24441', '212', '21412', '21421', '21422', '211', '2113', '21132', '21143', 
'22', '2233', '2234', '22342', '14', '14111', '14113', '1433', '14332', 
'132', '1322', '13223', '134', '1344', '13441', '1312', '13142', '13144', 
'13322', '13324', '1334', '1134', '11341', '11333', '11334', '11433', 
'1224', '12243', '12344', '124', '1241', '12421', '12423', '12431', '3112',
'31123', '31111', '31112', '31211', '32122', '322', '3223', '32213', '3224', 
'32242', '411', '412', '4124', '41241', '41234', '4211', '42121', '42122', 
'42211', '4131', '413114', '41321']
''')
stv_x3 = Stvorce(5)
x3 = ['2', '23224', '2411', '24123', '24131', '24132', '2422', '24223', '2444', '24441',
'212', '21412', '21421', '21422', '211', '2113', '21132', '21143', '22', '2233',
'2234', '22342', '14', '14111', '14113', '1433', '14332', '132', '1322', '13223',
'134', '1344', '13441', '1312', '13142', '13144', '13322', '13324', '1334', '1134',
'11341', '11333', '11334', '11433', '1224', '12243', '12344', '124', '1241', '12421',
'12423', '12431', '3112', '31123', '31111', '31112', '31211', '32122', '322', '3223',
'32213', '3224', '32242', '411', '412', '4124', '41241', '41234', '4211', '42121',
'42122', '42211', '4131', '413114', '41321']
for i in x3:
    stv_x3.urob(i)
stv_x3.pocet()
stv_x3.vypis()


input('''
Zmáčkni [enter] pro ukončení programu''')






        

