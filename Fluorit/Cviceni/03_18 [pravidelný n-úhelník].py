##  Program pre dané n a dĺžku strany a nakreslí pravidelný n-uholník so stranou a.
##  Využi body na kružnici so stredom x a y a polomerom r budeš musieť vypočítať. 


#úvodní a prázdný řádek:
print('PRAVIDELNÝ N-ÚHELNÍK')
print('(dle počtu stran a velikosti jedné strany nakreslí pravidelný n-úhelník)')
print()


#vstupní data:
n = int(input('Zadej počet stran: '))           #vstup počtu stran
a = int(input('Zadej délku strany: '))          #vstup délky strany


#moduly:
import tkinter
from math import sin, cos, tan, radians


#grafické okno:
canvas = tkinter.Canvas()
canvas.pack()


#promněné:
x0 = 180                                        #x-ová souřadnice středu
y0 = 130                                        #y-ová souřadnice středu
u1 = 360/n                                      #výpočet 1. úhlu pro výpočet poloměru
u2 = (180 - u1) / 2                             #výpočet 2. úhlu pro výpočet poloměru
r = (a * sin(radians(u2)))/ sin(radians(u1))    #poloměr kružnice
uhol = 0                                        #připočítávač úhlu
posun = 360/n                                   #o kolik se připočítává
x = x0 + r                                      #x-ová souřadnice prvního bodu
y = y0                                          #y-ová souřadnice prvního bodu


#výpočet:
for i in range(n+1):                            #cyklus
    x1 = x0 + r * cos(radians(uhol))            #x-ová souřadnice druhého bodu
    y1 = y0 + r * sin(radians(uhol))            #y-ová souřadnice druhého bodu
    canvas.create_line(x, y, x1, y1, width=3)            #vytvoření přímky
    uhol += posun                               #přípočet k úhlu pro další posun
    x, y = x1, y1                               #posunutí počátečního bodu


#grafické okno:
tkinter.mainloop()                              #aktivace grafické aplikace
