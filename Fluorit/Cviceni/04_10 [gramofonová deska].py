##  Napíš program, ktorý nakreslí gramofónovú LP platňu
##  ako niekoľko sústredných kružníc.
##  Najväčšia z nich má polomer r a každá ďalšia je o 3 menšia.
##  Najmenšia kružnica by nemala mať menší polomer ako 15.
##  Každú k-tu kružnicu nakresli šedou farbou (začni od najväčšej).
##
##  Premenné:
##    x, y = 190, 130
##    r = 120
##    k = 6


#úvodní a prázdný řádek:
print('GRAMOFONOVÁ DESKA')
print('program pouze zobrazí kruhy zapuštěné v sobě, vytvářející pocit gramofonové desky')
print()


#prázdný řádek a příkaz pro spuštění okna grafické aplikace:
print()
input('[zmáčkni [Enter] pro zobrazení grafické aplikace]')


#moduly:
import tkinter
import random


#grafické okno:
canvas = tkinter.Canvas()
canvas.pack()


#proměné:
r = 120                                                         #poloměr vnějšího kruhu gr. desky
x = 190                                                         #x-ová souřadnice středu gr. desky
y = 130                                                         #y-ová souřadnice středu gr. desky
k = 6                                                           #číslo kružnice, která bude šedou barvou
z = 3                                                           #hodnota zmenšení další kružnice
p = 0                                                           #počítadlo kružnic
e = 15                                                          #velikost nejmenšího kruhu v gr. desce 


#výpočet:
while r > e:                                                    #cyklus - dokud není poloměr kruhu menší než 15
    if (p + k) % k != 0:                                        #podmínka pokud se jedná o 1 a dále každý další 6-tý kruh
        b = 'blue'                                              #použij modrou barvu
    else:                                                       #jinak
        b = 'red'                                               #použij červenou barvu
    canvas.create_oval(x-r, y-r, x+r, y+r, outline=b)           #vytvoření kruhu
    r -= z                                                      #zmenšení poloměru pro další kruh
    p += 1                                                      #přípočet počítadla kružnic


#grafické okno:
tkinter.mainloop()                                                  #aktivace grafické aplikace
