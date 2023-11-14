##Napíš funkciu zvacsi(obr), ktorá z dvojrozmernej tabuľky obr vyrobí novú tak,
##že sa dvojnásobne zväčší: nová tabuľka má dvojnásobný počet riadkov aj stĺpcov
##a každý pôvodný prvok tu teraz bude 4-krát. Funkcia nezmení pôvodnú tabuľku obr.
##Napríklad pre obrázok z (12) úlohy:
##kresli(zvacsi(p), 10)
##nakreslí:
## 
##a potom aj:
##kresli(zvacsi(zvacsi(p)), 5)
##nakreslí:


#úvodní a prázdný řádek:                                                  
print('FUNKCE PRO DVOJNÁSOBNÉ ZVĚTŠENÍ RASTRU')                              
print('''
Program zdvojnásobý tabulku a její obsah tak,
aby vznikl jemnější rastr.
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

Nyní ale volanou příkazem: kresli(zvacsi(zvacsi(chodec)), 7)
>>funkce zvacsi je použita 2x za sebou,
hodnota 7 na konci značí velikost jednoho pole<<
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

def zvacsi(obr):
    novy_obr = []
    for podseznam in obr:
        novy_obr.append([])
        for znak in podseznam:
            novy_obr[-1].append(znak)
            novy_obr[-1].append(znak)
        novy_obr.append(novy_obr[-1])
    return novy_obr
        


canvas = tkinter.Canvas(height=320, width=150)
canvas.pack()

chodec = [[0, 0, 0, None, None], [1, 1, None, None, None], [1, 1, 1, None, 2], [3, None, None, None, 2],
          [3, 3, 2, 2, None], [3, 3, None, None, None], [4, 4, None, None, None], [4, 4, 4, None, None],
          [4, None, 4, 4, None], [2, None, None, 2, None], [2, 2, None, 2, 2]]

kresli(zvacsi(zvacsi(chodec)), 7)


tkinter.mainloop()
