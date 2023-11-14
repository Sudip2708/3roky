##  Napíš funkciu dom(x, y, vel1, vel2), ktorá nakreslí domček:
##  štvorec má ľavý dolný roh (x, y) a veľkosť strany je vel1,
##  trojuholník má výšku vel2 a základňu vel1.
##  Oba sú zafarbené rôznymi náhodnými farbami.
##
##  Napríklad pre volanie:
##    x, y = 10, 150
##    while x < 330:
##	v = random.randint(20, 50)
##        dom(x, y, v, random.randint(v//2, v))
##	x += v


#úvodní a prázdný řádek:
print('DOMEČKY')
print('funkce na vykreslení domečků \npouze zobrazení výsledku dle předem daného zadání')
print()


#prázdný řádek a příkaz pro spuštění okna grafické aplikace:
print()
input('[zmáčkni [Enter] pro zobrazení grafické aplikace]')


#moduly:
import tkinter
import random


#definice funkce:
def dom(x, y, vel1, vel2):                                      #parametry - osa x, osa y, velikost šířka domečku, výška střechy
    barva = f'#{random.randrange(256**3):06x}'                  #náhodná barva pro základ domečku
    canvas.create_rectangle(x, y-vel1, x+vel1, y, fill=barva)   #vytvoř domeček (čtverec) a vyplň barvou
    a = x, y-vel1                                               #levý spodní roh střechy
    b = x+vel1, y-vel1                                          #pravý spodní roh střechy
    c = x+vel1/2, y-vel1-vel2                                   #horní roh střechy
    barva = f'#{random.randrange(256**3):06x}'                  #náhodná barva pro střechu
    canvas.create_polygon(a, b, c, outline='black', fill=barva) #vytvoř střechu (trojůhelník), udělej obris a vyplň barvou


#vytvoření grafického prostředí:
canvas = tkinter.Canvas()
canvas.pack()


#výpočet:
x, y = 10, 150                                                  #parametry x a y
while x < 330:                                                  #cyklus - dokud x je menší než 330
    v = random.randint(20, 50)                                  #náhodná velikost domečku mezi hodnotami 20 a 50 
    dom(x, y, v, random.randint(v//2, v))                       #volání funkce "dom" + výpočet výšky střechy
    x += v                                                      #posunutí parametru x


#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]')    


#aktivace grafické aplikace:
tkinter.mainloop() 
