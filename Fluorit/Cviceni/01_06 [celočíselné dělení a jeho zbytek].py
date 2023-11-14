##  Napíš program, ktorý prečíta nejaké (aspoň štvorciferné) celé číslo.
##  Potom do štyroch riadkov postupne vypíše:
##
##    číslo celočíselne delené 10 a zvyšok po delení 10
##    číslo celočíselne delené 100 a zvyšok po delení 100
##    číslo celočíselne delené 1000 a zvyšok po delení 1000
##    číslo celočíselne delené 10000 a zvyšok po delení 10000
##
##  Takto vieme rozložiť dané číslo na dve časti.
##
##  Po spustení môžeš dostať:
##
##    zadaj číslo: 98765
##    9876 5
##    987 65
##    98 765
##    9 8765


#úvod
print('DESÍTKOVÉ DĚLENÍ A CELOČÍSELNÝ ZBYTEK')
print()


#získání čísla:
a = int(input('Zadej 5-TI MÍSTNÉ CELÉ ČÍSLO a zmáčkni [Enter]: '))


#prázdný řádek
print()


#výpisy výpočtů dle zadání:
print(f'{a//10} {a%10}')
print(f'{a//100} {a%100}')
print(f'{a//1000} {a%1000}')
print(f'{a//10000} {a%10000}')


#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]')
