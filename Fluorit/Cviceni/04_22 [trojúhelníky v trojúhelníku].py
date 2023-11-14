##  Pomocou polygónu nakresli farebný trojuholník
##  zadaný tromi jeho vrcholmi a, b, c.
##  Potom do neho nakresli vpísaný trojuholník
##  (jeho vrcholy sú v stredoch strán).
##  Toto opakuj, kým sú všetky dĺžky strán trojuholníka aspoň 30.
##  Trojuholníky vyfarbuj náhodnými farbami.
##
##  Príklad pre promnene:
##    a = 10, 100
##    b = 250, 10
##    c = 300, 250


#úvodní a prázdný řádek:
print('TROJÚHELNÍKY V TROJÚHELNÍKU')
print('pouze zobrazí, dle již předem zadaných parametrú, trojúhelníky zacyklené do určité hloubky v sobě')
print()


#prázdný řádek a příkaz pro spuštění okna grafické aplikace:
print()
input('[zmáčkni [Enter] pro zobrazení grafické aplikace]')


#moduly:
import tkinter
import random


#grafické okno:
canvas = tkinter.Canvas()
canvas.pack()


#proměné:
ax, ay = 10, 100                                            #osa 1. vrcholu trojuhelníku
bx, by = 250, 10                                            #osa 2. vrcholu trojuhelníku
cx, cy = 300, 250                                           #osa 3. vrcholu trojuhelníku
e1 = abs(((ax-bx)**2 + (ay-by)**2)**.5)                     #výpočet délky 1. strany
e2 = abs(((bx-cx)**2 + (by-cy)**2)**.5)                     #výpočet délky 2. strany
e3 = abs(((cx-ax)**2 + (cy-ay)**2)**.5)                     #výpočet délky 3. strany


#výpočet:
while e1 > 30 and e2 > 30 and e3 > 30:                      #cyklus - dokud je délka každé strany větší než 30
    d = f'#{random.randrange(256**3):06x}'                  #náhodná barva
    canvas.create_polygon(ax, ay, bx, by, cx, cy, fill=d)   #vytvoření trojúhelníku s náhodnou barvou
    ax1, ay1 = int((ax + bx) /2), int((ay + by) /2)         #výpočet osy pro 1. vrchol dalšího trojuhelníku
    bx1, by1 = int((bx + cx) /2), int((by + cy) /2)         #výpočet osy pro 2. vrchol dalšího trojuhelníku
    cx1, cy1 = int((cx + ax) /2), int((cy + ay) /2)         #výpočet osy pro 3. vrchol dalšího trojuhelníku
    ax, ay = ax1, ay1                                       #přiřazení osy 1. vrcholu dalšího trojuhelníku
    bx, by = bx1, by1                                       #přiřazení osy 2. vrcholu dalšího trojuhelníku
    cx, cy = cx1, cy1                                       #přiřazení osy 3. vrcholu dalšího trojuhelníku
    e1 = abs(((ax-bx)**2 + (ay-by)**2)**.5)                 #výpočet délky 1. strany dalšího trojúhelníku
    e2 = abs(((bx-cx)**2 + (by-cy)**2)**.5)                 #výpočet délky 2. strany dalšího trojúhelníku
    e3 = abs(((cx-ax)**2 + (cy-ay)**2)**.5)                 #výpočet délky 3. strany dalšího trojúhelníku


#aktivace grafické aplikace
tkinter.mainloop()                                          
