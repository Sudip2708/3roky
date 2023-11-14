##  Napíš program, ktorý vypíše naformátovanú tabuľku mocnín celých čísel
##  z nejakého daného intervalu.
##
##  Prvý stĺpec tabuľky obsahuje číslo,
##  v druhom je druhá mocnina tohto čísla,
##  v treťom tretia, vo štvrtom štvrtá.
##
##  Môžeš dostať takýto výstup:
##
##    zadaj od: 95
##    zadaj do: 103
##     95   9025   857375   81450625
##     96   9216   884736   84934656
##     97   9409   912673   88529281
##     98   9604   941192   92236816
##     99   9801   970299   96059601
##    100  10000  1000000  100000000
##    101  10201  1030301  104060401
##    102  10404  1061208  108243216
##    103  10609  1092727  112550881


#úvodní a prázdný řádek:
print('2. 3. A 4. MOCNINA ČÍSEL')
print()


#vstupní data:
a = int(input('Zadej PRVNNÍ ČÍSLO a po té zmáční [Enter]: '))   #počáteční číslo
b = int(input('Zadej DRUHÉ ČÍSLO a po té zmáční [Enter]: '))    #koncové číslo
c = ' č.'                                                       #popisek hlavy tabulky
d = '  2.m'                                                     #popisek hlavy tabulky       
e = '    3.m'                                                   #popisek hlavy tabulky
f = '      4.m'                                                 #popisek hlavy tabulky

#prázdný řádek
print()


#výpočet:
print(f'{c:3}  {d:5}  {e:7}  {f:9}')                            #hlava tabulka
for i in range(a, b+1):                         
    x1 = i                                                      #číslo
    x2 = i ** 2                                                 #výpočet 2. mocniny
    x3 = i ** 3                                                 #výpočet 3. mocniny
    x4 = i ** 4                                                 #výpočet 4. mocniny
    print(f'{x1:3}  {x2:5}  {x3:7}  {x4:9}')                    #výpis do naformátované tabulky
        

#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]')
