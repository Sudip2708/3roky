##Zadefinuj funkciu pascalov_trojuholnik(n),
##ktorá vygeneruje prvých n riadkov pascalovho trojuholníka a uloží ich do dvojrozmernej tabuľky.
##Pri vytváraní každého nasledovného riadka tabuľky využi predchádzajúci riadok
##(každý prvok v ňom je súčtom dvoch susedných).
##Napríklad:
##>>> pt = pascalov_trojuholnik(5)
##>>> vypis(pt)
##1
##       1    1
##       1    2    1
##       1    3    3    1
##       1    4    6    4    1


#úvodní a prázdný řádek:                                                  
print('PASKALŮV TROJÚHELNÍK')                              
print('''
Program po zadání hodnoty úpočtu řádků
vytvoří Paskalův trojůhelník.
''')


def vypis(tab, sirka=4):                        #definice funkce pro výpis dvojrozměrné tabulky
    for riadok in tab:                              #cyklus - pro každý řádek tabulky
        for prvok in riadok:                            #cyklus - pro každý prvek řádku
            print(f'{repr(prvok):>{sirka}}', end=' ')       #vytiskni hodnotu dle formátu pro počet míst, na konci neodskakuj na nový řádek
        print()                                         #po přečtení řádku vytiskni i znak pro nový řádek


def pascalov_trojuholnik(n):
    sez = []
    pocet = 0
    for i1 in range(n):
        pocet += 1
        sez.append([])
        for i2 in range(pocet):
            if i2 == 0 or i2 == range(pocet)[-1]:
                sez[i1].append(1)
            else:
                hodnota = sez[i1-1][i2-1] + sez[i1-1][i2]
                sez[i1].append(hodnota)
    return sez
                
                
n = int(input('''
Zadej počet řádků: '''))
print()


pt = pascalov_trojuholnik(n)
vypis(pt)


input('''
Zmáčkni [enter] pro ukončení programu
''')
