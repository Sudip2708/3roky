##  Napíš program, ktorý nakreslí cikcakovú čiaru zloženú z n úsečiek.
##  V premenných:
##    x, y = 10, 100
##    d = 20
##  má nastavené súradnice najľavejšieho bodu prvej úsečky
##  a v d je posunutie pre x aj y každého ďalšieho bodu čiary.
##  Zrejme k y sa to raz pripočíta a raz odpočíta.
##  Napríklad pre n=16 by si mohol dostať:


#úvodní a prázdný řádek:
print('KLIKATÁ ČÁRA')
print('(dle počtu zobrazí modrou klikatou čáru)')
print()


#vstupní data:
a = int(input('Zadej číslo: '))                                 #zdání počtu linek


#moduly:
import tkinter                                                  #import modulu


#grafické okno:
canvas = tkinter.Canvas()                                       #vytvoření plátna
canvas.pack()                                                   #umístění plátna do aplikace


#promněné:
x = 10                                                          #počáteční x-ová osa
y = 100                                                         #počáteční y-ová osa
d = 20                                                          #posun


#výpočet:
for i in range(a):                                              #cyklus
    canvas.create_line(x, y, x+d, y+d, fill='blue', width=5)    #vytvoření linky dolu
    x += d                                                      #změna x
    y += d                                                      #změna y
    canvas.create_line(x, y, x+d, y-d, fill='blue', width=5)    #vytvoření linky nahoru
    x += d                                                      #změna x
    y -= d                                                      #změna y


#grafické okno:
tkinter.mainloop()                                              #aktivace grafické aplikace
