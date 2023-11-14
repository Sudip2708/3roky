##  Do jedného bajtu (8 bitov) môžeme zapísať čísla od 0 do 255.
##  Keď máme dvojbajtovú pamäť, môžeme sem zapísať číslo od 0 až do 256*256-1.
##  Do trojbajtovej pamäte sa zmestí číslo do 256*256*256-1.
##  Napíš program, ktorému zadáme počet bajtov a ten potom vypíše maximálne číslo,
##  ktoré sa dá zapísať do takejto pamäte.
##
##  Program vyskúšaj pre rôzne počty bajtov, napríklad:
##
##    zadaj počet bajtov: 4
##    maximálna hodnota je 4294967295
##
##  Aké veľké číslo sa zmestí do 100 bajtov alebo jedného kilobajtu (1000 bajtov)?
##  Vedel/a by si zistiť, koľko cifier má takéto číslo?


#úvod
print('VÝPOČET MAXIMÁLNÍHO ČÍSLA V PAMĚTI BAJTŮ')
print()


#vstupní data:
a = int(input('Zadej POČET BAJTŮ a zmáčkni [Enter]: '))
b = 256     #maximální hodnota jednoho bajtu


#výpočet:
c = (b ** a) - 1    #maximální hodnota
d = len(str(c))


#prázdný řádek
print()


#výstup:
print(f'Maximální hodnota je {c}')
print(f'To je celkem {d} číslic')


#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]')
