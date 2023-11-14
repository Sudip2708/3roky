##  Napíš funkciu bodky(n, m),
##  ktorá nakreslí n radov bodiek (t.dot(...)) po m v každom rade.
##  Stredy bodiek v radoch aj stĺpcoch sú vo vzdialenosti 30.
##  Všetky bodky majú farbu 'salmon' a náhodnú veľkosť od 20 do 35.
##  Nepoužívaj metódu setpos.
##  Otestuj, napríklad bodky(10, 15)


#úvodní a prázdný řádek:
print('SÍŤ Z TEČEK')
print('''pouze k zobrazení - program generuje v modulu turle 150,
různě velikých bodů, umístěných pomyslné mřížce. ''')
print()


#prázdný řádek a příkaz pro spuštění okna grafické aplikace:
print()
input('[zmáčkni [Enter] pro zobrazení grafické aplikace]')


#definice funkce:
def bodky(n, m):                                        #definice funkce pro nakreslení bodů
    t1.up()                                                 #zvednutí pera
    for i in range(n):                                      #cyklus dle počtu řádků
        for i in range(m):                                      #cyklus dle počtu teček v řádku
            t1.dot(random.randint(20, 35), 'salmon')                #nakreslení tečky
            t1.fd(30)                                               #posunutí na další pozici
        t1.bk(m*30)                                             #vrácení se na výchozí pozici řádku
        t1.lt(90)                                               #natočení o devadesát stupňů nahoru
        t1.fd(30)                                               #posunutí se na další řádek
        t1.rt(90)                                               #natočení na směr řádku
    t1.pd()                                                 #položení pera


#import modulů:
import turtle                                           #import modulu turtle
import random                                           #import modulu random


#grafické okno:
t1 = turtle.Turtle()                                    #vytvoření grafického plátna a pera
#turtle.delay(0)                                         #zrychlení vykresloení


#výpočet:
bodky(10, 15)                                           #volání funkce pro nakreslení bodů


#aktivace grafické aplikace
turtle.done()                                           #hlavní smyčka grafického okna
