##  Napíš dve funkcie horna(x0, y0, r) a dolna(x0, y0, r),
##  ktoré nakreslia len polovicu kružnice so stredom (x0, y0) a s polomerom r.
##  Funkcia horna by mala nakresliť len hornú polovicu a dolna len dolnú.
##  Kružnicu kresli ako 36-uholník, a teda polovica označuje 18 úsečiek.
##
##  Napríklad volania:
##    horna(30, 100, 30)
##    dolna(90, 100, 30)
##    horna(150, 100, 30)
##    dolna(210, 100, 30)
##    horna(270, 100, 30)
##    dolna(330, 100, 30)
##
##    for i in range(6):
##        horna(30+60*i, 200, 30)


#úvodní a prázdný řádek:
print('HORNÍ / SPODÍ KRUŽNICE')
print('funkce na vykreslení horní, nebo spodní polovice kružnice \npouze zobrazení výsledku dle předem daného zadání')
print()


#prázdný řádek a příkaz pro spuštění okna grafické aplikace:
print()
input('[zmáčkni [Enter] pro zobrazení grafické aplikace]')


#moduly:
import tkinter
import math


#definice funkce:
def horna(x0, y0, r):                                           #parametry - x, y středu a poloměr
    uhol = 10                                                   #hodnota středového úhlu pro výpočet dašího bodu
    x1 = x0 - r                                                 #x-ová osa 1. bodu
    y1 = y0                                                     #y-ová osa 1. bodu
    for i in range(18):                                         #cyklus - dle počtu bodů
        x2 = x0 - r * round(math.cos(math.radians(uhol)), 4)    #x-ová osa 2. bodu
        y2 = y0 - r * round(math.sin(math.radians(uhol)), 4)    #y-ová osa 2. bodu
        canvas.create_line(x1 ,y1, x2, y2)                      #vytvoření linky
        uhol += 10                                              #přípočet k úhlu pro další bod
        x1, y1 = x2, y2                                         #posunutí počátečního bodu

#definice funkce:
def dolna(x0, y0, r):                                           #parametry - x, y středu a poloměr
    uhol = 10                                                   #hodnota středového úhlu pro výpočet dašího bodu
    x1 = x0 + r                                                 #x-ová osa 1. bodu
    y1 = y0                                                     #y-ová osa 1. bodu
    for i in range(18):                                         #cyklus - dle počtu bodů
        x2 = x0 + r * round(math.cos(math.radians(uhol)), 4)    #x-ová osa 2. bodu
        y2 = y0 + r * round(math.sin(math.radians(uhol)), 4)    #y-ová osa 2. bodu
        canvas.create_line(x1 ,y1, x2, y2)                      #vytvoření linky
        uhol += 10                                              #přípočet k úhlu pro další bod
        x1, y1 = x2, y2                                         #posunutí počátečního bodu


#vytvoření grafického prostředí:
canvas = tkinter.Canvas()
canvas.pack()


#výpočet:
horna(30, 100, 30)
dolna(90, 100, 30)
horna(150, 100, 30)
dolna(210, 100, 30)
horna(270, 100, 30)
dolna(330, 100, 30)

for i in range(6):
    horna(30+60*i, 200, 30)


#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]')    


#aktivace grafické aplikace:
tkinter.mainloop() 
