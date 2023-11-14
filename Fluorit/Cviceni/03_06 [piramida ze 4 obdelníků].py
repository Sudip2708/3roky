##  Napíš program, ktorý nakreslí pyramídu z kvádrov (obdĺžnikov)
##  veľkosti: 200x50, 150x50, 100x50 a 50x50.
##  Najväčší z nich má stred dolnej hrany (180, 250).
##  Všetky zafarbi štyrmi rôznymi odtieňmi zelenej.
##  Na kreslenie použi jeden for-cyklus, v ktorom premenná cyklu farba,
##  bude nadobúdať 4 rôzne reťazce (mená farieb)
##  a v cykle sa budú meniť premenné y a momentálna sirka kvádra.


#úvodní a prázdný řádek:
print('PYRAMIDA ZE ČTYŘ OBDELNÍKŮ')
print('(pouze zobrazí pyramidu ze 4 obdelníků, každý v jiném odstínu zelené)')
print()


#zobrazení výsledku:
input('Zmáčkni [ENTER] pro zobrazení')                  #přechod od grafického prostředí


#moduly:
import tkinter                                          #import modulu


#grafické okno:
canvas = tkinter.Canvas()                               #vytvoření plátna
canvas.pack()                                           #umístění plátna do aplikace


#promněné:
a1 = 200                                                #délka 1. obdelníka od spodu
b1 = 50                                                 #výška 1. obdelníka od spodu
xx1 = 180                                               #x-ová osa středu prvního obdelníka od spodu
yy1 = 250                                               #y-ová osa středu prvního obdelníka od spodu
x1 = 80                                                 #xx1-a1/2 (x-ová hodnota levého horního rohu 1. obdelníka)
y1 = 200                                                #yy1-50 (y-ová hodnota levého horního rohu 1. obdelníka)
x2 = 280                                                #xx1+a1/2 (x-ová hodnota pravého spodního rohu 1. obdelníka)
y2 = 250                                                #yy1 (x-ová hodnota pravého spodního rohu 1. obdelníka)


#barvy:
c1 = 'darkgreen'                                        #tmavě zelená
c2 = 'forestgreen'                                      #světlejší zelená
c3 = 'limegreen'                                        #ještě světlejší zelená
c4 = 'lawngreen'                                        #nejsvětlejší zelená


#výpočet:
d = 0                                                   #počítadlo měnitele barvy
e = c1                                                  #proměná barvy
for i in range(4):                                      #cyklus
    canvas.create_rectangle(x1, y1, x2, y2, fill=e)     #kreslení obdelníků
    x1 += 25                                            #přípočet x1 osy 
    y1 -= 50                                            #odpočet y1 osy
    x2 -= 25                                            #odpočet x2 osy
    y2 -= 50                                            #odpočet y2 osy
    d += 1                                              #přípočet počítadla měnitele barvy
    if d == 1:                                          #změna barvy
        e = c2 
    elif d == 2:
        e = c3
    else:
        e = c4


#grafické okno:
tkinter.mainloop()                                      #aktivace grafické aplikace
