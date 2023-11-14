##  Napíš program, ktorý najprv nakreslí dva štvorce vedľa seba
##  prvý má ľavý horný (x, y), veľkosť 100, druhý je o 10 odsunutý).
##
##  Potom postupne:
##  
##    zafarbí ich tak, že prvý bude červený a druhý modrý (parameter fill='...')
##
##    do stredu prvého vypíšeš text 'červený' a druhého 'modrý'
##
##    písmo oboch textov zväčšíš (napríklad parameter font='arial 20')
##    a zafarbíš na žlto (parameter fill='...')
##
##  Vyskúšaj spustiť aj pre iné hodnoty, napríklad x, y = 120, 10.


#úvodní a prázdný řádek:
print('DVA ČTVERCE VEDLE SEBE')
print('(pouze zobrazí 2 čtverce, kde jeden je modrý a druhý červený)')
print()


#zobrazení výsledku:
input('Zmáčkni [ENTER] pro zobrazení')              #přechod od grafického prostředí


#moduly:
import tkinter                                      #import grafické aplikace (modulu


#grafické okno:
canvas = tkinter.Canvas()                           #vytvoření plátna
canvas.pack()                                       #umístění plátna do aplikace


#promněné:
a = 100                                             #délka hrany čtverců
b = 10                                              #posun mezi čtverci

#výpočet:
x1 = 50                                             #x-ová souřadnice 1. čtverce
y1 = 50                                             #y-ová souřadnice 1. čtverce
x2 = x1 + a + b                                     #x-ová souřadnice 2. čtverce
y2 = y1                                             #y-ová souřadnice 2. čtverce
x3 = x1 + (a/2)                                     #x-ová souřadnice 1. textu
y3 = y1 + (a/2)                                     #y-ová souřadnice 1. textu
x4 = x2 + (a/2)                                     #x-ová souřadnice 1. textu
y4 = y2 + (a/2)                                     #y-ová souřadnice 1. textu

                                                    #vytvoření 1. čtverce:
canvas.create_rectangle(x1, y1, x1+a, y1+a, fill='red')
                                                    #vytvoření 2. čtverce:
canvas.create_rectangle(x2, y2, x2+a, y2+a, fill='blue')
                                                    #vytvoření textu do 1. čtverce:
canvas.create_text(x3, y3, text='červený', font='arial 20', fill='yellow')
                                                    #vytvoření textu do 2. čtverce:
canvas.create_text(x4, y4, text='modrý', font='arial 20', fill='yellow')


#grafické okno:
tkinter.mainloop()                  #aktivace grafické aplikace
