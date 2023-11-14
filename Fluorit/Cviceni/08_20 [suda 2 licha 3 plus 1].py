##  Napíš funkciu postupnost(x),
##  ktorá vygeneruje (vráti ako výsledok) takúto postupnosť celých čísel:
##  postupnosť začína hodnotou x;
##  ďalší prvok sa vždy vypočíta podľa predchádzajúceho tak,
##  že ak je párny, vydelí sa dvomi, inak sa vynásobí tromi a pripočíta jedna.
##  Generovanie postupnosti končí, keď sa objaví číslo 1 (bude posledným prvkom postupnosti).
##  Funkcia nič nevypisuje, len vráti (return) nejaký zoznam čísel.
##  Napríklad:
##    >>> p = postupnost(3)
##    >>> p
##        [3, 10, 5, 16, 8, 4, 2, 1]
##    >>> postupnost(1)
##        [1]
##    >>> postupnost(7)
##        [7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]


#úvodní a prázdný řádek:
print('DEFINOVÁNÍ FUNKCE - SUDÁ DVĚMI, LICHÁ TŘEMI PLUS JEDNA')
print('''funkce vytvoří z námi zadaného čísla seznam, na základě těchto 2 pravidel:
1) pokud je číslo sudé, vydělího dvěmi
2) pokud je liché, vynásobího 3 a přičte 1''')
print()


#definování funkce:
def postupnost(x):
    seznam = [x]
    while x != 1:
        if x % 2 == 0:
            x = x//2
            seznam.append(x)
        else:
            x = x*3+1
            seznam.append(x)
    return seznam


#vstup:
n = int(input('Zadej číslo: '))
print()


#výstup:
print('Výsledek:')
print(postupnost(n))
        

#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]') 
