##  Napíš funkciu prerob(cislo),
##  ktorá z daného celého čísla vyrobí reťazec,
##  ale tak, že cifry zoskupí do trojíc (sprava) a oddelí podčiarkovníkom.
##  Využi funkciu join, preto z čísla najprv vyrob zoznam trojznakových reťazcov.
##  Funkcia nič nevypisuje, ale vráti (return) výsledný reťazec.
##  Napríklad:	
##    >>> prerob(12345678)	
##        '12_345_678'	
##    Je zaujímavé, že Python aj takto zadané celé čísla považuje za korektné, napríklad:	
##    >>> 12_345_678	
##    12345678	
##    Výsledok svojej funkcie prerob môžeš skontrolovať pomocou f'{cislo:_}'.	


#úvodní a prázdný řádek:
print('FUNKCE - PŘEROB ČÍSLO')
print('''funkce předělá číslo na text, kdy "tisíce" (každétři čísla z prava)
oddělí podržítkem''')
print()


#definování funkce:
def prerob(cislo):
    cislo = str(cislo)
    a = len(cislo)
    b = []
    if a%3 != 0:
        b.append(cislo[0:a%3])
        cislo = cislo[a%3:]
    for i in range(a//3):
        b.append(cislo[0:3])
        cislo = cislo[3:]
    vysledek = '_'.join(b)
    return vysledek

                 
#vstup:
a = int(input('Zadej číslo: '))


#mezera a výstup:
print()
print(prerob(a))


#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]') 
