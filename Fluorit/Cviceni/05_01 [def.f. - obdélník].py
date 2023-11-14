##  Napíš funkciu obdlznik(sirka, znak='*'),
##  ktorá z daného znaku znak vypíše do 3 riadkov
##  výstupu obdĺžnik zadanej šírky.
##
##  Napríklad pre volania:
##    2. obdlznik(30, '#')
##    3. obdlznik(6)
##    4. obdlznik(19, 'O')
##
##  dostaneme výstup:
##    ##############################
##    #                            #
##    ##############################
##    ******
##    *    *
##    ******
##    OOOOOOOOOOOOOOOOOOO
##    O                 O
##    OOOOOOOOOOOOOOOOOOO


#úvodní a prázdný řádek:
print('DEFINOVÁNÍ FUNKCE - OBDELNÍK')
print('funkce vykreslí dle zadaných parametrů textový obdelník')
print()


#definování funkce:
def obdlznik(sirka, znak='*'):                  #parametry - šířka, znak
    print(znak * sirka)                         #výpis 1. řádku
    print(znak + ' ' * (sirka - 2) + znak)      #výpis 2. řádku
    print(znak * sirka)                         #výpis 3. řádku (stejný jako první)


#vstup:
sirka = int(input('Zadej číslo šířky řádku: '))
b = input('Zadej znak (pro * stačí zmáčknout [enter]): ')
if b != '':
    znak = b
else:
    znak = '*'


#výstup:
obdlznik(sirka, znak)
        

#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]')  

