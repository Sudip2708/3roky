##  Napíš funkciu vsetky_rozne(zoznam),
##  ktorá zistí (vráti True alebo False), či sú všetky prvky zoznamu rôzne.
##  Najprv si vyrob utriedený pomocný zoznam (nepokaz pôvodný) a v ňom zisťuj,
##  či sa nenachádzajú dve rovnaké hodnoty za sebou.
##  Napríklad:
##    >>> vsetky_rozne([3, 8, 7, 9, 4, 1, 6, 10, 5, 2])
##        True
##    >>> zoz = [3, 8, 7, 9, 4, 1, 6, 3, 10, 5, 2]
##    >>> vsetky_rozne(zoz)
##        False
##    >>> zoz
##        [3, 8, 7, 9, 4, 1, 6, 3, 10, 5, 2]


#úvodní a prázdný řádek:
print('FUNKCE - VŠECHNY ZNAKY RŮZNÉ')
print('''funkce ověří, zda jsou všechny položky seznamu různé
vrací hodnotu True / False
pouze pro zobrazení''')
print()
input('>>zmáčkni [enter] pro pokračování<<')
print()


#definování funkce:
def vsetky_rozne(zoznam):
    a = sorted(zoznam)
    b = ''
    for i in a:
        if i == b:
            return False
        else:
            b = i
    return True


#vstup a výstup
print("1. seznam na ověření: [3, 8, 7, 9, 4, 1, 6, 10, 5, 2]")
input('>>zmáčkni [enter] pro zobrazení<<')
print('Výsledek: ', vsetky_rozne([3, 8, 7, 9, 4, 1, 6, 10, 5, 2]))
print()
print("1. seznam na ověření: [3, 8, 7, 9, 4, 1, 6, 3, 10, 5, 2]")
input('>>zmáčkni [enter] pro zobrazení<<')
print('Výsledek: ', vsetky_rozne([3, 8, 7, 9, 4, 1, 6, 3, 10, 5, 2]))
   

#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]') 
