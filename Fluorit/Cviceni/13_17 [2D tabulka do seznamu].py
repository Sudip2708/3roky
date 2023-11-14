##Napíš funkciu do_radu(tab),
##ktorá vráti vytvorenú jednorozmernú tabuľku (zoznam list) z riadkov dvojrozmernej tabuľky tab.
##Použi na to jeden for-cyklus a metódu extend - štandardná funkcia,
##pomocou ktorej môžeme k nejakému zoznamu prilepiť na koniec naraz viac prvkov
##(na rozdiel od append, ktorý vie prilepiť len jeden prvok).
##Napríklad:
##>>> tab1 = [[1], [2, 3, 4], [5, 6], [7]]
##>>> zoz = do_radu(tab1)
##>>> zoz
##    [1, 2, 3, 4, 5, 6, 7]
##>>> do_radu([['prvy'], [], ['druhy', 'treti']])
##    ['prvy', 'druhy', 'treti']
##


#úvodní a prázdný řádek:                                                  
print('2D TABULKA DO 1. SEZNAMU')                              
print('''
Program obsahuje funkci která z 2D tabulky
vytvoří jednorozměrnou tabulku (seznam)''')


def do_radu(tab):
    seznam = []
    for i in tab:
        seznam.extend(i)
    return seznam


input('''
Zmáčkni [enter] pro zobrazení výsledku pro tabulku:
tab1 = [[1], [2, 3, 4], [5, 6], [7]]
''')
tab1 = [[1], [2, 3, 4], [5, 6], [7]]
print(do_radu(tab1))


input('''
Zmáčkni [enter] pro zobrazení výsledku pro tabulku:
tab2 = [['prvy'], [], ['druhy', 'treti']]
''')
tab2 = [['prvy'], [], ['druhy', 'treti']]
print(do_radu(tab2))


input('''
Zmáčkni [enter] pro ukončení programu
''')
