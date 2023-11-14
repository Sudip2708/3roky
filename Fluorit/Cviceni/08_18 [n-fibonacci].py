##  Napíš funkciu fibonacci(n),
##  ktorá vyrobí (vráti) n-prvkový zoznam prvých n prvkov fibonacciho postupnosti.
##  Funkcia nič nevypisuje.
##  Napríklad:
##    >>> fib = fibonacci(15)
##    >>> fib
##        [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]
##    >>> fibonacci(1)
##        [0]


#úvodní a prázdný řádek:
print('DEFINOVÁNÍ FUNKCE - N-FIBONACCI')
print('funkce vytvoří seznam s čísli fibonacciho posloupnosti, dle námi zadaného počtu')
print()


#definování funkce:
def fibonacci(n):
    seznam = [0, 1]
    for i in range(n-2):
        seznam.append(seznam[-1] + seznam[-2])
    return seznam


#vstup:
n = int(input('Zadej číslo, pro počet zobrazených Fibonacciho čísel: '))
print()


#výstup:
fib = fibonacci(n)
print(fib)
        

#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]') 
