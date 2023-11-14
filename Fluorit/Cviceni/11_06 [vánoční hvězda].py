##  Napíš funkciu kosostvorec(velkost, farba),
##  pomocou ktorej korytnačka nakreslí kosoštvorec s danou veľkosťou strany.
##  Vnútorný uhol nech je 45 stupňov. Korytnačka začína aj končí pri vrchole, ktorý má týchto 45 stupňov.
##  Vnútro kosoštvorca vyfarbi danou farbou.
##  Otestuj nakreslením 8 kosoštvorcov, ktoré majú jeden spoločný vrchol;
##  týmto kosoštvorcom pravidelne striedaj dve farby výplne 'tan' a 'tomato'.


#úvodní a prázdný řádek:
print('VÁMOČNÍ HVĚZDA')
print('''pouze k zobrazení - program kreslí v modulu turle
2 barvami kosočtverce uspořádané do hvězdy. ''')
print()


#prázdný řádek a příkaz pro spuštění okna grafické aplikace:
print()
input('[zmáčkni [Enter] pro zobrazení grafické aplikace]')


#definice funkce:
def kosostvorec(velkost, farba):        #definice funkce pro nakreslení barevného kosočtverce
    u1, u2 = 45, 135                    #proměnné pro výpočet úhlu
    t1.fillcolor(farba)                 #zvolení barvy výplně
    t1.begin_fill()                     #začátek oblasti pro vyplnění barvou
    for i in range(4):                  #cyklus dle počtu stran
        t1.fd(velkost)                      #nakresli čáru
        t1.lt(u1)                           #pootoč se o daný úhel
        u1, u2 = u2, u1                     #prohoď hodnoty úhlů
    t1.end_fill()                       #konec oblasti pro vyplnění barvou


#import modulů:
import turtle                           #import modulu turtle


#grafické okno:
t1 = turtle.Turtle()                    #vytvoření grafického plátna a pera
#turtle.delay(0)                         #zrychlení vykresloení


#výpočet:
barva1, barva2 = 'tan', 'tomato'        #proměnné pro barvu
velkost = 100                           #proměnná pro velikost
for i in range(8):                      #cyklus dle počtu objektů
    farba = barva1                          #přiřazení barvy
    t1.lt(360/8)                            #pootočení úhlu pera
    kosostvorec(velkost, farba)             #volání funkce pro nakreslení kosočtverce   
    barva1, barva2 = barva2, barva1         #prohození hodnot barev


#aktivace grafické aplikace
turtle.done()                           #hlavní smyčka grafického okna
