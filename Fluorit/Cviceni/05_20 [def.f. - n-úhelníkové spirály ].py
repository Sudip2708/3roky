##  Aj nasledovná funkcia n_spirala(n, x0, y0, r) vychádza z riešenia funkcie n_uholnik(n, x0, y0, r).
##  V tomto prípade sa nebude kresliť n-uholník, ale špirála.
##  Každá úsečka tu bude spájať dva vrcholy lenže na stále sa zväčšujúcej kružnici so stredom (x0, y0).
##  Začína sa na kružnici s polomerom 5.
##  Prvý vrchol sa spojí s nasledujúcim ale na kružnici s polomerom o 2 väčším.
##  Takto sa pokračuje, až kým by nebol polomer väčší ako r.
##
##  Príklad pre volanie:
##    n_spirala(5, 190, 130, 125)
##
##  A:
##    n_spirala(3, 50, 50, 45)
##    n_spirala(4, 150, 50, 45)
##    n_spirala(5, 250, 50, 45)
##
##    n_spirala(6, 50, 150, 45)
##    n_spirala(7, 150, 150, 45)
##    n_spirala(8, 250, 150, 45)


#úvodní a prázdný řádek:
print('N-ÚHELNÍKOVÉ SPIRÁLY')
print('funkce na kreslení n-úhelníkových spirál \npouze zobrazení výsledku dle předem daného zadání')
print()


#prázdný řádek a příkaz pro spuštění okna grafické aplikace:
print()
input('[zmáčkni [Enter] pro zobrazení grafické aplikace]')


#moduly:
import tkinter
import math


#definice funkce:
def n_spirala(n, x0, y0, r):                                    #parametry - počet stran, x, y středu a poloměr
    a = 360/n                                                   #počet stupňů na jeden středový úhel
    r1 = 5                                                      #počáteční poloměr
    uhol = a                                                    #hodnota středového úhlu pro výpočet dašího bodu
    x1 = x0 + r1                                                #x-ová osa 1. bodu
    y1 = y0                                                     #y-ová osa 1. bodu
    while r1 <= r:                                              #cyklus - dokud není prúměr kružnice roven průměru zadanému
        r1 += 2                                                 #přípočet k průměru kružnice dalšího bodu
        x2 = x0 + r1 * round(math.cos(math.radians(uhol)), 4)   #x-ová osa 2. bodu
        y2 = y0 + r1 * round(math.sin(math.radians(uhol)), 4)   #y-ová osa 2. bodu
        canvas.create_line(x1 ,y1, x2, y2)                      #vytvoření linky
        uhol += a                                               #přípočet k úhlu pro další bod
        x1, y1 = x2, y2                                         #posunutí počátečního bodu


#vytvoření grafického prostředí:
canvas = tkinter.Canvas()
canvas.pack()


#výpočet:
n_spirala(3, 50, 50, 45)
n_spirala(4, 150, 50, 45)
n_spirala(5, 250, 50, 45)

n_spirala(6, 50, 150, 45)
n_spirala(7, 150, 150, 45)
n_spirala(8, 250, 150, 45)


#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]')    


#aktivace grafické aplikace:
tkinter.mainloop() 

