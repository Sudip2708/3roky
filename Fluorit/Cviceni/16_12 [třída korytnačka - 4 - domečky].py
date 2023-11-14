##Otestuj, ako v tejto novej triede Korytnacka fungujú príklady z prednášky
##(alebo (6) úlohy z cvičení) s kreslením domčeka rôznym typom čiar:
##
##class MojaKor(Korytnacka):
##    def domcek(...):
##        ...
##
##    def fd(...):             # cikcaková čiara alebo náhodná čiara
##        ...
##
##MojaKor().domcek(100)


#úvodní a prázdný řádek:                                                  
print('''TŘÍDA KORITNACKA - 04 - DOMY

Následující program obsahuje 5 tříd.

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
je třída Domecek, která obsahuje následující metody:

1) inicializační metoda __init__()
    nepovinné parametry - hodnota x, y pro počáteční pozici 
    metoda použije inicializaci z třídy Koritnacka
    a nastaví počáteční hodnotu x a y
    
2) metoda domcek(délka_strany)
    povinné parametry - délka_strany
    metoda obsahuje pokyny k nakreslení domečku


Čtvrtou třídou odvozenou z třídy Domecek,
je třída Domecek1, která obsahuje následující metody:

1) inicializační metoda __init__()
    nepovinné parametry - hodnota x, y pro počáteční pozici 
    metoda použije inicializaci z třídy Domecek
    a nastaví počáteční hodnotu x a y
    
2) metoda fd(délka_strany)
    povinné parametry - délka_strany
    metoda mění původní rovnou čáru
    na čáru klikatou


Pátou třídou odvozenou z třídy koritnacka,
je třída Domecek, která obsahuje následující metody:

1) inicializační metoda __init__()
    nepovinné parametry - hodnota x, y pro počáteční pozici 
    metoda použije inicializaci z třídy Domecek
    a nastaví počáteční hodnotu x a y
    
2) metoda fd(délka_strany)
    povinné parametry - délka_strany
    metoda mění původní rovnou čáru
    na trojtou čáru
''')
print('----------------------------------------------------------------------')


import tkinter
import math
import random


class Pero:
    canvas = None
    kreslit = True
    sirka_plochy = 900
    vyska_plochy = 200
    

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


class Domecek(Korytnacka):
    def __init__(self, x=0, y=0):
        super().__init__()
        self.pu()
        self.setpos(x, y)
        self.pd()

    def domcek(self, dlzka):
        for uhol in 90, 90, 90, 30, 120, -60:
            self.fd(dlzka)
            self.rt(uhol)


class Domecek1(Domecek):
    def __init__(self, x=0, y=0):
        super().__init__(x, y)

    def fd(self, dlzka):
        while dlzka >= 5:
            self.lt(60)
            super().fd(5)
            self.rt(120)
            super().fd(5)
            self.lt(60)
            dlzka -= 5
        super().fd(dlzka)



class Domecek2(Domecek):
    def __init__(self, x=0, y=0):
        super().__init__(x, y)

    def fd(self, dlzka):
        super().fd(dlzka)
        self.rt(180 - random.randint(-3, 3))
        super().fd(dlzka)
        self.rt(180 - random.randint(-3, 3))
        super().fd(dlzka)


print('''
Následujícím příkazem:

odstup = 0
for i in range(10):
    velikost_domecku = random.randint(30, 50)
    odstup += velikost_domecku * 2
    trida = random.randrange(3)
    if trida == 0:
        t = Domecek(odstup, 100)
    elif trida == 1:
        t = Domecek1(odstup, 100)
    else:
        t = Domecek2(odstup, 100)
    t.domcek(velikost_domecku)

se nakreslí 10 domečků, s tím, že u každého
je náhodným losem zvoleno, zda bude kreslen
rovnou čárou, nebo klikatou, nebo trojtou.
''')
input('zmáčkni [enter] pro provedení příkazů')
print('----------------------------------------------------------------------')

odstup = 0
for i in range(10):
    velikost_domecku = random.randint(30, 50)
    odstup += velikost_domecku * 2
    trida = random.randrange(3)
    if trida == 0:
        t = Domecek(odstup, 100)
    elif trida == 1:
        t = Domecek1(odstup, 100)
    else:
        t = Domecek2(odstup, 100)
    t.domcek(velikost_domecku)


print()
input('zmáčkni [enter] pro ukončení programu')
