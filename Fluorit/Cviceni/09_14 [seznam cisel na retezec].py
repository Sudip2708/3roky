##  Napíš funkciu retazec(zoznam),
##  ktorá zo zoznamu čísel vyrobí reťazec - použi metódu join.
##  Napríklad:
##    >>> retazec([12, 3.45, 6, -78, 9000])
##        '12 3.45 6 -78 9000'


#úvodní a prázdný řádek:
print('FUNKCE - SEZNAM ČÍSEL NA ŘETĚZEC')
print('''funkce převede seznam čísel na řetězec, kde jsou čísla oddělena mezerou
pouze k zobrazení''')
print()
input('>>zmáčkni [enter] pro zobrazení<<')
print()


#definování funkce:
def retazec(zoznam):
    for i in range(len(zoznam)):
        zoznam[i] = str(zoznam[i])        
    return ' '.join(zoznam)


#vstup a výstup:
a = [12, 3.45, 6, -78, 9000]
print('Seznam pro převod: ')
print(a)
print()
print('Textový řetězec po převodu: ')
print(repr(retazec(a)))
     

#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]') 
