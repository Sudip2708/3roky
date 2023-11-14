##Napíš funkciu pridaj_sucty(tab),
##ktorá podobne ako v predchádzajúcej úlohe počíta súčty prvkov po riadkoch,
##ale ich ukladá na koniec každého riadka tabuľky.
##Funkcia nič nevracia ani nevypisuje.
##Namiesto toho modifikuje vstupnú tabuľku.
##Napríklad:
##>>> a = [[1, 2, 3], [4], [5, 6]]
##>>> pridaj_sucty(a)
##>>> vypis(a)
##       1    2    3    6
##       4    4
##       5    6   11
##>>> t = [['1', 'x', '2'], [], [5, 6], [3.1, 4], [(5, 6), (7,)]]
##>>> pridaj_sucty(t)
##>>> vypis(t, 7)
##        '1'     'x'     '2'   '1x2'
##       None
##          5       6      11
##        3.1       4     7.1
##     (5, 6)    (7,) (5, 6, 7)


#úvodní a prázdný řádek:                                                  
print('PŘIDÁNÍ SOUČTU DO TABULKY')                              
print('''
Program sečte obsah podtabulky v 2D tabulce
a hodnotu součtu přidá na konec podtabulky
''')


def vypis(tab, sirka=4):                        #definice funkce pro výpis dvojrozměrné tabulky
    for riadok in tab:                              #cyklus - pro každý řádek tabulky
        for prvok in riadok:                            #cyklus - pro každý prvek řádku
            print(f'{repr(prvok):>{sirka}}', end=' ')       #vytiskni hodnotu dle formátu pro počet míst, na konci neodskakuj na nový řádek
        print()                                         #po přečtení řádku vytiskni i znak pro nový řádek

def secti(sez):                                 #dedfinice rekurzivní funkce (parametr - neprázdný seznamú)
    if len(sez) == 1:                               #pokud má seznam (už) jen jednu položku
        return sez[0]                                   #vrať tuto položku
    return sez[0] + secti(sez[1:])                  #návratová hodnota - seznam poniž o první položku a znovu volej + hodnoty přičti k poslední položce


def pridaj_sucty(tab):                          #definice funkce pro přidání součtu vnitřních seznamů na jejich konec
    vysledek = []                                   #proměnná pro výsledný seznam hodnot
    for radek in tab:                               #cyklus - pro každý řádek ze seznamu tabulky
        if len(radek) == 0:                             #pokud je řádek prázdný
            radek.append(None)                              #přidej do seznamu 'vysledek' hodnotu 'None'
        else:                                           #pokud řádek není prázdný
            radek.append(secti(radek))                      #přidej do seznamu 'vysledek' výsledek volání rekurzivní funkce 'secti' 


input('''
Zmáčkni [enter] pro zobrazení výsledku pro tabulku:
a = [[1, 2, 3], [4], [5, 6]]
''')
a = [[1, 2, 3], [4], [5, 6]]
pridaj_sucty(a)
vypis(a)


input('''
Zmáčkni [enter] pro zobrazení výsledku pro tabulku:
t = [['1', 'x', '2'], [], [5, 6], [3.1, 4], [(5, 6), (7,)]]''')
t = [['1', 'x', '2'], [], [5, 6], [3.1, 4], [(5, 6), (7,)]]
pridaj_sucty(t)
vypis(t, 7)


input('''
Zmáčkni [enter] pro ukončení programu
''')

