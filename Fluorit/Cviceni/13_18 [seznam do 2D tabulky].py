##Napíš funkciu do_dvojrozmernej(postupnost, sirka),
##ktorá bude v istom zmysle fungovať naopak ako funkcia do_radu z predchádzajúceho príkladu:
##funkcia dostáva postupnosť nejakých hodnôt (napríklad jednorozmerný zoznam)
##a vyrobí z nej dvojrozmernú tabuľku, v ktorej okrem posledného riadku majú všetky zadanú šírku.
##Posledný riadok môže byť kratší. Napríklad:
##>>> t1 = do_dvojrozmernej(range(10), 3)
##>>> vypis(t1)
##       0    1    2
##       3    4    5
##       6    7    8
##9
##>>> t2 = do_dvojrozmernej(do_radu(t1), 5)
##>>> vypis(t2)
##       0    1    2    3    4
##       5    6    7    8    9
##>>> vypis(do_dvojrozmernej('programovanie', 5))
##     'p'  'r'  'o'  'g'  'r'
##     'a'  'm'  'o'  'v'  'a'
##     'n'  'i'  'e'


#úvodní a prázdný řádek:                                                  
print('SEZNAM DO 2D TABULKY')                              
print('''
Program obsahuje funkci která ze seznamu
vytvoří, dle hodnoty počtu sloupců,
(poslední parametr) 2D tabulku
''')


def vypis(tab, sirka=4):                        #definice funkce pro výpis dvojrozměrné tabulky
    for riadok in tab:                              #cyklus - pro každý řádek tabulky
        for prvok in riadok:                            #cyklus - pro každý prvek řádku
            print(f'{repr(prvok):>{sirka}}', end=' ')       #vytiskni hodnotu dle formátu pro počet míst, na konci neodskakuj na nový řádek
        print()                                         #po přečtení řádku vytiskni i znak pro nový řádek

def do_radu(tab):
    seznam = []
    for i in tab:
        seznam.extend(i)
    return seznam

def do_dvojrozmernej(postupnost, sirka):
    tabulka = [[]]
    for znak in postupnost:
        if len(tabulka[-1]) < sirka:
            tabulka[-1].append(znak)
        else:
            tabulka.append([znak,])
    return tabulka            
            


input('''
Zmáčkni [enter] pro zobrazení výsledku pro seznam:
t1 = do_dvojrozmernej(range(10), 3)
''')
t1 = do_dvojrozmernej(range(10), 3)
vypis(t1)


input('''
Zmáčkni [enter] pro zobrazení výsledku pro seznam
vytvořený z 2D tabulky t1:
t2 = do_dvojrozmernej(do_radu(t1), 5)
>>funkce do_radu vytváří seznam z 2D tabulky<<
''')
t2 = do_dvojrozmernej(do_radu(t1), 5)
vypis(t2)


input('''
Zmáčkni [enter] pro zobrazení výsledku pro seznam:
t3 = do_dvojrozmernej('programovanie', 5)
''')
t3 = do_dvojrozmernej('programovanie', 5)
vypis(t3)


input('''
Zmáčkni [enter] pro ukončení programu
''')
