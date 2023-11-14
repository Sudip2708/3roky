##  Napíš funkciu nahodne_farby(n),
##  ktorá vygeneruje a vráti n-prvkový zoznam náhodných farieb.
##  Tento zoznam môžeme poslať do funkcie kresli z predchádzajúcej úlohy.
##  Napríklad:
##    importtkinter
##    importrandom
##    defnahodne_farby(n):
##    ...
##    canvas = tkinter.Canvas()
##    canvas.pack()
##    kresli(9, nahodne_farby(20))
##    tkinter.mainloop()


#úvodní a prázdný řádek:
print('ŘADA BAREVNÝCH TEČEK')
print('''pouze k zobrazení - program obsahuje funkci, která vygeneruje seznam
náhodných barev, který je následně použit v grafickém programu pro
vytvoření řady berevných teček''')
print()


#prázdný řádek a příkaz pro spuštění okna grafické aplikace:
print()
input('[zmáčkni [Enter] pro zobrazení grafické aplikace]')


#definice funkce:
def nahodne_farby(n):
    seznam = []
    for i in range(n):
        seznam.append(f'#{random.randrange(256**3):06x}')
    return seznam

def kresli(r, seznam):
    x = 2*r
    y = 130
    for i in seznam:
        canvas.create_oval(x-r, y-r, x+r, y+r, fill=i)
        x += 2*r 


#import modulů:
import tkinter
import random


#grafické okno:
canvas = tkinter.Canvas()
canvas.pack()


#výpočet:
kresli(9, nahodne_farby(20))


#aktivace grafické aplikace
tkinter.mainloop()  

