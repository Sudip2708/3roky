##Modifikuj funkciu vypis(tab, sirka=4),
##ktorá vypisuje dvojrozmernú tabuľku do riadkov,
##pričom každý prvok je formátovaný na zadanú šírku,
##napríklad pre sirka = 5 takto f'{repr(prvok):>5}'.
##Otestuj:
##>>> vypis([[1, 6, 3.14], [0.5, 1.5, 2.5]], 5)
##        1     6  3.14
##      0.5   1.5   2.5
##>>> vypis([[1, 2, 3], [None, None], ['4', '5', '6'], ['Python', 3.9]])
##       1    2    3
##    None None
##     '4'  '5'  '6'
##    'Python'  3.9


#úvodní a prázdný řádek:                                                  
print('VÝPIS DVOJROZMĚRNÉ TABULKY')                              
print('''
Program obsahuje funkci "vypis(seznam, šířka_rozestupu)",
která vypíše dvojrozměrnou tabulku do sloupců a řádků
''')


def vypis(tab, sirka=4):                #definice funkce pro výpis tabulky (parametry - tabulka, počet znaků na rozestupy jednotlivých hodnot)
    for riadok in tab:                      #cyklus - pro každý řádek (seznam) v tabulce
        for prvok in riadok:                    #cyklus - pro každou hodnotu v seznamu řádku
            prvok = f'{repr(prvok):>{sirka}}'   #formát výpisu hodnoty
            print(prvok, end=' ')               #výpis hodnoty bez odskočení na nový řádek
        print()                             #výpis odskočení na nový řádek


input('''
Zmáčkni [enter] pro zobrazení příkazu:
vypis([[1, 6, 3.14], [0.5, 1.5, 2.5]], 5)
''')
vypis([[1, 6, 3.14], [0.5, 1.5, 2.5]], 5)


input('''
Zmáčkni [enter] pro zobrazení příkazu:
vypis([[1, 2, 3], [None, None], ['4', '5', '6'], ['Python', 3.9]])
''')
vypis([[1, 2, 3], [None, None], ['4', '5', '6'], ['Python', 3.9]])


input('''
Zmáčkni [enter] pro ukončení programu
''')
