##  Napíš funkciu rozklad(x),
##  ktorá rozloží dané celé číslo x na prvočinitele (súčin prvočísel).
##  Výsledkom funkcie bude zoznam týchto prvočísel (prvočiniteľov).
##  Funkcia nič nevypisuje.
##  Napríklad:
##    >>> r = rozklad(478632)
##    >>> r
##        [2, 2, 2, 3, 7, 7, 11, 37]
##    >>> rozklad(43)
##        [43]


#úvodní a prázdný řádek:
print('DEFINOVÁNÍ FUNKCE - ROZKLAD NA PRVOČINITELE')
print('funkce vytvoří seznam prvočinitelů námi zadaného čísla')
print()


#definování funkce:
def rozklad(x):
    seznam = []
    for i in range(x):
        while x % (i+2) == 0:
            seznam.append(i+2)
            x = x // (i+2)
    return seznam


#vstup:
n = int(input('Zadej číslo, které chceš rozložit na prvočinitele: '))
print()

#výstup:
r = rozklad(n)
print('Prvočinitele: ')
print(r)
        

#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]') 
