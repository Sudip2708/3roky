##Z prednášky uprav funkciu kresli:
##def kresli(tab, d=20, farby=('black', 'yellow', 'orange', 'blue', 'red', 'white')):
##    canvas.delete('all')
##    for r, riadok in enumerate(tab):
##        for s, prvok in enumerate(riadok):
##            x, y = s*d + 5, r*d + 5
##            farba = farby[prvok]
##            canvas.create_rectangle(x, y, x+d, y+d,
##                                    fill=farba, outline='light gray')
##    canvas.update()
##tak, aby sa prvky tabuľky, ktoré majú hodnotu None,
##nekreslili (ostalo po nich prázdne miesto).
##Teraz vytvor dvojrozmernú tabuľku p (všetky riadky majú rovnakú dĺžku 5),
##po vykreslení ktorej dostávaš takýto obrázok:


#úvodní a prázdný řádek:                                                  
print('KRESLENÍ 2D TABULKOU')                              
print('''
Program vykreslí 2D tabulku s čísli
(kde každé číslo reprezentuje určitou barvu)
do čtverečkované plochy vytvořené v canvasu
dle počtu řádků a sloupců.
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
''')

import tkinter

def kresli(tab, d=30, farby=('black', 'yellow', 'orange', 'blue', 'red', 'white')):
    canvas.delete('all')
    for r, riadok in enumerate(tab):
        for s, prvok in enumerate(riadok):
            x, y = s*d + 5, r*d + 5
            if prvok != None:
                farba = farby[prvok]
                canvas.create_rectangle(x, y, x+d, y+d, fill=farba, outline='light gray')
    canvas.update()


canvas = tkinter.Canvas(height=340, width=160)
canvas.pack()



chodec = [[0, 0, 0, None, None], [1, 1, None, None, None], [1, 1, 1, None, 2], [3, None, None, None, 2],
          [3, 3, 2, 2, None], [3, 3, None, None, None], [4, 4, None, None, None], [4, 4, 4, None, None],
          [4, None, 4, 4, None], [2, None, None, 2, None], [2, 2, None, 2, 2]]

kresli(chodec)


tkinter.mainloop()
