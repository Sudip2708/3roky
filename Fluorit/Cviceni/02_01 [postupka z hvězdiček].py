##  Napíš program, ktorý zo znakov hviezdička ('*') vytvorí takýto trojuholník:
##  v 1. riadku je jedna hviezdička, v 2. dve, v 3. tri, …,
##  v n-tom riadku je n hviezdičiek.
##
##  Môžeš dostať takýto výstup:
##    zadaj n: 6
##    *
##    **
##    ***
##    ****
##    *****
##    ******


#úvodní a prázdný řádek:
print('POSTUPKA Z HVĚZDIČEK')
print()


#vstupní data:
a = int(input('Zadej POČET ŘÁDKŮ a po té zmáční [Enter]: '))


#prázdný řádek
print()


#výpis:
for i in range(a):
    print('*' * (i + 1))
        

#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]')
