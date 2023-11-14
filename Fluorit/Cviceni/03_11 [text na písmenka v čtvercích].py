##  Program najprv prečíta nejaký text zo vstupu (input)
##  a potom postupne každé písmeno tohto textu zapíše ('arial 26')
##  do jedného farebného štvorca veľkosti 30x30.
##  Tieto štvorce sú umiestnené tesne vedľa seba.
##  Farby štvorcov aj písmen zvoľ náhodne. 


#úvodní a prázdný řádek:
print('TEXT PO JEDNOTLIVÝCH ZNACÍCH V BAREVNÝCH ČTVERCÍCH')
print('(zadaný text rozebere na jednotlivá písmena a ty pak zobrazí v barevných čtvercích)')
print()


#vstupní data:
a = input('Zadej text: ')                                               #vstup textu


#moduly:
import tkinter                                                          #import modulu
import random                                                           #import modulu


#grafické okno:
canvas = tkinter.Canvas()                                               #vytvoření plátna
canvas.pack()                                                           #umístění plátna do aplikace


#promněné:
b = 30                                                                  #velikost strany čtverce
c = len(a)                                                              #zjistí počet znaků v textu
x = 1                                                                   #x-ová souřadnice prvního bodu
y = 90                                                                  #y-ová souřadnice prvního bodu
f = 0                                                                   #posun dalšího čtverce


#výpočet:
for i in (a):                                                           #cyklus
    d = f'#{random.randrange(256**3):06x}'                              #náhodná barva čtverce
    canvas.create_rectangle(x+f, y, x+b+f, y+b, fill=d)                 #nakreslení čtverce
    e = f'#{random.randrange(256**3):06x}'                              #náhodná barva písmene
    canvas.create_text(x+b/2+f, y+b/2, text=i, font='arial 26', fill=e) #výpis písmene
    f += b                                                              #přípočet posunu dalšího čtverce 


#grafické okno:
tkinter.mainloop()                                                      #aktivace grafické aplikace
