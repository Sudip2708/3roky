##  Napíš funkciu nahodne_body(meno_suboru, pocet), ktorá vygeneruje súbor s daným menom.
##  Tento bude obsahovať zadaný pocet riadkov,
##  pričom v každom bude náhodná dvojica celých čísel oddelená medzerou.
##  Prvé číslo nech je z intervalu <10, 370> a druhé z intervalu <10, 250>.
##
##  Takto vytvorený súbor by sa mohol využiť vo funkcii kresli z (11) úlohy, napríklad:
##    >>> nahodne_body('body3.txt', 20)
##    >>> kresli('body3.txt')
##  nakreslí a spojí nejakých 20 náhodných bodov, dostaneš niečo podobné:


#úvodní a prázdný řádek:
print('SOUŘADNICE DO TEXTU - NÁHODNÉ BODY')
print('''program obsahuje funkci na vytvoření textového souboru s náhodně vygenerovanými
souřadnicemi, jeho následné přečtení a vykreslení do grafické plochy''')
print("funkce má tyto parametry: název souboru, počet bodů")
print()
print('''název souboru pro otestování: 07_16.txt,
počet bodů je neomezen, ideálně 2 - 2000''')
print()


#vstup:
meno_suboru = input('Zadej název souboru: ')
pocet = int(input('Zadej počet bodů: '))


#definice funkce:
def nahodne_body(meno_suboru, pocet):
    soubor = open(meno_suboru, 'w')                                             #vytvoření souboru
    for i in range(pocet):                                                      #cyklus dle počtu
        soubor.write(f'{random.randint(10, 370)} {random.randint(10, 250)}\n')  #zapsání dvou náhodných souřadnic oddělených mezerou
    soubor.close()                                                              #zavření souboru


#definice funkce:
def kresli(meno_suboru):
    soubor = open(meno_suboru)                                                  #otevření souboru
    radek = soubor.readline()                                                   #načtení prvního řádku
    x1 = int(radek[:radek.find(' ')])                                           #přiřazení první hodnoty z řádku do x1
    y1 = int(radek[radek.find(' ')+1:])                                         #přiřazení druhé hodnoty z řádku do y1
    canvas.create_oval(x1-2, y1-2, x1+2, y1+2)                                  #vytvoření prvního bodu
    while radek:                                                                #cyklus - dokud jsou řádky
        radek = soubor.readline()                                               #načtení řádku
        if radek.find(' ') != -1:                                               #podmínka - pokud řádek obsahuje mezeru
            x2 = int(radek[:radek.find(' ')])                                   #přiřazení první hodnoty z řádku do x2
            y2 = int(radek[radek.find(' ')+1:])                                 #přiřazení druhé hodnoty z řádku do y2
            canvas.create_line(x1, y1, x2, y2)                                  #vytvoření linky
            x1, y1 = x2, y2                                                     #prohození x1, y1 a x2, y2
            canvas.create_oval(x1-2, y1-2, x1+2, y1+2)                          #vytvoření dalšího bodu
    soubor.close()                                                              #zavření souboru


#import modulů:
import tkinter
import random


#grafické okno:
canvas = tkinter.Canvas()
canvas.pack()


#výstup:
nahodne_body(meno_suboru, pocet)
kresli(meno_suboru)


#aktivace grafické aplikace:
tkinter.mainloop()
