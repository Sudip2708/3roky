##  Máme mince a bankovky s hodnotami 1, 2, 5, 10, 20, 50, 100.
##  Napíš program, ktorý zistí, ako sa dá poskladať
##  ľubovoľná suma peňazí minimálnym počtom kusov peňazí.
##  Použi len jeden for-cyklus, v ktorom bude jeden if,
##  nejaké priradenia a tiež print.
##
##  Napríklad po spustení:
##    zadaj cislo: 346
##    3 krát hodnota 100
##    2 krát hodnota 20
##    1 krát hodnota 5
##    1 krát hodnota 1


#úvodní a prázdný řádek:
print('ROZLOŽENÍ HODNOTY NA MINIMÁLNÍ POČET BANKOVEK A MINCÍ')
print('program rozloží námi zadanou hodnotu na minimální počet bankovek a mincí - nejvyšší bankovka je 100')
print()


#vstupní data a proměné:
a = int(input('Zadej číslo: '))             #vstupní hodnota
b = 0                                       #počet od jednoho druhu
c = a                                       #zbytek pro další dělení


#výpočet a výstup:
for i in 100, 50, 20, 10, 5, 2, 1:          #cyklus s jednotlivíma hodnotama bankovek a mincí
    b = c // i                              #výpočet - kolikrát se vyskytuje konkrétní (i) hodnota
    c = c - b * i                           #výpočet - hodnota pro další dělení
    if b > 0:                               #podmínka - když počet od jednoho druhu je víc než 0
        print(f'{b} krát hodnota {i}')      #pokud ano - vypsat tuto větu
        

#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]')    
