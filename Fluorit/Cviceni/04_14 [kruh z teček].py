##  V ďalšej verzii bodkovacej úlohy vybodkuješ kruh.
##  Program opäť nakreslí 4000 náhodných bodiek, ale tie z nich,
##  ktoré majú vzdialenosť od (x0, y0) menšiu ako r,
##  zafarbí na červeno, zvyšné na modro.
##
##  Napríklad pre premenné:
##    x0, y0 = 180, 130
##    r = 110
##
##Úloha z které se vychází:
####  Využi program z prednášky, v ktorom sa vykresľovalo 1000 farebných bodiek
####  (malé krúžky s polomerom 5 bez obrysu) podľa toho či mali x-ovú,
####  alebo y-ovú súradnicu menšiu alebo väčšiu ako 150.
####  Veľkosť grafickej plochy bola 300x300.
####  Zmeň v tomto programe sériu príkazov if tak,
####  aby kreslené bodky vytvorili vnútorný červený štvorec s rozmermi 150x150.
####  Vykresli s 4000 farebnými bodkami.


#úvodní a prázdný řádek:
print('KRUH Z TEČEK')
print('program vykreslý kruh z červených teček a okolní prostředí vytečkuje modře')
print()


#prázdný řádek a příkaz pro spuštění okna grafické aplikace:
print()
input('[zmáčkni [Enter] pro zobrazení grafické aplikace]')


#moduly:
import tkinter
import random


#grafické okno:
canvas = tkinter.Canvas(bg='white', width=300, height=300)
canvas.pack()


#proměné:
x0 = 180                                                        #x-ová osa středu kružnice
y0 = 130                                                        #y-ová osa středu kružnice
r = 110                                                         #poloměr kružnice


#výpočet:
#canvas.create_oval(x0-r, y0-r, x0+r, y0+r)                     #náhled - kde má být kruh
for i in range(4000):                                           #cyklus pro 4000 teček
    x = random.randint(1, 300)                                  #x-ová osa tečky
    y = random.randint(1, 300)                                  #y-ová osa tečky
    a = abs(y0 - y)                                             #vypočítání strany A pravoúhlého trojuhelníku umístěného podél osy y
    b = abs(x0 - x)                                             #vypočítání strany B pravoúhlého trojuhelníku umístěného od středu podél osy x
    c = (a**2 + b**2)**.5                                       #vypočítání strany C, vycházející ze středu a souběžná s poloměrem
    if c <= r:                                                  #podmínka - když se c menší nebo roven poloměru kružnice
        farba = 'red'                                           #použij červenou barvu
    else:                                                       #a pokud je delší
        farba = 'blue'                                          #pouužij modrou barvu
    canvas.create_oval(x-5, y-5, x+5, y+5, fill=farba, width=0) #vytvožení tečky

#grafické okno:
tkinter.mainloop()                                              #aktivace grafické aplikace
