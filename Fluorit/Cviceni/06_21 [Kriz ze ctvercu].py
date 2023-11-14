##  Na konci prednášky je funkcia kresli(retazec),
##  pomocou ktorej môžeme vytvárať nejakú kresbu zakódovanú písmenami 'svjz'.
##
##  Nakresli pomocou tejto funkcie takýto obrázok:


#úvodní a prázdný řádek:
print('KŘÍŽ ZE ČTVERCŮ')
print('''funkce vytváří obrazce dle následujících instrukcí:

s = +10 na sever
j = +10 na jih
v = +10 na víchod
z = +10 na západ

Napiš z těchto znaků posloupnost, která vytvoří
ze 5 čtverců (o velikosti strany 20) kříř.
Středový čtverec má na každé straně další čtverec.

Nápověda: čtverec o straně 20 má kód: ssvvjjzz ''')
print()


#vstup:
a = input('Zadej celý příkaz (bez mezer): ')


#import modulů:
import tkinter


canvas = tkinter.Canvas()
canvas.pack()


#definice funkce:
def kresli(retazec):
    x, y = 180, 120
    for znak in retazec:
        x1, y1 = x, y
        if znak =='s':
            y1 -=10
        elif znak =='v':
            x1 +=10
        elif znak =='j':
            y1 +=10
        elif znak =='z':
            x1 -=10
        else:
            print(f'{a.find(znak)+1}. znak "{znak}" není platným příkazem.')
        canvas.create_line(x, y, x1, y1)
        x, y = x1, y1

#kresli('ssvvjjzzzzssvvssvvjjvvjjzzjjzzss')
kresli(a)


#aktivace grafické aplikace
tkinter.mainloop()  
