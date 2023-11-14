##  Funkciu kresli() z predchádzajúceho príkladu vylepši takto:
##  ak sa vo vstupnom súbore nachádza prázdny riadok, tento označuje,
##  že za ním nasleduje ďalšia skupina bodov,
##  ktorá ale nie je s predchádzajúcimi bodmi spojená.
##
##  Napríklad, pre súbor 'body1.txt':
##    100 100
##    150 200
##    200 150
##    150 150
##
##    220 50
##    320 50
##    320 150
##    220 150
##    220 50
##
##    50 30
##    150 70
##    80 90
##    50 30
##  nakreslí:


#úvodní a prázdný řádek:
print('SOUŘADNICE Z TEXTU - SPOJENÉ BODY 2')
print('''program obsahuje funkci na přečtení textového souboru se souřadnicema
a jejich následné vykreslení do grafické plochy
(prázdný řádek znamená nový objekt)''')
print()
print('soubor pro otestování: 07_12.txt')
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
        else:                                           #jinak - pokud řádek neobsahuje mezeru
            radek = soubor.readline()                   #načtení dalšího řádku
            if radek.find(' ') != -1:                   #podmínka - pokud řádek obsahuje mezeru
                x3 = int(radek[:radek.find(' ')])       #přiřazení první hodnoty z řádku do x3
                y3 = int(radek[radek.find(' ')+1:])     #přiřazení druhé hodnoty z řádku do y3
                x1, y1 = x3, y3                         #prohození x1, y1 a x2, y2
    soubor.close()                                      #zavření souboru


#import modulů:
import tkinter


#grafické okno:
canvas = tkinter.Canvas()
canvas.pack()


#výstup:
kresli(meno_suboru)


#aktivace grafické aplikace:
tkinter.mainloop()  


