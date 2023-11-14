##  Nechaj bežať na obrazovke veľké digitálne hodiny:
##  čas je zobrazený v tvare '9:22:34.5' a mení sa každú 0.1 sekundy.
##  Použi jeden textový objekt (create_text()),
##  ktorému pomocou itemconfig() meníš zobrazovanú hodnotu.
##    • pri štarte programu môžeš využiť h, m, s = time.localtime()[3:6]


#úvodní a prázdný řádek:
print('DIGITÁLNÍ HODINY MĚNÍCÍ MILIVTEŘINY')
print('''Program vytvoří uprostřed plochy digitální hodiny,
na kterých se mění hodnota o desetiny vteřiny''')
print()


#prázdný řádek a příkaz pro spuštění okna grafické aplikace:
print()
input('[zmáčkni [Enter] pro zobrazení grafické aplikace]')


#import modulů:
import tkinter
import math
import time

    
#grafické okno:
canvas = tkinter.Canvas(bg='yellow', width=200, height=50)
canvas.pack()


#definice funkcí:
def casovac():                                      #definice funkce - casovač
    ms.append(ms.pop(0))                            #změna - přípočet milisekund
    h, m, s = time.localtime()[3:6]                 #proměnné - hodiny, minuty, vteřiny
    text = f'{h:2} : {m:2} : {s:2}.{ms[0]}'         #proměnná - text
    canvas.itemconfig(1, text=text)                 #změna - přepiš text
    canvas.after(100, casovac)                      #nastavení časovače pro další zpuštění funkce "casovac"


#proměnné:
x, y = 100, 25                                      #proměnné - pro hodnoty osy 'x' a 'y'
font = ('Arial_Bold', 20)                           #proměnná - pro font
h, m, s = time.localtime()[3:6]                     #proměnné - hodiny, minuty, vteřiny
ms = list(range(0,10,1))                            #proměnná - seznam milisekund
text = f'{h:2} : {m:2} : {s:2}.0'                   #proměnná - text


#vytvoření hodin a volání funkce
canvas.create_text(x, y, text=text, font=font)      #vytvoření objektu - text
casovac()                                           #aktivace časovače


#aktivace grafické aplikace:
tkinter.mainloop()
