##  Napíš program, ktorý nakreslí vlajku Slovenska.
##  V súbore sk.png je obrázok štítu so znakom,
##  ktorý umiestniš (jeho stred) posunutý o ´´100´´ a 108
##  od ľavého horného okraja vlajky.
##
##  V premenných:
##    x, y = 30, 30
##    sir, vys = 325, 216
##    modra, cervena = '#0b4ea2', '#ee1c25'
##
##  je momentálna pozícia ľavého horného rohu,
##  šírka a výška, modrá a červená farba.


#úvodní a prázdný řádek:
print('VLAJKA SLOVENSKÉ REPUBLIKY')
print('(pouze zobrazí vlajku slovenské republiky)')
print()


#zobrazení výsledku:
input('Zmáčkni [ENTER] pro zobrazení')                                              #přechod od grafického prostředí


#moduly:
import tkinter


#grafické okno:
canvas = tkinter.Canvas()
canvas.pack()


#promněné:
x = 30                                                                              #x-ová osa levého horního rohu
y = 30                                                                              #y-ová osa levého horního rohu
sir = 325                                                                           #šířka vlajky
vys = 216                                                                           #výška vlajky
b1 = '#0b4ea2'                                                                      #modrá barva
b2 = '#ee1c25'                                                                      #červená barva
obr = tkinter.PhotoImage(file='03_21.png')                                          #načtení obrázku


#výpočet:
canvas.create_rectangle(x, y, x+sir, y+vys,fill='white', width=1)                   #nakreslení horního obdelníku
canvas.create_rectangle(x, y+(vys/3), x+sir, y+(vys/3)*2,fill='#0b4ea2', width=0)   #nakreslení středního obdelníku
canvas.create_rectangle(x, y+(vys/3)*2, x+sir, y+vys,fill='#ee1c25', width=0)       #nakreslení spodního obdelníku
canvas.create_image(x+100, y+108, image=obr)                                        #vložení znaku


#grafické okno:
tkinter.mainloop()                                                                  #aktivace grafické aplikace
