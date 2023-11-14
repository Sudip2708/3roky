##Napíš funkciu zoznam_suctov(tab)
##počíta súčty prvkov v jednotlivých riadkoch tabuľky
##a ukladá ich do výsledného zoznamu.
##Všetky hodnoty v tabuľke sú celé čísla.
##Napríklad:
##>>> suc = zoznam_suctov([[1, 2, 3], [4], [], [5, 6]])
##>>> suc
##    [6, 4, 0, 11]


#úvodní a prázdný řádek:                                                  
print('SEZNAM SOUČTU ŘÁDKŮ 2D TABULKY (ČÍSLA)')                              
print('''
Program obsahuje funkci, která vrací seznam součtu čísel
jednotlivých řádků 2D tabulky
''')


def zoznam_suctov(tab):             #definice funkce pro součet číselných hodnot řádků tabulky
    vysledek = []                       #proměnná pro seznam na výsledek
    for i in tab:                           #cyklus - pro každý řádek (podseznam) tabulky
        vysledek.append(sum(i))                 #přidej do seznamu výsledek součet všech čísel daného řádku (podseznamu)
    return vysledek                     #vrať seznam 'výsledek'


input('''
Zmáčkni [enter] pro zobrazení výsledku pro tabulku:
p = [[1, 6, 3.14], [0.5, 1.5, 2.5]]
''')
suc = zoznam_suctov([[1, 2, 3], [4], [], [5, 6]])
print('Součet jednotlivých podtabulek: ', suc)


input('''
Zmáčkni [enter] pro ukončení programu
''')

