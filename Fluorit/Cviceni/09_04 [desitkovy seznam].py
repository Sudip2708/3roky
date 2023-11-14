##  Napíš funkciu desiatkova(cislo),
##  ktorá vráti (return) zoznam cifier daného čísla v desiatkovej sústave.
##  Využi funkcie str a int.
##  Napríklad:	
##    >>> desiatkova(11213)	
##        [1, 1, 2, 1, 3]	
##    Všimni si, že takto sa dá vypočítať ciferný súčet čísla:	
##    >>> sum(desiatkova(11213))
##    8


#úvodní a prázdný řádek:
print('FUNKCE - DESÍTKOVÝ SEZNAM')
print('''funkce vytvoří ze zadaného čísla seznam jednotlivých čísel
desítkové soustavy''')
print()


#definování funkce:
def desiatkova(cislo):
    vysl = []
    for i in str(cislo):
        vysl.append(int(i))
    return vysl


#vstup:
a = int(input('Zadej číslo: '))


#prázdný řádek a výstup:
print()
print(desiatkova(a))
     

#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]') 
