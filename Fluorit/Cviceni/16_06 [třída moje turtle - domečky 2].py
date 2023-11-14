##Vytvor dve odvodené triedy od MojaTurtle (z úlohy (5))
##MojaTurtle1 a MojaTurtle2 (obe budú potomkami MojaTurtle).
##Prvá z nich MojaTurtle1 bude definovať novú verziu metódy fd,
##ktorá kreslí cikcakovú čiaru a druhá MojaTurtle2
##kreslí fd ako tri náhodné čiary vedľa seba (riešenie v prednáške).
##Teraz pooprav 10 domčekov vedľa seba z úlohy (5) tak,
##aby každý z nich bol náhodnej inštancie z
##(MojaTurtle, MojaTurtle1, MojaTurtle2).


#úvodní a prázdný řádek:                                                  
print('''TŘÍDA MOJA TURTLE - DOMEČKY 02

Následující program obsahuje 3 třídy:
Základní třídu MojaTurtle obsahující následující metody:

1) inicializační metoda __init__()
    nepovinné parametry - hodnota x, y pro posun 
    metoda přebere funkci __init__ z mateřského objektu
    nastaví zpomalení vykreslování na hodnotu 0
    a pokud je uvedeno, posune pero dle parametrů
    
2) metoda domcek(délka)
    povinný parametr - délka strany
    metoda nakreslí domeček

Dále obsahuje odvozenou třídu MojaTurtle1,
která přebýrá inicializační metodu od rodiče
a namísto rovné čáry kreslí čáru klikatou.

A po té ještě třídu MojaTurtle2,
která přebýrá inicializační metodu od rodiče
a namísto rovné čáry kreslí čáru trojtou.


Následujícím příkazem:

odstup = -450
for i in range(10):
    velikost_domecku = random.randint(30, 50)
    odstup += velikost_domecku * 2
    trida = random.randrange(3)
    if trida == 0:
        t = MojaTurtle(odstup, 100)
    elif trida == 1:
        t = MojaTurtle1(odstup, 100)
    else:
        t = MojaTurtle2(odstup, 100)
    t.domcek(velikost_domecku)

se nakreslí 10 domečků s odlišnou velikostí
a náhodně zvoleným formátem domečku.
''')
input('zmáčkni [enter] pro provedení příkazů')


import turtle
import random


class MojaTurtle(turtle.Turtle):
    def __init__(self, x=0, y=0):
        super().__init__()
        self.speed(0)
        self.pu()
        self.setpos(x, y)
        self.pd()

    def domcek(self, dlzka):
        for uhol in 90, 90, 90, 30, 120, -60:
            self.fd(dlzka)
            self.rt(uhol)


class MojaTurtle1(MojaTurtle):
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



class MojaTurtle2(MojaTurtle):
    def __init__(self, x=0, y=0):
        super().__init__(x, y)

    def fd(self, dlzka):
        super().fd(dlzka)
        self.rt(180 - random.randint(-3, 3))
        super().fd(dlzka)
        self.rt(180 - random.randint(-3, 3))
        super().fd(dlzka)


odstup = -450

for i in range(10):
    velikost_domecku = random.randint(30, 50)
    odstup += velikost_domecku * 2
    trida = random.randrange(3)
    if trida == 0:
        t = MojaTurtle(odstup, 100)
    elif trida == 1:
        t = MojaTurtle1(odstup, 100)
    else:
        t = MojaTurtle2(odstup, 100)
    t.domcek(velikost_domecku)
    

print()
input('zmáčkni [enter] pro ukončení programu')
    
