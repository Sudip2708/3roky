##  Napíš program, ktorý z hviezdičiek vytvorí takúto pyramídu:
##  v prvom riadku je najprv n-1 medzier a potom jedna hviezdička
##  v každom ďalšom riadku je o jednu medzeru menej a o dve hviezdičky viac
##
##  Môžeš dostať takýto výstup:
##
##    zadaj n: 7
##          *
##         ***
##        *****
##       *******
##      *********
##     ***********
##    *************


#úvodní a prázdný řádek:
print('PYRAMIDA Z HVĚZDIČEK')
print()


#vstupní data:
a = int(input('Zadej POČET ŘÁDKŮ a po té zmáční [Enter]: '))


#prázdný řádek
print()


#počítadlo:
b = 1       #počet kol pro výpočet počtu mezer
c = 1       #počet hvězdiček 


#zápis:
for i in range(a):
    print((a - b) * ' ' + c * '*')
    b += 1
    c += 2


#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]')
