##Zapíš funkciu nsd(a, b) (najväčší spoločný deliteľ) rekurzívne:
##triviálny prípad je vtedy, keď a==b, inak ak a>b,
##tak rekurzívne vypočíta nsd(b, a),
##inak rekurzívne zavolá nsd(a, b-a).
##Otestuj, napríklad:
##    >>> nsd(40, 24)
##        8
##Funkcia nsd sa dá urýchliť tak,
##že namiesto odčitovania sa nejako využije zvyšok po delení.
##Oprav túto funkciu.

##funkce s odčítáním:
#def nsd(a, b):
#    if a == b:
#        print(a)
#    else:
#        if a > b:
#            nsd(b, a-b)
#        else:
#            nsd(a, b-a)


#úvodní a prázdný řádek:
print('REKURZIVNÍ VÝPOČET NSD')
print(f'''Dle zadaných dvou hodnot program rekurzivně vypočítá
jejich společného největšího dělitele''')
print()


#vstupní data:
n1 = int(input('Zadej první celé číslo: '))  
n2 = int(input('Zadej druhé celé číslo: ')) 


#rekurzivní funkce:
def nsd(a, b):
    if a == 0 or b == 0:
        return(a+b)
    else:
        if a > b:
            return nsd(b, a%b)
        else:
            return nsd(a, b%a)


#výstup:
print()
print(f'Největší společný dělitel je: {nsd(n1, n2)}')


#prázdný řádek, příkaz pro zobrazení výsledků a prázdný řádek
print()
input('[zmáčkni [Enter] pro zobrazení rekurzivní funkce]')


#dovětek:
print()
print(f'''def nsd(a, b):
    if a == 0 or b == 0:
        return(a+b)
    else:
        if a > b:
            return nsd(b, a%b)
        else:
            return nsd(a, b%a)
''')


#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]')
