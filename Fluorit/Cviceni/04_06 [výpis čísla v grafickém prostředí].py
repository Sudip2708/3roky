##  Využi while-cyklus z predchádzajúcej úlohy
##  a vypíš cifry do grafickej plochy (zrejme sprava do ľava).
##  Program jednotlivé cifry vypíše do farebných štvorcov.
##
##  Předchozí úloha:
####  Napíš program, ktorý vypíše cifry zadaného čísla postupným delením desiatimi,
####  teda vo while-cykle vypíšeš poslednú cifru (číslo % 10)
####  a pritom ešte samotné číslo vydelíš 10.
####  Súčasne každú túto cifru pripočítaš do počítadla cs (ciferný súčet).
####
####  Môžeš dostať takýto výstup:
####    zadaj číslo: 4132
####    2
####    3
####    1
####    4
####    ciferný súčet = 10
####
####  Všimni si, že cifry sú vypísané v opačnom poradí ako sú v zadanom čísle.


#úvodní a prázdný řádek:
print('VÝPIS ČÍSLA V GRAFICKÉM PROSTŘEDÍ')
print('program vakreslí zadané číslo v grafickém prostředí')
print()


#vstupní data:
a = int(input('Zadej číslo: '))                                     #vstup - počet


#moduly:
import tkinter


#grafické okno:
canvas = tkinter.Canvas(bg='white')
canvas.pack()


#proměné:
x = 330                                                             #x-ová souřadnice levého horního rohu 1. čísla
y = 130                                                             #y-ová souřadnice levého horního rohu 1. čísla
c = 35                                                              #šířka obdelníku čísla
d = 40                                                              #výška obdelníku čísla
e = 5                                                               #mezera mezi obdelníky


#výpočet:
while a != 0:                                                       #cyklus - dokuď nebude 0
    canvas.create_rectangle(x, y, x+c, y+d, fill='cyan')            #vytvoření obdelníku
    canvas.create_text(x+c/2, y+d/2, text=a%10, font='ariel 32')    #výpis čísla
    a //= 10                                                        #vyděl a deseti
    x -= 40                                                         #posunutí x-ové pozice pro další obdelník


#aktivace grafické aplikace:
tkinter.mainloop()                                                  
