##  Napíš funkciu kresli_text(zoznam),
##  v ktorej parameter zoznam je troj alebo štvor prvkový zoznam.
##  Tento zoznam má na začiatku dve celé čísla (označujú súradnice x a y),
##  tretím prvkom je znakový reťazec.
##  Štvrtým prvkom zoznamu je reťazec, ktorý špecifikuje font.
##  Keď tento prvok chýba, použi 'arial 20'.
##  Funkcia vypíše do grafickej plochy na zadané súradnice daný reťazec
##  s daným fontom.
##  Napríklad:
##    import tkinter
##    def kresli_text(zoznam):
##    ...
##    canvas = tkinter.Canvas()
##    canvas.pack()
##    zoz = [200, 100, 'PYTHON']
##    kresli_text(zoz)
##    kresli_text([200, 150, 'programovanie', 'consolas 35'])
##    kresli_text([200, 60, 'najlepšie je', 'tahoma 15'])
##    tkinter.mainloop()
##  vypíše tri texty: jeden na súradnice (200, 100),
##  druhý na (200, 150) a tretí (200, 60):


#úvodní a prázdný řádek:
print('VYKRESLENÍ TEXTU')
print('''pouze k zobrazení - program obsahuje funkci "kresli", která vykreslí
do grafické plocha text na zadané souřadnice a zadaným fontem.

Následné zobrazení je výsledek pro zadání:

zoz = [200, 100, 'PYTHON']
kresli_text(zoz)
kresli_text([200, 150, 'programovanie', 'consolas 35'])
kresli_text([200, 60, 'najlepšie je', 'tahoma 15'])''')
print()


#prázdný řádek a příkaz pro spuštění okna grafické aplikace:
print()
input('[zmáčkni [Enter] pro zobrazení grafické aplikace]')


#definice funkce:
def kresli_text(seznam):
    'funkce překreslí text do grafické plochy dle parametrů uložených jako seznam'
    x = seznam[0]                                   #proměná pro x - 1. položka ze seznamu
    y = seznam[1]                                   #proměná pro y - 2. položka ze seznamu
    text = seznam[2]                                #proměná pro text - 3. položka ze seznamu
    if len(seznam) > 3:                             #podmínka - když má seznam i 4 položku
        font = seznam[3]                            #použij font ze seznamu
    else:                                           #jinak
        font = 'arial 20'                           #použij tento font
    canvas.create_text(x, y, text=text, font=font)  #vykreslení textu do grafické plochy


#import modulů:
import tkinter


#grafické okno:
canvas = tkinter.Canvas()
canvas.pack()


#výpočet
zoz = [200, 100, 'PYTHON']
kresli_text(zoz)
kresli_text([200, 150, 'programovanie', 'consolas 35'])
kresli_text([200, 60, 'najlepšie je', 'tahoma 15'])


#aktivace grafické aplikace
tkinter.mainloop()  

