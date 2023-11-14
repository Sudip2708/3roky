##  Napíš funkciu vybodkuj_usecku(x1, y1, x2, y2, n),
##  ktorá nakreslí úsečku z bodu (x1, y1) do bodu (x2, y2).
##  Túto úsečku nekreslí pomocou create_line, ale pomocou n bodiek,
##  t.j. malých modrých kruhov s polomerom 3.
##  Parameter n je minimálne 2 a vtedy sa nakreslia len dve bodky v koncových vrcholoch úsečky.
##  Pre kontrolu najprv vykreslíme originálnu úsečku šedou farbou.
##
##  Otestuj, napríklad:
##    canvas.create_line(100, 80, 280, 120, fill='lightgray', width=11)
##    vybodkuj_usecku(100, 80, 280, 120, 20)
##    canvas.create_line(280, 120, 150, 200, fill='lightgray', width=11)
##    vybodkuj_usecku(280, 120, 150, 200, 10)
##    canvas.create_line(150, 200, 100, 80, fill='lightgray', width=11)
##    vybodkuj_usecku(150, 200, 100, 80, 8)


#úvodní a prázdný řádek:
print('ČÁRA Z TEČEK')
print('funkce na kreslení čáry z teček \npouze zobrazení výsledku dle předem daného zadání')
print()


#prázdný řádek a příkaz pro spuštění okna grafické aplikace:
print()
input('[zmáčkni [Enter] pro zobrazení grafické aplikace]')


#moduly:
import tkinter


#definice funkce:
def vybodkuj_usecku(x1, y1, x2, y2, n):                                     #parametry - x,y prvního bodu, x,y druhého bodu, počet bodů - rozdělení úsečky
    for i in range(n):                                                      #cyklus - dle počtu bodů rozdělení úsečky
        if x1 >= x2 and y1 >= y2:                                           #podmínka, když x 1.bodu je větší než x 2.bodu a y 1.bodu je větší než y 2.bodu
            x = ((x1-x2)/(n-1)*i+x2)                                        #výpočet pro x středu tečky
            y = ((y1-y2)/(n-1)*i+y2)                                        #výpočet pro y středu tečky
        elif x1 >= x2 and y1 <= y2:                                         #podmínka, když x 1.bodu je větší než x 2.bodu a y 1.bodu je menší než y 2.bodu
            x = ((x1-x2)/(n-1)*i+x2)                                        #výpočet pro x středu tečky
            y = (y2-(y2-y1)/(n-1)*i)                                        #výpočet pro y středu tečky
        elif x1 <= x2 and y1 <= y2:                                         #podmínka, když x 1.bodu je menší než x 2.bodu a y 1.bodu je menší než y 2.bodu
            x = ((x2-x1)/(n-1)*i+x1)                                        #výpočet pro x středu tečky
            y = ((y2-y1)/(n-1)*i+y1)                                        #výpočet pro y středu tečky
        else:                                                               #ve všech ostatních případech (když x 1.bodu je menší než x 2.bodu a y 1.bodu je větší než y 2.bodu
            x = (x2-(x2-x1)/(n-1)*i)                                        #výpočet pro x středu tečky
            y = ((y1-y2)/(n-1)*i+y2)                                        #výpočet pro y středu tečky
        canvas.create_oval(x+3, y+3, x-3, y-3, fill='blue', outline='')     #vytvožení modré tečky




#vytvoření grafického prostředí:
canvas = tkinter.Canvas()
canvas.pack()


#výpočet:
canvas.create_line(100, 80, 280, 120, fill='lightgray', width=11)
vybodkuj_usecku(100, 80, 280, 120, 20)
canvas.create_line(280, 120, 150, 200, fill='lightgray', width=11)
vybodkuj_usecku(280, 120, 150, 200, 10)
canvas.create_line(150, 200, 100, 80, fill='lightgray', width=11)
vybodkuj_usecku(150, 200, 100, 80, 8)


#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]')    


#aktivace grafické aplikace:
tkinter.mainloop() 

