##  Napíš program, ktorý nakreslí farebnú šachovnicu.
##  Program si najprv pomocou dvoch input vypýta počet stĺpcov a počet riadkov.
##
##  V premenných:
##    vel = 30
##    farba1, farba2 = 'maroon', 'gold'
##
##  má nastavenú veľkosť štvorčeka a dve farby,
##  ktoré sa majú na šachovnici striedať.
##  Medzi nakreslenými štvorčekmi je ešte medzera veľkosti 3.


#úvodní a prázdný řádek:
print('ŠACHOVNICE')
print('(dle zadaného počtu řádků a sloupců zobrazí šachovnici kde se střídají 2 barvy)')
print()


#vstupní data:
a = int(input('Zadej počet řádků: '))                               #zadání počtu řádků
b = int(input('Zadej počet sloupců: '))                             #zadání počtu sloupců


#moduly:
import tkinter


#grafické okno:
canvas = tkinter.Canvas()
canvas.pack()


#promněné:
c = 3                                                               #mezera
d = 10                                                              #odsazení
e = 30                                                              #velikost strany čtverce
f1, f2 =  'maroon', 'gold'                                          #barvy
g = 0                                                               #počítadlo přírůstku odsazení čtvrců v řádcích
h = 0                                                               #počítadlo přírůstku odsazení řádků


#výpočet:
for i in range(a):
    for j in range(b):
        canvas.create_rectangle(d+g, d+h, d+e+g, d+e+h, fill=f1)    #vytvoření čtverce
        f1, f2 = f2, f1                                             #prohození barev
        g += e + c                                                  #přípočet odsazení vodorovně
    h += e + c                                                      #přípočet odsazení svisle
    g = 0                                                           #vynulování odsazení čtverců v řadě
    if b % 2 == 0:                                                  #kontrola zda je lichý nebo sudý počet sloupců
        f1, f2 = f2, f1                                             #prohození barev


#grafické okno:
tkinter.mainloop()                                                  #aktivace grafické aplikace
