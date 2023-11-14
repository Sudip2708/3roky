##  Napíš funkciu postupnost(start, koniec),
##  ktorá vytvorí znakový reťazec z postupnosti čísel range(start, koniec).
##  Čísla v tejto postupnosti budú oddelené znakom medzera ' '.
##
##  Napríklad:
##    >>>p = postupnost(5, 13)
##    >>>p
##    '5 6 7 8 9 10 11 12'
##
##  Do funkcie pridaj ešte jeden parameter postupnost(start, koniec, krok=1) tak,
##  aby fungovalo napríklad:
##    >>>p = postupnost(13, 5, -2)
##    >>>p
##    '13 11 9 7'


#úvodní a prázdný řádek:
print('DEFINOVÁNÍ FUNKCE - POSLOUPNOST DVOU ČÍSEL S KROKEM,')
print('funkce vypíše v zadaném kroku všechna čísla mezi prvním a druhým zadaným číslem')
print()


#definování funkce:
def postupnost(start, koniec, krok=1):
    '''Funkce vytváří z řetězce z posloupnosti čísel v daném kroku.'''
    vysledek = ''                           #promněná výsledku
    for i in range(start, koniec+1, krok):  #cyklus - dle parametrů
        if i == koniec:                     #podmínka - pokud "i" není rovno konečnému číslu
            vysledek += str(i)              #připočti číslo k výsledku
        else:                               #jinak
            vysledek += str(i) + ' '        #připočti číslo k výsledku a přidej za něj mezeru
    return(vysledek)                        #vrať výsledek


#vstup:
start = int(input('zadej první číslo: '))
koniec = int(input('zadej druhé, větší číslo: '))
krok = int(input('zadej číslo kroku: '))


#výstup:
print(postupnost(start, koniec, krok))
        

#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]')  
