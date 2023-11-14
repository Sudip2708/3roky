##Do triedy Klikanie z (5) úlohy pridaj ďalšiu metódu:
##o	metóda vypis vypíše momentálny zoznam všetkých kliknutých bodov (dvojíc čísel),
##napríklad v tvare:
##>>> k.vypis()          # zavolané po troch kliknutých bodoch
##    (162, 129)
##    (231, 51)
##    (273, 199)


#úvodní a prázdný řádek:                                                  
print('TŘÍDA KLIKANIE - BAREVNÉ TEČKY 2')                              
print('''
Třída Klikanie vytvoří grafickou plochu
kde levým kliknutím myšy kreslí malé různo barevné kroužky
a pravým kliknutím myšy maže obsah grafické púlochy
a prostředním tlačítkem myši, vytiskne obsah souřadnic teček.

Obsahuje následující funkce:

1) inicializační funkce __init__() bez parametrů,
    která vytvoří grafické plátno a naváže metodu klik a smazat plochu

2) metoda klik(), událost navázaná na levý klik myši,
    která v místě kliknutí do plochy nakreslí kolečko
    vyplněné náhodnou barvou

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
        self.seznam.append((x, y))

    def smazat_plochu(self, event):
        self.canvas.delete('all')
        self.seznam = []

    def vypis(self, event):
        print()
        if len(self.seznam) > 0:
            for i in self.seznam:
                print(i)
        else:
            print('seznam souřadnic je prázdný')


#aktivace programu:
k = Klikanie()


#aktivace grafické aplikace:
tkinter.mainloop()
