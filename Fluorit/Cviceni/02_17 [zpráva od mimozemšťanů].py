##  Dostali sme správu od mimozemšťanov, ktorá je zložená zo znakov 'O' a '-'.
##  Správa obsahuje istý počet riadkov a stĺpcov takýchto znakov.
##  Napíš program, ktorým náhodne vygeneruješ podobnú správu.
##
##  Môžeš dostať takýto výstup:
##
##    zadaj počet riadkov: 5
##    zadaj počet stĺpcov: 28
##    O-OOO----OO-OOO---O---OOOO-O
##    OOO-OOOO----OO----O-OOOOO-O-
##    O-OO-OO-OOO--O-OOO--O----OOO
##    ---OO--OO-O-O--OO----OOOO--O
##    -O-----O--OOOO-OO-OOO-OO---O


#úvodní a prázdný řádek:
print('ZPRÁVA OD MIMOZEMŠŤANŮ')
print()


#vstupní data:
a = int(input('Zadej POČET ŘÁTKŮ a po té zmáční [Enter]: '))     #vstup na počet hodů
b = int(input('Zadej POČET SLOUPCŮ a po té zmáční [Enter]: '))   #vstup na počet hodů


#prázdný řádek
print()


#výpočet:
import random                                                   #import modulu random
for i in range(a):                                              #cyklus pro počet řádků
    for j in range(b):                                          #cyklus pro počet sloupců
        print(random.choice('O-'), end='')                      #náhodný výběr znaků a jejich výpis v jednom řádku
    print()                                                     #odskočení na další řádek
        

#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]')        
    
