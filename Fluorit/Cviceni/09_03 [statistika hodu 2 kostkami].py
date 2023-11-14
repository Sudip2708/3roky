##  Napíš funkciu dve_kocky(pocet),
##  ktorá vráti 13-prvkový zoznam celých čísel.
##  Tento sa skonštruuje takto: zadaný pocet-krát hodí dvoma kockami
##  (dve nádodné čísla od 1 do 6),
##  pre každý takýto hod urobí ich súčet a v 13-prvkovom zozname
##  si eviduje počet výskytov každého súčtu,
##  napríklad zoznam[5] bude označovať,
##  koľko krát pri našej simulácii padol súčet 5;
##  zrejme na začiatku budú v zozname samé 0
##  a potom pri každom hode sa číslo na príslušnom indexe zvýši o 1.
##  Funkcia nič nevypisuje, len vráti vytvorený 13-prvkový zoznam celých čísel.
##  Mohol by si dostať napríklad, takýto zoznam:
##    >>> dve_kocky(1000)
##        [0, 0, 29, 36, 90, 105, 137, 181, 125, 126, 93, 50, 28]


#úvodní a prázdný řádek:
print('DEFINOVÁNÍ FUNKCE - SEZNAM HODŮ 2 KOSTKAMI')
print('''funkce vytvoří seznam statistiky padlých bodů, hodů dvěma kostkami''')
print()


#definování funkce:
def dve_kocky(pocet):
    sez = [0,0,0,0,0,0,0,0,0,0,0,0,0]
    for i in range(pocet):
        a = random.randint(1,6)
        b = random.randint(1,6)
        soucet = a + b
        sez[soucet] = sez[soucet]+1
    return sez


#import modulu:
import random


#vstup:
a = int(input('Zadej počet hodů (tisíce): '))


#prázdný řádek a výstup:
print()
print(f'Statistika pro proběhlých {a} hodů dvěma kostkami: ')
n = 2
for i in range(11):
    print(f'{n} padla {dve_kocky(a)[n]}x')
    n += 1
     

#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]') 
