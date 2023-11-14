##  Täto úloha je podobná predchádzajúcej,
##  ale funkcia veza(dlzka, krok) bude kresliť náhodne zafarbené štvorce nad seba.
##  Každý menší je vycentrovaný na predchádzajúci.
##  Nepoužívaj setpos.
##  Otestuj na volanie veza(120, 30)


#úvodní a prázdný řádek:
print('VĚŽ Z KOSTEK')
print('''pouze k zobrazení - program nakreslí v modulu turle 4 barevné kostky.
Každá je vždy o něco menší a stují na druhé. ''')
print()


#prázdný řádek a příkaz pro spuštění okna grafické aplikace:
print()
input('[zmáčkni [Enter] pro zobrazení grafické aplikace]')


#definice funkce:
def veza(dlzka, krok):                                      #definice funkce pro nakreslení věže z čtverců
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
        t1.fd(d_ctv)                                                #posunutí o délku strany čtverce
        t1.rt(90)                                                   #natočení o 90 stuňů doprava
    t1.pd()                                                     #položení pera


#import modulů:
import turtle                                               #import modulu turtle
import random                                               #import modulu random


#grafické okno:
t1 = turtle.Turtle()                                        #vytvoření grafického plátna a pera
#turtle.delay(0)                                             #zrychlení vykresloení


#výpočet:
veza(120, 30)                                               #volání funkce pro nakreslení věže z čtverců


#aktivace grafické aplikace
turtle.done()                                               #hlavní smyčka grafického okna
