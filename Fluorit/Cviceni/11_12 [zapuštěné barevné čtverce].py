##  Napíš funkciu stvorce(dlzka, krok),
##  ktorá nakreslí niekoľko farebných štvorcov.
##  Všetky budú zafarbené náhodnými farbami a budú bez obrysu (kreslia sa so zvihnutym perom).
##  Najväčší z nich je prvý a má veľkosť strany dlzka.
##  Každý ďalší má rovnaký stred (ako predchádzajúci), ale stranu štvorca má o krok menšiu.
##  Ak by mal takýto štvorec nulovú alebo zápornú stranu, kreslenie skončí.
##  Nepoužívaj metódu setpos.
##  Otestuj na volanie stvorce(200, 25)
##  Asi sa ti oplatí vytvoriť pomocnú funkciu stvorec(dlzka),
##  ktorá nakreslí náhodne zafarbený štvorec so stranou dlzka.


#úvodní a prázdný řádek:
print('ZAPUŠTĚNÉ BAREVNÉ ČTVERCE')
print('''pouze k zobrazení - program generuje v modulu turle postupně
8 barevných, zmenšujících se čtverců. ''')
print()


#prázdný řádek a příkaz pro spuštění okna grafické aplikace:
print()
input('[zmáčkni [Enter] pro zobrazení grafické aplikace]')


#definice funkce:
def stvorce(dlzka, krok):                                   #definice funkce pro nakreslení čtverců
    t1.pu()                                                     #zvednutí pera
    for d_ctv in range(dlzka, 0, -krok):                        #cyklusdle počtu možných čtverců
        t1.fillcolor(f'#{random.randrange(256**3):06x}')            #zvolení barvy výplně
        t1.begin_fill()                                             #začátek oblasti pro vyplnění barvou
        for i in range(4):                                          #cyklus dle počtu stran
            t1.fd(d_ctv)                                                #nakreslení čáry
            t1.lt(90)                                                   #natočení o úhel
        t1.end_fill()                                               #konec oblasti pro vyplnění barvou
        t1.fd(krok/2)                                               #posunutí o polovinu hodnoty kroku
        t1.lt(90)                                                   #natočení o 90 stuňů doleva
        t1.fd(krok/2)                                               #posunutí o polovinu hodnoty kroku
        t1.rt(90)                                                   #natočení o 90 stuňů doprava
    t1.pd()                                                     #položení pera


#import modulů:
import turtle                                               #import modulu turtle
import random                                               #import modulu random


#grafické okno:
t1 = turtle.Turtle()                                        #vytvoření grafického plátna a pera
#turtle.delay(0)                                             #zrychlení vykresloení


#výpočet:
stvorce(200, 25)                                            #volání funkce pro nakreslení čtverců


#aktivace grafické aplikace
turtle.done()                                               #hlavní smyčka grafického okna
