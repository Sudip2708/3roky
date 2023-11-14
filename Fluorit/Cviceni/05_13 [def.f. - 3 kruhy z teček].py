##  Na prednáške sa pomocou farebných bodiek kreslil červený mesiac na modrom pozadí.
##  Využívala sa pritom funkcia vzd.
##  Napíš funkciu farebne_bodky(r, x1, y1, x2, y2, x3, y3),
##  ktorá na podobnom princípe grafickú plochu vybodkuje podľa týchto pravidiel:
##  ak by sme nakreslili tri kruhy s polomerom r
##  ale s rôznymi stredmi (x1, y1), (x2, y2), (x3, y3),
##  tieto by sa mohli čiastočne prekrývať.
##  Bodky budeš farbiť tak, že tie oblasti,
##  v ktorých nie je žiaden kruh alebo sa prekrývajú práve 2 kruhy zafarbíš na modro,
##  ostatné oblasti budú žlté.
##
##  Napríklad pre volanie:
##    farebne_bodky(80, 120, 120, 180, 110, 160, 170)


#úvodní a prázdný řádek:
print('3 KRUHY Z TEČEK')
print('funkce na vykreslení prolínajících se 3 kruhů z teček \npouze zobrazení výsledku dle předem daného zadání')
print()


#prázdný řádek a příkaz pro spuštění okna grafické aplikace:
print()
input('[zmáčkni [Enter] pro zobrazení grafické aplikace]')


#moduly:
import tkinter
import random
import math


#definice funkce:
def vzd(x1, y1, x2, y2):                                            #parametry - x,y prvního bodu a x,y druhého bodu
    return math.sqrt((x1-x2) ** 2 + (y1-y2) ** 2)                   #vypočítání vzdálenosti mezi bodem 1 a bodem 2

def kresli_bodku(x, y, farba):                                      #parametry - x,y středu a barva
    canvas.create_oval(x-2, y-2, x+2, y+2, fill=farba, width=0)     #vytvoř kolečko s poloměrem 2

def farebne_bodky(r, x1, y1, x2, y2, x3, y3):                       #parametry - poloměr, x,y středu 1. kruhu, 2. kruh a 3. kruhu
    for i in range(20000):                                          #cyklus - vykonej 20 000x
        x = random.randint(5, 375)                                  #náhodná x-ová pozice středu tečky
        y = random.randint(5, 255)                                  #náhodná y-ová pozice středu tečky
        a = vzd(x, y, x1, y1)                                       #pozice tečky vůči 1. kruhu
        b = vzd(x, y, x2, y2)                                       #pozice tečky vůči 2. kruhu
        c = vzd(x, y, x3, y3)                                       #pozice tečky vůči 3. kruhu
        if a < r and b < r and c < r:                               #podmínka - když se tečka nachází v protnutí všeh kruhů
            kresli_bodku(x, y, 'yellow')                            #nakresli žlutou tečku
        elif a < r and b > r and c > r:                             #podmínka - kyž se tečka nalézá v 1. kruhu, ale nezasahuje do zbylích kruhů
            kresli_bodku(x, y, 'yellow')                            #nakresli žlutou tečku  
        elif a > r and b < r and c > r:                             #podmínka - kyž se tečka nalézá v 2. kruhu, ale nezasahuje do zbylích kruhů
            kresli_bodku(x, y, 'yellow')                            #nakresli žlutou tečku
        elif a > r and b > r and c < r:                             #podmínka - kyž se tečka nalézá v 3. kruhu, ale nezasahuje do zbylích kruhů
            kresli_bodku(x, y, 'yellow')                            #nakresli žlutou tečku
        else:                                                       #ve všech ostatních případech
            kresli_bodku(x, y, 'navy')                              #nakresli modrou tečku


#vytvoření grafického prostředí:
canvas = tkinter.Canvas()
canvas.pack()


#výpočet:
farebne_bodky(80, 120, 120, 180, 110, 160, 170)


#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]')    


#aktivace grafické aplikace:
tkinter.mainloop() 
    
