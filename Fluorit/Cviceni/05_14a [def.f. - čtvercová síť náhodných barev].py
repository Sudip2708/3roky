##  Napíš funkciu stv(riadok, stlpec, farba='white'),
##  ktorá nakreslí farebný štvorec do myslenej štvorcovej siete,
##  v ktorej je každé políčko veľké 30x30.
##  Ľavý horný roh najľavejšieho horného štvorca má súradnice (5, 5).
##
##  Napríklad pre volanie:
##    for i in range(8):
##        for j in range(12):
##            if i == j:
##                stv(i, j)
##            else:
##                stv(i, j, nahodna_farba())


#úvodní a prázdný řádek:
print('ČTVERCOVÁ SÍŤ NÁHODNÝCH BAREV')
print('funkce na vykreslení náhodných barev do sítě z čtverců \npouze zobrazení výsledku dle předem daného zadání')
print()


#prázdný řádek a příkaz pro spuštění okna grafické aplikace:
print()
input('[zmáčkni [Enter] pro zobrazení grafické aplikace]')


#moduly:
import tkinter
import random


#definice funkce:
def nahodna_farba():                                                #parametry - žádné
    return f'#{random.randrange(256**3):06x}'                       #vytvoření náhodné barvy

def stv(riadok, stlpec, farba='white'):                             #parametry - řádek, sloupec, barva
    a = 30                                                          #šířka čtverce
    b = 5                                                           #odstup od kraje
    c = riadok                                                      #číslo řádku
    d = stlpec                                                      #číslo sloupce
    e = farba                                                       #barva
    canvas.create_rectangle(a*d+b, a*c+b, a+a*d+b, a+a*c+b, fill=e) #vytvoř čtverec a vyplň barvou

    
#vytvoření grafického prostředí:
canvas = tkinter.Canvas()
canvas.pack()


#výpočet:
for i in range(8):                                                  #cyklus - 8x
    for j in range(12):                                             #podcyklus - 12x
        if i == j:                                                  #když číslo řádku a sloupce jsou stejné
            stv(i, j)                                               #udej pouze číslo řádku a sloupce, barvu nech defaultní
        else:                                                       #ve všech ostatních případech
            stv(i, j, nahodna_farba())                              #udej číslo řádku, sloupce a barvu


#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]')    


#aktivace grafické aplikace:
tkinter.mainloop() 

