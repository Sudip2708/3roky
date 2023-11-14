##  Napíš funkciu karticka(x, y, text),
##  ktorá nakreslí bledošedý obdĺžnik a do jeho stredu vypíše zadaný text.
##  Stred kartičky má súradnice (x, y) a jej strany majú dĺžky 100 a 40.
##  Font písma môže byť, napríklad 'arial 14'.
##
##  Otestuj náhodným vygenerovaním 10 kartičiek, napríklad:
##    for i in range(10):
##        karticka(random.randint(50, 300), random.randint(50, 200), 'Python')


#úvodní a prázdný řádek:
print('TEXT V OBDELNÍKU')
print('funce na vykreslení textu do obdelníku \npouze zobrazení výsledku dle předem daného zadání')
print()


#prázdný řádek a příkaz pro spuštění okna grafické aplikace:
print()
input('[zmáčkni [Enter] pro zobrazení grafické aplikace]')


#moduly:
import tkinter
import random


#definice funkce:
def karticka(x, y, text):                                                   #parametry - osa x, osa y a text
    canvas.create_rectangle(x-50, y-20, x+50, y+20, fill='lightgray')       #vytvoř kartičku o velikosti 100 / 40
    canvas.create_text(x, y, text=text, font='arial 14')                    #vytvoř text


#vytvoření grafického prostředí:
canvas = tkinter.Canvas()
canvas.pack()


#výpočet:
for i in range(10):                                                         #cyklus - 10x
    karticka(random.randint(50, 300), random.randint(50, 200), 'Python')    #vytvoř náhodné pozice pro x a y funkce "kruhy"


#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]')    


#aktivace grafické aplikace:
tkinter.mainloop() 
