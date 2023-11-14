##  Na prednáške si sa zoznámil s funkciou je_prvocislo(cislo),
##  ktorá pomocou funkcie pocet_delitelov(cislo) zisťovala,
##  či je dané cislo prvočíslo.
##  Oprav túto funkciu je_prvocislo(cislo) tak,
##  aby nevyužívala pocet_delitelov(cislo),
##  ale vo while-cykle zisťovala,
##  či neexistuje aspoň jeden deliteľ v intervale <2, odmocnina>.
##  Funkcia sa bude postupne snažiť nájsť takého deliteľa daného čísla,
##  ktorého druhá mocnina nie je väčšia ako dané číslo.
##  Napríklad, číslo 25 bude postupne deliť 2, 3, 4, 5
##  (pre všetky ich druhá mocnina nie je väčšia ako 25)
##  a na 5 skončí, lebo delí 25.
##  Číslo 37 sa tiež pokúsi deliť 2, 3, 4, 5, 6 (žiadne z nich nie je deliteľom)
##  a keďže pre všetky väčšie je ich druhá mocnina väčšia ako 37,
##  vyhlásime 37 za prvočíslo.
##  Okrem funkcie je_prvocislo(cislo) napíš aj funkciu dvojicky(od, do),
##  ktorá v danom intervale <od, do>
##  nájde všetky prvočíselné dvojičky (ich rozdiel je 2).
##
##  Napríklad:
##    >>> dvojicky(3, 50)
##    3 5
##    5 7
##    11 13
##    17 19
##    29 31
##    41 43
##    >>> dvojicky(1000000, 1000300)
##    1000037 1000039
##    1000211 1000213
##    1000289 1000291


#úvodní a prázdný řádek:
print('DEFINOVÁNÍ FUNKCE - DVOJIČKY')
print('funkce hledá v určitém intervalu prvočíselné dvojičky')
print()


#definování funkce:
def je_prvocislo(cislo):
    a = 2                                   #proměná dělitele
    while cislo >= a**2:                    #cyklus - dokud je číslo menší nebo rovno než dělitel na druhou
        if cislo % a == 0:                  #podmínka - když zbytek po dělení je nula
            return False                    #vrať "False"
        a += 1                              #pokud ne, připočti 1 a cyklus zopakuj
    return True                             #pokud se dělitel nenajde, vrať "True"


#definování funkce:
def dvojicky(od, do):
    a = 0                                   #proměná pro poslední nalezené prvočíslo
    for i in range(od, do):                 #caklus - pro všechna čísla "od" a "do"
        if je_prvocislo(i):                 #zjisti, zda se jedná o prvočíslo
            if i - a == 2:                  #podmínka - pokud ano zjisti, zda rtozdíl mezi tímto číslem a předešlím je 2
                print(a, i)                 #pokud ano - vypiš obě čísla
            a = i                           #pokud ne - přepiš nalezené prvočíslo do promněné "a" a pokračuj v cyklu
    
#vstup:
od = int(input('Zadej první číslo: '))
do = int(input('Zadej první číslo: '))


#výstup:
print(f'Mezi čísly {od} a {do} se nacházejí následující dvojce prvočísel s rozdílem 2 čísel: ')
dvojicky(od, do)
        

#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]')  
        
        
