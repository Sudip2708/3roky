##  Napíš funkciu do_dvojic(zoznam),
##  ktorá daný zoznam (alebo n-ticu) párnej dĺžky „rozseká“ na zoznam dvojíc (list s prvkami tuple),
##  dvojice postupne budú (prvý, druhý), (tretí, štvrtý), …
##  Napríklad:	
##    >>> x = do_dvojic(('11', 22, '3', 4))	
##        [('11', 22), ('3', 4)]	
##    Rieš najprv bez použitia funkcie moj_zip() z predchádzajúcich úloh (teda pomocou for-cyklu)
##    a potom pomocou tejto funkcie (bez cyklu).	


#úvodní a prázdný řádek:
print('FUNKCE - SEZNAM DO DVOJIC')
print('''funkce převede několika položkovou ntici (musí mýt sudý počet)
na seznam s dvou položkovými nticemi''')
print()


#definování funkce:
def do_dvojic(zoznam):
    if len(zoznam)%2 != 0:
        print('Seznam nemá sudý počet položek.')
    a = ''
    vysledek = []
    for i in zoznam:
        if len(a) == 0:
            a = i
        else:
            vysledek.append((a, i))
            a = ''
    return vysledek


#vstup a výstup:
print('Vstup: ')
a = input('''Zadej sudý počet libovolných hodnot (text, čísla) pro seznam:
''').split()
print()
print('Výstup: ')
print(do_dvojic(a))


###varianta se zipem:
##def moj_zip(post1, post2):
##    vysledek = []
##    for i in range(len(post1)):
##        vysledek.append((post1[i], post2[i]))
##    return vysledek
##
##def do_dvojic2(zoznam):
##    a = []
##    b = []
##    for i in zoznam:
##        a.append(i)
##        a, b = b, a
##    return moj_zip(a, b)
##
##x = do_dvojic2(('11', 22, '3', 4))
##print(x)
     

#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]')       
    
