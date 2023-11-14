##  Zovšeobecni funkciu sucet(retazec) z predchádzajúcej úlohy:
##  vstupný reťazec obsahuje aspoň jedno číslo a keď ich je viac,
##  sú oddelené znakom '+'.
##  Funkcia vypočíta súčet.
##
##  Napríklad:
##    >>>x = sucet('12+9')
##    >>>x
##        21
##    >>>sucet('1+2+3+4')
##        10
##    >>>sucet('1234')
##        1234


#úvodní a prázdný řádek:
print('DEFINOVÁNÍ FUNKCE - SOUČET VÍCE ČÍSEL')
print('funkce sečte všechna čísla uvedená jako řetězes oddělená plusem')
print()


#definování funkce:
def sucet(retazec):
    '''Funkce sečte čísla oddělené plusem, zadané jako textový řetězec.'''
    a = retazec                                 #řetězec ze vstupu
    b = 0                                       #připočítávadlo součtu
    for i in range(a.count('+')):               #cyklus - dle počtu "+"
        b += int(a[:a.find('+')])               #nalezení prvního čísla a připočítání do součtu
        a = a[a.find('+')+1:]                   #odebrání přičteného čísla z řetězce
    b += int(a)                                 #přípočet posledního čísla
    return(b)                                   #vrácení výsledku


#vstup:
a = input('Zadej čísla s plusem mezi nimi (bez mezer), která chceš sečíst: ')


#výstup:
print(f'Součet zadaných čísle je {sucet(a)}')
        

#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]')  

