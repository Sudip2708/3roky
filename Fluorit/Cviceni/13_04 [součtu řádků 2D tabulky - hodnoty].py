##Vylepši funkciu zoznam_suctov(tab) tak,
##aby fungovala nielen pre celočíselné hodnoty,
##ale pre ľubovoľný typ, v ktorom funguje operácia +.
##Pre prázdny riadok tabuľky, funkcia spočíta None.
##Napríklad:
##>>> zoznam_suctov([['1', 'x', '2'], [], [5, 6], [3.1, 4], [(5, 6), (7,)]])
##    ['1x2', None, 11, 7.1, (5, 6, 7)]


#úvodní a prázdný řádek:                                                  
print('SEZNAM SOUČTU ŘÁDKŮ 2D TABULKY (HODNOTY)')                              
print('''
Program obsahuje funkci, která vrací seznam součtu hodnot
jednotlivých řádků 2D tabulky
''')


def secti(sez):                     #dedfinice rekurzivní funkce (parametr - neprázdný seznamú)
    if len(sez) == 1:                   #pokud má seznam (už) jen jednu položku
        return sez[0]                       #vrať tuto položku
    return sez[0] + secti(sez[1:])      #návratová hodnota - seznam poniž o první položku a znovu volej + hodnoty přičti k poslední položce


def zoznam_suctov(tab):             #definice funkce pro součet obsahu řádků dvojrozměrné tabulky
    vysledek = []                       #proměnná pro výsledný seznam hodnot
    for radek in tab:                   #cyklus - pro každý řádek ze seznamu tabulky
        if len(radek) == 0:                 #pokud je řádek prázdný
            vysledek.append(None)               #přidej do seznamu 'vysledek' hodnotu 'None'
        else:                               #pokud řádek není prázdný
            vysledek.append(secti(radek))       #přidej do seznamu 'vysledek' výsledek volání rekurzivní funkce 'secti' 
    return vysledek                     #návratová hodnota - seznam 'vysledek'


input('''
Zmáčkni [enter] pro zobrazení výsledku pro tabulku:
t = [['1', 'x', '2'], [], [5, 6], [3.1, 4], [(5, 6), (7,)]]
''')
t = [['1', 'x', '2'], [], [5, 6], [3.1, 4], [(5, 6), (7,)]]
print('Součet hodnot podtabulek: ', zoznam_suctov(t))


input('''
Zmáčkni [enter] pro ukončení programu
''')
