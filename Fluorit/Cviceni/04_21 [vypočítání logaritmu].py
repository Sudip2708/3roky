##  Dvojkový logaritmus môžeme počítať pomocou funkcie math.log2(cislo),
##  ale vieme na to použiť aj algoritmus z prednášky,
##  ktorý delením intervalu na polovice počítal druhú odmocninu.
##  Napíš program, ktorý to s nejakou presnosťou vypočíta takýmto algoritmom.
##
##  Napríklad po spustení:
##    zadaj číslo: 1000
##    logaritmus 1000.0 je 9.965784382075071
##    >>> import math
##    >>> math.log2(1000)
##    9.965784284662087


#úvodní a prázdný řádek:
print('VYPOČÍTÁNÍ LOGARITMU')
print('program vypočítá logaritmus zadaného čísla a po té zobrazí i výsledek spočítaný zabudovanou funkcí')
print()


#vstupní data a proměné:
a = int(input('Zadej číslo (max10na10): ')) #vstup - číslo
a1 = a/100                                  #výpočet dělitele pro první hodnotu "do"
b = 0                                       #rozsah od
c = a / a1                                  #rozsah do
d = (b + c) / 2                             #polovina z aktuální hodnoty


#výpočet a výstup:
while abs(2**d - a) > 0.0001:               #while cyklus - dokud není rozdíl na 0,0001
    if 2**d > a:                            #podmínka - pokud výsledek je větší než hodnota "do"
        c = d                               #použij aktuální hodnotu do "rozsah do"
    else:                                   #jinak
        b = d                               #použij aktuální hodnotu do "rozsah od"
    d = (b + c) / 2                         #vypočti polovinu z nové hodnoty
print(f'Logaritmus {a} je {d}')             #vypiš výsledek
print()                                     #prázdný řádek


#porovnání se zabudovanou funkcí:
print('Porovnání výsledku s výsledkem funkce math.log2()')
import math                                 #import modulu math
e = math.log2(a)                            #vypočítání hodnoty za pomoci funkce
print('>>> import math')                    #pomocný výpis1
print(f'>>> math.log2({a})')                #pomocný výpis2
print(e)                                    #hodnota vypočítaná pomocí funkce math.log2(a)
        

#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]')    



              
