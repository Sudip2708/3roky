##  Vektor si môžeme predstaviť ako úsečku, ktorá je daná jedným vrcholom (x, y), dĺžkou a uhlom.
##  Uvedom si, že koncové body takéhoto vektora ležia na kružnici
##  s polomerom dĺžka a daným stredom (bodom (x, y)).
##  Úsečku nakreslíme tak, aby mala tvar šípky
##  (do create_line pridáme pomenovaný parameter arrow='last').
##  Napíš funkciu vektor(x, y, dlzka, uhol).
##
##  Otestuj, napríklad takto:
##    for i in range(10):
##        vektor(random.randint(50, 300), random.randint(50, 200),
##            random.randint(10, 80), random.randint(0, 359))


#úvodní a prázdný řádek:
print('VEKTOROVÉ ŠIPKY')
print('funkce náhodně vykreslí 10 šipek \npouze zobrazení výsledku dle předem daného zadání')
print()


#prázdný řádek a příkaz pro spuštění okna grafické aplikace:
print()
input('[zmáčkni [Enter] pro zobrazení grafické aplikace]')


#moduly:
import tkinter
import random
import math


#definice funkce:
def vektor(x, y, dlzka, uhol):                              #parametry - osa x, y, délká úsečky a úhel
    a = dlzka/2 * math.sin(math.radians(uhol))              #výpočet rozdílu x-ové souřadnice
    b = ((dlzka/2)**2 - a**2)**.5                           #výpočet rozdílu x-ové souřadnice
    canvas.create_line(x-a, y+b, x+a, y-b, arrow='last')    #nakreselní úsečky



#vytvoření grafického prostředí:
canvas = tkinter.Canvas()
canvas.pack()


#výpočet:
for i in range(10):
    vektor(random.randint(50, 300), random.randint(50, 200), random.randint(10, 80), random.randint(0, 359))


#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]')    


#aktivace grafické aplikace:
tkinter.mainloop() 


