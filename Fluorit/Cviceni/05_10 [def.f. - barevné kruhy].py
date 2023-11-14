##  Napíš funkciu kruhy(x, y), ktorá nakreslí 10 sústredných náhodne zafarbených kruhov,
##  ich polomery budú 5, 10, 15, …
##
##  Napríklad pre volanie:
##    for i in range(10):
##        kruhy(random.randint(50, 330), random.randint(50, 210))


#úvodní a prázdný řádek:
print('BAREVNÉ KRUHY')
print('funkce na náhodné vykreslení barevných kruhů  \npouze zobrazení výsledku dle předem daného zadání')
print()


#prázdný řádek a příkaz pro spuštění okna grafické aplikace:
print()
input('[zmáčkni [Enter] pro zobrazení grafické aplikace]')


#moduly:
import tkinter
import random


#definice funkce:
def kruhy(x, y):                                                #parametry - osa x a osa y
    r = 55                                                      #poloměr největšího kruhu
    for i in range(11):                                         #cyklus - 10x
        canvas.create_oval(x-r, y-r, x+r, y+r, fill=f'#{random.randrange(256**3):06x}') #vytvoř kruh a vyplň ho náhodnou barvou
        r -= 5                                                  #zmenši poloměr pro příští kruh o 5


#vytvoření grafického prostředí:
canvas = tkinter.Canvas()
canvas.pack()


#výpočet:
for i in range(10):                                             #cyklus - 10x
    kruhy(random.randint(50, 330), random.randint(50, 210))     #vytvoř náhodné pozice pro x a y funkce "kruhy"


#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]')    


#aktivace grafické aplikace:
tkinter.mainloop() 
