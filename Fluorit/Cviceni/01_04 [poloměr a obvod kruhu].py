##  Napíš program, ktorý prečíta polomer kruhu a vypíše obvod a obsah tohto kruhu.
##  Môžeš predpokladať, že pi = 3.14159.
##
##  Po spustení môžeš dostať:
##
##    zadaj polomer: 10
##    obvod je 62.8318
##    obsah je 314.159


#úvod
print('VÝPOČET OBVODU A OBSAHU KRUHU Z POLOMĚRU')
print()


#Pi
π = 3.141592653589793


#získání poloměru:
r = float(input('Zadej POLOMĚR a zmáčkni [Enter]: '))


#prázdný řádek
print()


#výpočet obvodu (2πr):
print(f'OBVOD je {2 * π * r}')


#výpočet obsahu (πr2):
print(f'OBSAH je {π * (r ** 2)}')


#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]')

