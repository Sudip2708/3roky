##  Napíš funkciu rgb (z prednášky) a pomocou nej zafarbi štvorce takto
##  (ľavý horný štvorec má farbu rgb(255, 0, 0)
##  a pravý dolný skoro rgb(255, 255, 0),
##  farba v ostatných štvorcoch plynulo prechádza - čím je štvorec bližšie
##  k pravému dolnému rohu, tým je bližšie k žltej):
##
##  Předchozí úloha z které vycházím:
####  Napíš funkciu stv(riadok, stlpec, farba='white'),
####  ktorá nakreslí farebný štvorec do myslenej štvorcovej siete,
####  v ktorej je každé políčko veľké 30x30.
####  Ľavý horný roh najľavejšieho horného štvorca má súradnice (5, 5).
####
####  Napríklad pre volanie:
####    for i in range(8):
####        for j in range(12):
####            if i == j:
####                stv(i, j)
####            else:
####                stv(i, j, nahodna_farba())


#úvodní a prázdný řádek:
print('ČTVERCOVÁ SÍŤ JEDNOHO ODSTÍNU')
print('funkce na uspořádané vykreslení barvy jednoho odstínu v síti čtverců \npouze zobrazení výsledku dle předem daného zadání')
print()


#prázdný řádek a příkaz pro spuštění okna grafické aplikace:
print()
input('[zmáčkni [Enter] pro zobrazení grafické aplikace]')


#moduly:
import tkinter
import random


#definice funkce:
def stv(riadok, stlpec, farba='white'):                                         #parametry - řádek, sloupec, barva
    a = 30                                                                      #šířka čtverce
    b = 5                                                                       #odstup od kraje
    c = riadok                                                                  #číslo řádku
    d = stlpec                                                                  #číslo sloupce
    e = farba                                                                   #barva
    canvas.create_rectangle(a*d+b, a*c+b, a+a*d+b, a+a*c+b, fill=e, outline='') #vytvoř čtverec, vyplň barvou, odeber obris
    
def rgb(r, g, b):
    return f'#{r:02x}{g:02x}{b:02x}'

    
#vytvoření grafického prostředí:
canvas = tkinter.Canvas()
canvas.pack()


#výpočet:
a = 8                                                                           #počet řádků
b = 12                                                                          #počet sloupců
for i in range(a):                                                              #cyklus - počet řádků
    for j in range(b):                                                          #podcyklus - počet sloupců
        z1 = (255 // (a+b)) * (j+i)                                             #vyděl číslo celé barvy(255) součtem sloupců a řádků (=počtem odstínů) a výsledek vynásob součtem cyklu řádku a sloupce - celkem je 20 odstínů a v každém řádku se začíná o jeden míň
        barva = rgb(255, z1, 0)                                                 #přiděl výsledné číslo do funkce rgb()
        stv(i, j, barva)                                                        #výsledek odešli do funkce stv()


#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]')    


#aktivace grafické aplikace:
tkinter.mainloop() 

