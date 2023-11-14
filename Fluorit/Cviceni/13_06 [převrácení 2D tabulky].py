##Napíš funkciu preklop(tab),
##ktorá vyrobí novú dvojrozmernú tabuľku,
##v ktorej bude pôvodná tabuľka preklopená okolo hlavnej uhlopriečky
##(vymenené riadky a stĺpce).
##Predpokladaj, že všetky riadky majú rovnakú dĺžku.
##Napríklad:
##>>> p = [[1, 2], [5, 6], [3, 4]]
##>>> vypis(preklop(p), 2)
##     1  5  3
##     2  6  4
##>>> vypis(p, 2)
##     1  2
##     5  6
##     3  4


#úvodní a prázdný řádek:                                                  
print('PŘEVRÁCENÍ 2D TABULKY')                              
print('''
Program obsahuje funkcikterá vyrobí novou 2D tabulku,
kde mezi sebou prohodí řádky a sloupce.
''')


def vypis(tab, sirka=4):                        #definice funkce pro výpis dvojrozměrné tabulky
    for riadok in tab:                              #cyklus - pro každý řádek tabulky
        for prvok in riadok:                            #cyklus - pro každý prvek řádku
            print(f'{repr(prvok):>{sirka}}', end=' ')       #vytiskni hodnotu dle formátu pro počet míst, na konci neodskakuj na nový řádek
        print()                                         #po přečtení řádku vytiskni i znak pro nový řádek


def preklop(tab):                               #definice funkce na výměnu řádků a sloupců v dvojrozměrné tabulce
    vysledek = []                                   #proměnná pro výsledný seznam 
    for ix in range(len(tab[0])):                   #cyklus dle počtu položek v sloupci = index pro výpočet z kterého řádku má být hodnota přidaná
        vysledek.append([])                             #přidej do seznamu 'vysledek' nový prázdný seznam
        for radek in tab:                               #cyklus pro každý řádek tabulky
            vysledek[-1].append(radek[ix])                  #přidej do nově vytvořeného seznamu položku z tohoto řádku s aktuálním indexem 
    return vysledek                                 #vrať seznam výsledek
        

input('''
Zmáčkni [enter] pro zobrazení 2D tabulky:
p = [[1, 6, 3.14], [0.5, 1.5, 2.5]]
''')
p = [[1, 2], [5, 6], [3, 4]]
vypis(p, 2)


input('''
Zmáčkni [enter] pro zobrazení nové tabulky
s prohozenými řádky a sloupci:
''')
vypis(preklop(p), 2)



input('''
Zmáčkni [enter] pro ukončení programu
''')
