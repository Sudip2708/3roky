##  Napíš program, ktorý prečíta dve celé čísla (napríklad 27 a 342)
##  a vypíše ich v tvare takejto rovnosti: 27+342=369, teda bez medzier.
##  Použi na to formátovaciu šablónu f'...{hodnota}...'.
##
##  Po spustení teda môžeš dostať:
##    
##    zadaj 1. číslo: 27
##    zadaj 2. číslo: 342
##    27+342=369


#úvod
print('SČÍTÁNÍ DVOU ČÍSEL')
print()


#vstupní čísla:
a = int(input('Zadej 1. ČÍSLO a zmáčkni [Enter]: '))
b = int(input('Zadej 2. ČÍSLO a zmáčkni [Enter]: '))


#prázdný řádek
print()


#výstup:
print(f'{a} + {b} = {a+b}')


#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]')

