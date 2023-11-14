##  Napíš program, ktorý vygeneruje na číselnej osi dva náhodné body
##  (v intervale <0, 100>) a vypočíta ich vzdialenosť.
##  Toto urobí n-krát.
##
##  Môžeš dostať takýto výstup:
##
##    zadaj n: 6
##    Prvý bod na priamke je 32, druhý bod 10. Ich vzdialenosť je 22
##    Prvý bod na priamke je 61, druhý bod 12. Ich vzdialenosť je 49
##    Prvý bod na priamke je 62, druhý bod 35. Ich vzdialenosť je 27
##    Prvý bod na priamke je 9, druhý bod 78. Ich vzdialenosť je 69
##    Prvý bod na priamke je 5, druhý bod 82. Ich vzdialenosť je 77
##    Prvý bod na priamke je 16, druhý bod 20. Ich vzdialenosť je 4


#úvodní a prázdný řádek:
print('2. NÁHODNÉ BODY PŘÍMKY A JEJICH VZDÁLENOST')
print()


#vstupní data:
import random                                                   #import modulu random
a = int(input('Zadej POČET ŘÁDKŮ  a po té zmáční [Enter]: '))   #počet cyklů (řádků)
b = random.randint(0, 100)                                      #1. náhodné číslo
c = random.randint(0, 100)                                      #2. náhodné číslo


#prázdný řádek
print()


#výpočet:
for i in range(a):
    print(f'První bod na přímce je {b}, druhý bod {c} a jejich vzdálenost je {abs(b-c)}.')   #výpis
    b = random.randint(0, 100)                                  #generování dalšího náhodného 1. čísla
    c = random.randint(0, 100)                                  #generování dalšího náhodného 2. čísla

     
#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]')
