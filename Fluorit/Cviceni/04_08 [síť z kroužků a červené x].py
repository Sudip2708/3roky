##  Nasledovný program vykresľuje farebné krúžky v štvorcovej sieti n x n
##  a zafarbuje ich podľa podmienky v príkaze if:
##    import tkinter
##
##    canvas = tkinter.Canvas()
##    canvas.pack()
##
##    n = 13
##    for i in range(n):
##        for j in range(n):
##            x = j * 20 + 100
##            y = i * 20 + 12
##            if i == 5:
##                farba = 'red'
##            else:
##                farba = 'white'
##            canvas.create_oval(x-8, y-8, x+8, y+8, fill=farba)
##
##    tkinter.mainloop()
##
##  A. Zmeň túto podmienku tak, aby sa nakreslil obrázok,
##  v ktorom sa zafarbí stredný rad a stredný stĺpec
##  (v programe nemeň iné príkazy, nepridávaj ďalšie).
##
##  B. Zmeň túto podmienku tak, aby sa nakreslil obrázok,
##  v ktorom sa zafarbia obe uhlopriečky.
##
##  Programy by mali fungovať správne aj pri zmenenom rozmere n.
##  Vyskúšaj napríklad n=10.
#výpočet:


#úvodní a prázdný řádek:
print('SÍŤ Z KROUŽKŮ A ČERVENÉ X')
print('program zobrazí síť z kroužků dle zadaného počtu a vkreslí dovnitř červený kříž')
print()


#vstupní data:
n = int(input('Zadej číslo od 3 do 18-ti: '))                           #vstup počtu řad a sloupců


#moduly:
import tkinter


#grafické okno:
canvas = tkinter.Canvas()
canvas.pack()


###výpočet zadání "A":
##for i in range(n):                                                      #1. cyklus - sloupce
##    for j in range(n):                                                  #2. cyklus - řádky
##        x = j * 20 + 20                                                 #x-ová souřadnice prvního kruhu (vlevo nahoře)
##        y = i * 20 + 20                                                 #y-ová souřadnice prvního kruhu (vlevo nahoře)
##        if n%2 == 0:                                                    #podmínka - která pole mají být kterou barvou když je sudý počet
##            if i == n//2-1 or i == n//2 or j == n//2-1 or j == n//2:  
##                farba = 'red'
##            else:
##                farba = 'white'
##        else:                                                           #podmínka - která pole mají být kterou barvou když je lichý počet
##            if i == n//2 or j == n//2:
##                farba = 'red'
##            else:
##                farba = 'white'
##        canvas.create_oval(x-8, y-8, x+8, y+8, fill=farba)              #vytvoření kolečka


#výpočet zadání "B":
for i in range(n):                                                      #1. cyklus - sloupce
    for j in range(n):                                                  #2. cyklus - řádky
        x = j * 20 + 20                                                 #x-ová souřadnice prvního kruhu (vlevo nahoře)
        y = i * 20 + 20                                                 #y-ová souřadnice prvního kruhu (vlevo nahoře)
        if i == j or j == n-1-i:                                        #podmínka - která pole mají být kterou barvou
            farba = 'red'
        else:
            farba = 'white'
        canvas.create_oval(x-8, y-8, x+8, y+8, fill=farba)              #vytvoření kolečka


#aktivace grafické aplikace
tkinter.mainloop()                                                  
