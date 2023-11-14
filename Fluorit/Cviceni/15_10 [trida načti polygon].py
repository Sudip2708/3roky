##Zadefinuj triedu CitajPolygon, ktorá vykreslí polygóny uložené v súbore z úlohy (9).
##Zapíš tieto dve metódy:
##o	metóda __init__(meno_suboru) vytvorí grafickú plochu,
##        prečíta súradnice z daného súboru a vykreslí všetky polygóny s čiernym obrysom a bielym vnútrom;
##        zároveň zviaže metódu self.prefarbi s udalosťou kliknutia
##o	metóda prefarbi zmení vnútro (fill) všetkých nakreslených polygónov na náhodné farby
##o	keď bude táto trieda hotová, program naštartuj pomocou:
##        CitajPolygon('poly.txt')    # týmto sa zavolá konštruktor __init__()


#úvodní a prázdný řádek:                                                  
print('TŘÍDA ČÍTAJ POLYGON')                              
print('''
Třída CitajPolygon obsahuje následující funkce:

1) inicializační metoda __init__()
    povynný parametr - jméno textového souboru
    metoda nejhprve vytvoří seznam na id objektů
    po té vytvoří grafickou plochu
    a prováže ji s událostí kliknutí levým tlačítkem myši.
    Dále načte uvedený textový soubor
    a po řádkách z něj vyhreslí všechny polygony

2) metoda prefarbi(),
    je událostí navázanou na klikání levým tlačítkem myši
    a překreslí všechny polygony na náhodnou barvu
''')

input('zmáčkni [entter] pro zobrazení grafické plochy')


import tkinter                                              #import modulu tkinter
import random                                               #import modulu random


class CitajPolygon:                                         #definice třídy CitajPolygon
    def __init__(self, meno_suboru):                            #definice inicializační metody - povinný parametr: jméno textového souboru
        self.seznam_id_objektu = []                                 #vytvoření atributu self.seznam_id_objektu pro seznam 'id' objektu
        
        self.canvas = tkinter.Canvas(height=300, width=300)         #vytvoření atributu self.canvas
        self.canvas.pack()                                          #vytvoření grafického plátna
        self.canvas.bind('<ButtonPress-1>', self.prefarbi)          #provázání kliknutí levým tlačítkem myši s metodou self.prefarbi


        soubor = open(meno_suboru, 'r')                             #otevření souboru pro čtení
        radek = soubor.readline().strip().split(', ')               #načtení prvního řádku bez bílích znaků a rozděleného na jednotlivé souřadnice
        while len(radek) > 1:                                       #cyklus - dokud je počet souřadnic v seznamu řádek větší než jedna
            self.seznam_id_objektu.append(
                self.canvas.create_polygon(
                    radek, fill='white', outline='black'))              #vytvoření polygonu a zapsání jeho id do seznamu
            radek = soubor.readline().strip().split(', ')               #načtení dalšího řádku souřadnic pro další polygon
        soubor.close()                                              #zavření souboru



    def prefarbi(self, event):                                  #definice metody prefarbi
        for id_objektu in self.seznam_id_objektu:                      #cyklus pro každou položku z obsahu 'id' objektů
            barva = f'#{random.randrange(256**3):06x}'                  #generování náhodné barvy
            self.canvas.itemconfig(id_objektu, fill=barva)              #změna barvy


CitajPolygon('15_09_poly.txt')                              #aktivace programu


tkinter.mainloop()                                          #aktivace smyčky grafického okna
