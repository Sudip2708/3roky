##  Napíš funkciu start(zoznam, n),
##  ktorá z daného zoznamu znakových reťazcov vyrobí (a vráti) nový,
##  v ktorom sa z každého reťazca ponechá len prvých n znakov.
##  Funkcia nemodifikuje vstupný zoznam a nič nevypisuje.
##  Napríklad:
##    >>>mesiace = ['januar', 'februar', 'marec', 'april', 'maj',
##                   'jun', 'jul', 'august', 'september',
##                   'oktober', 'november', 'december']
##    >>>zoz3 = start(mesiace, 3)
##    >>>zoz3
##        ['jan', 'feb', 'mar', 'apr', 'maj', 'jun', 'jul', 'aug', 'sep', 'okt', 'nov', 'dec']
##    >>>start(mesiace, 1)
##        ['j', 'f', 'm', 'a', 'm', 'j', 'j', 'a', 's', 'o', 'n', 'd']
##    >>>start(den, 2)             # den z prvej úlohy
##        ['po', 'ut', 'st', 'št', 'pi', 'so', 'ne']


#úvodní a prázdný řádek:
print('DEFINOVÁNÍ FUNKCE - ZKRATKY')
print('funkce všechny delší položky seznamu zkrátí na námi uvedený počet znaků')
print()


#definování funkce:
def start(seznam, n):
    'funkce vrátí nový seznam, kde z každého text. řeť. ponechá jen prvních "n" znaků'
    n_seznam = [None] * len(seznam)
    for i, prvek in enumerate(seznam):
        n_seznam[i] = prvek[:3]
    return n_seznam


#seznam:
mesiace = ['januar', 'februar', 'marec', 'april', 'maj', 'jun', 'jul', 'august', 'september', 'oktober', 'november', 'december']


#intro:
print('Seznam, který je zde pro ukázku funkce:')
print(mesiace)
print()
print('Pro ukázku funkce je hodnota zkrácení zvolena "3"')
print()
input('zmáčkni [enter] pro zobrazení výsledku')
print()


#výstup:
zoz3 = start(mesiace, 3)
print(zoz3)
        

#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]')         
    
