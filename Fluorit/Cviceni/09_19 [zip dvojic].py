##  Python ponúka ešte jednu štandardnú funkciu zip.
##  Táto funkcia, keď dostane nejaké dve postupnosti
##  (napríklad zoznam, n-ticu, reťazec, range, …),
##  vytvorí z nich jednu novú postupnosť dvojíc (tuple):
##  v každej takejto dvojici je jeden prvok z prvej a jeden z druhej postupnosti.
##  Môžeš vyskúšať, napríklad:	
##    >>> list(zip('python', [2, 3, 5, 7]))	
##        [('p', 2), ('y', 3), ('t', 5), ('h', 7)]	
##    Zrejme, ak je jedna z týchto postupností kratšia, výsledok sa nastaví podľa nej.
##    Napíš funkciu moj_zip(post1, post2), ktorá z dvoch postupností
##    (iterovateľných objektov možno rôznej dĺžky) vytvorí jeden zoznam dvojíc.
##    Nepouži štandardnú funkciu zip().	


#úvodní a prázdný řádek:
print('FUNKCE - ZIP DVOJIC')
print('''funkce zipovitě seskládá obsah dvou seznamů dle délky toho kratšího
a vytvoří nový seznam s vloženými nticemi dvojic
pouze k zobrazení''')
print()
input('>>zmáčkni [enter] pro zobrazení<<')
print()


#definování funkce:
def moj_zip(post1, post2):
    vysledek = []
    if len(post1) > len(post2):
        pocet = len(post2)
    else:
        pocet = len(post1)
    for i in range(pocet):
        vysledek.append((post1[i], post2[i]))
    return vysledek


#vstup a výstup:
a = (None, 1, None, None, 2, None)
print('1. seznam: [p, y, t, h, o, n]')
print('2. seznam: [2, 3, 5, 7]')
print()
print('Výsledný seznam dvojic: ')
print(moj_zip('python', [2, 3, 5, 7]))

     
#alternativa pythonu:
#print(list(zip('python', [2, 3, 5, 7])))


#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]') 
