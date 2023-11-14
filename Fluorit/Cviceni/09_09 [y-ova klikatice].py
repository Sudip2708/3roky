##  Napíš funkciu sort_y(zoznam),
##  kde zoznam obsahuje dvojice (typ tuple) celých čísel.
##  Tieto reprezentujú súradnice (x, y) nejakých bodov v rovine.
##  Tento zoznam treba usporiadať od najmenšieho po najväčší,
##  lenže podľa druhých prvkov dvojíc (y-ových súradníc).
##  Uvedom si, že volanie zoznam.sort() by usporiadalo zoznam
##  podľa prvých prvkov dvojíc (x-ových súradníc).
##  Napríklad:	
##    >>> xy = [(100, 30), (200, 10), (300, 20)]	
##    >>> sort_y(xy)	
##    >>> xy	
##        [(200, 10), (300, 20), (100, 30)]	
##    Triediť môžeš takto: najprv v zozname v každej dvojici vymeníš x a y,
##    potom normálne utriediš (napríklad pomocou metódy sort)
##    a nakoniec v takto utriedenom zozname vrátiš všetky dvojice
##    do pôvodného stavu (vymeníš x a y).	
##    Podobne ako v predchádzajúcej úlohe
##    vykresli takto usporiadanú postupnosť vrcholov pomocou create_line:	


#úvodní a prázdný řádek:
print('Y-OVÁ KLIKATICE')
print('''pouze k zobrazení - program obsahuje funkci, která vygeneruje 100 položkový
seznam (x, y) souřadnic, které následně program setřídí dle y-ové pozice
a v grafickém prostředí propojí všechny body linkou.''')
print()


#prázdný řádek a příkaz pro spuštění okna grafické aplikace:
print()
input('[zmáčkni [Enter] pro zobrazení grafické aplikace]')


#definice funkcí:
def nahodne_body(pocet):
    a = []                              #proměnná pro tvořený seznam
    for i in range(pocet):              #cyklus - dle poctu
        x = random.randint(10, 380)     #proměnná pro náhodnou hodnotu x-ové pozice
        y = random.randint(10, 260)     #proměnná pro náhodnou hodnotu y-ové pozice
        a.append((x, y))                #přidání dvojce do seznamu
    return a                            #vrácení seznamu dvojic bodů x a y

def sort_y(zoznam):
    for i, prvek in enumerate(zoznam):  #cyklus - pro každý prvek ze seznamu
        x, y = prvek                    #přiřazení hodnot x a y
        zoznam[i] = (y, x)              #prohození hodnot x a y (y se dostane do popředí)
    zoznam = sorted(zoznam)             #setřídit seznam (dle y)
    for i, prvek in enumerate(zoznam):  #cyklus - pro každý prvek ze seznamu
        x, y = prvek                    #přiřazení hodnot x a y
        zoznam[i] = (y, x)              #prohození hodnot x a y (y se dostane do popředí)
    return zoznam                       #vrácení setříděného seznamu


#import modulů:
import random
import tkinter


#grafické okno:
canvas = tkinter.Canvas()
canvas.pack()


#výpočet:
zoznam = nahodne_body(100)              #volání funkce "náhodné body" a přiřadění výsledku do seznamu
a = sort_y(zoznam)                      #volání funkce "sort y" a přiřadění výsledku do proměnné
b = ''                                  #proměnná pro první bod přímky
for i in a:                             #cyklus - pro každou položku seznamu "a"
    if b != '':                         #podmínka - pokud proměnná "b" je prázdná
        canvas.create_line(b, i)        #vytvoř linky z předešlé hodnoty (proměnná "b") do načtených souřadnic
    b = i                               #přiřaď načtené souřadnice do proměnné "b"


#aktivace grafické aplikace:
tkinter.mainloop()  
