##  (trochu matematiky)
##  Napíš funkciu troj(rameno, uhol),
##  ktorá nakreslí rovnoramenný trojuholník s danou dĺžkou ramena a uhlom, ktorý zvierajú tieto dve ramená.
##  V tomto vrchole začne aj skonči kresliť.
##  Trojuholník vyplň náhodnou farbou.
##    otestuj nakreslením 36 takýchto trojuholníkov s ramenom 300 a s uhlom 10,
##    po každom trojuholníku sa otoč o 10 stupňov


#úvodní a prázdný řádek:
print('MNOHOBAREVNÝ 36 ÚHELNÍK')
print('''pouze k zobrazení - program generuje v modulu turle 36 ůhelník,
vybarvený 36 náhodně vybranými barvami''')
print()


#prázdný řádek a příkaz pro spuštění okna grafické aplikace:
print()
input('[zmáčkni [Enter] pro zobrazení grafické aplikace]')
print()


#definice funkce:
def troj(rameno, uhol):                         #funkce pro nakreslení rovnorameného trojúhelníku
    a = rameno                                      #hodnota strany a
    u1 = uhol                                       #hodnota úhlu 1

    u2 = 180 - ((180 - uhol) / 2)                   #výpočet úhlu 2
    cos = math.cos(math.radians(uhol))              #výpočet hodnoty cos
    c = a * ((2 * (1 - cos)) ** .5)                 #výpočet strany c

    barva = f'#{random.randrange(256**3):06x}'      #náhodná barva
    t1.fillcolor(barva)                             #zvolení barvy výplně
    t1.begin_fill()                                 #začátek úseku pro barevnou výplň        

    t1.lt(u1)                                       #otočení se doleva o úhel 1
    t1.fd(a)                                        #jdi dopředu o hodnotu strany a
    t1.rt(u2)                                       #otočení se doprava o úhel 2
    t1.fd(c)                                        #jdi dopředu o hodnotu strany c
    t1.rt(u2)                                       #otočení se doprava o úhel 2
    t1.fd(a)                                        #jdi dopředu o hodnotu strany a
    t1.rt(180)                                      #otočení se doprava o 180 stupňů (pro původní pozici)

    t1.end_fill()                                   #konec úseku pro barevnou výplň

    
#import modulů:
import turtle                                   #import modulu turtle
import math                                     #import modulu math
import random                                   #import modulu random


#grafické okno:
t1 = turtle.Turtle()                            #vytvoření grafické plochy a  pera
#turtle.delay(0)                                 #zrychlení vykresloení


#výpočet:
for i in range(36):                             #cyklus 36x
    troj(300, 10)                               #volání funkce pro nakreslení rovnorameného trojůhelníku
    t1.lt(10)                                   #natočení o 10 stupňů


#aktivace grafické aplikace
turtle.done()                                   #hlavní smyčka grafického okna
