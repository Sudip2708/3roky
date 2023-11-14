##  Napíš program, ktorý vytvorí tabuľku násobenia, podobnú malej násobilke.
##  Násobiť sa budú čísla z nejakého daného intervalu:
##  v prvom riadku (aj stĺpci) sú násobky prvého čísla, v druhom druhého, atď.
##
##  Môžeš dostať takýto výstup:
##
##    zadaj od: 8
##    zadaj do: 13
##      64   72   80   88   96  104
##      72   81   90   99  108  117
##      80   90  100  110  120  130
##      88   99  110  121  132  143
##      96  108  120  132  144  156
##     104  117  130  143  156  169
##
##  Do výpisu tabuľky pridaj prvý stĺpec aj riadok navyše s číslami z daného intervalu,
##  napríklad v takomto tvare:
##
##    zadaj od: 8
##    zadaj do: 13
##         |    8    9   10   11   12   13
##    =====|===============================
##       8 |   64   72   80   88   96  104
##       9 |   72   81   90   99  108  117
##      10 |   80   90  100  110  120  130
##      11 |   88   99  110  121  132  143
##      12 |   96  108  120  132  144  156
##      13 |  104  117  130  143  156  169


#úvodní a prázdný řádek:
print('NÁSOBENÍ ČÍSEL INTERVALU')
print()


#vstupní data:
a = int(input('Zadej od: '))                #vstup počáteční hodnoty
b = int(input('Zadej do: '))                #vstup koncové hodnoty
c = 0                                       #počítadlo počtu hodnot


#prázdný řádek
print()


###výpočet: 1. tabulky:
##for i in range(a, b+1):                     #cyklus pro řádkování
##    for j in range (a, b+1):                #vnořený cyklus pro jednotlivé řádky
##        print(f'{i*j:4}', end=' ')          #výpis hodnot s formátováním na 4 znaky
##    print()                                 #přesun na další řádek
##print()                                     #přesun na další řádek (pro oddělení tabulek)


#výpočet: 2. tabulky:
print(f'     |', end=' ')                   #výpis 1. prázdného sloupce 1. řádku
for i in range(a, b+1):                     #cyklus 1. řádku
    print(f'{i:4}', end=' ')                #výpis zbylích sloupců v 1. řádku s formátováním na 4. znaky
    c += 1                                  #přípis do počítadla počtu hodnot
print()                                     #přesun na další řádek
print(5 * '=' + '|' + c * 5 * '=' + '=')    #výpis oddělovacího řádku
for i in range(a, b+1):                     #cyklus pro řádkování
    print(f'{i:4} |', end=' ')              #výpis 1. sloupce v řádku
    for j in range (a, b+1):                #vnořený cyklus pro jednotlivé řádky
        print(f'{i*j:4}', end=' ')          #výpis zbylých sloupců v řádku
    print()                                 #přesun na další řádek
        

#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]')           
