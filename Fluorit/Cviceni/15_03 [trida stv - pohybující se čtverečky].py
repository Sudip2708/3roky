##Zadefinuj triedu Stv, ktorá zabezpečí definovanie farebného štvorčeka v grafickej ploche.
##Trieda bude mať tieto matódy:
##o	metóda __init__(x, y, a=20, farba='') vytvorí v grafickej ploche
##        štvorček so stredom (x, y), so stranou a a s výplňou farba;
##        ak má parameter farba hodnotu prázdny reťazec,
##        tak sa nahradí vygenerovanou náhodnou farbou
##o	metóda posun(dx, dy) posunie objekt o (dx, dy)
##o	metóda zmen_farbu(farba) prefarbí štvorček na zadanú farbu
##Okrem týchto metód definuj aj triedny atribút canvas,
##ktorý bude spoločný pre všetky definované štvorčeky.
##Otestuj napríklad:
##    for i in range(30):
##       Stv(random.randint(50, 300), random.randint(50, 200))
##Otestuj aj posúvanie všetkých štvorčekov metódou posun aj prefarbovanie metódou zmen_farbu


#úvodní a prázdný řádek:                                                  
print('TŘÍDA STV - POHYBUJÍCÍ SE ČTVEREČKY')                              
print('''
Třída Stv vytvoří v canvasu 100 náhodně rozmístěných
a barevných čtverečků, a po té jimi pohybuje a zároveň jim mění barvu.
Třída Stv obsahuje následující funkce:

1) inicializační funkce __init__()očekávající 3-4 parametry:
povině:
    hodnota osy x (atribut self.x) 
    hodnota osy y (atribut self.y) 
    velikost strany (atribut self.a)
nepovině:
    barva - pokud není uvedena bude vybraná náhodně

2) metoda posun(), která generuje hodnotu posunu

3) metoda zmen_farbu(), která generuje novou barvu

4) metoda pozdrzeni(self), která zpomaluje proces
vykreslování objektú na plochu a aktualizuje plátno
''')

input('''Zmáčkni [enter] pro zpuštění programu
Pro ukončení programu zavři okno canvasu''')

#import modulů:
import tkinter
import random

#definice třídy:
class Stv:
    canvas = tkinter.Canvas(height=300, width=300)
    canvas.pack()
    seznam = []
    
    def __init__(self, x, y, a=20, farba=''):
        '''inicializace:
povinné parametry: osa x, osa y, strana a
nepovinné parametry: barva (při nezadání bude použita náhodná
metoda v grafické ploše vytvoří čtverec dle zadaných parametrů'''
        self.x = x
        self.y = y
        self.a = a
        r = a/2
        if farba == '':
            self.farba = f'#{random.randrange(256**3):06x}'
        else:
            self.farba = farba
        self.id = self.canvas.create_rectangle(
            x-r, y-r, x+r, y+r, fill=self.farba)
        Stv.seznam.append(self)

    def posun(self, dx, dy):
        '''metoda posun:
povinné parametry: hodnota posunu osy x a y
metoda posune objekt o zadané hodnoty'''
        if self.x + dx > 280 or self.x + dx < 20:
            dx = dx * -1
        if self.y + dy > 280 or self.y + dy < 20:
            dy = dy * -1
        self.canvas.move(self.id, dx, dy)
        self.x += dx
        self.y += dy

    def zmen_farbu(self, farba):
        '''metoda změň barvu:
poviné parametry: barva
metoda mění barvu objektu'''
        self.farba = farba
        self.canvas.itemconfig(self.id, fill=farba)

    def pozdrzeni(self):
        '''metoda pozdržení: bez parametrů
metoda zpožďuje vykreslení objektů v grafické ploše'''
        self.canvas.after(10)
        self.canvas.update()

#cyklus pro vytvoření čtverců:
for i in range(100):
   Stv(random.randint(20, 280), random.randint(20, 280))

#cyklus pro pohyb a změnu barvy:
while True:
    delka_seznamu = len(Stv.seznam)
    inx = random.randrange(delka_seznamu)
    self = Stv.seznam[inx]
    dx = random.randint(-20, 20)
    dy = random.randint(-20, 20)
    farba = f'#{random.randrange(256**3):06x}'
    self.posun(dx, dy)
    self.zmen_farbu(farba)
    self.pozdrzeni()
    
