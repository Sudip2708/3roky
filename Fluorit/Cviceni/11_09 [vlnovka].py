##  Napíš funkciu polkruznica(velkost, smer),
##  pomocou ktorej korytnačka nakreslí 18 strán z pravidelného 36-uholníka so stranou danej veľkosti.
##  Parameter smer určuje, či sa pri kreslení korytnačka otáča vľavo (smer=True) alebo vpravo (smer=False).
##  Otestuj nakreslením 10 polkružníc tak, aby z toho vznikli vlnky (veľkosť nech je napríklad 3).


#úvodní a prázdný řádek:
print('VLNOVKA')
print('''pouze k zobrazení - program generuje v modulu turle vlnovku. ''')
print()


#prázdný řádek a příkaz pro spuštění okna grafické aplikace:
print()
input('[zmáčkni [Enter] pro zobrazení grafické aplikace]')


#definice funkce:
def polkruznica(velkost, smer):         #definice funkce pro kreslení půl kružnice
    for i in range(18):                     #cyklus dle počtu stran 'půlkruhu'
        t1.lt(10*smer)                          #natočení
        t1.fd(velkost)                          #nakreslení čáry


#import modulů:
import turtle                           #import modulu turtle


#grafické okno:
t1 = turtle.Turtle()                    #vytvoření grafického plátna a pera
#turtle.delay(0)                         #zrychlení vykresloení


#výpočet:
t1.lt(90)                               #natočení tušky do počáteční pozice
for i in range(5):                      #cyklus dle počtu vlnek
    polkruznica(3, -1)                      #volání funkce pro nakreslení půlkruhu
    polkruznica(3, 1)                       #volání funkce pro nakreslení půlkruhu                  


#aktivace grafické aplikace
turtle.done()                           #hlavní smyčka grafického okna
