##  Napíš program, ktorý nakresli vlajku Českej republiky
##  (vlajku bývalého Československa).
##
##  V premenných:
##    sirka, vyska = 300, 200
##
##  má zadané rozmery vlajky.
##  Modrý klin ide do polovice šírky vlajky.


#úvodní a prázdný řádek:
print('VLAJKA ČESKÉ REPUBLIKY')
print('(pouze zobrazí vlajku české republiky)')
print()


#zobrazení výsledku:
input('Zmáčkni [ENTER] pro zobrazení')                              #přechod od grafického prostředí


#moduly:
import tkinter


#grafické okno:
canvas = tkinter.Canvas()
canvas.pack()


#promněné:
x = 300                                                             #šířka vlajky
y = 200                                                             #výška vlajky
z = 20                                                              #odsazení od kraje


#výpočet bílý obdelník:
x1b = z                                                             #x-ová souřadnice levého horního rohu bílého obdelníku
y1b = z                                                             #y-ová souřadnice levého horního rohu bílého obdelníku
x2b = z + x                                                         #x-ová souřadnice pravého dolního rohu bílého obdelníku
y2b = z + y                                                         #y-ová souřadnice pravého dolního rohu bílého obdelníku
canvas.create_rectangle(x1b, y1b, x2b, y2b, fill='white')           #vytvoření bílého obdelníku


#výpočet červený obdelník:
x1c = z                                                             #x-ová souřadnice levého horního rohu červeného obdelníku
y1c = z + y/2                                                       #y-ová souřadnice levého horního rohu červeného obdelníku
x2c = z + x                                                         #x-ová souřadnice pravého dolního rohu červeného obdelníku
y2c = z + y                                                         #y-ová souřadnice lpravého dolního rohu červeného obdelníku
canvas.create_rectangle(x1c, y1c, x2c, y2c, fill='red', outline='') #vytvoření červeného obdelníku


#výpočet modrý trojúhelník:
x1m = z                                                             #x-ová souřadnice levého horního rohu modrého trojúhelníku
y1m = z                                                             #y-ová souřadnice levého horního rohu modrého trojúhelníku
x2m = z                                                             #x-ová souřadnice levého spodního rohu modrého trojúhelníku
y2m = z + y                                                         #y-ová souřadnice levého spodního rohu modrého trojúhelníku
x3m = z + x/2                                                       #x-ová souřadnice pravého rohu modrého trojúhelníku
y3m = z + y/2                                                       #y-ová souřadnice pravého rohu modrého trojúhelníku
canvas.create_polygon(x1m, y1m, x2m, y2m, x3m, y3m, fill='blue')    #vytvoření modrého trojúhelníku


#grafické okno:
tkinter.mainloop()                                                  #aktivace grafické aplikace
