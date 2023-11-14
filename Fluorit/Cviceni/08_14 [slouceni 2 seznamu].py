##  Napíš funkciu zluc(zoz1, zoz2),
##  ktorá z daných dvoch zoznamov zoz1 a zoz2 vyrobí (a vráti) nový,
##  v ktorom budú prvky z pôvodných dvoch zoznamov na striedačku
##  (najprv prvý prvok z prvého, potom prvý prvok z druhého,
##  potom druhý z prvého, atď.).
##  Funkcia nemodifikuje vstupné zoznamy a nič nevypisuje.
##  Napríklad:
##    >>>zoz = zluc([1, 2, 3, 4, 5, 6, 7], [11, 22, 33])
##    >>>zoz
##        [1, 11, 2, 22, 3, 33, 4, 5, 6, 7]
##    >>>zluc(list('Python'), list(range(10)))
##        ['P', 0, 'y', 1, 't', 2, 'h', 3, 'o', 4, 'n', 5, 6, 7, 8, 9]


#úvodní a prázdný řádek:
print('DEFINOVÁNÍ FUNKCE - STŘÍDAVÉ SLOUČENÍ 2 SEZNAMŮ')
print('funkce střídavě spojí dva seznami')
print()


#definování funkce:
def zluc(zoz1, zoz2):
    if len(zoz1) >= len(zoz2):
        pocet = len(zoz1)
    else:
        pocet = len(zoz2)
    seznam = []
    for i in range(pocet):
        if len(zoz1) > i:
            seznam.append(zoz1[i])
        if len(zoz2) > i:
            seznam.append(zoz2[i])
    return seznam


#vstup:
a = list(input('''Zapiš první řetězec, který bude rozebrán na seznam znaků:
'''))
print()
b = list(input('''Zapiš druhý řetězec, který bude rozebrán na seznam znaků:
'''))
print()


#výstup:
print('Sloučení seznamů:')
print(zluc(a, b))
        

#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]') 
