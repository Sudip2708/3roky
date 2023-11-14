##  Napíš program, ktorý n-krát vypíše zadané slovo takto:
##  v 1. riadku bez odsadenia, v 2. s 1 odsadením (4 medzery),
##  v 3. s 2 odsadeniami (8 medzier), v 4. s 3 odsadeniami (12 medzier),
##  pre ďalšie riadky sa to opakuje od začiatku.
##  V programe využi zvyšok po delení, napríklad i%4*4.
##
##  Môžeš dostať takýto výstup:
##
##    zadaj slovo: Python
##    zadaj n: 9
##    Python
##        Python
##            Python
##                Python
##    Python
##        Python
##            Python
##                Python
##    Python


#úvodní a prázdný řádek:
print('VÝPIS SLOVA V 4-KOVÉM CYKLU')
print()


#vstupní data:
a = input('Zadej SLOVO a po té zmáční [Enter]: ')
b = int(input('Zadej POČET a po té zmáční [Enter]: '))


#prázdný řádek
print()


#zápis:
for i in range(b):
    print(i%4 * 4 * ' ' + a)


#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]')
