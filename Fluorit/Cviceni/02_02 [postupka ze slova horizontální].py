##  Napíš program, ktorý bude podobný predchádzajúcej úlohe:
##  program prečíta nejaké slovo a trojuholník bude skladať z písmen tohto slova:
##  v 1. riadku je prvé písmeno, v 2. druhé písmeno ale dvakrát, v 3. tretia písmeno trikrát,
##  …, v poslednom je posledné písmeno veľakrát podľa počtu znakov slova.
##
##  Môžeš dostať takýto výstup:
##    zadaj slovo: PYTHON
##    P
##    YY
##    TTT
##    HHHH
##    OOOOO
##    NNNNNN


#úvodní a prázdný řádek:
print('POSTUPKA ZE SLOVA')
print()


#vstupní data:
a = input('Zadej SLOVO a po té zmáční [Enter]: ')


#počítadlo řádků:
b = 1


#prázdný řádek
print()


#výpis:
for i in a:
    print(i * b)
    b += 1


#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]')
