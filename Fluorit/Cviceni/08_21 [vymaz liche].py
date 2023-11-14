##  Napíš funkciu vyhod_neparne(zoznam),
##  ktorá z daného zoznamu celých čísel vyhodí tie prvky, ktoré sú nepárne.
##  Funkcia nič nevracia ani nevypisuje, len modifikuje hodnotu zoznamu.
##  Napríklad:
##    >>> x = [2, 3, 4, 5, 7, 8, 10, 11, 13, 15, 17]
##    >>> vyhod_neparne(x)
##    >>> x
##        [2, 4, 8, 10]
##    >>> x = list(range(1, 100, 2))
##    >>> vyhod_neparne(x)
##    >>> x
##        []


#úvodní a prázdný řádek:
print('DEFINOVÁNÍ FUNKCE - VYMAŽ LICHCÉ')
print('funkce odebere ze seznamu čísel, všechna lichá čísla')
print()


#definování funkce:
def vyhod_neparne(seznam):
    pocitadlo = 0
    while pocitadlo < len(seznam):
        if seznam[pocitadlo] % 2 != 0:
            seznam.pop(pocitadlo)
        else:
            pocitadlo += 1            


#intro:
print('Seznam pro vyzkoušení funkce:')
print('[2, 3, 4, 5, 7, 8, 10, 11, 13, 15, 17]')
print()
input('zmáčkni [enter] pro zobrazení výsledku')
print()

#seznam:
x = [2, 3, 4, 5, 7, 8, 10, 11, 13, 15, 17]


#výstup:
vyhod_neparne(x)
print(x)
        

#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]') 
