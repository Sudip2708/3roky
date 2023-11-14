##  Napíš funkciu body_na_kruznici(meno_suboru, n, r, x, y),
##  ktorá vygeneruje súbor s daným menom. Tento bude obsahovať n+1 riadkov,
##  pričom v každom budú súradnice nejakého bodu ako dvojica celých čísel oddelená medzerou.
##  Súbor bude obsahovať body pravidelného n-uholníka,
##  ktoré sú rozložené na kružnici s polomerom r a so stredom v (x, y).
##  Zrejme prvý a posledný (n+1) bod budú rovnaké, aby sa pri kreslení tento n-uholník uzavrel.
##
##  Takto vytvorený súbor by sa mohol využiť vo funkcii kresli z (10) úlohy, napríklad:
##    >>> body_na_kruznici('body4.txt', 20, 120, 250, 130)
##    >>> kresli('body4.txt')
##  nakreslí takýto 20-uholník:
## 
##  to isté pre trojuholník:


#úvodní a prázdný řádek:
print('SOUŘADNICE DO TEXTU - PRAVIDELNÝ N-ÚHELNÍK')
print('''program obsahuje funkci na vytvoření textového souboru se souřadnicema
a jeho následné přečtení a vykreslení do grafické plochy''')
print("funkce má tyto parametry: název souboru, počet stran, poloměr, osa x, osa y")
print()
print("zadání pro otestování: 07_17.txt, 20, 120, 190, 130")
print()


#vstup:
meno_suboru = input('Zadej název souboru: ')
n = int(input('Zadej počet stran n-úhelníku: '))
r = int(input('Zadej poloměr kružnice n-úhelníku: '))
x = int(input('Zadej osu "x" středu n-úhelníku: '))
y = int(input('Zadej osu "y" středu n-úhelníku: '))


#definice funkce:
def body_na_kruznici(meno_suboru, n, r, x, y):
    soubor = open(meno_suboru, 'w')                                 #vytvoření souboru
    a = 360 / n                                                     #počet stupňů na jeden středový úhel
    uhol = a                                                        #hodnota středového úhlu pro výpočet dašího bodu
    x1 = x + r                                                      #x-ová osa 1. bodu
    y1 = y                                                          #y-ová osa 1. bodu
    for i in range(n+1):                                            #cyklus - dle počtu stran
        soubor.write(f'{x1} {y1}\n')                                #zapsání hodnot
        x2 = int(x + r * round(math.cos(math.radians(uhol)), 4))    #x-ová osa 2. bodu
        y2 = int(y + r * round(math.sin(math.radians(uhol)), 4))    #y-ová osa 2. bodu
        uhol += a                                                   #přípočet k úhlu pro další bod
        x1, y1 = x2, y2                                             #posunutí počátečního bodu
    soubor.close()
    

#definice funkce:
def kresli(meno_suboru):
    soubor = open(meno_suboru)                                      #otevření souboru
    radek = soubor.readline()                                       #načtení prvního řádku
    x1 = int(radek[:radek.find(' ')])                               #přiřazení první hodnoty z řádku do x1
    y1 = int(radek[radek.find(' ')+1:])                             #přiřazení druhé hodnoty z řádku do y1
    canvas.create_oval(x1-2, y1-2, x1+2, y1+2)                      #vytvoření prvního bodu
    while radek:                                                    #cyklus - dokud jsou řádky
        radek = soubor.readline()                                   #načtení řádku
        if radek.find(' ') != -1:                                   #podmínka - pokud řádek obsahuje mezeru
            x2 = int(radek[:radek.find(' ')])                       #přiřazení první hodnoty z řádku do x2
            y2 = int(radek[radek.find(' ')+1:])                     #přiřazení druhé hodnoty z řádku do y2
            canvas.create_line(x1, y1, x2, y2)                      #vytvoření linky
            x1, y1 = x2, y2                                         #prohození x1, y1 a x2, y2
            canvas.create_oval(x1-2, y1-2, x1+2, y1+2)              #vytvoření dalšího bodu
    soubor.close()                                                  #zavření souboru


#import modulů:
import tkinter
import math


#grafické okno:
canvas = tkinter.Canvas()
canvas.pack()


#výstup:
body_na_kruznici(meno_suboru, n, r, x, y)
kresli(meno_suboru)


#aktivace grafické aplikace:
tkinter.mainloop()  
