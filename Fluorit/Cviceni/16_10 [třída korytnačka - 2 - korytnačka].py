##Zadefinuj novú triedu Korytnacka,
##ktorá bude odvodená od triedy Pero z úlohy (9):
##    o metóda __init__() vytvorí pero v strede plochy
##    a do nového atribútu uhol nastaví 0
##    (teda otočenie smerom na východ)
##    o metódy lt(uhol) a rt(uhol) zmenšia,
##    resp. zväčšia atribút uhol o zadanú hodnotu,
##    uhly sa budú počítať v stupňoch
##    o metóda fd(dlzka) presunie pero (zavolá metódu setpos())
##    o zadanú dĺžku, ktorá je v momentálnom smere natočenia
##         asi použiješ približne takýto vzorec pre nové x a y:
##        x+dlzka*cos(uhol), y+dlzka*sin(uhol)
##         nezabudni, že sin() a cos() fungujú v radiánoch,
##        pričom atribút uhol pracuje v stupňoch
##    o nepouží modul turtle
##
##Otestuj napríklad takto:
##class Korytnacka(Pero):
##    ...
##
###---- test -------
##
##t = Korytnacka()
##for i in range(1, 200, 2):
##    t.fd(i)
##    t.lt(89)


#úvodní a prázdný řádek:                                                  
print('''TŘÍDA KORITNACKA - 02 - KORITNACKA

Následující program obsahuje 2 třídy.
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

Druhou a odvozenou třídou je koritnacka,
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
        self.uhel += uhel
    
    def rt(self, uhel):
        self.uhel -= uhel
    
    def fd(self, delka):
        cos_uhel = round(math.cos(math.radians(self.uhel)), 3)
        sin_uhel = round(math.sin(math.radians(self.uhel)), 3)
        x = round(self.x + delka * cos_uhel, 3)
        y = round(self.y + delka * sin_uhel, 3)
        self.setpos(x, y)


print('''
Následujícím příkazem:

t = Korytnacka()
for i in range(1, 200, 2):
    t.fd(i)
    t.lt(89)

se nakreslí čtvercová spirála.
''')
input('zmáčkni [enter] pro provedení příkazů')
print('----------------------------------------------------------------------')

t = Korytnacka()
for i in range(1, 200, 2):
    t.fd(i)
    t.lt(89)


print()
input('zmáčkni [enter] pro ukončení programu')
