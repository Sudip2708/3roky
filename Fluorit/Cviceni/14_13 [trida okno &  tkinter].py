##Zadefinuj triedu Okno, ktorá otvorí grafické okno a do stredu vypíše zadaný text.
##Výška otvoreného okna nech je 100. Vypísaný text nech je v strede okna fontom veľkosti 50.
##Inicializácia (metóda __init__()) vytvorí nový canvas (výšky 100) a do jeho stredu vypíše zadaný text.
##V svojich atribútoch si zapamätá canvas aj identifikačný kód pre create_text().
##Ďalšie dve metódy menia vypísaný text:
##metóda zmen(text) zmení vypísaný text (zrejme na to použije itemconfig())
##metóda farba(farba) zmení farbu vypísaného textu (zrejme na to použije itemconfig())
##Napríklad:
##import tkinter
##okno = Okno('ahoj')
##okno.farba('red')
##okno.zmen('Python')
##Vyskúšaj vytvoriť dve inštancie Okno.


#úvodní a prázdný řádek:                                                  
print('TŘÍDA OKNO & GRAFICKÁ PLOCHA')                              
print('''
Třída Okno obsahuje následující funkce:

1) inicializační funkce očekávající parametr textu
tato funkce dále vytvoří grafické okno 200/100
ve kterém vykreslí zadaný text fontem Arial 50

2) metoda zmen(text), pro změnu textu

3) metoda farba(barva), pro změnu barvy textu''')


#import modulu tkinter
import tkinter 


#definice třídy Okno
class Okno:
    def __init__(self, text):                                       #definice inicializačního procesu
        self.canvas = tkinter.Canvas(width=200, height=100)             #vytvoření grafické plochy
        self.canvas.pack()                                              #zpuštění správce rozmístění
        self.text = text                                                #atribut text
        self.font = ('Arial', 50)                                       #atrubut font
        self.cislo = self.canvas.create_text(
                    100, 50, text=self.text, font=self.font)            #atribut čísla objektu + vytvoř objekt

    def zmen(self, text):                                           #definice metody zmen
        self.text = text                                                #atribut text
        self.canvas.itemconfig(self.cislo, text=self.text)              #změň text objektu
        self.canvas.update()                                            #obnov grafickou plochu

    def farba(self, barva):                                         #definice metody farba
        self.barva = barva                                              #atribut barva
        self.canvas.itemconfig(self.cislo, fill=self.barva)             #změň barvu textu
        self.canvas.update()                                            #obnov grafickou plochu


print()
input("""zmáčkni [enter] pro zadání příkazu: okno = Okno('ahoj')
které vytvoří grafickou plochu s textem 'ahoj'""")
okno = Okno('ahoj')
print()
input("""zmáčkni [enter] pro zadání příkazu: okno.farba('red')
které změní barvu textu na červenou""")
okno.farba('red')
print()
input("""zmáčkni [enter] pro zadání příkazu: okno.zmen('Python')
které změní text 'ahoj' na 'python'""")
okno.zmen('Python')
print()
input("""zmáčkni [enter] pro ukončení programu""")
