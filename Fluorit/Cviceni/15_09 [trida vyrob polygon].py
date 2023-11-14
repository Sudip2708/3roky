##Zadefinuj triedu VyrobPolygon, ktorá bude fungovať takto:
##o	metóda __init__(meno_suboru) si zapamätá meno súboru a vytvorí prázdny súbor
##        s týmto menom (súbor zatvorí), vytvorí grafickú plochu (self.canvas)
##        a v nej jeden polygón s jediným bodom (0, 0), s čiernym obrysom
##        a bielym vnútrom; zároveň zviaže (bind) dve metódy self.klik
##        a self.enter na udalosti kliknutia a stlačenie klávesu Enter
##        (udalosť '<Return>' zviaž pomocou bind_all);
##        okrem toho vytvorí atribút zoznam s prázdnym obsahom
##o	metóda klik(event) pridá do zoznamu self.zoznam kliknuté súradnice
##        (nie ako dvojicu, ale dve celé čísla za sebou) a pomocou
##        self.canvas.coords(...) zmení vykresľovaný polygón na obsah tohto zoznamu
##o	metóda enter(event) zapíše momentálny obsah zoznamu (súradnice polygónu)
##        na koniec súboru do jedného riadka ako postupnosť celých čísel oddelených medzerou;
##        atribút zoznam potom vyprázdni a ďalšie klikania potom už vytvárajú nový polygón
##        (opätovný Enter zapíše nový polygón ako ďalší riadok súboru)
##o	keď bude táto trieda hotová, program naštartuj pomocou:
##    VyrobPolygon('poly.txt')    # týmto sa zavolá konštruktor __init__()
##o	naklikaj niekoľko polygónov a skontroluj obsah súboru


#úvodní a prázdný řádek:                                                  
print('TŘÍDA VYROB POLYGON')                              
print('''
Třída VyrobPolygon obsahuje následující funkce:

1) inicializační metoda __init__()
    povynný parametr - jméno textového souboru
    metoda nejhprve vytvoří textový soubor s daným jménem
    po té vytvoří grafickou plochu canvasu
    a vytvoří v ní nulový (neviditelný) polygon
    dále ještě vytvoří prázdný seznam pro souřadnice

2) metoda klik(),
    je událostí navázanou na klikání levým tlačítkem myši
    a zaznamenává kliknutí do grafické plocha
    upravuje tím tvar polygonu
    a souřadnice bodu zapisuje do seznamu

3) metoda enter(),
    je událostí navázanou na zmáčknutí klávesy enter
    po jejím zmáčknutí zapíše obsah seznamu
    se souřadnicema polygonu do textového souboru
    seznam následně vymaže a po té i grafickou plochu
''')

input('zmáčkni [entter] pro zobrazení grafické plochy')


import tkinter                                              #import modulu tkinter


class VyrobPolygon:                                         #definice třídy VyrobPolygon
    def __init__(self, meno_suboru):                            #definice inicializační metody - povinný parametr: jméno souboru
        self.meno_suboru = meno_suboru                              #vytvoření atributu self.meno_suboru
        subor = open(self.meno_suboru, 'w')                         #vytvoření textového souboru pro zápis
        subor.close()                                               #zavření textového souboru

        self.canvas = tkinter.Canvas(height=300, width=300)         #vytvoření atributu self.canvas
        self.canvas.pack()                                          #vytvoření grafického plátna
        self.canvas.bind('<ButtonPress-1>', self.klik)              #provázání na kliknutí levým tlačítkem myši
        self.canvas.bind_all('<Return>', self.enter)                #provázání na klávesu enter
        self.id_objektu = self.canvas.create_polygon(
            0, 0, fill='white', outline='black')                    #vytvoření 'nulového' polygonu a atributu self.id_objektu

        self.seznam_souradnic = []                                  #vytvoření atributu self.seznam_souradnic pro seznam souřadic


    def klik(self, event):                                      #definice události klik
        x, y = event.x, event.y                                     #vytvoření lokální proměné x a y z místa kliknutí
        self.seznam_souradnic.extend([x, y])                        #přidání hodnot x a y do seznamu souřadnic

        self.canvas.coords(self.id_objektu, self.seznam_souradnic)  #aktualizace objektu s novou souřadnicí


    def enter(self, event):                                     #definice události enter
        subor = open(self.meno_suboru, 'a')                         #otevření souboru pro přidání textu
        subor.write(str(self.seznam_souradnic)[1:-1] + '\n')        #přidání obsahu seznamu souřadnic
        subor.close()                                               #zavření souboru

        self.seznam_souradnic = []                                  #vyprázdnění obsahu seznamu souřadnic
        self.canvas.delete('all')                                   #vymazání grafické plochy
        self.id_objektu = self.canvas.create_polygon(
            0, 0, fill='white', outline='black')                    #vytvoření nového 'nulového' polygonu a atributu self.id_objektu


x = VyrobPolygon('15_09_poly.txt')                          #aktivace programu


tkinter.mainloop()                                          #aktivace smyčky grafického okna
