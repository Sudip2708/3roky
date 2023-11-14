##  Aj nasledovný program bude podobný predchádzajúcemu:
##  Program prečíta nejaké slovo a trojuholník sa bude skladať z písmen tohto slova:
##  v 1. riadku je prvé písmeno, v 2. sú prvé dve, v 3. sú prvé tri,
##  … v poslednom riadku je kompletné slovo.
##
##  Môžeš dostať takýto výstup:
##
##    zadaj slovo: Python
##    P
##    Py
##    Pyt
##    Pyth
##    Pytho
##    Python


#úvodní a prázdný řádek:
print('POSTUPKA ZE SLOVA [VERTIKÁLNÍ]')
print()


#vstupní data:
a = input('Zadej SLOVO a po té zmáční [Enter]: ')


#prázdný řádek
print()


#počítadlo řádků:
c = 0


#zápis:
r = ''
for i in a:
    r += i
    print(r)


#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]')
