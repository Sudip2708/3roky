##  Na prednáške si sa zoznámil s funkciou fibonacci(n),
##  ktorá počítala n-tý člen fibonacciho postupnosti.
##  Napíš funkciu fib_medzi(od, do), ktorá vypíše (pomocou print)
##  všetky fibonacciho čísla z daného intervalu <od, do>.
##  Táto funkcia by mala obsahovať len jeden while-cyklus
##  okrem priradení a if).
##
##  Napríklad pre volania:
##    fib_medzi(10, 100)
##    fib_medzi(1000, 3000)
##
##  dostaneme výstup:
##    13 21 34 55 89
##    1597 2584


#úvodní a prázdný řádek:
print('DEFINOVÁNÍ FUNKCE - FIBONACCIHO MEZI-ČÍSLA')
print('funkce vypíše fibonacciho čísla v zadaném intervalu')
print()


#definování funkce:
def fib_medzi(od, do):
    a, b = 0, 1                             #přiřazení prvních 2 čísel
    while b < do:                           #cyklus - dokud nebude fibonacciho číslo větší než námi uvedené
        a, b = b, a+b                       #počítej fibonacciho čísla
        if a > od:                          #podmínka - když je číslo větší než námi uvedené číslo od
            print(a, end=' ')               #vypiš číslo


#vstup:
od = int(input('Zadej první číslo: '))
do = int(input('Zadej první číslo: '))


#výstup:
print(f'Mezi čísly {od} a {do} se nacházejí následující fibonacciho čísla: ')
fib_medzi(od, do)
        

#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]')  
