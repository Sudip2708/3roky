##  Na prednáške bol program, ktorý z textového súboru čítal súradnice bodov x, y
##  a do grafickej plochy na príslušných miestach kreslil malé krúžky.
##  Zapíš to ako funkciu kresli(meno_suboru), ktorá namiesto kreslenia krúžkov,
##  bude postupne spájať body zo súboru,
##  t.j. najprv sa nakreslí úsečka z prvého bodu do druhého,
##  potom z druhého do tretieho, …
##
##  Napríklad, pre súbor 'body.txt' z prednášky:
##    100 100
##    150 200
##    200 150
##    150 150
##  volanie:
##    >>> kresli('body.txt')
##  nakreslí tieto tri úsečky:


#úvodní a prázdný řádek:
print('SOUŘADNICE Z TEXTU - SPOJENÉ BODY')
print('''program obsahuje funkci na přečtení textového souboru se souřadnicema
a jejich následné vykreslení do grafické plochy''')
print()
print('soubor pro otestování: 07_11.txt')
print()


#vstup:
meno_suboru = input('Zadej název souboru: ')


#definice funkce:
def kresli(meno_suboru):
    soubor = open(meno_suboru)                          #otevření souboru
    radek = soubor.readline()                           #načtení prvního řádku
    x1 = int(radek[:radek.find(' ')])                   #přiřazení první hodnoty z řádku do x1
    y1 = int(radek[radek.find(' ')+1:])                 #přiřazení druhé hodnoty z řádku do y1
    canvas.create_oval(x1-2, y1-2, x1+2, y1+2)          #vytvoření prvního bodu
    while radek:                                        #cyklus - dokud jsou řádky
        radek = soubor.readline()                       #načtení řádku
        if radek.find(' ') != -1:                       #podmínka - pokud řádek obsahuje mezeru
            x2 = int(radek[:radek.find(' ')])           #přiřazení první hodnoty z řádku do x2
            y2 = int(radek[radek.find(' ')+1:])         #přiřazení druhé hodnoty z řádku do y2
            canvas.create_line(x1, y1, x2, y2)          #vytvoření linky
            x1, y1 = x2, y2                             #prohození x1, y1 a x2, y2
            canvas.create_oval(x1-2, y1-2, x1+2, y1+2)  #vytvoření dalšího bodu
    soubor.close()                                      #zavření souboru


#import modulů:
import tkinter


#grafické okno:
canvas = tkinter.Canvas()
canvas.pack()


#výstup:
kresli('07_body.txt')


#aktivace grafické aplikace:
tkinter.mainloop()
