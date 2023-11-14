##  Napíš funkciu posun(zoznam),
##  ktorá posunie prvky v danom zozname tak, že prvý sa presťahuje na koniec.
##  Funkcia nič nevracia, len zmení obsah pôvodného zoznamu.
##  Napríklad:
##    >>> a = [2, 3, '5', 7, 11]	
##    >>> posun(a)	
##    >>> a	
##        [3, '5', 7, 11, 2]	
##    >>> zoz = 'kto druhemu jamu kope'.split()	
##    >>> for i in range(5):	
##            print(zoz)	
##            posun(zoz)	
##        ['kto', 'druhemu', 'jamu', 'kope']	
##        ['druhemu', 'jamu', 'kope', 'kto']	
##        ['jamu', 'kope', 'kto', 'druhemu']	
##        ['kope', 'kto', 'druhemu', 'jamu']	
##        ['kto', 'druhemu', 'jamu', 'kope']	


#úvodní a prázdný řádek:
print('DEFINOVÁNÍ FUNKCE - POSUN')
print('''funkce vezme první položku seznamu a vloží ji na konec
pouze k zobrazení''')
print()


#definování funkce:
def posun(seznam):
    seznam.append(seznam[0])
    seznam.pop(0)


#vstup a výstup:    
zoz = 'kto druhemu jamu kope'.split()
print('''Text pro vyskoušení funkce: "kto druhemu jamu kope"
(bude převeden na seznam a pak 4x setříděn)''')
print()
input('>>zmáčkni [enter] pro zobrazení<<')
print()
for i in range(5):	
    print(zoz)	
    posun(zoz)
     

#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]') 
