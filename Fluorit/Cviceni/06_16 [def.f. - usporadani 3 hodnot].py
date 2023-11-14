##  Napíš funkciu usporiadaj(h1, h2, h3),
##  ktorá z troch zadaných hodnôt (všetky tri sú rovnakého typu, napríklad reťazce)
##  vytvorí reťazec (vráti ho ako výsledok funkcie)
##  zlepením týchto troch hodnôt v utriedenom poradí:
##  najprv najmenšia (napríklad reťazec prvý v abecede),
##  potom väčšia a na koniec najväčšia.
##  Medzi zlepené reťazce vloží medzeru.
##
##  Napríklad:
##    >>>x = usporiadaj('python', 'pytliak', 'pytagoras')
##    >>>x
##        'pytagoras python pytliak'
##    >>>usporiadaj(345, 123, 234)
##        '123 234 345'


#úvodní a prázdný řádek:
print('DEFINOVÁNÍ FUNKCE - USPOŘÁDÁNÍ')
print('funkce uspořádá tři zadané hodnoty od nejmenší po největší (hodnoty musí být stejného tipu)')
print()


#definování funkce:
def usporiadaj(h1, h2, h3):     
    if h1 > h2:                                         #podmínka - když je 1. hodnota větší než 2.
        if h2 > h3:                                     #podmínka - když je 2. hodnota větší než 3.
            return(f'{str(h3)} {str(h2)} {str(h1)}')    #vrať pořadí: 3, 2, 1
        elif h3 > h1:                                   #podmínka - když je 3. hodnota větší než 1.                                   
            return(f'{str(h2)} {str(h1)} {str(h3)}')    #vrať pořadí: 2, 1, 3
        else:                                           #jinak
            return(f'{str(h2)} {str(h3)} {str(h1)}')    #vrať pořadí: 2, 3, 1
    elif h2 > h3:                                       #podmínka - když je 2. hodnota větší než 3.
        if h3 > h1:                                     #podmínka - když je 2. hodnota větší než 3.
            return(f'{str(h1)} {str(h3)} {str(h2)}')    #vrať pořadí: 1, 3, 2
        else::                                          #jinak
            return(f'{str(h3)} {str(h1)} {str(h2)}')    #vrať pořadí: 3, 1, 2
    else::                                              #jinak
        return(f'{str(h1)} {str(h2)} {str(h3)}')        #vrať pořadí: 1, 2, 3
        

#vstup:
a = input('Zadej 1. hodnotu: ')
b = input('Zadej 1. hodnotu: ')
c = input('Zadej 1. hodnotu: ')


#výstup:
print()
print(f'Vzestupné pořadí těchto 3. hodnot je: {usporiadaj(a, b, c)}')
        

#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]')  
