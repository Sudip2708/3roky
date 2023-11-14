##Textový súbor v každom riadku obsahuje niekoľko slov,
##oddelených medzerou (riadok môže byť aj prázdny).
##Napíš funkciu citaj(meno_suboru),
##ktorá prečíta tento súbor a vyrobí z neho dvojrozmernú tabuľku slov:
##každý riadok tabuľky zodpovedá jednému riadku súboru.
##Napríklad, ak súbor 'text.txt' obsahuje:
##Anicka dusicka
##kde si bola
##ked si si cizmicky
##zarosila
##potom
##>>> x = citaj('text.txt')
##>>> x
##    [['Anička', 'dušička'], ['kde', 'si', 'bola'], ['keď', 'si', 'si', 'čižmičky'], ['zarosila']]


#úvodní a prázdný řádek:                                                  
print('TEXT DO 2D TABULKY')                              
print('''
Program načte textový soubor a uloží jej do 2D tabulky,
kde řákdy tabulky odpovídají řádkům v textu
a sloupce tabulky tvoří jednotlivá slova řádků.
''')


def vypis(tab, sirka=4):                        #definice funkce pro výpis dvojrozměrné tabulky
    for riadok in tab:                              #cyklus - pro každý řádek tabulky
        for prvok in riadok:                            #cyklus - pro každý prvek řádku
            print(f'{repr(prvok):>{sirka}}', end=' ')       #vytiskni hodnotu dle formátu pro počet míst, na konci neodskakuj na nový řádek
        print()                                         #po přečtení řádku vytiskni i znak pro nový řádek


def citaj(meno_suboru):
    seznam = []
    text = open(meno_suboru, 'r')
    for radek in text:
        seznam.append([])
        radek = radek.strip().split()
        for slovo in radek:
            seznam[-1].append(slovo)
    text.close()
    return seznam


input('''
Zmáčkni [enter] pro zobrazení výsledku pro textový
soubor obsahující následující text:

"Anicka dusicka
kde si bola
ked si si cizmicky
zarosila"

''')
meno_suboru = '13_09.txt'
x = citaj(meno_suboru)
#print('2D tabulka: ', x)
print('''Výpis 2D tabulky:
''')
vypis(x, sirka=10)


input('''
Zmáčkni [enter] pro ukončení programu
''')
