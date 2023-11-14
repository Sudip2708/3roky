##  Napíš program, ktorý pomocou canvas.create_polygon
##  nakreslí rovnostranný trojuholník.
##
##  V premenných:
##    x, y = 50, 250
##    a = 280
##    
##  má nastavené súradnice ľavého dolného vrcholu
##  a veľkosť strany trojuholníka.
##  Spomeň si, ako vypočítaš výšku rovnostranného trojuholníka.


#úvodní a prázdný řádek:
print('MODRÝ TROJÚHELNÍK')
print('(pouze zobrazí modrý trojúhelník)')
print()


#zobrazení výsledku:
input('Zmáčkni [ENTER] pro zobrazení')              #přechod od grafického prostředí


#moduly:
import tkinter


#grafické okno:
canvas = tkinter.Canvas()
canvas.pack()


#promněné:
a = 280                                             #strana trojúhelníka
x = 50                                              #x-ová osa levého dolního vrcholu
y = 250                                             #y-ová osa levého dolního vrcholu
v = (280*(3**(1/2)))/2                              #výška trojůhelníka
x1 = x                                              #x-ová osa levého dolního vrcholu
y1 = y                                              #y-ová osa levého dolního vrcholu
x2 = x + a                                          #x-ová osa pravého dolního vrcholu
y2 = y                                              #y-ová osa pravého dolního vrcholu
x3 = x + a/2                                        #x-ová osa horního vrcholu
y3 = y - v                                          #y-ová osa horního vrcholu


#výpočet:
canvas.create_polygon(x1, y1, x2, y2, x3, y3, fill='blue')


#grafické okno:
tkinter.mainloop()                                  #aktivace grafické aplikace
