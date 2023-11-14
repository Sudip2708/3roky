##  Napíš funkciu priemer(a, b), ktorá vypočíta priemer dvoch zadaných čísel.
##  Funkcia nič nevypisuje, ale pomocou return vráti vypočítanú hodnotu.
##  Otestuj ju s rôznymi hodnotami parametrov.
##
##  Napríklad:
##    4. >>> priemer(1, 4)
##    5. 2.5
##    6. >>> priemer(3.14, 31.4)
##    7. 17.27


#úvodní a prázdný řádek:
print('DEFINOVÁNÍ FUNKCE - PRŮMĚR')
print('funkce spočítá průměr dvou zadaných čísel')
print()


#definování funkce:
def priemer(a, b):                      #parametry - 1. číslo, 2. číslo
    c = (a + b) / 2                     #výpočet průměru
    return c                            #vrácení výsledku


#vstup:
a = int(input('Zadej první číslo: '))
b = int(input('Zadej první číslo: '))


#výstup:
print(f'Průměr {a} a {b} je {priemer(a, b)}')
        

#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]')  
