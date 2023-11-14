##  Napíš funkciu zoznam_cisel(retazec),
##  ktorá z daného reťazca vyrobí zoznam celých čísel - použi metódu split.
##  Napríklad:
##    >>> a = zoznam_cisel('12 345 6 -78 9000')
##    >>> a
##        [12, 345, 6, -78, 9000]


#úvodní a prázdný řádek:
print('FUNKCE - ŘETĚZEC NA SEZNAM ČÍSEL')
print('''funkce vytvoří z textového řetězce obsahující čísla oddělené mezerou
seznam obsahující jednotlivé čísla''')
print()


#definování funkce:
def zoznam_cisel(retazec):
    seznam = []
    for i in retazec.split():
        seznam.append(int(i))
    return seznam


#vstup:
a = input('Zadej čísla oddělená mezerou: ')


#prázdný řádek a výstup:
print()
print(zoznam_cisel(a))
     

#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]') 
