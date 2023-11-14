##  Na prednáške si sa zoznámil s funkciou nsd(a, b),
##  ktorá počítala najväčší spoločný deliteľ dvoch čísel.
##  Inšpiruj sa touto funkciou a napíš funkciu nsn(a, b),
##  ktorá vypočíta najmenší spoločný násobok dvoch čísel.
##
##  Napríklad pre volania:
##    5. a, b = 129, 162
##    6. print(f'nsn({a}, {b}) =', nsn(a, b))
##    7. a, b = 60, 168
##    8. print(f'nsn({a}, {b}) =', nsn(a, b))
##
##  dostaneme výstup:
##    nsn(129, 162) = 6966
##    nsn(60, 168) = 840


#úvodní a prázdný řádek:
print('DEFINOVÁNÍ FUNKCE - NEJMENŠÍ SPOL. NÁSOBEK')
print('funkce vypočítá nejmenší společný násobek dvou čísel')
print()


#definování funkce:
def nsn(a, b):
    c = a                               #přiřazení vstupní hodnoty "a" do náhradní promněné "c"
    d = b                               #přiřazení vstupní hodnoty "b" do náhradní promněné "d"
    if a > b:                           #podmínka - když je první číslo menší než druhé číslo
        while d % a != 0:               #cyklus - dokud zbytek po dělení mezi "d" a "a" není 0
            d += b                      #připočítávej k "d" hodnotu "b"
        return d                        #jeli podmínka cyklu splněna, vrať výsledné "d"
    else:                               #když výše uvedená podmínka neplatí
        while c % b != 0:               #cyklus - dokud zbytek po dělení mezi "c" a "b" není 0
            c += a                      #připočítávej k "c" hodnotu "a"
        return c                        #jeli podmínka cyklu splněna, vrať výsledné "c"


#vstup:
a = int(input('Zadej první číslo: '))
b = int(input('Zadej první číslo: '))


#výstup:
print(f'Nejmenší společný násobek {a} a {b} je číslo: {nsn(a, b)}')
        

#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]')  
