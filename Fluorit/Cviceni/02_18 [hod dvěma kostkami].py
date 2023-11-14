##  Budeme simulovať hádzanie dvomi hracími kockami.
##  Zakaždým vypíšeme aj ich súčet.
##  Napíš program, ktorý to simuluje n-krát.
##
##  Môžeš dostať takýto výstup:
##
##    zadaj n: 4
##    na 1. kocke padla 1
##    na 2. kocke padla 4
##    ich súčet je 5
##    ======================
##    na 1. kocke padla 4
##    na 2. kocke padla 5
##    ich súčet je 9
##    ======================
##    na 1. kocke padla 6
##    na 2. kocke padla 1
##    ich súčet je 7
##    ======================
##    na 1. kocke padla 4
##    na 2. kocke padla 1
##    ich súčet je 5
##    ======================


#úvodní a prázdný řádek:
print('HOD DVĚMA KOSTKAMI A JEJICH SOUČET')
print()


#vstupní data:
a = int(input('Zadej POČET HODŮ a po té zmáční [Enter]: '))     #vstup na počet hodů


#prázdný řádek
print()


#výpočet:
import random                                                   #import modulu random
for i in range(a):                                              #cyklus pro počet hodů
    b = random.randint(1,6)                                     #náhodné číslo první kostky
    c = random.randint(1,6)                                     #náhodné číslo druhé kostk
    print(f'na první kostce padla {b}')                         #výpis prvního hodu
    print(f'na druhé kostce padla {c}')                         #výpis druhého hodu
    print(f'jejich součet je {b + c}')                          #výpis jejich součtu
    print(23 * '=')                                             #oddělení hodů


#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]')
