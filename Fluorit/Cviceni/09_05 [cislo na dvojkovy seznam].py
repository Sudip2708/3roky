##  Napíš funkciu dvojkova(cislo),
##  ktorá vráti (return) zoznam cifier daného čísla v dvojkovej sústave.
##  Využi f'{cislo:b}'.
##  Napríklad:
##    >>> dvojkova(11213)
##        [1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1]


#úvodní a prázdný řádek:
print('FUNKCE - DO DVOJKOVÉ')
print('''funkce ze zadaného čísla vrátí seznam jedniček a nul,
reprezentující zadané číslo ve dvojkové soustavě''')
print()


#definování funkce:
def dvojkova(cislo):
    a = list(f'{cislo:b}')
    for i in range(len(a)):
        a[i] = int(a[i])
    return a


#vstup:
a = int(input('Zadej číslo: '))


#prázdný řádek a výstup:
print()
print('Číslo v dvojkové soustavě: ')
print(dvojkova(a))
     

#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]') 
