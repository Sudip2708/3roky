##V triede Klikanie zo (6) úlohy uprav metódu klik tak,
##aby okrem kreslenia malej kružnice spojila úsečkou posledne nakreslený bod
##s predchádzajúcim bodom (zrejme okrem prvého kliknutia).
##Nepoužívaj globálne premenné.


#úvodní a prázdný řádek:                                                  
print('TŘÍDA KLIKANIE - BAREVNÉ TEČKY 3')                              
print('''
Třída Klikanie vytvoří grafickou plochu
kde levým kliknutím myšy kreslí malé různo barevné kroužky
které snásledně spojuje přímkou.
Pravým kliknutím myšy maže obsah grafické púlochy.
Prostředním tlačítkem myši, vytiskne obsah souřadnic teček.

Obsahuje následující funkce:

1) inicializační funkce __init__() bez parametrů,
    která vytvoří grafické plátno a naváže metodu klik a smazat plochu

2) metoda klik(), událost navázaná na levý klik myši,
    která v místě kliknutí do plochy nakreslí kolečko
    vyplněné náhodnou barvou a propojené přímkou
    s posledním nakresleným kolečkem

3) metoda smazat_plochu(),  událost navázaná na pravý klik myši,
    která smaže obsah plochy

4) metodu vypis(), událost navázaná na prostřední klik myši (kolečko),
    která vypíše seznam souřadnic

''')
input('zmáčkni [enter] pro zpuštění programu')


#import modulů:
import tkinter
import random


#definice třídy:
class Klikanie:
    canvas = tkinter.Canvas(height=300, width=300)
    canvas.pack()
    seznam = []

    def __init__(self):
        self.canvas.bind('<ButtonPress-1>', self.klik)
        self.canvas.bind('<ButtonPress-2>', self.vypis)
        self.canvas.bind('<ButtonPress-3>', self.smazat_plochu)

    def klik(self, event):
        self.x = event.x
        self.y = event.y
        self.r = 5
        self.barva = f'#{random.randrange(256**3):06x}'
        x, y, r, b = self.x, self.y, self.r, self.barva
        self.canvas.create_oval(x-r, y-r, x+r, y+r, fill=b)
        if len(self.seznam) > 0:
            x0, y0 = self.seznam[-1]
            self.canvas.create_line(x0, y0, x, y, fill=b, width=self.r)
        self.seznam.append((x, y))

    def smazat_plochu(self, event):
        self.canvas.delete('all')
        self.seznam = []

    def vypis(self, event):
        if len(self.seznam) > 0:
            for i in self.seznam:
                print(i)
        else:
            print('seznam souřadnic je prázdný')


#aktivace programu:
k = Klikanie()


#aktivace grafické aplikace:
tkinter.mainloop()
