##Napíš rekurzívnu funkciu sucet(zoznam),
##ktorá bez cyklov zistí súčet prvkov zoznamu.
##Prvkami sú len celé čísla. Otestuj, napríklad:
##    >>> sucet([2, 4, 6, 8])
##        20
##    >>> sucet([])
##        0
##    >>> sucet(list(range(500)))
##        124750
##Otestuj aj sucet(list(range(2000))).
##Ak tento test spadol na pretečení rekurzie,
##inšpiruj sa riešením funkcie otoc z prednášky.


##jednoduchý zápis funkce pro max 1000 rekurzí:
#def sucet(zoznam):
#    if len(zoznam) == 0:
#        return 0
#    else:
#        return zoznam[0] + sucet(zoznam[1:])


#úvodní a prázdný řádek:
print('REKURZIVNÍ VÝPOČET SOUČTU ČÍSEL')
print(f'''Program provede rekurzivně výpočet součtu hodnot.

K ukázce výpočtu budou použity tyto 4 zadání:
    1) sucet([2, 4, 6, 8])
    2) sucet([])
    3) sucet(list(range(500)))
    4) sucet(list(range(2000)))''')
print()
input('[zmáčkni [Enter] pro zobrazení výsledků]')


#rekurzivní funkce:
def sucet(zoznam):
    if len(zoznam) == 0:
        return 0
    elif len(zoznam) == 1:
        return zoznam[0]
    else:
        pulka = len(zoznam)//2
        return  sucet(zoznam[:pulka]) + sucet(zoznam[pulka:])


#výstup:
print()
print(f'''Výsledky:
    1) sucet([2, 4, 6, 8]) = {sucet([2, 4, 6, 8])}
    2) sucet([]) = {sucet([])}
    3) sucet(list(range(500))) = {sucet(list(range(500)))}
    4) sucet(list(range(2000))) = {sucet(list(range(2000)))}''')


#prázdný řádek, příkaz pro zobrazení výsledků a prázdný řádek
print()
input('[zmáčkni [Enter] pro zobrazení rekurzivní funkce]')


#dovětek:
print()
print(f'''def sucet(zoznam):
    if len(zoznam) == 0:
        return 0
    elif len(zoznam) == 1:
        return zoznam[0]
    else:
        pulka = len(zoznam)//2
        return  sucet(zoznam[:pulka]) + sucet(zoznam[pulka:])
''')


#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]')
