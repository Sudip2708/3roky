##  Euro je zavedené na Slovensku od 1. januára 2009.
##  Zisti, koľko približne dní od vtedy uplynulo
##  (do dnes uplynulo 12 rokov, 8 mesiacov a 21 dní).
##  Predpokladaj, že každý rok má 365 dní a každý mesiac má 30 dní.
##  Potom vypočítaj koľko je to hodín a aj sekúnd.
##
##  Po spustení môžeš dostať:
##
##    počet dní je ????
##    počet hodín je ?????
##    počet sekúnd je ?????????
##
##  Takto by si mohol vypočítať približný počet dní, hodín a sekúnd aj pre svoj vek.


#úvod
print('UPLYNULÁ DOBA K DNEŠKU')
print()


#moduly:
import time


#1.Převody na vteřiny:
x_min = 60                          #1 min. (60 sec.)
x_hod = x_min * 60                  #1 hod. (60 min.)
x_den = x_hod * 24                  #1 den (24 hodin)
x_mes = x_den * 30                  #1 mesíc (30 dní)
x_rok = x_den * 365                 #1 rok (12 měsíců)


#dnešní datum:
x = time.localtime()
a1 = x[0] * x_rok                   #rok/sec
b1 = x[1] * x_mes                   #měsíc/sec
c1 = x[2] * x_den                   #den/sec
d1 = x[3] * x_hod                   #hodina/sec
e1 = x[4] * x_min                   #minuta/sec
f1 = x[5]                           #vteřina
g1 = a1 + b1 + c1 + d1 + e1 + f1    #celkem/sec


#vstupní data:
a2 = int(input('Zadej ROK a zmáčkni [Enter]: ')) * x_rok    #rok/sec
b2 = int(input('Zadej MĚSÍC a zmáčkni [Enter]: ')) * x_mes  #měsíc/sec
c2 = int(input('Zadej DEN a zmáčkni [Enter]: ')) * x_den    #den/sec
g2 = a2 + b2 + c2                   #celkem/sec


#výpočet výpisů:
a3 = (g1 - g2) // x_rok             #rok
b3 = (g1 - g2) // x_mes             #měsíc
c3 = (g1 - g2) // x_den             #den
d3 = (g1 - g2) // x_hod             #hodina
e3 = (g1 - g2) // x_min             #minuta
f3 = (g1 - g2)                      #vteřina


#prázdný řádek
print()


#výstup:
print(f'''xxxxxxxxxxx
K dnešnímu dni uběhlo:
{a3} roků
{b3} měsíců
{c3} dnů
{d3} hodin
{e3} minut
{f3} vteřin''')

#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]')

