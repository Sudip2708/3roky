##  Napíš funkciu strom(kmen, koruna),
##  ktorá nakreslí strom s hnedým kmeňom (hrúbka 15) a zelenou korunou (hrúbka 40).
##  Otestuj na:
##    for i in range(8):
##    strom(random.randint(30, 60), random.randint(10, 40))
##    t.pu()
##    t.fd(50)
##    t.pd()


#úvodní a prázdný řádek:
print('STROMOVÁ ALEJ')
print('''pouze k zobrazení - program nakreslí v modulu turle 
8 různě velkých ikon stromů. ''')
print()


#prázdný řádek a příkaz pro spuštění okna grafické aplikace:
print()
input('[zmáčkni [Enter] pro zobrazení grafické aplikace]')


#definice funkce:
def strom(kmen, koruna):                #definice funkce pro nakreslení stromu
    t1.lt(90)                           #otočení pera směrem nahoru
        
    hod_kme = 15, 'brown', kmen         #hodnoty pro nakreslení kmenu
    hod_kor = 40, 'green', koruna       #hodnoty pro nakreslení koruny

    for v, b, d in hod_kme, hod_kor:    #cyklus pro hodnoty kmenu a koruny
        t1.pensize(v)                       #výběr tloušťky kreslící čáry
        t1.pencolor(b)                      #výběr barvy kreslící čáry
        t1.fd(d)                            #nakreslení čáry

    t1.pu()                             #zvednutí pera
    t1.bk(kmen + koruna)                #vrácení se na původní pozici
    t1.rt(90)                           #otočení se na původní natočení
    t1.pd()                             #položení pera


#import modulů:
import turtle                           #import modulu turtle
import random                           #import modulu random


#grafické okno:
t1 = turtle.Turtle()                    #vytvoření grafického plátna a pera
#turtle.delay(0)                         #zrychlení vykresloení


#výpočet:
for i in range(8):                      #cyklus dle počtu stromů
    kmen = random.randint(30, 60)           #výpočet hodnoty pro nakreslení kmenu
    koruna = random.randint(10, 40)         #výpočet hodnoty pro nakreslení koruny
    strom(kmen, koruna)                     #volání funkce pro nakreslení stromu
    t1.pu()                                 #zvednutí pera
    t1.fd(50)                               #posunutí na další pozici
    t1.pd()                                 #položení pera


#aktivace grafické aplikace
turtle.done()                           #hlavní smyčka grafického okna
