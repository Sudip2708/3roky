##  Napíš program, ktorý nakreslí n náhodných farebných domčekov.
##  Každý domček sa skladá z rovnostranného trojuholníka
##  (použi riešenie z predchádzajúcej úlohy) a štvorca.
##  Polohu domčeka, veľkosť strany jeho štvorca a trojuholníka zvoľ náhodne
##  (veľkosť bude náhodné číslo z <10, 50>).
##  Tiež ich farby zvoľ náhodne.


#úvodní a prázdný řádek:
print('BAREVNÉ DOMEČKY')
print('(dle počtu zobrazí náhodně umístěné a barevné malé domečky)')
print()


#vstupní data:
z = int(input('Zadej číslo: '))                                     #vstup pro počet


#moduly:
import tkinter
import random


#grafické okno:
canvas = tkinter.Canvas()
canvas.pack()


#výpočet:
for i in range (z):                                                 #cyklus
    a = random.randint(10, 50)                                      #strana
    b1 = f'#{random.randrange(256**3):06x}'                         #barva čtverce
    b2 = f'#{random.randrange(256**3):06x}'                         #barva trojuhelníku
    x = random.randint(20, 350)                                     #x=ová souřadnice levého horního rohu čtverce
    y = random.randint(20, 240)                                     #y=ová souřadnice levého horního rohu čtverce
    v = (a*(3**(1/2)))/2                                            #výška trojůhelníka
    canvas.create_rectangle(x, y, x+a, y+a, fill=b1, outline='')    #vytvoření čtverce
    canvas.create_polygon(x, y, x+a, y, x+a/2, y-v, fill=b2)        #vytvoření trojúhelníku


#grafické okno:
tkinter.mainloop()                                                  #aktivace grafické aplikace
