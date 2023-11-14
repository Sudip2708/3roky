##  Napíš funkciu cele(zoznam),
##  ktorá z daného zoznamu vytvorí (a vráti) nový,
##  v ktorom sa každý prvok previedol (pomocou funkcie int())
##  na celočíselnú hodnotu.
##  Funkcia nemodifikuje vstupný zoznam a nič nevypisuje.
##  Napríklad:
##    >>>x = cele([3.14, '14', 53])
##    >>>x
##        [3, 14, 53]
##    >>>cele(list(str(2**20)))
##        [1, 0, 4, 8, 5, 7, 6


#úvodní a prázdný řádek:
print('DEFINOVÁNÍ FUNKCE - ČÍSLA NA CELÁ ČÍSLA')
print('funkce načte textový seznam s čísli a převede je na celé číslo')
print()


#definování funkce:
def cele(seznam):
    'funkce vrátí nový seznam, kde všechna čísla převede na celé číslo'
    n_seznam = [None] * len(seznam)
    for i, prvek in enumerate(seznam):
        n_seznam[i] = int(prvek)
    return n_seznam


#seznam:
x = [3.14, '14', 53]


#intro:
print('Seznam, který je zde pro ukázku funkce:')
print(x)
print()
input('zmáčkni [enter] pro zobrazení výsledku')
print()


#výstup:
print(cele(x))
        

#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]') 
