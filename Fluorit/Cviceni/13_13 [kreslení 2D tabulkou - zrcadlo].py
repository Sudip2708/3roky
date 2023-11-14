##Napíš funkciu zrkadlo(obr), ktorá z dvojrozmernej tabuľky obr vyrobí novú tak,
##že každému riadku pridá None a zrkadlový obsah riadka.
##Napríklad pre obrázok z (12) úlohy:
##kresli(zrkadlo(p))
##nakreslí:
## 
##a potom aj:
##kresli(zrkadlo(zrkadlo(p)), 15)
##nakreslí:


#úvodní a prázdný řádek:                                                  
print('FUNKCE ZRCADLO')                              
print('''
Program vytvoří v 2D tabulce zrcadlový opis každého řádku
a po té, ho přidá na konce řádku.
''')


input('''
Zmáčkni [enter] pro zobrazení výsledku kresby 2D tabulky:

chodec = [
[0, 0, 0, None, None],
[1, 1, None, None, None],
[1, 1, 1, None, 2],
[3, None, None, None, 2],
[3, 3, 2, 2, None],
[3, 3, None, None, None],
[4, 4, None, None, None],
[4, 4, 4, None, None],
[4, None, 4, 4, None],
[2, None, None, 2, None],
[2, 2, None, 2, 2]
]

Nyní ale volanou příkazem: kresli(zrkadlo(zrkadlo(chodec)))
>>funkce zrcadlo je použita 2x za sebou<<
''')


import tkinter

def kresli(tab, d=30, farby=('black', 'yellow', 'orange', 'blue', 'red', 'white')):
    canvas.delete('all')
    for r, riadok in enumerate(tab):
        for s, prvok in enumerate(riadok):
            x, y = s*d + 5, r*d + 5
            if prvok != None:
                fb = farby[prvok]
                lg = 'light gray'
                canvas.create_rectangle(x, y, x+d, y+d, fill=fb, outline=lg)
    canvas.update()

def zrkadlo(obr):
    novy_obr = []
    for ix, podseznam in enumerate(obr):
        nova_verze = podseznam + [None] + podseznam[::-1]
        novy_obr.append(nova_verze)
    return novy_obr
        


canvas = tkinter.Canvas(height=340, width=700)
canvas.pack()

chodec = [[0, 0, 0, None, None], [1, 1, None, None, None], [1, 1, 1, None, 2], [3, None, None, None, 2],
          [3, 3, 2, 2, None], [3, 3, None, None, None], [4, 4, None, None, None], [4, 4, 4, None, None],
          [4, None, 4, 4, None], [2, None, None, 2, None], [2, 2, None, 2, 2]]

kresli(zrkadlo(zrkadlo(chodec)))


tkinter.mainloop()
