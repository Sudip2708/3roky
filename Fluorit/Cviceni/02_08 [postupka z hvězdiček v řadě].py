##  Napíš program, ktorý vyrobí jeden dlhý znakový reťazec,
##  zložený z úsekov hviezdičiek oddelených medzerami:
##  na začiatku je 1 hviezdička (znak '*'), za ňou medzera,
##  potom 2 hviezdičky a medzera, 3 hviezdičky a medzera …
##  Počet hviezdičkových úsekov je n.
##
##  Program by mal mať takúto schému:
##
##    n = ...
##    retazec = ''
##    for ...:
##        ...
##    print(retazec)
##
##  Po spustení môžeš dostať takýto výstup:
##
##    zadaj n: 10
##    * ** *** **** ***** ****** ******* ******** ********* **********


#úvodní a prázdný řádek:
print('POSTUPKA Z HVĚZDIČEK V ŘADĚ ZA SEBOU')
print()


#vstupní data:
a = int(input('Zadej číslo: '))             #vstupní číslo
d = ''                                      #výsledný řetězec


#prázdný řádek
print()


#výpočet:
for i in range(a):                      
    d += ('*' * (i + 1)) + ' '              #výpočet pro vytvoření textového řetězce
print(d)                                    #tisk výsledného textového řetězce
        

#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]')
