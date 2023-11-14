##  Napíš program, ktorý nakreslí vlajky týchto štátov:
##  Nemecko, Taliansko, Francúzsko a Rusko.
##  Všetky nech majú rozmery 135 x 90.


#úvodní a prázdný řádek:
print('ČTYŘI VLAJKY')
print('(pouze zobrazí 4 vlajky - německo, itálie, francouzko, rusko)')
print()


#zobrazení výsledku:
input('Zmáčkni [ENTER] pro zobrazení')          #přechod od grafického prostředí


#moduly:
import tkinter                                  #import modulu


#grafické okno:
canvas = tkinter.Canvas()                       #vytvoření plátna
canvas.pack()                                   #umístění plátna do aplikace


#promněné:
a = 30                                          #odsazení od hran okna a mezi vlajkama
c = 135                                         #délka vlajky
d = 90                                          #výška vlajky


#výpočet německo:
canvas.create_rectangle(a, a, a+c, a+d/3,fill='black')
canvas.create_rectangle(a, a+d/3, a+c, a+d/3*2,fill='red')
canvas.create_rectangle(a, a+d/3*2, a+c, a+d,fill='yellow')


#výpočet itálie:
canvas.create_rectangle(a+c+a, a, a+c+a+c/3, a+d,fill='green')
canvas.create_rectangle(a+c+a+c/3, a, a+c+a+c/3*2, a+d,fill='white')
canvas.create_rectangle(a+c+a+c/3*2, a, a+c+a+c, a+d,fill='red')


#výpočet francouzko:
canvas.create_rectangle(a, a+d+a, a+c/3, a+d+a+d,fill='blue')
canvas.create_rectangle(a+c/3, a+d+a, a+c/3*2, a+d+a+d,fill='white')
canvas.create_rectangle(a+c/3*2, a+d+a, a+c, a+d+a+d,fill='red')

    
#výpočet rusko:
canvas.create_rectangle(a+c+a, a+d+a, a+c+a+c, a+d+a+d/3,fill='white')
canvas.create_rectangle(a+c+a, a+d+a+d/3, a+c+a+c, a+d+a+d/3*2,fill='blue')
canvas.create_rectangle(a+c+a, a+d+a+d/3*2, a+c+a+c, a+d+a+d,fill='red')


#grafické okno:
tkinter.mainloop()                              #aktivace grafické aplikace
