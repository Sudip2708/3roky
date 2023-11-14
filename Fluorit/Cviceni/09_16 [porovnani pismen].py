##  Napíš funkciu zisti(slovo1, slovo2),
##  ktorá zistí (vráti True alebo False),
##  či sú dve zadané slová zložené presne z tých istých písmen - možno v inom poradí.
##  Napríklad:	
##    >>> zisti('Skola', 'Lasko')	
##        True	
##    >>> zisti('poobede', 'bopeodo')	
##        False	
##    Pomôcka: použi funkciu sorted	


#úvodní a prázdný řádek:
print('FUNKCE - POROVNÁNÍ PÍSMEN')
print('''funkce porovná dvě slova, zda jsou složena ze stejných písmen
vrací hodnotu True / False
pouze pro zobrazení''')
print()
input('>>zmáčkni [enter] pro pokračování<<')
print()


#definování funkce:
def zisti(slovo1, slovo2):
    a = sorted(slovo1.lower())
    b = sorted(slovo2.lower())
    return a == b


#vstup a výstup
print("1) porovnej tyto dvě slova: 'Skola', 'Lasko'")
input('>>zmáčkni [enter] pro zobrazení<<')
print('Výsledek: ', zisti('Skola', 'Lasko'))
print()
print("1) porovnej tyto dvě slova: 'poobede', 'bopeodo'")
input('>>zmáčkni [enter] pro zobrazení<<')
print('Výsledek: ', zisti('poobede', 'bopeodo'))
     

#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]') 
