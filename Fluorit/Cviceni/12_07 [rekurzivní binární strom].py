##Nasledovná funkcia kreslí binárny strom:
##    import turtle
##    
##    def strom(d):
##        t.fd(d)
##        if d > 20:
##            t.lt(40)
##            strom(d * 0.7)
##            t.rt(90)
##            strom(d * 0.6)
##            t.lt(50)
##        t.fd(-d)
##    
##    turtle.delay(0)
##    t = turtle.Turtle()
##    t.speed(0)
##    t.lt(90)
##    t.pu()
##    t.setpos(0, -200)
##    t.pd()
##    zoznam = []
##    strom(150)
##Doplň do tejto rekurzívnej funkcie triviálny prípad rekurzie tak,
##aby sa na všetkých pozíciách listov stromu vytvorili nové korytnačky.
##Tieto korytnačky ulož do globálnej premennej zoznam.
##Po nakreslení stromu by malo fungovať:
##for p in zoznam:
##    p.color('green')
##    p.shape('turtle')
##while True:
##    for p in zoznam:
##        p.lt(15)
##Na strome v pozíciách listov sa zobrazia malé zelené korytnačky
##a tieto sa budú otáčať na mieste.


#úvodní a prázdný řádek:
print('REKURZIVNÍ VÝPOČET BINÁRNÍHO STROMU')
print(f'''Program rekurzivně nakreslí binární strom,
kde na každým konci větve vytvoří novou želvu (jakožto list)
a tu pak nechá otáčet se kolem vlastní osy.''')
print()
input('[zmáčkni [Enter] pro zobrazení]')


#import modulů:
import turtle


#definice funkce:
def strom(d, v):            #definice funkce na kreslení binárního stromu s proměnou výšky základního kmenu a jeho tloušťky
    t.pensize(v)            #nastavení tloušťky čáry
    t.fd(d)                 #kresli čáru směrem dopředu dle zadané délky
    if d <= 20:                 #pokud je délka menší než 20
        tn = turtle.Turtle()        #vytvoř novou želvu
        tn.pu()                     #zvedni pero
        tn.setpos(t.pos())          #přesuň želvu na pozici první želvy
        tn.pd()                     #polož pero
        zoznam.append(tn)           #vlož vytvořenou želvu do seznamu

    else:                       #pokud je délka větší než 20
        t.lt(40)                    #natoč se doleva o 40°
        strom(d*0.7, v*0.7)         #rekurzivní volání funkce s poníženými hodnotami
        t.rt(90)                    #natoč se doprava o 90°
        strom(d*0.6, v*0.6)         #rekurzivní volání funkce s poníženými hodnotami
        t.lt(50)            #natoč se doleva o 50°
    t.fd(-d)                #vrať se na původní pozici


#výpočet:
#turtle.delay(0)             #zrychlení vykreslení
t = turtle.Turtle()         #vytvoření želvy
t.lt(90)                    #otoč želvu doleva o 90°
t.pu()                      #zvedni pero
t.setpos(0, -200)           #přesuň se na uvedenou pozici
t.pd()                      #polož pero
zoznam = []                 #seznam na želvičky
strom(150, 10)              #volání rekurzivní funkce na nakreslení stromu

for p in zoznam:            #cyklus pro každou položku ze seznamu želv
    p.color('green')            #změň barvu na zelenou
    p.shape('turtle')           #změň tvar na želvu

while True:                 #nekonečný cyklus
    for p in zoznam:            #cyklus pro každou položku ze seznamu želv
        p.lt(15)                #otoč želvu doleva o 15°


#smyčka hlavního okna
turtle.mainloop()
