##  Vo vlaku sa vezie 100 cestujúcich.
##  V každej stanici, v ktorej zastane, niekoľko ľudí vystúpi a niekoľko nastúpi.
##  Napíš program, ktorý odsimuluje n takýchto staníc
##  s vystupovaním a nastupovaním cestujúcich.
##  Predpokladáme, že v každej stanici vystúpi aj nastúpi
##  náhodný počet cestujúcich z intervalu <0, 9>.
##
##  Môžeš dostať takýto výstup:
##
##    zadaj n: 8
##    Vo vlaku bolo 100 ľudí, 0 nastúpilo, 7 vystúpilo. Zostalo 93.
##    Vo vlaku bolo 93 ľudí, 4 nastúpilo, 0 vystúpilo. Zostalo 97.
##    Vo vlaku bolo 97 ľudí, 9 nastúpilo, 5 vystúpilo. Zostalo 101.
##    Vo vlaku bolo 101 ľudí, 3 nastúpilo, 9 vystúpilo. Zostalo 95.
##    Vo vlaku bolo 95 ľudí, 6 nastúpilo, 8 vystúpilo. Zostalo 93.
##    Vo vlaku bolo 93 ľudí, 3 nastúpilo, 4 vystúpilo. Zostalo 92.
##    Vo vlaku bolo 92 ľudí, 8 nastúpilo, 6 vystúpilo. Zostalo 94.
##    Vo vlaku bolo 94 ľudí, 8 nastúpilo, 7 vystúpilo. Zostalo 95.


#úvodní a prázdný řádek:
print('VLAK, CESTUJÍCÍ A STANICE')
print()


#vstupní data:
import random                                                   #import modulu random
a = int(input('Zadej POČET STANIC a po té zmáční [Enter]: '))   #počet stanic (řádků)
b = random.randint(0, 9)                                        #1. náhodný počet nastupujících lidí
c = random.randint(0, 9)                                        #2. náhodný počet vystupujících lidí
d = 100                                                         #počáteční stav lidí ve vlaku


#prázdný řádek
print()


#výpočet:
for i in range(a):
    print(f'Ve vlaku bylo {d} ľudí, {b} nastúpilo, {c} vystúpilo. Zostalo {d+b-c}.')   #výpis
    d = d + b - c                                               #nový počet cestujících
    b = random.randint(0, 9)                                    #generování dalšího náhodného početu nastupujících lidí
    c = random.randint(0, 9)                                    #generování dalšího náhodného početu vystupujících lidí
    
    
#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]')
