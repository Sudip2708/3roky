##Zadefinuj triedu Klikanie s dvomi metódami __init__ a klik:
##o	metóda __init__ (okrem self nemá ďalšie parametre) vytvorí grafickú plochu (do self.canvas)
##        a zviaže ju (bind) s metódou self.klik pri kliknutí do plochy ('<ButtonPress>')
##o	metóda klik zrejme musí mať jeden parameter event (okrem self), z ktorého získa x a y
##        kliknutého miesta; metóda na toto kliknuté miesto nakreslí kružnicu s polomerom 5
##o	keď bude táto trieda hotová, program naštartuj a otestuj pomocou:
##k = Klikanie()      # týmto sa zavolá konštruktor __init__()


#úvodní a prázdný řádek:                                                  
print('TŘÍDA KLIKANIE - BAREVNÉ TEČKY 1')                              
print('''
Třída Klikanie vytvoří grafickou plochu kde levým kliknutím myšy
kreslí malé různo barevné kroužky a pravým kliknutím myšy
maže obsah grafické púlochy.
Obsahuje následující funkce:

1) inicializační funkce __init__() bez parametrů,
    která vytvoří grafické plátno a naváže metodu klik a smazat plochu

2) metoda klik(), událost navázaná na levý klik myši,
    která v místě kliknutí do plochy nakreslí kolečko
    vyplněné náhodnou barvou

3) metoda smazat_plochu(),  událost navázaná na pravý klik myši,
    která smaže obsah plochy
''')
input('zmáčkni [enter] pro zpuštění programu')


#import modulů:
import tkinter
import random


#definice třídy:
class Klikanie:
    canvas = tkinter.Canvas(height=300, width=300)
    canvas.pack()

    def __init__(self):
        self.canvas.bind('<ButtonPress-1>', self.klik)
        self.canvas.bind('<ButtonPress-3>', self.smazat_plochu)

    def klik(self, event):
        self.x = event.x
        self.y = event.y
        self.r = 5
        self.barva = f'#{random.randrange(256**3):06x}'
        x, y, r, b = self.x, self.y, self.r, self.barva
        self.canvas.create_oval(x-r, y-r, x+r, y+r, fill=b)

    def smazat_plochu(self, event):
        self.canvas.delete('all')


#aktivace programu:
k = Klikanie()


#aktivace grafické aplikace:
tkinter.mainloop()
