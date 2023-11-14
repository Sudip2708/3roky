##  Napíš funkciu od_zip(zoznam),
##  ktorá bude fungovať ako opak funkcie moj_zip.
##  Funkcia dostáva zoznam dvojíc a vráti dva zoznamy prvých a druhých prvkov dvojíc.
##  Napríklad:
##    >>> z1, z2 = od_zip([(2, 'a'), ('h', 3), (5, 'o'), ('j', 7)])
##    >>> z1
##        [2, 'h', 5, 'j']
##    >>> z2
##        ['a', 3, 'o', 7]


#úvodní a prázdný řádek:
print('FUNKCE - ODZIPOVAČ')
print('''funkce rozdělí seznam s dvoupoložkovými nticemi na dva samostatné seznami
pouze pro zobrazení''')
print()
input('>>zmáčkni [enter] pro zobrazení<<')
print()


#definování funkce:
def od_zip(zoznam):
    z1 = []
    z2 = []
    for i in zoznam:
        z1.append(i[0])
        z2.append(i[1])
    return z1, z2


#vstup a výstup:
a = [(2, 'a'), ('h', 3), (5, 'o'), ('j', 7)]
z1, z2 = od_zip(a)
print('Vstupní seznam: ')
print(a)
print()
print('Výstupní 1. seznam: ', z1)
print('Výstupní 2. seznam: ', z2)
     

#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]') 
