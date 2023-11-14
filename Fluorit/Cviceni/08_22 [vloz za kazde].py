##  Napíš funkciu vloz_za_kazde(zoznam, hodnota),
##  ktorá do daného zoznamu vloží za každý prvok danú hodnotu.
##  Funkcia nič nevracia ani nevypisuje, len modifikuje hodnotu zoznamu.
##  Napríklad:
##    >>> z = list('Python')
##    >>> vloz_za_kazde(z, 99)
##    >>> z
##        ['P', 99, 'y', 99, 't', 99, 'h', 99, 'o', 99, 'n', 99]



#úvodní a prázdný řádek:
print('DEFINOVÁNÍ FUNKCE - VLOŽ ZA KAŽDÉ')
print('funkce upravuje seznam tím, že za každý prvek vloží námi definovanou hodnotu')
print()


#definování funkce:
def vloz_za_kazde(seznam, hodnota):
    for i in range(len(seznam)):
        seznam.append(seznam[0])
        seznam.append(hodnota)
        seznam.pop(0)

def rozdel(retazec):
    'vrátí znaky a slova oddělené čárkou'
    n_retazec = ''
    seznam = []
    for i in retazec:
        if i != ',':
            n_retazec += i
        else:
            seznam.append(n_retazec.strip())
            n_retazec = ''
    return(seznam)


#vstup:
a = input('Zapiš seznam (text, či hodnoty oddělené čárkou): ')
b = input('Zapiš hodnotu, kterou chceš text, či seznam proložit: ')

        
#seznam:
z = rozdel(a)


#volání funkce:
vloz_za_kazde(z, b)


#výstup:
print()
print('Výsledný seznam: ')
print(z)
        

#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]')
        
