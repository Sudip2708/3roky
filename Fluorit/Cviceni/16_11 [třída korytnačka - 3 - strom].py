##Z triedy Korytnacka z (10) úlohy odvoď triedu Kor1,
##do ktorej dopíšeš metódu strom(n, d) (napríklad z prednášky).
##Potom otestuj:
##t = Kor1()
##t.pu()
##t.setpos(200, 280)
##t.pd()
##t.lt(90)
##t.strom(5, 100)


#úvodní a prázdný řádek:                                                  
print('''TŘÍDA KORITNACKA - 03 - STROM

Následující program obsahuje 3 třídy.
První a základní třídou je Pero
které obsahuje následující metody:

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

Druhou a odvozenou třídou je Koritnacka,
která obsahuje následující rozšiřující metody:

1) inicializační metoda __init__()
    bez aparametrů 
    metoda použije inicializaci ze základní třídy,
    hodnotu atrubutů pro x a y nastaví na střed plochy
    a vytvoří nový atribut pro uhel
    
2) metoda lt(úhel)
    povinný parametr - úhel
    změní hodnotu úhlu pohybu, o daný úhel,
    směrem do leva

3) metoda rt(úhel)
    povinný parametr - úhel
    změní hodnotu úhlu pohybu, o daný úhel,
    směrem do prava

4) metoda fd(délka)
    povinný parametr - délka posunu
    dle hodnoty úhlu pohybu a délky,
    vypočítá novou hodnotu souřadnic x a y
    a s těmito hodnotami volá metodu setpos(x, y)

5) metoda bk(délka)
    povinný parametr - délka posunu
    metoda nejprve otočí úhel posunu o 180 stupňů
    poté zavolá metodu fd(délka) pro přesun
    a nakonec znovu otočí úhel posunu o 180 stupňů,
    tak aby byl natočen původním směrem

Třetí třídou odvozenou z třídy koritnacka,
je třída Strom, která obsahuje následující metody:

1) inicializační metoda __init__()
    bez aparametrů 
    metoda použije inicializaci z třídy Koritnacka
    
2) metoda strom(počet_vnoření, délka_kmenu)
    povinné parametry - počet_vnoření, délka_kmenu
    metoda obsahuje rekurzivní volání
    pro nakreslení binárního stromu
''')
print('----------------------------------------------------------------------')


import tkinter
import math

class Pero:
    canvas = None
    kreslit = True
    sirka_plochy = 400
    vyska_plochy = 300
    

    def __init__(self, x=0, y=0):
        self.x, self.y = x, y
        if self.canvas == None:
            Pero.canvas = tkinter.Canvas(width = self.sirka_plochy,
                                         height = self.vyska_plochy)
            Pero.canvas.pack()

    def pu(self):
        self.kreslit = False

    def pd(self):
        self.kreslit = True

    def setpos(self, x, y):
        if self.kreslit == True:
            id_obj = self.canvas.create_line(self.x, self.y, x, y)
        self.x, self.y = x, y


class Korytnacka(Pero):
    def __init__(self):
        super().__init__()
        self.uhel = 0
        self.x = self.sirka_plochy / 2
        self.y = self.vyska_plochy / 2
    
    def lt(self, uhel):
        self.uhel -= uhel
    
    def rt(self, uhel):
        self.uhel += uhel
    
    def fd(self, delka):
        cos_uhel = round(math.cos(math.radians(self.uhel)), 3)
        sin_uhel = round(math.sin(math.radians(self.uhel)), 3)
        x = round(self.x + delka * cos_uhel, 3)
        y = round(self.y + delka * sin_uhel, 3)
        self.setpos(x, y)

    def bk(self, delka):
        self.uhel += 180
        self.fd(delka)
        self.uhel -= 180
        


class Strom(Korytnacka):
    def __init__(self):
        super().__init__()

    def strom(self, n, d):
        self.fd(d)
        if n > 0:
            self.lt(40)
            self.strom(n-1, d*0.6)
            self.rt(90)
            self.strom(n-1, d*0.7)
            self.lt(50)
        self.bk(d)


print('''
Následujícím příkazem:

t = Strom()
t.pu()
t.setpos(200, 280)
t.pd()
t.lt(90)
t.strom(5, 100)

se nakreslí binární strom.
''')
input('zmáčkni [enter] pro provedení příkazů')
print('----------------------------------------------------------------------')

t = Strom()
t.pu()
t.setpos(200, 280)
t.pd()
t.lt(90)
t.strom(5, 100)


print()
input('zmáčkni [enter] pro ukončení programu')
