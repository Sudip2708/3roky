##  Napíš program, ktorý si najprv zo vstupu (input) vypýta n
##  a potom medzi šírku 10 a 380 vykreslí n čo najväčších
##  rovnako veľkých štvorcov (s medzerou 5).
##  Pre dané n teda najprv vypočítaš veľkosť štvorcov tak,
##  aby boli čo najväčšie a zmestili sa do danej šírky.
##  Štvorce vyplň náhodnými farbami. 


#úvodní a prázdný řádek:
print('ZOBRAZENÍ ČTVERCŮ V DANÉM POČTU')
print('(ze zadaného počtu čtverců vypočítá jejich maximální velikost aby se vešli všechny vedle sebe)')
print()


#vstupní data:
a = int(input('Zadej počet: '))                         #vstup počtu


#moduly:
import tkinter                                          #import modulu
import random                                           #import modulu


#grafické okno:
canvas = tkinter.Canvas()                               #vytvoření plátna
canvas.pack()                                           #umístění plátna do aplikace


#promněné:
b1 = 10                                                 #rozmezí "od"
b2 = 380                                                #rozmezí "do"
c = 5                                                   #mezera mezi čtverci
d = (b2 - b1 - a*c) // a                                #velikost strany čtverce (zaokrouhleno celočíselným dělením)
e = 0                                                   #osazení dalšího čtverce


#výpočet:
for i in range(a):
    f = f'#{random.randrange(256**3):06x}'              #náhodná barva
    canvas.create_rectangle(c+e, d, c+d+e, d+d, fill=f) #kreslení čtverce
    e += d + c                                          #přípočet odsazení dalšího čtverce


#grafické okno:
tkinter.mainloop()                                      #aktivace grafické aplikace
