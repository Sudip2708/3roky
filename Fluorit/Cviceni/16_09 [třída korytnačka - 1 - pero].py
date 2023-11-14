##Naprogramuj triedu Pero,
##pomocou ktorej budeme vedieť kresliť do grafickej plochy.
##Trieda má tieto metódy:
##    o __init__(x=0, y=0), ak ešte nebola vytvorená grafická plocha
##    (canvas má hodnotu None), vytvorí ju s danou šírkou a výškou,
##    zapamätá si súradnice pera a stav,
##    že pero je spustené dolu (bude kresliť)
##    o pu() zdvihne pero, odteraz pohyb pera nekreslí
##    o pd() spustí pero, pohyb bude zanechávať čiaru
##    o setpos(x, y) presunie pero na novú pozíciu,
##    ak je pero spustené, zanecháva čiernu čiaru hrúbky 1
##import tkinter
##from math import sin, cos, radians
##
##class Pero:
##    canvas = None
##    sirka, vyska = 400, 300
##
##    def __init__(...):
##        ...
##    ...
##Otestuj vytvorením dvoch inštancií pera,
##ktoré nakreslia napríklad dva štvorce:
##p1 = Pero(100, 200)
##p2 = Pero(200, 150)
##...


#úvodní a prázdný řádek:                                                  
print('''TŘÍDA KORITNACKA - 01 - PERO

Následující program obsahuje základní třídu Pero
která obsahuje následující metody:

1) inicializační metoda __init__()
    nepovinné parametry - hodnota x, y pro počáteční pozici 
    metoda zjistí, zda je vytvořená grafická plocha,
    pokud není, vytvoří ji dle zadaných hodnot.
    Dále vytvoří atributy self.x a self.y,
    a přiřadí jim dané hodnoty.
    
2) metoda pu()
    bez aparametrů
    metoda nastaví atribut kreslit na hodnotu False

3) metoda pd()
    bez aparametrů
    metoda nastaví atribut kreslit na hodnotu True

4) metoda setpos(x, y)
    povinné parametry - hodnota souřadnic x a y
    metoda přesune pero (nastaví nové souřadnice)
    a pokud má atribut kreslit hodnotu True,
    nakreslí z původního bodu do nového bodu čáru.

5) metoda ctverec(strana)
    povinný parametr - délka strany
    metoda nakreslí čtverec
''')
print('----------------------------------------------------------------------')


import tkinter

class Pero:
    canvas = None
    kreslit = True


    def __init__(self, x=0, y=0):
        self.x, self.y = x, y
        if self.canvas == None:
            Pero.canvas = tkinter.Canvas(width=400, height=300)
            Pero.canvas.pack()
            

    def pu(self):
        self.kreslit = False


    def pd(self):
        self.kreslit = True


    def setpos(self, x, y):
        if self.kreslit == True:
            id_obj = self.canvas.create_line(self.x, self.y, x, y)
        self.x, self.y = x, y


    def ctverec(self, strana):
        x, y, s = self.x, self.y, strana
        for i in ((x, y), (x+s, y), (x+s, y+s), (x, y+s), (x, y)):
            self.setpos(i[0], i[1])


print('''
Následujícím příkazem:

p1 = Pero(125, 75)
p1.ctverec(150)
p1.pu()
p1.setpos(150, 100)
p1.pd()
p1.ctverec(100)
p1.pu()
p1.setpos(175, 125)
p1.pd()
p1.ctverec(50)

se nakreslí 3 čtverce uvnitř sebe.
''')
input('zmáčkni [enter] pro provedení příkazů')
print('----------------------------------------------------------------------')

p1 = Pero(125, 75)
p1.ctverec(150)
p1.pu()
p1.setpos(150, 100)
p1.pd()
p1.ctverec(100)
p1.pu()
p1.setpos(175, 125)
p1.pd()
p1.ctverec(50)


print('''
A následujícím příkazem:

p2 = Pero(195, 145)
p2.ctverec(10)

se dokreslí novým perem (novou instancí)
do středu čtverců ještě jeden malý čtvereček.
''')
input('zmáčkni [enter] pro provedení příkazů')
print('----------------------------------------------------------------------')

p2 = Pero(195, 145)
p2.ctverec(10)


print()
input('zmáčkni [enter] pro ukončení programu')
