##  Budeš vytvárať dlhý znakový reťazec podobne ako v predchádzajúcej úlohe.
##  Namiesto úsekov hviezdičiek budeš do reťazca zapisovať čísla
##  z nejakého intervalu (v tvare '<číslo>').
##  Schéma programu by mala byť podobná predchádzajúcej úlohe.
##
##  Po spustení môžeš dostať takýto výstup:
##
##    zadaj od: 88
##    zadaj do: 100
##    <88> <89> <90> <91> <92> <93> <94> <95> <96> <97> <98> <99> <100>


#úvodní a prázdný řádek:
print('ŘETĚZEC ČÍSEL')
print()


#vstupní data:
a = int(input('Zadej PRVNÍ ČÍSLO a po té zmáční [Enter]: '))        #počáteční číslo
b = int(input('Zadej POSLEDNÍ ČÍSLO a po té zmáční [Enter]: '))     #koncové číslo


#prázdný řádek
print()


#výpočet:
for i in range(a, b+1):         
    print(f'<{i}>', end=' ')                                        # výpočet a výpis textového řetězce


#prázdný řádek
print()


###alternativní zápis:
##f = ''                                                            #kontejner na textový řetězec
##for i in range(a, b+1):
##    f += f'<{i}> '                                                #výpočet pro vytvoření textového řetězce
##print(f)                                                          #výpis výsledného textového řetězce
        

#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]')


