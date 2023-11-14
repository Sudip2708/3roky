##  Program pre dané n nakreslí n dotýkajúcich sa kruhov,
##  ktorých stredy ležia na obvode kružnice.
##  Tieto kruhy zafarbi náhodnými farbami.


#úvodní a prázdný řádek:
print('BAREVNÁ KOLEČKA V KRUHU')
print('(dle zadaného počtu vypočítá velikost koleček, tak aby se vešli a zobrazili se v kruhu)')
print()


#vstupní data:
n = int(input('Zadej počet kruhů: '))                           #vstup počtu kruhů


#moduly:
import tkinter
from math import sin, cos, radians, pi
import random


#grafické okno:
canvas = tkinter.Canvas()
canvas.pack()


#promněné:
x0 = 180                                                        #x-ová souřadnice středu
y0 = 130                                                        #y-ová souřadnice středu
r1 = 125                                                        #poloměr hlavní kružnice
posun = 360/n                                                   #o kolik se připočítává
uhol = 0                                                        #připočítávač úhlu 
x = x0 + r1                                                     #1. x-ová souřadnice aktuálního kruhu
y = y0                                                          #1. y-ová souřadnice aktuálního kruhu
r2 = ((2 * r1**2 - 2 * r1**2 * cos(radians(posun)))**(1/2))/2   #poloměr malých kružnic


#výpočet:
for i in range(n+1):                                            #cyklus
    barva = f'#{random.randrange(256**3):06x}'                  #barva 
    canvas.create_oval(x+r2, y+r2, x-r2, y-r2, fill=barva)      #vytvoření kruhu
    x = x0 + r1 * cos(radians(uhol))                            #výpočet x-ová souřadnice dalšího kruhu
    y = y0 + r1 * sin(radians(uhol))                            #výpočet y-ová souřadnice dalšího kruhu
    uhol += posun                                               #přípočet k úhlu pro další posun


#grafické okno:
tkinter.mainloop()                                              #aktivace grafické aplikace
