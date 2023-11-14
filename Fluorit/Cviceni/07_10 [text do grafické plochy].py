##  Vypíš obsah textového súboru do grafickej plochy.
##  Súbor obsahuje niekoľko riadkov a funkcia vypis_subor(meno_suboru)
##  tieto riadky vypíše pod sebou nejakým fontom.
##  V globálnej premennej canvas je referencia na grafickú plochu.
##
##  Napríklad:
##    >>> vypis_subor('text3.txt')
##  vypíše do grafickej plochy:
## 
##  Pre zarovnanie vypisovaného textu pomocou create_text nie na stred
##  ale na ľavý okraj môžeš použiť ďalší pomenovaný parameter anchor='nw',
##  potom by si mal dostať takýto výpis:


#úvodní a prázdný řádek:
print('TEXT DO GRAFICKÉ PLOCHY')
print('program přečte a vypíše soubor s textem do grafické plochy')
print()
print('soubor pro otestování: 07_10.txt')
print()


#vstup:
meno_suboru = input('Zapiš název souboru: ')


#definice funkce:
def vypis_subor(meno_suboru):
    soubor = open(meno_suboru)                                  #proměnná pro otevřený soubor
    x = 190                                                     #x-ová osa
    y = 15                                                      #y-ová osa prvního řádku
    for radek in soubor:                                        #cyklus - dokud má soubor řádky
        #canvas.create_text(x, y, text=radek)                   #text na střed
        canvas.create_text(x-150, y, text=radek, anchor='nw')   #text na kraj
        y += 18                                                 #přípočet y-ové osy dalšího řádku
    soubor.close()                                              #zavření souboru


#import modulů:
import tkinter


#grafické okno:
canvas = tkinter.Canvas()
canvas.pack()


#výstup:
vypis_subor(meno_suboru)


#aktivace grafické aplikace:
tkinter.mainloop()

