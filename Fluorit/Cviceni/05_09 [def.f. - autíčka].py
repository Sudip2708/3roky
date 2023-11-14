##  Do daného programu dopíš dve chýbajúce funkcie
##  koleso a doska
##  tak, aby si dostal daný obrázok.
##
##    import tkinter
##
##    def koleso(...):
##        ...
##
##    def doska(...):
##        ...
##
##    def vozik(x, y):
##        doska(x, y)
##        koleso(x-30, y)
##        koleso(x+30, y)
##
##    def velky_vozik(x, y):
##        doska(x, y, 150, 40, 'green')
##        koleso(x-35, y, 25, 'orange')
##        koleso(x+35, y, 25, 'orange')
##
##    canvas = tkinter.Canvas()
##    canvas.pack()
##
##    vozik(200, 100)
##    velky_vozik(150, 200)
##    vozik(300, 210)
##
##    tkinter.mainloop()


#úvodní a prázdný řádek:
print('AUTÍČKY')
print('funkce na vykreslení autíčka \npouze zobrazení výsledku dle předem daného zadání')
print()


#prázdný řádek a příkaz pro spuštění okna grafické aplikace:
print()
input('[zmáčkni [Enter] pro zobrazení grafické aplikace]')


#moduly:
import tkinter


#definice funkcí:
def koleso(x, y, r=15, barva='blue'):                                           #parametry - osa x, osa x, poloměr, barva
    canvas.create_oval(x-r, y-r, x+r, y+r, fill=barva)                          #vytvoření kruhu

def doska(x, y, sirka=100, vyska=20, barva='red'):                              #parametry - osa x, osa x, šířka, výška, barva
    canvas.create_rectangle(x-(sirka/2), y-vyska, x+(sirka/2), y, fill=barva)   #vytvoření obdelníku

def vozik(x, y):                                                                #parametry - osa x a osa y
    doska(x, y)                                                                 #volání funkce "doska"
    koleso(x-30, y)                                                             #volání funkce "koleso" - změna osy x
    koleso(x+30, y)                                                             #volání funkce "koleso" - změna osy x

def velky_vozik(x, y):                                                          #parametry - osa x a osa y
    doska(x, y, 150, 40, 'green')                                               #volání funkce "doska" - změna šířky, výšky a barvy
    koleso(x-35, y, 25, 'orange')                                               #volání funkce "koleso" - změna osy x, poloměru a barvy
    koleso(x+35, y, 25, 'orange')                                               #volání funkce "koleso" - změna osy x, poloměru a barvy


#vytvoření grafického prostředí:
canvas = tkinter.Canvas()
canvas.pack()


#výpočet:
vozik(200, 100)
velky_vozik(150, 200)
vozik(300, 210)


#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]')    


#aktivace grafické aplikace:
tkinter.mainloop() 


###výpočet bez funkcí (pro pochopení zadání):
##canvas.create_rectangle(200-50, 100-20, 200-50+100, 100, fill='green')
##canvas.create_oval(200-30-15, 100-15, 200-30+15, 100+15, fill='orange')
##canvas.create_oval(200+30-15, 100-15, 200+30+15, 100+15, fill='orange')
##
##canvas.create_rectangle(150-75, 200-40, 150-75+150, 200, fill='green')
##canvas.create_oval(150-35-25, 200-25, 150-35+25, 200+25, fill='orange')
##canvas.create_oval(150+35-25, 200-25, 150+35+25, 200+25, fill='orange')
##
##canvas.create_rectangle(300-50, 210-20, 300-50+100, 210, fill='green')
##canvas.create_oval(300-30-15, 210-15, 300-30+15, 210+15, fill='orange')
##canvas.create_oval(300+30-15, 210-15, 300+30+15, 210+15, fill='orange')
