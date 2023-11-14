##  Napíš funkciu zadaj(pocet),
##  ktorá vráti prečítanú n-ticu čísel zo vstupu (input).
##  Funkcia si vypýta od používateľa, aby zadal príslušný počet čísel
##  (napríklad input(f'zadaj {pocet} čísla: '))
##  a ak ich používateľ nezadá požadovaný počet,
##  bude si tento input pýtať znovu a znovu.
##  Funkcia vráti (return) n-ticu celých čísel a nie n-ticu reťazcov.
##  Napríklad:
##    >>> tri = zadaj(3)
##        zadaj 3 čísla: 12 3
##        zadaj 3 čísla: 12 3 456
##    >>> tri
##        (12, 3, 456)


#úvodní a prázdný řádek:
print('FUNKCE - ZADEJ POČET')
print('''funkce, dle zadaného počtu, vyžádá na vstupu daný počet čísel
oddělených mezerou a ty pak převede na číselnou ntici''')
print()


#definování funkce:
def zadaj(pocet):
    a = []
    while len(a) != pocet:
        a = input(f'Zadaj přesně {pocet} čís. oddělených mezerou: ').split()
    for i in range(len(a)):
        a[i] = int(a[i])
    return tuple(a)


#vstup:
a = int(input('Zadej číslo: '))


#výstup:
print(zadaj(a))
     

#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]') 
