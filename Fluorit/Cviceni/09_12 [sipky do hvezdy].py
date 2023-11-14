##  Napíš funkciu vektor(xy, dlzka, uhol),
##  ktorá nakreslí vektor (teda šípku) z bodu xy (dvojprvkový tuple celých čísel)
##  s danou dĺžkou a s daným uhlom (v stupňoch).
##  Uvedom si, že koncové body takéhoto vektora ležia na kružnici
##  s polomerom dlzka a stredom xy.
##  Na kreslenie šípky využi volanie funkcie sipka z predchádzajúcej úlohy.
##  Funkcia vektor vráti (return) súradnicu koncového bodu vektora
##  ako dvojicu (tuple) celých čísel.
##  Napríklad:	
##    import tkinter	
##    from math import sin, cos, radians	
##            
##    def sipka(xy1, xy2):	
##        ...	
##            
##    def vektor(xy, dlzka, uhol):	
##        ...	
##        return ...	
##            
##    canvas = tkinter.Canvas()	
##    canvas.pack()	
##            
##    poz = (200, 120)	
##    for uhol in range(0, 720, 144):	
##        poz = vektor(poz, 100, uhol)	
##            
##    tkinter.mainloop()	
##    nakreslí:	


#úvodní a prázdný řádek:
print('ŠIPKY DO HVĚZDIČKY')
print('''Pouze k zobrazení - program obsahuje 2 funkce, první kreslí šipky,
druhá vypočítává souřadnice dle délky a úhlu. V programu jsou
použity na nakreslení hvězdy.''')
print()


#prázdný řádek a příkaz pro spuštění okna grafické aplikace:
print()
input('[zmáčkni [Enter] pro zobrazení grafické aplikace]')


#definice funkcí:
def sipka(xy1, xy2):
    canvas.create_line(xy1, xy2, arrow='last', width=4)     #příkaz na kreslení šipky

def vektor(xy, dlzka, uhol):                                #parametry - osa xy, délká úsečky a úhel
    a = dlzka * math.sin(math.radians(uhol))                #výpočet délky strany "a" pravoúhlého trojúhelníku dle déky strany "c" a úhlu
    b = dlzka * math.cos(math.radians(uhol))                #výpočet délky strany "b" pravoúhlého trojúhelníku dle déky strany "c" a úhlu
    x1, y1 = xy                                             #přiřazení x1 a y1 ze vstupu
    x2 = x1 + b                                             #výpočet souřadnice x druhého bodu
    y2 = y1 + a                                             #výpočet souřadnice y druhého bodu
    sipka(xy, (x2, y2))                                     #volání funkce "sipka" pro nakreslení šipky
    return x2, y2                                           #vrácení hodnot "x2", "y2"


#import modulů:
import tkinter
import math


#grafické okno:
canvas = tkinter.Canvas()
canvas.pack()


#vypočet:
poz = (145, 110)	                                    #pozice výchozího bodu
for uhol in range(0, 720, 144):                             #cyklus - pro uhel 144 v rozmezí 0 - 720
    poz = vektor(poz, 100, uhol)	                    #volání funkce "vektor" - nakreslení šipky, přiřazení nových hodnot pro pozici výchozího bodu


#aktivace grafické aplikace:
tkinter.mainloop()  
