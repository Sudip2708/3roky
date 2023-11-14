##  Napíš funkciu stvorec(n, znak),
##  ktorá vráti jeden dlhý znakový reťazec.
##  Znakový reťazec by po vypísaní pomocou print
##  vytvoril obvod štvorca z daného znaku.
##  Môžeš predpokladať, že n nebude menšie ako 2.
##
## Napríklad:
##  >>>r = stvorec(5, '#')
##  >>>r
##    '#####\n#   #\n#   #\n#   #\n#####'
##  >>>print(r)
##    #####
##    #   #
##    #   #
##    #   #
##    #####
##
##  Pokús sa to vyriešiť tak, že telo funkcie bude obsahovať jediný riadok return:
##    defstvorec(n, znak):
##    return...


#úvodní a prázdný řádek:
print('DEFINOVÁNÍ FUNKCE - N-ČTVEREC')
print('funkce vytvoří čtverec z námi zadaného znaku a velikosti')
print()


#definování funkce:
def stvorec(n, znak):
    return((n * znak + '\n') + ((n-2) * (znak + (n-2) * ' ' + znak + '\n')) + (n * znak + '\n'))    #vytvoř jedenořádkový zápis pro čtverec


#vstup:
znak = input('Zadej znak z kterého chceš tvořit čtverec: ')
n = int(input('Zadej počet znaků jedné strany: '))


#výstup:
print(stvorec(n, znak))
        

#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]')  
