##  Prepíš funkciu enum z (18) úlohy tak,
##  aby neobsahovala cyklus a využila tvoju funkciu moj_zip.
##  Teda:
##    def enum(postupnost):
##        return ... moj_zip ...


#úvodní a prázdný řádek:
print('FUNKCE - ENTICE SE ZIPEM')
print('''funkce ze seznamu vztvoří ntici, kde pro kaaždou položku
ze seznamu vytvoří dvoupoložkovou entici, kde první
položka je její index''')
print()


#definování funkce:
def moj_zip(post1, post2):
    vysledek = []
    for i in range(len(post1)):
        vysledek.append((post2[i], post1[i]))
    return vysledek


def enum(postupnost):
    post1 = postupnost
    post2 = list(range(0, len(post1)))
    return moj_zip(post1, post2)


#vstup:
a = input('''Zadej pár různých hodnot (text, číslo), oddělených mezerou:
''').split()
print()
print(f'Výsledek: {enum(a)}')


#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]') 
