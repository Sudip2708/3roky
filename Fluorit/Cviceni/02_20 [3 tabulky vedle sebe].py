##  Pomocou tohto programu vieme zaplniť štvorcovú tabuľku
##  n x n číslami od 1 do n**2:
##
##    n = int(input('zadaj n: '))
##    for i in range(n):
##        for j in range(n):
##            print(f'{i*n + j + 1:2}', end=' ')
##        print()
##
##  Oprav tento program tak, aby vypísal túto tabuľku trikrát vedľa seba,
##  napríklad takto:
##
##    zadaj n: 5
##     1  2  3  4  5     1  2  3  4  5     1  2  3  4  5
##     6  7  8  9 10     6  7  8  9 10     6  7  8  9 10
##    11 12 13 14 15    11 12 13 14 15    11 12 13 14 15
##    16 17 18 19 20    16 17 18 19 20    16 17 18 19 20
##    21 22 23 24 25    21 22 23 24 25    21 22 23 24 25


#úvodní a prázdný řádek:
print('3 TABULKY VEDLE SEBE')
print()


#vstupní data:
a = int(input('Zdej ČÍSLO VELIKOSTI TABULKY a po té zmáční [Enter]: ')) #vstup velikosti tabulky
b = 3                                                                   #počet tabulek vedle sebe     


#prázdný řádek
print()


#výpočet:
for i in range(a):                                                      #cyklus řádků
    for k in range(b):                                                  #cyklus počtu tabulek vedle sebe
        for j in range(a):                                              #cyklus prvního řádku tabulky
            print(f'{i*a + j + 1:2}', end=' ')                          #výpis sady čísel jednoho řádku
        print('  ', end=' ')                                            #odskočení jednotlivých tabulek
    print()                                                             #odskočení na další řádek tabulky
        

#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]')
