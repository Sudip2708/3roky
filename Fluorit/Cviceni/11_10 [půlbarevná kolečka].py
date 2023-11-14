##  Na rovnakom princípe, ako bola funkciu polkruznica z predchádzajúcej úlohy,
##  napíš funkciu polkruh(velkost, smer).
##  Korytnačka teraz vnútro nakresleného oblúka vyfarbí náhodnou farbou.
##  Otestuj podobne ako predchádzajúcu úlohu, ale po nakreslení 10 farebných polkruhov
##  dokresli ďalších 10 tak, aby sa vlnky doplnili do farebných kruhov
##  - zrejme každý z takýchto kruhov sa bude skladať z dvoch rôzne zafarbených polovíc.


#úvodní a prázdný řádek:
print('PŮLBAREVNÁ KOLEČKA')
print('''pouze k zobrazení - program generuje v modulu turle 20
různě barevných půlkruhů, které se spojují v dvoubarevné kruhy.''')
print()


#prázdný řádek a příkaz pro spuštění okna grafické aplikace:
print()
input('[zmáčkni [Enter] pro zobrazení grafické aplikace]')


#definice funkce:
def polkruznica(velkost, smer):                     #definice funkce pro kreslení půl kružnice
    t1.fillcolor(f'#{random.randrange(256**3):06x}')    #zvolení barvy výplně
    t1.begin_fill()                                     #začátek oblasti pro vyplnění barvou
    for i in range(18):                                 #cyklus dle počtu stran 'půlkruhu'
        t1.lt(10*smer)                                      #natočení
        t1.fd(velkost)                                      #nakreslení čáry
    t1.end_fill()                                       #konec oblasti pro vyplnění barvou


#import modulů:
import turtle                                       #import modulu turtle
import random                                       #import modulu random


#grafické okno:
t1 = turtle.Turtle()                                #vytvoření grafického plátna a pera
#turtle.delay(0)                                     #zrychlení vykresloení


#výpočet:
t1.lt(90)                                           #natočení tužky do pozice na kreslení prvního kruhu
for i in range(5):                                  #cyklus dle počtu vlnek
    polkruznica(3, -1)                                  #volání funkce pro nakreslení půlkruhu
    polkruznica(3, 1)                                   #volání funkce pro nakreslení půlkruhu                  
t1.lt(180)                                          #natočení tužky do opopačného směru
for i in range(5):                                  #cyklus dle počtu vlnek
    polkruznica(-3, 1)                                  #volání funkce pro nakreslení půlkruhu
    polkruznica(-3, -1)                                 #volání funkce pro nakreslení půlkruhu                  
t1.lt(90)                                          #natočení tužky do počáteční pozice


#aktivace grafické aplikace
turtle.done()                                       #hlavní smyčka grafického okna
