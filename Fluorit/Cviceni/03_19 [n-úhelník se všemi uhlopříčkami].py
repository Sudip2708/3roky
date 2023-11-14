##  Program pre dané n nakreslí pravidelný n-uholník,
##  ale dokreslí do neho aj všetky uhlopriečky. 


#úvodní a prázdný řádek:
print('N-ÚHELNÍK SE VŠEMI ÚHLOPŘÍČKAMI')
print('(dle počtu stran nakreslí pravidelný n-úhelník se všemi vnitřními úhlopříčkami)')
print()


#vstupní data:
n = int(input('Zadej počet stran: '))               #vstup počtu stran


#moduly:
import tkinter
from math import sin, cos, radians


#grafické okno:
canvas = tkinter.Canvas()
canvas.pack()


#promněné:
x0 = 180                                            #x-ová souřadnice středu
y0 = 130                                            #y-ová souřadnice středu
r = 125                                             #poloměr kružnice
posun = 360/n                                       #o kolik se připočítává
uhol = 0                                            #připočítávač úhlu 1. cyklu
x = x0 + r                                          #1. x-ová souřadnice 1. cyklu
y = y0                                              #1. y-ová souřadnice 1. cyklu


#výpočet:
for i in range(n+1):                                #první cyklus
    uhol1 = 0                                       #připočítávač úhlu 2. cyklu
    x2 = x                                          #1. x-ová souřadnice 2. cyklu
    y2 = y                                          #1. y-ová souřadnice 2. cyklu
    for j in range(n+1):                            #druhý cyklus
        x3 = x0 + r * cos(radians(uhol1))           #2. x-ová souřadnice 2. cyklu
        y3 = y0 + r * sin(radians(uhol1))           #2. y-ová souřadnice 2. cyklu
        canvas.create_line(x2, y2, x3, y3, width=1) #vytvoření přímky
        uhol1 += posun                              #přípočet k úhlu 2. cyklu pro další posun
    x1 = x0 + r * cos(radians(uhol))                #2. x-ová souřadnice 1. cyklu
    y1 = y0 + r * sin(radians(uhol))                #2. y-ová souřadnice 1. cyklu
    uhol += posun                                   #přípočet k úhlu 1. cyklu pro další posun
    x, y = x1, y1                                   #posunutí počátečního bodu 1. cyklu


#grafické okno:
tkinter.mainloop()                                  #aktivace grafické aplikace
