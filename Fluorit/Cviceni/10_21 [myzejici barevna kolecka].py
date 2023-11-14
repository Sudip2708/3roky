##  Na mieste kliknutia myšou sa nakreslí kruh s polomerom 50
##  a s náhodnou farbou výplne, ďalších 50 tiknutí časovača
##  sa jej polomer zmenšuje o 1 s časovým intervalom 0.1 sekundy.
##  Keď bude polomer 0, časovač túto kružnicu (grafický objekt kruh) zruší.
##  Zabezpeč, aby aj viac kliknutí tesne za sebou na rôzne miesta plochy
##  vytvorilo viac kruhov a aby sa všetky postupne zmenšovali o 1.
#1234567890123456789012345678901234567890123456789012345678901234567890123456789
                                                                               #
                                                                               #
print('MYZEJÍCÍ BAREVNÁ KOLEČKA')                                               #úvodní text - nadpis
print('''Program po kliknutí vytvoří kruh vyplněný náhodnou barvou,
který se postupně zmenšuje, až zmyzí''')                                        #úvodní text - popis programu
print()                                                                         #úvodní text - prázdný řádek
print()                                                                         #úvodní text - prázdný řádek
input('[zmáčkni [Enter] pro zobrazení grafické aplikace]')                      #úvodní text - vyzvání vstupu do aplikace
                                                                               #
import tkinter                                                                  #impor modulu tk inter
import random                                                                   #impor modulu random
                                                                               #
canvas = tkinter.Canvas(bg='black', width=500, height=400)                      #vytvoření grafického prostředí
canvas.pack()                                                                   #zobrazení grafického prostředí
                                                                               #
seznam_objektu = []                                                             #seznam pro ukládání info o objektech
                                                                               #
def myzeni():                                                                   #definice funkce - pro myzení
    for n, i in enumerate(seznam_objektu):                                          #cyklus - pro každou položku seznamu + pořadové číslo položky
        c_ob, x, y, r = i[0], i[1], i[2], i[3]-1                                        #proměnná - pro číslo objektu, osu x a y, a poloměr
        if r != 0:                                                                      #podmínka - pokud hodnota poloměru není 0
            canvas.coords(c_ob, x-r, y-r, x+r, y+r)                                         #změna - změň velikost objektu
            seznam_objektu[n][3] = r                                                        #zapiš do seznamu objektu novou hodnotu poloměru
        else:                                                                           #podmínka - pokud je hodnota poloměru 0
            canvas.delete(c_ob)                                                             #změna - smaž objekt
    canvas.after(500, myzeni)                                                       #časovač
                                                                               #
def klik(event):                                                                #definice funkce - klik
    x, y = event.x, event.y                                                         #proměnná - pro hodnoty x a y kliku
    r = 50                                                                          #proměnná - pro hodnotu poloměru
    barva = f'#{random.randrange(256**3):06x}'                                      #proměnná - pro náhodnou barvu
    c_ob = canvas.create_oval(x-r, y-r, x+r, y+r, fill=barva)                       #proměnná & canvas - vytvoření objektu kru a přiřazení jeho čísla
    seznam_objektu.append([c_ob, x, y, r])                                          #změna - přidání seznamu s info o objektu do seznamu objektů
    myzeni()                                                                        #volání funkce - myzení
                                                                               #
canvas.bind('<ButtonPress-1>', klik)                                            #provázání kliknutí
                                                                               #
tkinter.mainloop()                                                              #aktivace grafické aplikace                                                                   
