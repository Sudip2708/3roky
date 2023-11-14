##  Napíš funkciu slnko(n, x, y), ktorá nakreslí slnko ako n lúčov
##  (hrubšie žlté, resp. zlaté úsečky, ktoré vychádzajú zo stredu (x, y) a majú dĺžku 70)
##  a veľký žltý/zlatý kruh so stredom (x, y) a polomerom 40.
##
##  Otestuj, napríklad:
##    slnko(10, 100, 80)
##    slnko(20, 250, 120)


#úvodní a prázdný řádek:
print('SLUNCE')
print('funkce na kreslení slunce \npouze zobrazení výsledku dle předem daného zadání')
print()


#prázdný řádek a příkaz pro spuštění okna grafické aplikace:
print()
input('[zmáčkni [Enter] pro zobrazení grafické aplikace]')


#moduly:
import tkinter
import math


#definice funkce:
def slnko(n, x, y):                                                         #parametry - počet paprsků, x, y středu
    for i in range(n):                                                      #cyklus - dle počtu paprsků
        sin = abs(round(math.sin(math.radians((360/n)*(i+1))), 4))          #výpočet sinus pro daný úhel - zaokrouhleno na 4 místa a v absolutní hodnotě (žádné mínus)
        c = 70                                                              #strana "c" pravoúhého trojúhelníku mezi středem kružnice a bodu na ní
        a = round(c * sin, 4)                                               #výpočet strany "a" pravoúhého trojúhelníku mezi středem kružnice a bodu na ní
        b = round((c**2 - a**2)**.5, 4)                                     #výpočet strany "b" pravoúhého trojúhelníku mezi středem kružnice a bodu na ní
        if (360/n)*(i+1) <= 90:                                             #podmínka - pokud má úhel roven,nebo menší než 90°
            canvas.create_line(x, y, x+a, y-b, width=10, fill='gold')       #udělej přímku s těmito souřadnicemi
        elif (360/n)*(i+1) <= 180:                                          #podmínka - pokud má úhel roven,nebo menší než 180°
            canvas.create_line(x, y, x+a, y+b, width=10, fill='gold')       #udělej přímku s těmito souřadnicemi
        elif (360/n)*(i+1) <= 270:                                          #podmínka - pokud má úhel roven,nebo menší než 270°
            canvas.create_line(x, y, x-a, y+b, width=10, fill='gold')       #udělej přímku s těmito souřadnicemi
        else:                                                               #podmínka - ve všech ostatních případech
            canvas.create_line(x, y, x-a, y-b, width=10, fill='gold')       #udělej přímku s těmito souřadnicemi
    canvas.create_oval(x+40, y-40, x-40, y+40, fill='gold', width=0)        #nakresli středový kruh slunce


#vytvoření grafického prostředí:
canvas = tkinter.Canvas()
canvas.pack()


#výpočet:
slnko(10, 100, 80)
slnko(20, 250, 120)


#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]')    


#aktivace grafické aplikace:
tkinter.mainloop() 

