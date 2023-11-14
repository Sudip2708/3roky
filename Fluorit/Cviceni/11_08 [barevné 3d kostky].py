##  Napíš funkciu kocka(d), ktorá nakreslí 3D kocku.
##  Strana štvorca má veľkosť d, tri šikmé čiary sú pod uhlom 45 a majú dĺžku d/2.
##  Všetky tri štvoruholníky sú zafarbené náhodnými farbami.
##  Nepoužívaj metódu setpos.
##  Otestuj:
##     for i in range(4):
##     kocka(50)
##     t.pu()
##     t.fd(75)
##     t.pd()


#úvodní a prázdný řádek:
print('4 3D KOSTKY')
print('''pouze k zobrazení - program kreslí v modulu turle
4 barevné 3D kostky. ''')
print()


#prázdný řádek a příkaz pro spuštění okna grafické aplikace:
print()
input('[zmáčkni [Enter] pro zobrazení grafické aplikace]')


#definice funkce:
def kocka(d):                                           #definice funkce pro kreslení 3D kostky
    t1.fillcolor(f'#{random.randrange(256**3):06x}')    #zvolení barvy výplně
    t1.begin_fill()                                     #začátek oblasti pro vyplnění barvou
    for i in range(4):                                  #cyklus dle počtu stran
        t1.rt(90)                                           #natočení o úhel
        t1.fd(d)                                            #nakreslení čáry
    t1.end_fill()                                       #konec oblasti pro vyplnění barvou

    t1.fillcolor(f'#{random.randrange(256**3):06x}')    #zvolení barvy výplně
    t1.begin_fill()                                     #začátek oblasti pro vyplnění barvou
    for i in range(2):                                  #cyklus dle poloviny počtu stran
        t1.lt(45)                                           #natočení o úhel
        t1.fd(d/2)                                          #nakreslení čáry
        t1.lt(135)                                          #natočení o úhel
        t1.fd(d)                                            #nakreslení čáry
    t1.end_fill()                                       #konec oblasti pro vyplnění barvou

    t1.rt(90)                                           #otočení o 90

    t1.fillcolor(f'#{random.randrange(256**3):06x}')    #zvolení barvy výplně
    t1.begin_fill()                                     #začátek oblasti pro vyplnění barvou
    for i in range(2):                                  #cyklus dle poloviny počtu stran
        t1.fd(d)                                            #nakreslení čáry
        t1.lt(135)                                          #natočení o úhel
        t1.fd(d/2)                                          #nakreslení čáry
        t1.lt(45)                                           #natočení o úhel
    t1.end_fill()                                       #konec oblasti pro vyplnění barvou

    t1.lt(90)                                           #otočení o 90


#import modulů:
import turtle                                           #import modulu turtle
import random                                           #import modulu random


#grafické okno:
t1 = turtle.Turtle()                                    #vytvoření grafického plátna a pera
#turtle.delay(0)                                         #zrychlení vykresloení


#výpočet:
for i in range(4):                                      #cyklus 4 x
    kocka(50)                                           #volání funkce pro kreslení 3D kostky
    t1.pu()                                             #zvednutí pera
    t1.fd(75)                                           #posun
    t1.pd()                                             #položení pera


#aktivace grafické aplikace
turtle.done()                                           #hlavní smyčka grafického okna
