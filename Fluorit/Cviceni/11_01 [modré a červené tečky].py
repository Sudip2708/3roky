##  1. Napíš funkciu bodka(velkost, farba),
##  ktorá na pozícii korytnačky nakreslí farebnú bodku danej veľkosti.
##    • bodku budeš kresliť takto: zmení hrúbku a farbu pera na parametrami zadané hodnoty a
##    potom nakreslí čiaru dĺžky 0
##    • funkciu otestuj nakreslením 100 bodiek na náhodných pozíciách, pričom v pomere 1:2 budú
##    červené veľkosti 50 ku modrým veľkosti 30 (v cykle generuj náhodné čísla randrange(3) a pri
##    • kresli väčšie červené a inak menšie modré)
##    o v tomto testovacom programe nahraď volanie tvojej funkcie bodka(...) na korytnačiu
##    metódu t.dot(...) - mal by si dostať rovnaký výsledok (môžeš poštudovať help(t.dot));
##    skontroluj, či táto metóda dot kreslí bodku aj pri zdvihnutom pere


#úvodní a prázdný řádek:
print('MODRÉ A ČERVENÉ TEČKY')
print('''pouze k zobrazení - program generuje v modulu turle 100 náhodně
umístěných modrých a červených teček v poměru 1:2. ''')
print()


#prázdný řádek a příkaz pro spuštění okna grafické aplikace:
print()
input('[zmáčkni [Enter] pro zobrazení grafické aplikace]')


#definice funkce:
def bodka(velkost, farba):          #definice funkce nakreslení tečky
##    t1.pensize(velkost)                 #výběr tloušťky kreslící čáry
##    t1.pencolor(farba)                  #výběr barvy kreslící čáry
##    t1.bk(0)                            #vytvoř čáru délky 0
    t1.dot(velkost, farba)              #vytvoř tečku dle zadaných parametrů


def posun():                        #definice funkce pro posun
    x = random.randint(-200, 200)       #generování pozice x
    y = random.randint(-200, 200)       #generování pozice y
    t1.pu()                             #zvednutí pera
    t1.setpos(x, y)                     #posun na nové souřadnice
    t1.pd()                             #položení pera


#import modulů:
import turtle                       #import modulu turtle
import random                       #import modulu random


#grafické okno:
t1 = turtle.Turtle()                #vytvoření grafické plochy a  pera
#turtle.delay(0)                     #zrychlení vykresloení


#výpočet:
for i in range(100):                #cyklus pro 100 opakování
    if random.randrange(3):             #podmínka - pokud vybraná hodnota není 0 (not False)
        farba = 'blue'                      #vyber tuto barvu
        velkost = 30                        #vyber tuto tloučťku
    else:                               #podmínka - pokud vybraná hodnota je 0 (False)
        farba = 'red'                       #vyber tuto barvu
        velkost = 50                        #vyber tuto tloučťku
    posun()                             #volání funkce pro posun
    bodka(velkost, farba)               #volání funkce pro nakreslení tečky


#aktivace grafické aplikace
turtle.done()                       #hlavní smyčka grafického okna
