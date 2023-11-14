##  Napíš dve funkcie vyrob(n, poz) a smerom(zoznam, poz):
##    • prvá funkcia vyrob(n, poz) vytvorí na náhodných pozíciách n korytnačiek,
##    každej nastaví náhodnú farbu pera a hrúbku pera 5;
##    každú korytnačku ešte natočí smerom k bodu poz (parameter poz je dvojica nejakých súradníc (x, y));
##    všetky tieto korytnačky vloží do zoznamu a tento zoznam vráti (return) ako výsledok funkcie;
##    zrejme využiješ korytnačiu metódu towards
##    • druhá funkcia smerom(zoznam, poz) dostáva zoznam korytnačiek
##    a nechá postupne všetky korytnačky z tohto zoznamu presúvať k bodu poz tak,
##    že 50-krát robí toto:
##        každá korytnačka si vypočíta vzdialenosť k bodu poz a prejde (forward) desatinu tejto vzdialenosti
##  Otestuj, napríklad:
##    pp = (0, ‐300)
##    zoz = vyrob(100, pp)
##    smerom(zoz, pp)


#úvodní a prázdný řádek:
print('100 ŽELVICEK DO JEDNOHO BODU')
print('''pouze k zobrazení - program vyrobí 100 želviček na náhodných
pozicí a pak je nechá zbýhat do jenoho bodu.''')
print()


#prázdný řádek a příkaz pro spuštění okna grafické aplikace:
print()
input('[zmáčkni [Enter] pro zobrazení grafické aplikace]')
print()


#definice funkce:
def smerovac(x1, y1, x2, y2):                       #definice funkce - na určení úhlu mezi dvěma body
    a = abs(x1 - x2)                                    #proměnná - výpočet strany 'a' 
    b = abs(y1 - y2)                                    #proměnná - výpočet strany 'b' 
    c = (a**2 + b**2)**.5                               #proměnná - výpočet strany 'c' (pravoúhlý trojúhelník)
    sin_a = a/c                                         #proměnná - výpočet sinus úhlu 'a'
    uh_a = math.degrees(math.asin(sin_a))               #proměnná - výpočet úhlu převedením hodnoty sin_a přes radiány na stupně

    if y1 > y2 or y1 == y2:                             #podmínka - když 'y1' je větší nebo rovno 'y2'
        if x1 > x2:                                         #podmínka - když 'x1' je větší než 'x2'
            uhel = (270 - uh_a)                                 #proměnná - výpočet úhlu
        elif x1 < x2 or x1 == x2:                           #podmínka - když 'x1' je menší nebo rovno 'x2'
            uhel = (uh_a + 270)                                 #proměnná - výpočet úhlu

    elif y1 < y2:                                       #podmínka - když 'y1' je menší než 'y2'
        if x1 > x2:                                         #podmínka - když 'x1' je větší než 'x2'
            uhel = (uh_a + 90)                                  #proměnná - výpočet úhlu
        elif x1 < x2 or x1 == x2:                           #podmínka - když 'x1' je menší nebo rovno 'x2'
            uhel = (90 - uh_a)                                  #proměnná - výpočet úhlu

    return (uhel, c)                                    #návratová hodnoty - úhel


def vyrob(n, poz):                                  #definice funkce - na vyrobení seznamu 'želvých' per (počet, souřadnice směru)
    x2, y2 = poz                                        #proměnná - pro hodnoty 'x2', 'y2' (pro výpočet úhlu)
    for i in range(n):                                  #cyklus - dle počtu 
        x1 = random.randint(-300, 300)                      #proměnná - generování hodnoty 'x1'
        y1 = random.randint(-300, 300)                      #proměnná - generování hodnoty 'y1'
        uhel = smerovac(x1, y1, x2, y2)[0]                  #proměnná - volání funkce pro výpočet úhlu
        barva = f'#{random.randrange(256**3):06x}'          #proměnná - generování náhodné barvy

        t = turtle.Turtle()                                 #proměnná - pro vytvořené 'želvý' pero
        t.pencolor(barva)                                   #změna - zvolení barvy pera
        t.pensize(5)                                        #změna - zvolení tloušťky čáry pera
        t.pu()                                              #změna - zvednout pero
        t.setpos(x1, y1)                                    #změna - přesunout pero na vytvořené souřadnice 'x1', 'y1'
        t.seth(uhel)                                        #změna - natočit pero o úhel
        t.pd()                                              #změna - položit pero
        seznam.append(t)                                    #změna - přidat pero do seznamu 


def smerom(seznam, poz):                            #definice funkce - pro pohyb 'želvých' per (seznam, souřadnice směru)
    x2, y2 = poz                                        #proměnná - pro hodnoty 'x2', 'y2' (pro výpočet úhlu)
    for i in range(50):                                 #cyklus - 50x zopakuj
        for t in seznam:                                    #cyklus - pro každé 'želvý' pero ze seznamu
            x1, y1 = t.xcor(), t.ycor()                     #proměnná - pro hodnoty 'x1', 'y1' (pro výpočet úhlu)
            uhel, c = smerovac(x1, y1, x2, y2)              #proměnná - volání funkce pro výpočet úhlu a vzdálenosti
            t.fd(c/10)                                      #změna - posuň pero dopředu o 1/10 vzdálenosti
            t.seth(uhel)                                    #změna - nastav úhel pro příští posun


#import modulů:
import turtle                                       #import modulu - turtle
import random                                       #import modulu - random
import math                                         #import modulu - math


#výpočet:
turtle.delay(0)
seznam = []                                         #seznam - pro 'želví' pera
poz = (0, -300)                                     #proměnná - pro souřadnice pozice, kam pera směřují
vyrob(100, poz)                                     #volání funkce - na výrobu želvých per (počet, směr)
smerom(seznam, poz)                                 #volání funkce - na posun 


#aktivace grafické aplikace
turtle.mainloop()                                   #hlavní smyčka grafického okna
