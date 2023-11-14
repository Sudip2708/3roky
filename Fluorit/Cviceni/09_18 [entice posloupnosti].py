##  Napíš funkciu enum(postupnost),
##  ktorá vráti (return) n-ticu dvojíc.
##  V tejto n-tici je prvý prvok poradové číslo (od 0 do počet prvkov postupnosti minus 1)
##  a druhým je prvok z danej postupnosti.
##  Malo by to dať rovnaký výsledok ako tuple(enumerate(postupnost))
##  ale bez použitia enumerate.
##  Napríklad:
##    >>> enum([12, 'dva', 3.14])
##        ((0, 12), (1, 'dva'), (2, 3.14))


#úvodní a prázdný řádek:
print('FUNKCE - ENTICE POSTUPNOSTI')
print('''funkce ze seznamu vztvoří ntici, kde pro kaaždou položku
ze seznamu vytvoří dvoupoložkovou entici, kde první
položka je její index
pouze pro zobrazení''')
print()
input('>>zmáčkni [enter] pro zobrazení<<')
print()


#definování funkce:
def enum(postupnost):
    pocitadlo = 0
    vysledek = []
    for i in postupnost:
        vysledek.append((pocitadlo, i))
        pocitadlo += 1
    return tuple(vysledek)


#vstup a výstup:
a = [12, 'dva', 3.14]
print('Vstupní seznam: ')
print(a)
print()
print('Výstup ntice: ')
print(repr(enum(a)))
     

#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]') 
