##  Napíš funkciu vyhod_none(ntica),
##  ktorá z danej n-tice vyhodí všetky výskyty None.
##  Funkcia vráti (return) túto novú n-ticu (nič nevypisuje).
##  Napríklad:
##    >>> vyhod_none((None, 1, None, None))
##    (1,)


#úvodní a prázdný řádek:
print('DEFINOVÁNÍ FUNKCE - VYHOĎ "NONE"')
print('''funkce vyhodí z n-tice všechny položky "None"
pouze k zobrazení''')
print()
input('>>zmáčkni [enter] pro zobrazení<<')
print()

#definování funkce:
def vyhod_none(ntica):
    vysl = ()
    for i in ntica:
        if i != None:
            vysl += (i,)
    return vysl


#vstup a výstup:
a = (None, 1, None, None, 2, None)
print('n-tice pro utřídění: ')
print(repr(a))
print()
print('n-tice po protřídění: ')
print(repr(vyhod_none(a)))
     

#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]') 
