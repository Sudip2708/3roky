##  Napíš funkciu stvorec(x, y, r, uhol),
##  ktorá vytvorí (vráti) 8-prvkový zoznam čísel v tvare [x, y, x, y, x, y, x, y].
##  Tieto čísla sú súradnicami štyroch vrcholov štvorca v grafickej ploche
##  a tieto vrcholy ležia na kružnici so stredom (x, y) s polomerom r.
##  Vrcholy štvorca budú na kružnici natočené o daný uhol.
##  Ak by si tento zoznam poslal ako parameter do grafického príkazu
##  canvas.create_polygon, dostaneš vyfarbený natočený štvorec.
##  Napríklad:
##    import tkinter
##    from math import sin, cos, radians
##    def stvorec(x, y, r, uhol):
##        ...
##    canvas = tkinter.Canvas()
##    canvas.pack()
##    canvas.create_polygon(stvorec(180, 130, 110, 20), fill='red')
##    canvas.create_polygon(stvorec(180, 130, 90, 45), fill='green')
##    canvas.create_polygon(stvorec(180, 130, 70, 70), fill='gold')
##    canvas.create_polygon(stvorec(180, 130, 50, 95), fill='blue')
##    ckinter.mainloop()
##    nakreslí:


#úvodní a prázdný řádek:
print('4 ČTVERCE')
print('''pouze k zobrazení - program obsahuje funkci, která po zadání souřadnic
středu, poloměru, úhlu a barvy, vytvoří seznam se souřadnicemi, které se následně
použijí pro vytvoření čtverce.
Zde se jedná o 4 čtverce, kde každý další je o něco menší,
jinou barvou a více nahnut.''')
print()


#prázdný řádek a příkaz pro spuštění okna grafické aplikace:
print()
input('[zmáčkni [Enter] pro zobrazení grafické aplikace]')


#definice funkce:
def stvorec(x, y, r, uhol):
    seznam = []
    for i in range(4):
        seznam.append(x + r * cos(radians(uhol+(i*90))))
        seznam.append(y + r * sin(radians(uhol+(i*90))))
    return seznam


#import modulů:
import tkinter
from math import sin, cos, radians


#grafické okno:
canvas = tkinter.Canvas()
canvas.pack()


#výpočet
canvas.create_polygon(stvorec(180, 130, 110, 20), fill='red')
canvas.create_polygon(stvorec(180, 130, 90, 45), fill='green')
canvas.create_polygon(stvorec(180, 130, 70, 70), fill='gold')
canvas.create_polygon(stvorec(180, 130, 50, 95), fill='blue')


#aktivace grafické aplikace
tkinter.mainloop()  
