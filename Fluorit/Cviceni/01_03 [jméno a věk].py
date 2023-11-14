##  Napíš program, ktorý pomocou príkazu input prečíta meno študenta a jeho vek.
##  Potom to vypíše pomocou príkazu print
##  a tiež vypíše informáciu jeho veku o rok a aj o 10 rokov.
##
##  Po spustení programu môžeš dostať takýto výpis:
##
##    zadaj meno: Ema
##    zadaj vek: 17
##    Ema má 17 rokov
##    Ema bude mať o rok 18
##    Ema bude mať o 10 rokov 27


#úvod
print('JMÉNO A VĚK')
print()
input('[zmáčkni [Enter] pro zadání údajů]')
print()

#získání dat:
a = input('Zadej JMÉNO a zmáčkni [Enter]: ')
b = int(input('Zadej VĚK a zmáčkni [Enter]: '))

#mezera
print()

#výpis:
print(f'{a} má {b} roků')
print(f'{a} bude mít za rok {b+1}')
print(f'{a} bude mít za 10 roků {b+10}')

#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]')
