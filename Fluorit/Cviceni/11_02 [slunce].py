##  Napíš funkciu slnko(pocet, velkost), pomocou ktorej korytnačka nakreslí slnko s daným počtom lúčov.
##  Každý lúč je úsečka danej veľkosti a hrúbky 10. Okrem lúčov nakresli kruh danej veľkosti
##  (priemer kruhu je tiež velkost) - použi metódu t.dot(...).
##  Na kreslenie lúčov aj slnka použi farbu 'gold'.


#úvodní a prázdný řádek:
print('SLUNCE')
print('''pouze k zobrazení - program nakreslí v modulu turle slunce. ''')
print()


#prázdný řádek a příkaz pro spuštění okna grafické aplikace:
print()
input('[zmáčkni [Enter] pro zobrazení grafické aplikace]')


#definice funkce:
def slnko(pocet, velkost):      #definice funkce pro nakreslení slunce
    t1.pensize(10)                  #výběr tloušťky kreslící čáry
    t1.pencolor('gold')             #výběr barvy kreslící čáry
    for i in range(pocet):          #cyklus dle počtu paprsků
        t1.fd(velkost)                  #nakreslení paprsku
        t1.pu()                         #zvednutí pera
        t1.bk(velkost)                  #navrácení se na původní pozici
        t1.lt(360/pocet)                #atočení pera dle počtu paprsků
        t1.pd()                         #položení pera
    t1.dot(velkost)                 #nakreslení vnitřní části slunce

    
import turtle                   #import modulu turtle


#grafické okno:
t1 = turtle.Turtle()            #vytvoření grafického plátna a pera
#turtle.delay(0)                 #zrychlení vykresloení


#výpočet:
slnko(16, 100)                  #volání funkce pro nakreslení slunce


#aktivace grafické aplikace
turtle.done()                   #hlavní smyčka grafického okna
