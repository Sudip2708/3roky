##  Napíš funkciu stvorce(vel, retazec),
##  ktorá dostáva dva parametre: veľkosť štvorca a znakový reťazec s menami farieb.
##  Funkcia nakreslí rad farebných štvorcov veľkosti vel,
##  ktoré budú zafarbené farbami z reťazca.
##  Zrejme štvorcov bude toľko, koľko farieb je v reťazci.
##
##  Pre takéto volanie:
##    stvorce(40, 'red blue purple red gold')


#úvodní a prázdný řádek:
print('BAREVNÉ ČTVERCE')
print('pouze k zobrazení - funkce vytváří barevné čtverce dle zadaných barev')
print()


#prázdný řádek a příkaz pro spuštění okna grafické aplikace:
print()
input('[zmáčkni [Enter] pro zobrazení grafické aplikace]')


#import modulů:
import tkinter


#grafické okno:
canvas = tkinter.Canvas()
canvas.pack()


#definice funkce:
def stvorce(vel, retazec):
    počet = retazec.count(' ')+1                    #počet čtverců
    x = 380 // (počet*2)                            #x středu prvního čtverce
    y = 260 // 2                                    #y středu prvního čtverce
    x1 = x - (vel // 2)                             #x levého horníého rohu prvního čtverce
    y1 = y - (vel // 2)                             #y levého horníého rohu prvního čtverce
    x2 = x + (vel // 2)                             #x pravého dolního rohu prvního čtverce
    y2 = y + (vel // 2)                             #y pravého dolního rohu prvního čtverce
    n = 0                                           #počítadlo posunu dalšího čtverce

    for i in range (počet):                         #cyklus dle počtu čtverců    
        if retazec.find(' ') != -1:                 #podmínka - když řetězec obsahuje mezeru
            barva = retazec[:retazec.find(' ')]     #použij tuto barvu
        else:                                       #jinak
            barva = retazec                         #použij poslední barvu v řetězci
        retazec = retazec[retazec.find(' ')+1:]     #úprava řetězce s barvami pro další průchod
        canvas.create_rectangle(x1+(x*n), y1, x2+(x*n), y2, outline='', fill=barva )    #vytvoření čtverce
        n += 2                                      #přípočet do počítadla pro posun dalšího čtverce
    

#výpočet
stvorce(40, 'red blue purple red gold')   


#aktivace grafické aplikace
tkinter.mainloop()  
