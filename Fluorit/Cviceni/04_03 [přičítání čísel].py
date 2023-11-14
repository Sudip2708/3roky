##  Napiš program, který čte desetinná čísla ze vstupu a když zadáme 0,
##  čtení čísel ze vstupu skončí a program vypíše součet všech těchto čísel.
##
##  Použij while-cyklus. Například po spuštění:
##    zadaj 1. číslo: 17
##    zadaj 2. číslo: 3.14
##    zadaj 3. číslo: -9.8
##    zadaj 4. číslo: 6
##    zadaj 5. číslo: 0
##    súčet všetkých prečítaných čísel je 16.34


#úvodní a prázdný řádek:
print('PŘIČÍTÁNÍ ČÍSEL')
print('program přičítá zadávané čísla (včetně záporných) dokud nezadáme 0')
print()


#vstupní data a proměné:
a = 1                                           #počítadlo kol
b = float(input(f'Zadej {a}. číslo: '))         #vstup čísla
c = 0                                           #celkový součet


#výpočet a výstup:
while b < 0 or b > 0:                           #když vstup není 0
    c += b                                      #přičti číslo do celkového součtu
    a += 1                                      #přičti 1 k počítadlu kol
    b = float(input(f'Zadej {a}. číslo: '))     #získej další číslo
print(f'Součet všech čísle je {c}')             #pokud je číslo 0 vypiš celkový počet
        

#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]')    
