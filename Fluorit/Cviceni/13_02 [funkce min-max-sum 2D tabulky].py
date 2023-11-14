##Zadefinuj funkcie max2(tab), min2(tab) a sum2(tab),
##ktoré zistia najväčší prvok, najmenší prvok
##a súčet všetkých prvkov dvojrozmernej tabuľke.
##Využi štandardné funkcie max(), min() a sum().
##Napríklad:
##>>> p = [[1, 6, 3.14], [0.5, 1.5, 2.5]]
##>>> max2(p)
##6
##>>> min2(p)
##    0.5
##>>> sum2(p)
##    14.64
##>>> r = [[-1, -2], [-3, -4]]
##>>> max2(r)
##-1
##>>> min2(r)
##-4


#úvodní a prázdný řádek:                                                  
print('FUNKCE MIN, MAX, SUM 2D TABULKY')                              
print('''
Program obsahuje 3 funkce:
max2(2d_seznam) - pro zobrazení největšího prvku 2D tabulky
min2(2d_seznam) - pro zobrazení nejmenšího prvku 2D tabulky
sum2(2d_seznam) - pro zobrazení součtu všech prvků 2D tabulky
''')


def max2(tab):                  #definice funkce pro největší prvek tabulky
    vysledek = tab[0][0]            #proměnná pro výsledek s vloženou první hodnotou prvního řádku (podseznamu)
    for i in tab:                   #cyklus - pro každý řádek (podseznam) v tabulce
        if max(i) > vysledek:           #podmínka - pokud největší číslo řádku je větší než číslo ve výsledku
            vysledek = max(i)               #přesměruj výsledek na tuto hodnotu
    return vysledek                 #vrať výsledek


def min2(tab):                  #definice funkce pro nejmenší prvek tabulky
    vysledek = tab[0][0]            #proměnná pro výsledek s vloženou první hodnotou prvního řádku (podseznamu)
    for i in tab:                   #cyklus - pro každý řádek (podseznam) v tabulce
        if min(i) < vysledek:           #podmínka - pokud nejmenší číslo řádku je menší než číslo ve výsledku
            vysledek = min(i)               #přesměruj výsledek na tuto hodnotu
    return vysledek                 #vrať výsledek


def sum2(tab):                  #definice funkce pro součet všech prvků tabulky
    vysledek = 0                    #proměnná pro výsledek s vloženou prvnotní nulou
    for i in tab:                   #cyklus - pro každý řádek (podseznam) v tabulce
        vysledek += sum(i)              #přičti do výsledkou součet hodnot řádku (podseznamu)
    return vysledek                 #vrať výsledek


input('''
Zmáčkni [enter] pro zobrazení výsledku pro tabulku:
p = [[1, 6, 3.14], [0.5, 1.5, 2.5]]
''')
p = [[1, 6, 3.14], [0.5, 1.5, 2.5]]
print('Největší prvek 2D tabulky: ', max2(p))
print('Nejmenší prvek 2D tabulky: ', min2(p))
print('Součet všech prvků 2D tabulky: ', sum2(p))


input('''
Zmáčkni [enter] pro zobrazení výsledku pro tabulku:
r = [[-1, -2], [-3, -4]]
''')
r = [[-1, -2], [-3, -4]]
print('Největší prvek 2D tabulky: ', max2(r))
print('Nejmenší prvek 2D tabulky: ', min2(r))
print('Součet všech prvků 2D tabulky: ', sum2(r))


input('''
Zmáčkni [enter] pro ukončení programu
''')

