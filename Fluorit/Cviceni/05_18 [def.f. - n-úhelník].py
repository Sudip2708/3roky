##  Napíš funkciu n_uholnik(n, x0, y0, r), ktorá nakreslí pravidelný n-uholník.
##  Tento n-uholník bude vpísaný v myslenej kružnici so stredom (x0, y0) a s polomerom r.
##
##  Napríklad pre volanie:
##    n_uholnik(3, 50, 50, 45)
##    n_uholnik(4, 150, 50, 45)
##    n_uholnik(5, 250, 50, 45)
##
##    n_uholnik(6, 50, 150, 45)
##    n_uholnik(7, 150, 150, 45)
##    n_uholnik(8, 250, 150, 45)


#úvodní a prázdný řádek:
print('N-ÚHELNÍK')
print('funkce na kreslení n-úhelníků \npouze zobrazení výsledku dle předem daného zadání')
print()


#prázdný řádek a příkaz pro spuštění okna grafické aplikace:
print()
input('[zmáčkni [Enter] pro zobrazení grafické aplikace]')


#moduly:
import tkinter
import math


#definice funkce:
def n_uholnik(n, x0, y0, r):                                    #parametry - počet stran, x, y středu a poloměr
    a = 360 / n                                                 #počet stupňů na jeden středový úhel
    uhol = a                                                    #hodnota středového úhlu pro výpočet dašího bodu
    x1 = x0 + r                                                 #x-ová osa 1. bodu
    y1 = y0                                                     #y-ová osa 1. bodu
    for i in range(n):                                          #cyklus - dle počtu stran
        x2 = x0 + r * round(math.cos(math.radians(uhol)), 4)    #x-ová osa 2. bodu
        y2 = y0 + r * round(math.sin(math.radians(uhol)), 4)    #y-ová osa 2. bodu
        canvas.create_line(x1 ,y1, x2, y2)                      #vytvoření linky
        uhol += a                                               #přípočet k úhlu pro další bod
        x1, y1 = x2, y2                                         #posunutí počátečního bodu


#vytvoření grafického prostředí:
canvas = tkinter.Canvas()
canvas.pack()


#výpočet:
n_uholnik(3, 50, 50, 45)
n_uholnik(4, 150, 50, 45)
n_uholnik(5, 250, 50, 45)

n_uholnik(6, 50, 150, 45)
n_uholnik(7, 150, 150, 45)
n_uholnik(8, 250, 150, 45)


#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]')    


#aktivace grafické aplikace:
tkinter.mainloop() 


