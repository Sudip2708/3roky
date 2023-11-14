##  Vytvor program, ktorý podobne, ako v predchádzajúcej úlohe,
##  nakreslí vlajku Českej republiky (bývalého Československa):
##
##  Předcházející úloha:
####  Vlajku Nemecka môžeš do štandardnej veľkosti grafickej plochy nakresliť tak,
####  že pomocou cyklu vygeneruješ 10000 náhodných súradníc x z intervalu <10, 350>
####  a y z intervalu <10, 250>.
####  Na vygenerované súradnice nakreslíš farebnú bodku (kruh s polomerom 5 bez obrysu).
####
####  Farbu bodky zvolíš podľa y-ovej súradnice:
####    ak je y < 90 kresli čierny krúžok,
####    inak, ak je y < 170 kresli červený krúžok,
####    inak nakresli žltý (môže byť 'gold') krúžok.


#úvodní a prázdný řádek:
print('VLAJKA ČESKÉ REPUBLIKY Z TEČEK')
print('program pouze zobrazí vlajku české republiky vyrobenou z puntíků, dle již předem zadaných parametrů')
print()


#prázdný řádek a příkaz pro spuštění okna grafické aplikace:
print()
input('[zmáčkni [Enter] pro zobrazení grafické aplikace]')


#moduly:
import tkinter
import random


#grafické okno:
canvas = tkinter.Canvas()
canvas.pack()


#výpočet:
for i in range(10000):                                              #cyklus
    x = random.randint(10, 350)                                     #x-ová osa tečky
    y = random.randint(10, 250)                                     #y-ová osa tečky
    if x <= y and 260 - y >= x:                                                      #podmínka - když je y-ový osa menší než 90
        barva = 'blue'                                             #použij čenou barvu
    elif y < 130:                                                   #po té, když je y-ová osa menší než 170
        barva = 'white'                                               #použij červenou barvu
    else:                                                           #ve všech ostatních případech
        barva = 'red'                                              #použij žlutou zlatou barvu
    canvas.create_oval(x-5, y-5, x+5, y+5, fill=barva, outline='')  #vytvožení tečky


#grafické okno:
tkinter.mainloop()                                                  #aktivace grafické aplikace
