##  Napíš funkciu histogram(zoznam),
##  ktorá z daného zoznamu čísel nakreslí stĺpcový diagram
##  (obdĺžniky rovnakej šírky a výšky podľa číselnej hodnoty zo zoznamu).
##  Obdĺžniky budú mať takú šírku,aby čo najlepšie vyplnili šírku plochy 360
##  a budú mať náhodne zafarbenú výplň.
##  Funkcia nemodifikuje vstupný zoznam.
##  Môžeš počítať s tým, že všetky hodnoty v zozname nie sú väčšie ako 240.
##  Napríklad:
##    importtkinter
##    importrandom
##    defhistogram(zoznam):
##    ...
##    canvas = tkinter.Canvas()
##    canvas.pack()
##    histogram([120, 220, 180, 80, 90, 30, 200, 190, 240, 150])
##    tkinter.mainloop()
##    nakreslí:


#úvodní a prázdný řádek:
print('HISTOROGRAM')
print('''pouze k zobrazení - program obsahuje funkci, která po zadání hodnot
vytvoří v grafické aplikaci historogram pro před definované hodnoty:
120, 220, 180, 80, 90, 30, 200, 190, 240 a 150''')
print()


#prázdný řádek a příkaz pro spuštění okna grafické aplikace:
print()
input('[zmáčkni [Enter] pro zobrazení grafické aplikace]')


#definice funkce:
def histogram(seznam):
    sirka = 360//len(seznam)
    x = 10
    y = 260
    for i in seznam:
        barva = f'#{random.randrange(256**3):06x}'
        canvas.create_rectangle(x, y-i, x+sirka, y, fill=barva)
        x = x+sirka


#import modulů:
import tkinter
import random


#grafické okno:
canvas = tkinter.Canvas()
canvas.pack()


#výpočet
histogram([120, 220, 180, 80, 90, 30, 200, 190, 240, 150])


#aktivace grafické aplikace
tkinter.mainloop()  
