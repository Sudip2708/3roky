##Zadefinuj triedu MojaGrafika s týmito metódami:
##o	metóda __init__() vytvorí grafickú plochu veľkosti 400x300 (atribút self.canvas)
##o	metóda kruh(r, x, y, farba=None) nakreslí kruh s polomerom r so stredom (x, y)
##        s danou výplňou (None označuje náhodnú farbu)
##o	metóda stvorec(a, x, y, farba=None) nakreslí štvorec so stranou a so stredom (x, y)
##        s danou výplňou (None označuje náhodnú farbu)
##o	metóda text(text, x, y, farba=None) vypíše daný text na súradnice (x, y)
##        s danou farbou (None označuje náhodnú farbu)
##o	metóda zapis(meno_suboru) zapíše všetky nakreslené útvary do textového súboru:
##        každý do samostatného riadka v tvare,
##        napríklad kruh 40 100 150 red alebo text Python 100 50 #12ff3a, …
##o	metóda citaj(meno_suboru) zruší všetky nakreslené objekty
##        (self.canvas.delete('all')), prečíta súbor a nakreslí všetky v ňom zapísané útvary
##Napríklad:
##    g = MojaGrafika()
##    g.stvorec(280, 200, 150, 'yellow')
##    for x in range(20, 400, 40):
##        g.kruh(20, x, 100)               # náhodné farby
##    g.text('Python', 200, 150, 'red')
##    g.zapis('grafika.txt')               # vytvorí súbor
##    g = MojaGrafika()
##    g.citaj('grafika.txt')               # znovu ho prečíta a vykreslí


#úvodní a prázdný řádek:                                                  
print('TŘÍDA MOJE GRAFIKA')                              
print('''
Třída MojaGrafika obsahuje následující funkce:

1) inicializační funkce __init__(),
    která vytvoří seznam pro objekty,
    případně vyprázní stávající

2) metoda kruh(r, x, y, farba=None),
    která vytvoří kruh dle zadaných parametrů
    a do seznamu objektů zapíše jeho údaje

3) metoda stvorec(a, x, y, farba=None),
    která vytvoří čtverec dle zadaných parametrů
    a do seznamu objektů zapíše jeho údaje

4) metoda text(text, x, y, farba=None),
    která vytvoří text dle zadaných parametrů
    a do seznamu objektů zapíše jeho údaje

5) metoda zapis(meno_suboru),
    vytvoří textový soubor dle zadaného jména
    a zapíše do něj obsah seznamu objeků

6) metoda citaj(meno_suboru),
    otevře textový soubor dle zadaného jména
    postupně volá a vykreslí všechny objekty
    a po té soubor zavře
''')

import tkinter
import random

#definice třídy:
class MojaGrafika:
    canvas = tkinter.Canvas(width=400, height=300)
    canvas.pack()

    def __init__(self):
        self.canvas.delete('all')
        self.canvas.update()
        self.seznam_objektu = []
        print('>>>Byla vyčištěna grafická plocha')
        print('a smazán seznam objektů<<<')
        print()

    def kruh(self, r, x, y, farba=None):
        if farba==None:
            farba = f'#{random.randrange(256**3):06x}'
        self.canvas.create_oval(x-r, y-r, x+r, y+r, fill=farba)
        self.canvas.update() 
        self.seznam_objektu.append(f'kruh {r} {x} {y} {farba}')
        print('>>>Byl vytvořen kruh s parametry:')
        print(f'r-{r} x-{x} y-{y} barva-{farba}')
        print('a přidán do seznamu objektů<<<')
        print()

    def stvorec(self, a, x, y, farba=None):
        r = a/2
        if farba==None:
            farba = f'#{random.randrange(256**3):06x}'
        self.canvas.create_rectangle(x-r, y-r, x+r, y+r, fill=farba)
        self.canvas.update()
        self.seznam_objektu.append(f'stvorec {a} {x} {y} {farba}')
        print('>>>Byl vytvořen čtverec s parametry:')
        print(f'strana-{a} x-{x} y-{y} barva-{farba}')
        print('a přidán do seznamu objektů<<<')
        print()

    def text(self, text, x, y, farba=None):
        if farba==None:
            farba = f'#{random.randrange(256**3):06x}'
        font = 'Arial 40'
        self.canvas.create_text(x, y, text=text, fill=farba, font=font)
        self.canvas.update()
        self.seznam_objektu.append(f'text {text} {x} {y} {farba}')
        print('>>>Byl vytvořen text s parametry:')
        print(f'text-{text} x-{x} y-{y} barva-{farba}')
        print('a přidán do seznamu objektů<<<')
        print()

    def zapis(self, meno_suboru):
        soubor = open(meno_suboru, 'w')
        for polozka in self.seznam_objektu:
            soubor.write(polozka + '\n')
        soubor.close()
        print(f'>>>Byl vytvořen textový soubor {meno_suboru}')
        print('který obsahuje údaje ke všem objektům <<<')
        print()
            
    def citaj(self, meno_suboru):
        print(f'>>>Byl načten textový soubor {meno_suboru}')
        print('a vytvořeny následující objekty <<<')
        print()
        soubor = open(meno_suboru, 'r')
        r = radek = soubor.readline().split()
        while len(r) > 0:
            if radek[0] == 'kruh':
                self.kruh(int(r[1]), int(r[2]), int(r[3]), r[4])
            elif radek[0] == 'stvorec':
                self.stvorec(int(r[1]), int(r[2]), int(r[3]), r[4])
            elif radek[0] == 'text':
                self.text(r[1], int(r[2]), int(r[3]), r[4])
            r = radek = soubor.readline().split()
        soubor.close()
        

print()
input('''Zmáčkni [enter] pro vytvoření instance třídy:
g = MojaGrafika()''')
g = MojaGrafika()

print()
input('''Zmáčkni [enter] pro vytvoření čtverce:
g.stvorec(280, 200, 150, 'yellow')''')
g.stvorec(280, 200, 150, 'yellow')

print()
input('''Zmáčkni [enter] pro vytvoření 20-ti kruhů:
for x in range(20, 400, 40):
    g.kruh(20, x, 100)''')
for x in range(20, 400, 40):
    g.kruh(20, x, 100)

print()
input('''Zmáčkni [enter] pro vytvoření textu:
g.text('Python', 200, 150, 'red')''')
g.text('Python', 200, 150, 'red')

print()
input('''Zmáčkni [enter] pro zápis do souboru:
g.zapis('15_11_grafika.txt') ''')
g.zapis('15_11_grafika.txt') 

print()
input('''Zmáčkni [enter] pro smazání plochy skrze inicializaci:
g = MojaGrafika()''')
g = MojaGrafika()

print()
input('''Zmáčkni [enter] pro načtení a vykreslení
objektů z textového souboru:
g.citaj('15_11_grafika.txt')''')
g.citaj('15_11_grafika.txt')
        
print('pro ukončení programu zavři grafické okno')
tkinter.mainloop()
