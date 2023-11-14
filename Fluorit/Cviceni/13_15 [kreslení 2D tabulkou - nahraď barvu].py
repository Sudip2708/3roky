##Napíš funkciu nahrad(obr, post),
##ktorá z dvojrozmernej tabuľky obr vyrobí novú tak,
##že zoberie postupnosť dvojíc post,
##každá dvojica obsahuje dve hodnoty (čo nahradiť, čím nahradiť)
##a postupne všetky prvky pôvodnej tabuľky nahradí podľa tohto zoznamu.
##Napríklad pre obrázok z (12) úlohy:
##kresli(nahrad(p, ((3, 4), (4, 0), (None, 5))))
##nakreslí:


#úvodní a prázdný řádek:                                                  
print('FUNKCE NAHRAĎ')                              
print('''
Program projde 2D tabulku a podle zadání změní její hodnoty.
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

Nyní ale volanou příkazem: kresli(nahrad(chodec, ((3, 4), (4, 0), (None, 5))))
>>kde první číslo ntice odkazuje na číslo, které má být nahrazeno
a druhé číslo ntice odkazuje na číslo kterým bude nahrazeno<<
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


def nahrad(obr, post):
    dvojice_1 = []
    dvojice_2 = []
    novy_obr = []

    for dvojce in post:
        dvojice_1.append(dvojce[0])
        dvojice_2.append(dvojce[1])

    for radek in obr:
        novy_obr.append(radek)
        for ix, znak in enumerate(radek):
            if znak in dvojice_1:
                ixx = dvojice_1.index(znak)
                radek[ix] = dvojice_2[ixx]

    return novy_obr
        


canvas = tkinter.Canvas(height=400, width=200)
canvas.pack()

chodec = [[0, 0, 0, None, None], [1, 1, None, None, None], [1, 1, 1, None, 2], [3, None, None, None, 2],
          [3, 3, 2, 2, None], [3, 3, None, None, None], [4, 4, None, None, None], [4, 4, 4, None, None],
          [4, None, 4, 4, None], [2, None, None, 2, None], [2, 2, None, 2, 2]]

kresli(nahrad(chodec, ((3, 4), (4, 0), (None, 5))))


tkinter.mainloop()
