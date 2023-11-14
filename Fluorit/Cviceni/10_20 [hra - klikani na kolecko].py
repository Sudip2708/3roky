##  Naprogramuj takúto hru na postreh:
##    • každých interval milisekúnd sa farebný kruh s polomerom r presunie
##    na náhodnú pozíciu v ploche
##    • keď klikneme do plochy a trafíme do vnútra kruhu, ku nášmu skóre
##    sa pripočíta 10
##    • keď klikneme do plochy, ale netrafíme do kruhu, skóre sa zníži o 1
##    • aktuálne skóre sa vypisuje niekde v rohu obrazovky
##    (ako grafický objekt create_text())
##    • interval a r sú nejaké globálne premenné, napríklad s hodnotami 1000 a 20;
##    po niekoľkých klikaniach sa tieto hodnoty môžu automaticky meniť
##
#1234567890123456789012345678901234567890123456789012345678901234567890123456789
                                                                               #
                                                                               #
#úvodní a prázdný řádek:                                                       #
print('HRA NA POSTŘEH - "KLIKNI NA KOLEČKO"')                                  ##základní popis programu
print('''
Hra trénuje postřeh tím, že se na obrazovce, na náhodnou pozici
a náhodně krátkou dobu zobrazí malé kolečko, a na nás je,
stihnout na něj kliknout než zmizí a trefit se.

Hra má 4 stupně obtížnosti, podle délky doby, po kterou kolečko
zůstává na obrazovce.

1 = Lehký
2 = Normální
3 = Těžký
4 = Expert''')
                                                                               #
print()                                                                        ##prázdný řádek
ixo = int(input('Zvol obtížnost: '))                                           ##proměnná - pro volbu obtížnosti
while ixo not in (1, 2, 3, 4):                                                 ##cyklus - když volba není mezi 1-4
    ixo = int(input('''zadané číslo nebylo mezi 1 - 4.
Prosím o nové zadání: '''))                                                    #    #proměnná - pro novou volbu obtížnosti
                                                                               #
obt = [0, 'lehká', 'normální', 'těžká', 'velmi těžká']                         ##seznam - pro jméno obtížnosti
print()                                                                        ##prázdný řádek
print(f'''Je zvolena {obt[ixo]} obtížnost.
Přeji příjemnou hru.''')                                                       ##info o zvolené obtížnosti
                                                                               #
#import modulů:                                                                #
import tkinter                                                                 #
import math                                                                    #
import random                                                                  #
                                                                               #
                                                                               #
#grafické okno:                                                                #
canvas = tkinter.Canvas(bg='black', width=500, height=400)                     #
canvas.pack()                                                                  #
                                                                               #
                                                                               #
#proměnné:                                                                     #
uvodni_tx = '''Úkolem hry je trefit myší kolečko, které se na obrazovce objeví.
Kolečko se na obrazovce zobrazuje po náhodnou dobu a je třeba ho trefit na první klik.
Pokud se trefíme, připočte se nám 5 bodů, pokud se netrefíme, body se nám odečtou.
Hru začínáme s 50 body a končí ve chvíli, kdy dosáhneme 100 bodů a vyhrajeme,
nebo když dosáhneme 0 bodů a výhry nedosáhneme.
Hru začni kliknutím.'''                                                        #
                                                                               #
vyhra_tx = '''Gratuluji dosáhl jsi 100 bodů!
Pokud chceš hrát další hru, klikni.
Pokud již hrát nechceš, zavři okno, jinak jsi v tom navždy :-)'''              #
                                                                               #
prohra_tx = ''' Bohužel, tvůj počet bodů je nula!
Hra tímto končí. Pokud chceš hrát další hru, klikni.
Pokud již hrát nechceš, zavři okno, jinak jsi v tom navždy :-)'''              #
                                                                               #
tx = [uvodni_tx, vyhra_tx, prohra_tx]                                          ##seznam - pro info texty
body_ = [55]                                                                   ##seznam - počítání bodů
x_, y_, r_ = [250], [200], [10]                                                ##seznam - hodnoty x, y, r
cyklus_ = [False]                                                              ##seznam - on/of cyklu
prvoklik_ = [True]                                                             ##seznam - on/of prvokliku
trefa_ = [False]                                                               ##seznam - on/of trefy
rychlost_ = list(range(2000, 1, -100))                                         ##seznam - možných rychlostí
b = ['white', 'yellow', 'black']                                               ##seznam - barev
u = ['center']                                                                 ##seznam - vycentrování textu
o = [0, 5, 10, 15, 20]                                                         ##seznam - obtížnost
ixo = [ixo]                                                                    ##seznam - index obtížnosti
                                                                               #
                                                                               #
#funkce:                                                                       #
def body():                                                                    ##definice funkce - body
    canvas.delete('body')                                                      #    #změna - smazat předchozí informaci
    tx= f'Body: {body_[0]}'                                                    #    #proměnná - pro vytvoření textu počítadla 
    canvas.create_text(250, 350, text=tx, fill=b[0], justify=u[0], tag='body') #    #plátno - vepsání počítadla s aktuálním počtem bodů
                                                                               #
                                                                               #
def hrat_hru():                                                                ##definice funkce - hrát hru
    if body_[0] in range(1, 99):                                               #    #podmínka - pokud jsou body mezi 1 a 99
        canvas.delete('all')                                                   #        #změna - vyčistit plátno
        prvoklik_[0] = True                                                    #        #změna - nastav hodnotu prvokliku na True
        x_[0] = x = random.randrange(15, 485)                                  #        #proměnná - pro výpočet osy x kolečka
        y_[0] = y = random.randrange(15, 385)                                  #        #proměnná - pro výpočet osy y kolečka
        r = r_[0]                                                              #        #proměnná - pro hodnotu poloměru
        bn = f'#{random.randrange(256**3):06x}'                                #        #proměnná - pro výpočet náhodné barvy kolečka
        canvas.create_oval(x-r, y-r, x+r, y+r, fill=bn, outline=b[1], width=1) #        #plátno - nakreslení kolečka
        if trefa_[0] == False:                                                 #        #podmínka - pokud trefa má hodnotu False
            body_[0] -= 5                                                      #            #změna - sniž hodnotu bodů o 5 bodů
        else:                                                                  #        #podmínka - pokud trefa má hodnotu True
            trefa_[0] = False                                                  #            #změna - změň hodnotu trefa na False
        body()                                                                 #        #volání funkce - pro výpis bodů
        ix = random.randrange(0, o[ixo[0]])                                    #        #proměnná - pro výpočet indexu rychlosti zpoždění
        canvas.after(rychlost_[ix], hrat_hru)                                  #        #časovač zpoždění pro další cyklus
                                                                               #
    else:                                                                      #    #podmínka - pokud jsou body mimo rozmezí 1 a 99
        canvas.delete('all')                                                   #        #změna - vyčistit plátno
        cyklus_[0] = False                                                     #        #změna - změň hodnotu cyklu na False
        if body_[0] == 100:                                                    #        #podmínka - pokud hodnota bodů je 100
            canvas.create_text(250, 200, text=tx[1], fill=b[0], justify=u[0])  #            #plátno - vypiš text o výhře
        else:                                                                  #        #podmínka - pokud hodnota bodů je 0
            canvas.create_text(250, 200, text=tx[2], fill=b[0], justify=u[0])  #            #plátno - vypiš text o prohře
                                                                               #
                                                                               #
def klik(event):                                                               ##definice funkce - klik
    if cyklus_[0] == True:                                                     #    #podmínka - pokud má cyklus hodnotu True
        if prvoklik_[0] == True:                                               #        #podmínka - pokud má prvoklik hodnotu True
            prvoklik_[0] = False                                               #            #změna - změň hodnotu prvokliku na False
            x_kl, y_kl = event.x, event.y                                      #            #proměnná - pro osu x a y kliknutí
            x_ob, y_ob, r_ob = x_[0], y_[0], r_[0]                             #            #proměnná - pro osu x, y a poloměr kolečka
            if x_kl in range(x_ob-r_ob, x_ob+r_ob):                            #            #podmínka - když je osa x kliku mezi hodnotami os x kolečka
                if y_kl in range(y_ob-r_ob, y_ob+r_ob):                        #                #podmínka - když je osa y kliku mezi hodnotami os y kolečka
                    x1, y1, x2, y2 = x_ob-15, y_ob-15, x_ob+15, y_ob+15        #                    #proměnné pro osy x a y pro nakreslení zásahu
                    canvas.create_oval(x1, y1, x2, y2, fill=b[1])              #                    #plátno - nakreslení kolečka zásahu
                    canvas.create_line(x1, y1, x2, y2, fill=b[2], width=4)     #                    #plátno - nakreslení jedné nožičky křížku zásahu
                    canvas.create_line(x1, y2, x2, y1, fill=b[2], width=4)     #                    #plátno - nakreslení druhé nožičky křížku zásahu
                    body_[0] += 5                                              #                    #změna - zvyš hodnotu bodů o 5 bodů
                    body()                                                     #                    #volání funkce - pro vypsání bodů na obrazovku
                    trefa_[0] = True                                           #                    #změna - změň hodnotu trefa na True
                                                                               #
    else:                                                                      #    #podmínka - pokud cyklus má hodnotu False
        cyklus_[0] = True                                                      #        #změna - změň hodnotu cyklu na True
        body_[0] = 55                                                          #        #změna - nastav hodnotu bodů na 50
        hrat_hru()                                                             #        #volání funkce - pro spuštění hry
                                                                               #
                                                                               #
#úvod:                                                                         #
canvas.create_text(250, 200, text=tx[0], fill=b[0], justify=u[0])              ##plátno - vypiš úvodní text
canvas.bind('<ButtonPress-1>', klik)                                           ##provázání kliknutí
                                                                               #
                                                                               #
#aktivace grafické aplikace:                                                   #
tkinter.mainloop()                                                             #                                                                  
                                                                               #
                                                                               #
#1234567890123456789012345678901234567890123456789012345678901234567890123456789
