##Zadefinuj Turtle2 odvodenú od Turtle1 z úlohy (7),
##v ktorej predefinuješ metódu trojuholnik.
##Táto nová verzia metódy najprv nastaví náhodnú farbu výplne
##(self.fillcolor(...)), naštartuje vypĺňanie (self.begin_fill()),
##zavolá metódu trojuholník z rodičovskej triedy (super triedy)
##a ukončí vypĺňanie (self.end_fill()).
##
##Otestuj, napríklad:
##t = Turtle2()
##for i in range(5):
##    t.trojuholnik(150)
##    t.lt(72)
##
##Teraz v triede Turtle1 oprav metódu trojuholník tak,
##aby namiesto otáčania napríklad self.rt(120)
##bola trojica príkazov self.rt(60), self.fd(10), self.rt(60)
##a znovu otestuj:
##t = Turtle2()
##for i in range(5):
##    t.trojuholnik(150)
##    t.lt(72)


#úvodní a prázdný řádek:                                                  
print('''TŘÍDA MOJA TURTLE - TROÚHELNÍKY 02

Následující program obsahuje 2 třídy:
Základní třídu MojaTurtle obsahující následující metody:

1) inicializační metoda __init__()
    bez povynných parametrů
    metoda přebere funkci __init__ z mateřského objektu
    a nastaví zpomalení vykreslování na hodnotu 0
    
2) metoda trojuholnik(velikost)
    povinný parametr - délka strany
    metoda nakreslí rovnoramenný trojúhelník
    s malým trojůhelníkem v každém jeho vrcholu

Dále obsahuje odvozenou třídu MojaTurtle1,
která přebýrá __init__ ze základní třídy
a definici kreslení trojúhelníku rozšiřuje
o volbu náhodné barvy

Následujícím příkazem:

t = MojaTurtle1()
for i in range(5):
    t.trojuholnik(150)
    t.lt(72)

se nakreslí 5 různobarevných trojúhelníku
spojených vrcholem
''')

input('zmáčkni [enter] pro provedení příkazů')


import turtle
import random


class MojaTurtle(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)

    def trojuholnik(self, velikost):
        for i in range(3):
            self.bk(velikost)
            #self.rt(120)
            self.rt(60)
            self.fd(10)
            self.rt(60)

class MojaTurtle1(MojaTurtle):
    def __init__(self):
        super().__init__()

    def trojuholnik(self, velikost):
        barva = f'#{random.randrange(256**3):06x}'
        self.fillcolor(barva)
        self.begin_fill()
        super().trojuholnik(velikost)
        self.end_fill()
    
        
t = MojaTurtle1()
for i in range(5):
    t.trojuholnik(150)
    t.lt(72)
    

print()
input('zmáčkni [enter] pro ukončení programu')
