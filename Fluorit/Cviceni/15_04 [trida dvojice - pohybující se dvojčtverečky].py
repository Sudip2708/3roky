##Okrem triedy Stv z (3) úlohy zadefinuj triedu Dvojica,
##pomocou ktorej sa budú vytvárať dvojice „zlepených“ štvorčekov (inštancií Stv).
##Trieda bude mať tieto matódy:
##o	metóda __init__(x, y, a=20) zadefinuje dva štvorčeky, pričom prvý z nich má stred v (x, y)
##        a druhý je k nemu prilepený sprava (má posunutý x); oba majú veľkosť strán a a náhodné farby
##o	metóda posun(dx, dy) posunie oba štvorčeky o (dx, dy)
##o	metóda vymen() navzájom vymení farby oboch štvorčekov
##Otestuj tak, že najprv vytvoríš 20 dvojíc na náhodných pozíciách s náhodnými veľkosťami z intervalu <20, 50>.
##Potom ich všetky poposúvaj o nejaké (dx, dy) a otestuj aj výmenu farieb v štvorčekoch.


#úvodní a prázdný řádek:                                                  
print('TŘÍDA DVOJICA - POHYBUJÍCÍ SE DVOJČTVEREČKY')                              
print('''
Program obsahuje třídu Stv pro kreslení a pohyb čtverečků v grafické ploše
a třídu Dvojice, pro kreslení dvojčtverečků, které občas mění barvu
''')
input('zmáčkni [enter] pro zpuštění programu')


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
        self.canvas.itemconfig(self.id, fill=farba)
        self.farba = farba

    def pozdrzeni(self):
        '''metoda pozdržení: bez parametrů
metoda zpožďuje vykreslení objektů v grafické ploše'''
        self.canvas.after(10)
        self.canvas.update()

#definice třídy:
class Dvojica:
    seznam = []
    
    def __init__(self, x, y, a=20):
        '''inicializace:
povinné parametry: osa x, osa y, strana a
metoda v grafické ploše vytvoří dle zadaných parametrů
2 čtverce vedle sebe, a každému přiřadí náhodnou barvu'''
        self.x1 = x
        self.y = y
        self.barva1 = f'#{random.randrange(256**3):06x}'
        self.x2 = x + a
        self.barva2 = f'#{random.randrange(256**3):06x}'
        self.a = a
        self.ctverec1 = Stv(self.x1, self.y, a, self.barva1)
        self.ctverec2 = Stv(self.x2, self.y, a, self.barva2)
        Dvojica.seznam.append(self)

    def posun(self, dx, dy):
        '''metoda posun:
povinné parametry: hodnota posunu osy x a y
metoda posune čtverce o zadané hodnoty'''
        if self.x2 + dx > 280 or self.x1 + dx < 20:
            dx = dx * -1
        if self.y + dy > 280 or self.y + dy < 20:
            dy = dy * -1
        self.ctverec1.posun(dx, dy)
        self.ctverec2.posun(dx, dy)
        self.x1 += dx
        self.x2 += dx
        self.y += dy

    def vymen(self):
        '''metoda vyměň: bez parametrů
metoda prohodí barvu sousedících čtverců'''
        self.ctverec1.zmen_farbu(self.barva2)
        self.ctverec2.zmen_farbu(self.barva1)
        self.barva1, self.barva2 = self.barva2, self.barva1


#cyklus pro vytvoření čtverců:
for i in range(20):
    x = random.randint(50, 250)
    y = random.randint(50, 250)
    a = random.randint(20, 50)
    Dvojica(x, y, a)

#cyklus pro pohyb a změnu barvy:
while True:
    idx = random.randrange(len(Dvojica.seznam))
    objekt = Dvojica.seznam[idx]
    dx = random.randint(-20, 20)
    dy = random.randint(-20, 20)
    objekt.posun(dx, dy)
    if random.randrange(3) == 2:
        objekt.vymen()
    Stv.canvas.after(100)
    Stv.canvas.update()
    
