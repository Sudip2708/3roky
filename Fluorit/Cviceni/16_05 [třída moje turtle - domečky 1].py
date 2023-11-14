##Z prednášky skopíruj triedu MojaTurtle,
##v ktorej sa definovali dve metódy __init__(x, y) a domcek(dlzka).
##Teraz vytvor 10 inštancií tejto triedy,
##ktoré budú pravidelne rozostavené na jednej priamke.
##Potom každá z nich nakreslí svoj domček náhodnej veľkosti
##z intervalu <30, 50>.


#úvodní a prázdný řádek:                                                  
print('''TŘÍDA MOJA TURTLE - DOMEČKY 01

Třída MojaTurtle obsahuje následující metody:

1) inicializační metoda __init__()
    nepovinné parametry - hodnota x, y pro posun 
    metoda přebere funkci __init__ z mateřského objektu
    nastaví zpomalení vykreslování na hodnotu 0
    a pokud je uvedeno, posune pero dle parametrů
    
2) metoda fd(délka)
    povinný parametr - délka strany
    metoda každou úsečku projede 3x
    pokaždé s malou náhodnou odchylkou

3) metoda domcek(délka)
    povinný parametr - délka strany
    metoda nakreslí domeček

Následujícím příkazem:

odstup = -450
for i in range(10):
    velikost_domecku = random.randint(30, 50)
    odstup += velikost_domecku * 2
    t = MojaTurtle(odstup, 100)
    t.domcek(velikost_domecku)

se nakreslí 10 domečků s odlišnou velikostí
''')
input('zmáčkni [enter] pro provedení příkazů')


import turtle
import random


#definice třídy:
class MojaTurtle(turtle.Turtle):
    def __init__(self, x=0, y=0):
        super().__init__()
        self.speed(0)
        self.pu()
        self.setpos(x, y)
        self.pd()

    def fd(self, dlzka):
        super().fd(dlzka)
        self.rt(180 - random.randint(-3, 3))
        super().fd(dlzka)
        self.rt(180 - random.randint(-3, 3))
        super().fd(dlzka)

    def domcek(self, dlzka):
        for uhol in 90, 90, 90, 30, 120, -60:
            self.fd(dlzka)
            self.rt(uhol)


odstup = -450
for i in range(10):
    velikost_domecku = random.randint(30, 50)
    odstup += velikost_domecku * 2
    t = MojaTurtle(odstup, 100)
    t.domcek(velikost_domecku)
    

print()
input('zmáčkni [enter] pro ukončení programu')
