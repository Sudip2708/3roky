##  Napíš funkciu stvorec(velkost),
##  pomocou ktorej korytnačka nakreslí náhodne zafarbený štvorec danej veľkosti.
##  Otestuj nakreslením 10 štvorcov v rade vedľa seba s náhodnými veľkosťami strán od 20 do 50.
##  Otestuj na:
##    for i in range(10):
##    stvorec(random.randint(20, 50))


#úvodní a prázdný řádek:
print('BAREVNÉ ČTVEREČKY VEDLE SEBE')
print('''pouze k zobrazení - program kreslí v modulu turle 10 náhodně
barevných a různě velikých čtverců. ''')
print()


#prázdný řádek a příkaz pro spuštění okna grafické aplikace:
print()
input('[zmáčkni [Enter] pro zobrazení grafické aplikace]')


#definice funkce:
def stvorec(velkost):                       #definice funkce pro nakreslení barevného čtverce
    b = f'#{random.randrange(256**3):06x}'      #výběr náhodné barvy
    t1.fillcolor(b)                             #zvolení barvy výplně
    t1.up                                       #zvednutí pera
    t1.begin_fill()                             #začátek oblasti pro vyplnění barvou
    for i in range(4):                          #cyklus dle počtu stran
        t1.fd(velkost)                              #nakreslení čáry
        t1.lt(90)                                   #otočení o 90 
    t1.end_fill()                               #konec oblasti pro vyplnění barvou
    t1.fd(velkost)                              #posunutí na další pozici
    t1.down()                                   #položení pera


#import modulů:
import turtle                               #import modulu turtle
import random                               #import modulu random


#grafické okno:
t1 = turtle.Turtle()                        #vytvoření grafického plátna a pera
#turtle.delay(0)                             #zrychlení vykresloení


#výpočet:
for i in range(10):                         #cyklus dle počtu čtverců
    velkost = random.randint(20, 50)            #výpočet náhodné velikosti
    stvorec(velkost)                            #volání funkce pro kreslení čtverce


#aktivace grafické aplikace
turtle.done()                               #hlavní smyčka grafického okna
