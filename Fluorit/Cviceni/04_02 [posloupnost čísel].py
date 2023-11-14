##  Budeme konstruovat takovou posloupnost celých čísel:
##    - začneme zadaným číslem n
##    - pokud je sudé, vydělíme ho 2
##    - jinak se vynásobí 3a přičte 1
##    - toto se opakuje, dokud nedostaneme číslo 1
##
##  Napiš program, který pro dané startovní číslo vypíše
##  takto zkonstruovanou posloupnost.
##
##  Například:
##    zadaj číslo: 44
##    44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1


#úvodní a prázdný řádek:
print('HRA ČÍSEL')
print('''program ze zadaného čísla vytvoří posloupnost celých čísel - pokud je (dané a pak i výsledné) číslo sudé, vydělího 2 a pokud je liché, vynásobýho 3 a přičte 1''')
print()


#vstupní data a proměné:
a = int(input('Zadej číslo: '))         #vstup čísla
b = a                                   #aktuální číslo
c = 1                                   #počítadlo průběhu


#prázdný řádek
print()


#výpočet a výstup:
print(int(b), end=', ')                 #výpis prvního čísla
while b > 1:                            #cyklus
    if b % 2 == 0:                      #zjištění zbytku po dělení 2
        b = b / 2                       #při 0 vyděl 2
    else:                               #a při zbytku jiném než 0
        b = b * 3 + 1                   #vyděl aktuální číslo 3 a přičti 1
    print(int(b), end=', ')             #vypiš číslo
    c += 1                              #přípočet počítadla průběhů

print()                                 #odskočení na další řádek
print(f'1 bylo dosaženo v {c}. kole.')  #výpis kdy bylo dosaženo 1
        

#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]')    

