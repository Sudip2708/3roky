##  Napíš program, ktorý vypíše cifry zadaného čísla postupným delením desiatimi,
##  teda vo while-cykle vypíšeš poslednú cifru (číslo % 10)
##  a pritom ešte samotné číslo vydelíš 10.
##  Súčasne každú túto cifru pripočítaš do počítadla cs (ciferný súčet).
##
##  Môžeš dostať takýto výstup:
##    zadaj číslo: 4132
##    2
##    3
##    1
##    4
##    ciferný súčet = 10
##
##  Všimni si, že cifry sú vypísané v opačnom poradí ako sú v zadanom čísle.


#úvodní a prázdný řádek:
print('ČÍSLO SVISLE ZEZADU')
print('program vypíše zadané číslo po jednotlivých číslicích, začínaje poslední a zobrazí jejich ciferný součet')
print()


#vstupní data a proměné:
a = int(input('Zadej číslo: ')) #vstup - počet
b = 0                           #počítadlo ciferného součtu


#výpočet a výstup:
while a != 0:                   #cyklus - dokuď nebude 0
    print(a%10)                 #vypiš poslední číslo (zbytek po dělení 10-ti)
    b += a%10                   #přičti ho do počítadla ciferného součtu
    a //= 10                    #vyděl a deseti
print('ciferný součet =', b)    #výpis celociferného součtu
        

#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]')    
