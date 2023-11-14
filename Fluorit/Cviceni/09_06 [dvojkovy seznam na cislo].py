##  Napíš funkciu z_dvojkovej(zoznam),
##  ktorá dostane zoznam cifier dvojkového zápisu čísla v tvare z predchádzajúcej úlohy.
##  Funkcia vráti celé číslo (return),
##  ktorého cifry v dvojkovej sústave zodpovedajú zadanému zoznamu.
##  Napríklad:	
##    >>> z_dvojkovej([1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1])	
##    11213	
##    >>> z = [1] + [0] * 20	
##        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]	
##    >>> z_dvojkovej(z)	
##    1048576	
##    >>> 2 ** 20	
##    1048576	
##    Využi funkciu int(reťazec, 2), pomocou ktorej sa zo znakového reťazca
##    s dvojkovým zápisom čísla vyrobí celé číslo.	


#úvodní a prázdný řádek:
print('FUNKCE - Z DVOJKOVÉ')
print('''funkce načte seznamu jedniček a nul, a vrátí odpovídající hodnotu
v desítkové soustavě''')
print()


#definování funkce:
def z_dvojkovej(zoznam):
    a = ''
    for i in zoznam:
        a += str(i)
    b = int(a, 2)
    return b


#vstup:
a = list(input('Zadej číslo v dvojkové soustavě (1/0): '))


#prázdný řádek a výstup:
print()
print('Vámi zadané číslo reprezentuje v 10 soustavě číslo: ', z_dvojkovej(a))
     

#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]') 	

