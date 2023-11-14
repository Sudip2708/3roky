##Zadefinuj triedu Turtle1 odvodenú od turtle.
##Turtle, v ktorej bude definova metóda trojuholník.
##Metóda nakreslí rovnostranný trojuholník s danou veľkosťou strany.
##Otestuj, napríklad:
##t = Turtle1()
##for i in range(5):
##    t.trojuholnik(150)
##    t.lt(72)


#úvodní a prázdný řádek:                                                  
print('''TŘÍDA MOJA TURTLE - TROÚHELNÍKY 01

Třída MojaTurtle obsahuje následující metody:

1) inicializační metoda __init__()
    bez povynných parametrů
    metoda přebere funkci __init__ z mateřského objektu
    a nastaví zpomalení vykreslování na hodnotu 0
    
2) metoda trojuholnik(velikost)
    povinný parametr - délka strany
    metoda nakreslí rovnoramenný trojúhelník

Následujícím příkazem:

t = MojaTurtle()
for i in range(5):
    t.trojuholnik(150)
    t.lt(72)

se nakreslí 5 trojúhelníku spojených vrcholem
''')

input('zmáčkni [enter] pro provedení příkazů')


import turtle


class MojaTurtle(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)

    def trojuholnik(self, velikost):
        for i in range(3):
            self.bk(velikost)
            self.rt(120)
        
t = MojaTurtle()
for i in range(5):
    t.trojuholnik(150)
    t.lt(72)
    

print()
input('zmáčkni [enter] pro ukončení programu')
