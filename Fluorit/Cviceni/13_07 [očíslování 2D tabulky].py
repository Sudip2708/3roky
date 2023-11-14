##Zadefinuj funkciu ocisluj2(tab),
##ktorá zmení všetky prvky dvojrozmernej tabuľky tak,
##že ich postupne prechádza po stĺpcoch a čísluje ich celými číslami od 0.
##Riadky tabuľky nemusia mať rovnakú dĺžku.
##Napríklad:
##>>> ab = [[1, 1], [], [1, 1, 1], [1], [1, 1, 1, 1]]
##>>> ocisluj2(ab)
##>>> vypis(ab)
##       0    4
##
##       1    5    7
##2
##       3    6    8    9


#úvodní a prázdný řádek:                                                  
print('OČÍSLOVÁNÍ TABULKY')                              
print('''
Program projde všemi prvky tabulky
a změní jejich hodnotu na hodnotu pořadí.
''')


def vypis(tab, sirka=4):                        #definice funkce pro výpis dvojrozměrné tabulky
    for riadok in tab:                              #cyklus - pro každý řádek tabulky
        for prvok in riadok:                            #cyklus - pro každý prvek řádku
            print(f'{repr(prvok):>{sirka}}', end=' ')       #vytiskni hodnotu dle formátu pro počet míst, na konci neodskakuj na nový řádek
        print()                                         #po přečtení řádku vytiskni i znak pro nový řádek


def ocisluj2(tab):
    poradi = nejvic_polozek = 0
    for sez in tab:
        if len(sez) > nejvic_polozek:
            nejvic_polozek = len(sez)
    for ix in range(nejvic_polozek):
        for sloupec in tab:
            if len(sloupec) > ix:
                sloupec[ix] = poradi
                poradi += 1
                
 
input('''
Zmáčkni [enter] pro zobrazení výsledku pro tabulku:
ab = [[1, 1], [], [1, 1, 1], [1], [1, 1, 1, 1]]
''')
ab = [[1, 1], [], [1, 1, 1], [1], [1, 1, 1, 1]]
ocisluj2(ab)
vypis(ab)


input('''
Zmáčkni [enter] pro ukončení programu
''')
