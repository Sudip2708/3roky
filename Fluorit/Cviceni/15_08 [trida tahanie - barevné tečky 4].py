##Zadefinuj triedu Tahanie s tromi metódami __init__, klik a tahanie:
##o	metódy __init__ a klik budú veľmi podobné metódam z (5) úlohy:
##        __init__ vytvorí grafickú plochu a zviaže udalosť kliknutia
##        s metódou self.klik a udalosť ťahania ('<B1-Motion>') s metódou self.tahanie
##o	metóda klik nakreslí malú kružnicu
##o	metóda tahanie umožní pri ťahaní myšou kresliť čiaru
##        (posledný kliknutý/ťahaný bod spojí úsečkou s novým bodom)


#úvodní a prázdný řádek:                                                  
print('TŘÍDA TAHANIE - BAREVNÉ TEČKY 4')                              
print('''
Třída Tahanie vytvoří grafickou plochu
kde levým kliknutím myšy kreslí malé různo barevné kroužky propojené přímkou.
Prostředním tlačítkem myši, přeruší kreslení přímky.
Pravým kliknutím myšy maže obsah grafické plochy.


Obsahuje následující funkce:

1) inicializační funkce __init__() bez parametrů,
    která vytvoří grafické plátno a naváže metodu klik, přeruš čáru,
    smazat plochu a tahání.

2) metoda klik(), událost navázaná na levý klik myši,
    která v místě kliknutí do plochy nakreslí kolečko
    vyplněné náhodnou barvou

3) metoda smazat_plochu(),  událost navázaná na pravý klik myši,
    která smaže obsah plochy

4) metodu prerus_caru(), událost navázaná na prostřední klik myši (kolečko),
    která přeruší kreslení uhlopříčky

5) metoda tahanie(), událost navázaná na pohyb myši,
    která vykreslúje pohybem myši přímku

''')
input('zmáčkni [enter] pro zpuštění programu')


#import modulů:
import tkinter
import random


#definice třídy:
class Tahanie:
    canvas = tkinter.Canvas(height=300, width=300)
    canvas.pack()
    seznam = []

    def __init__(self):
        self.canvas.bind('<ButtonPress-1>', self.klik)
        self.canvas.bind('<ButtonPress-2>', self.prerus_caru)
        self.canvas.bind('<ButtonPress-3>', self.smazat_plochu)
        self.canvas.bind('<Motion>', self.tahanie)

    def klik(self, event):
        self.x = event.x
        self.y = event.y
        self.r = 5
        self.barva = f'#{random.randrange(256**3):06x}'
        x, y, r, b = self.x, self.y, self.r, self.barva
        self.canvas.create_oval(x-r, y-r, x+r, y+r, fill=b)
        self.cara = self.canvas.create_line(x, y, x, y, fill=b, width=r)
        self.seznam.append((x, y))

    def smazat_plochu(self, event):
        self.canvas.delete('all')
        self.seznam = []

    def prerus_caru(self, event):
        self.canvas.delete(self.cara)

    def tahanie(self, event):
        if len(self.seznam) > 0:
            self.canvas.coords(self.cara, self.x, self.y, event.x, event.y)


#aktivace programu:
k = Tahanie()


#aktivace grafické aplikace:
tkinter.mainloop()
