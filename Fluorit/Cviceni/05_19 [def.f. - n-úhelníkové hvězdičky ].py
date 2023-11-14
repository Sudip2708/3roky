##  Napíš funkciu n_hviezda(n, x0, y0, r, k=2), ktorá pracuje na rovnakom princípe
##  ako n_uholnik(n, x0, y0, r) z predchádzajúcej úlohy.
##  V tomto prípade sa ale nespájajú úsečkami najbližšie vrcholy n-uholníka,
##  ale parameter k určuje, o koľko vrcholov sa presunieme pre každú úsečku.
##  Napríklad n_hviezda(5, 50, 50, 45, 2) označuje, že sa budú spájať vrcholy 5-uholníka takto:
##  0. vrchol s 2., potom 2. vrchol s 4., potom 4. s 1., 1. vrchol so 3.
##  a na koniec (piata úsečka) 3. vrchol s 0.
##  Zrejme pre k=1 by sa kreslili pôvodné n-uholníky.
##
##  Napríklad pre volanie:
##    n_hviezda(5, 50, 50, 45)
##    n_hviezda(7, 150, 50, 45)
##    n_hviezda(7, 250, 50, 45, 3)
##
##    n_hviezda(9, 50, 150, 45)
##    n_hviezda(9, 150, 150, 45, 4)
##    n_hviezda(11, 250, 150, 45, 4)


#úvodní a prázdný řádek:
print('N-ÚHELNÍKOVÉ HVĚZDIČKY')
print('funkce na kreslení n-úhelníkových hvězdiček \npouze zobrazení výsledku dle předem daného zadání')
print()


#prázdný řádek a příkaz pro spuštění okna grafické aplikace:
print()
input('[zmáčkni [Enter] pro zobrazení grafické aplikace]')


#moduly:
import tkinter
import math


#definice funkce:
def n_hviezda(n, x0, y0, r, k=2):                               #parametry - počet stran, x, y středu, poloměr a ob-kolik bodů další linka
    a = 360 / n                                                 #počet stupňů na jeden středový úhel
    uhol = a * k                                                #hodnota středového úhlu pro výpočet dašího bodu
    x1 = x0 + r                                                 #x-ová osa 1. bodu
    y1 = y0                                                     #y-ová osa 1. bodu
    for i in range(n):                                          #cyklus - dle počtu stran
        x2 = x0 + r * round(math.cos(math.radians(uhol)), 4)    #x-ová osa 2. bodu
        y2 = y0 + r * round(math.sin(math.radians(uhol)), 4)    #y-ová osa 2. bodu
        canvas.create_line(x1 ,y1, x2, y2)                      #vytvoření linky
        uhol += a * k                                           #přípočet k úhlu pro další bod
        x1, y1 = x2, y2                                         #posunutí počátečního bodu


#vytvoření grafického prostředí:
canvas = tkinter.Canvas()
canvas.pack()


#výpočet:
n_hviezda(5, 50, 50, 45)
n_hviezda(7, 150, 50, 45)
n_hviezda(7, 250, 50, 45, 3)

n_hviezda(9, 50, 150, 45)
n_hviezda(9, 150, 150, 45, 4)
n_hviezda(11, 250, 150, 45, 4)


#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]')    


#aktivace grafické aplikace:
tkinter.mainloop() 


