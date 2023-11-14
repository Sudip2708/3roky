##  Napíš program, ktorý nakreslí olympijské kruhy.
##  V premenných:
##    x, y = 70, 100
##    r = 50
##    dx, dy = 120, 60
##
##  má zadané: súradnice stredu horného najľavejšieho kruhu (x, y),
##  polomer kruhov (r) a vzdialenosť medzi kruhmi v jednom rade (dx)
##  a vzdialenosť medzi radmi (dy).
##  Hrúbka čiar kružníc nech je 15.


#úvodní a prázdný řádek:
print('OLYMPIJSKÉ KRUHY')
print('(pouze zobrazí olympijské kruhy v 5-ti barvách)')
print()


#zobrazení výsledku:
input('Zmáčkni [ENTER] pro zobrazení')                          #přechod od grafického prostředí


#moduly:
import tkinter                                                  #import modulu


#grafické okno:
canvas = tkinter.Canvas()                                       #vytvoření plátna
canvas.pack()                                                   #umístění plátna do aplikace


#promněné:
x = 70                                                          #x-óvá souřadnicestředu horního levého kruhu
y = 100                                                         #y-óvá souřadnicestředu horního levého kruhu
r = 50                                                          #poloměr kruhu
dx = 120                                                        #vzdálenost mezi kruhy v jednom řadě
dy = 60                                                         #vzdálenost mezi řadami
x1 = 70                                                         #x-ová souřadnice středu prvního kruhu
y1 = 100                                                        #y-ová souřadnice středu horních 3 kruhů
y2 = 160                                                        #y-ová souřadnice středu dolních 2 kruhů


#barvi:
a1 = 'blue'                                                     #modrá
a2 = 'black'                                                    #černá
a3 = 'red'                                                      #červená
a4 = 'yellow'                                                   #žlutá
a5 = 'green'                                                    #zelená
d = 0                                                           #počítadlo měnitele barvy
e = a1                                                          #proměná barvy


#výpočet bez for cyklu:
##canvas.create_oval(x-r, y-r, x+r, y+r, outline=a1, width=20)
##canvas.create_oval(x-r+dx/2, y-r+dy, x+r+dx/2, y+r+dy, outline=a4, width=20)
##canvas.create_oval(x-r+dx, y-r, x+r+dx, y+r, outline=a2, width=20)
##canvas.create_oval(x-r+dx/2+dx, y-r+dy, x+r+dx/2+dx, y+r+dy, outline=a5, width=20)
##canvas.create_oval(x-r+dx*2, y-r, x+r+dx*2, y+r, outline=a3, width=20)


#výpočet za pomocí for cyklu:
for i in range(5):                                              #cyklus pro kreslení kol
    canvas.create_oval(x1-r, y1-r, x1+r, y1+r, outline=e, width=20)
    x1 += dx/2                                                  #přípočet x-ové hodnoty
    y1, y2 = y2, y1                                             #změna horní za spodní y-ovou polohu
    d += 1                                                      #přípočet počítadla měnitele barvy
    if d == 1:                                                  #změna barvy:
        e = a4 
    elif d == 2:
        e = a2
    elif d == 3:
        e = a5
    else:
        e = a3


#grafické okno:
tkinter.mainloop()                                              #aktivace grafické aplikace
