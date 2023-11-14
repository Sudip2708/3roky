##  Napíš funkciu sucet(retazec), ktorá dostáva znakový reťazec
##  s dvomi celými číslami oddelenými znakom '+'.
##  Funkcia vráti (nič nevypisuje) celé číslo,
##  ktoré je súčtom dvoch čísel v reťazci.
##  Použi metódu retazec.find('+') a funkciu int().
##
##  Napríklad:
##    >>>x = sucet('12+9')
##    >>>x
##        21
##    >>>sucet('987654321+99999')
##        987754320


#úvodní a prázdný řádek:
print('DEFINOVÁNÍ FUNKCE - SOUČET DVOU ČÍSEL')
print('funkce sečte dvě čísla zapsaná jako řetězec s plusem')
print()


#definování funkce:
def sucet(retazec):
    '''Funkce sečte dvě čísla oddělené plusem, zadané jako textový řetězec.'''
    b = int(a[:a.find('+')])                        #nalezení "+" a vypis všeho co je před ním, a převod na číslo
    c = int(a[a.find('+')+1:])                      #nalezení "+" a vypis všeho co je za ním, a převod na číslo
    return(b+c)                                     #vrácení součru


#vstup
a = input('Zadej dvě čísla s plusem mezi nimi (bez mezer), která chceš sečíst: ')


#výstup:
print(f'Součet zadaných čísle je {sucet(a)}')
        

#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]')  
