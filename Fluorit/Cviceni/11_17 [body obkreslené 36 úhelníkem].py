##  Napíš funkciu kruznica(r),
##  ktorá nakreslí kružnicu s polomerom r a so stredom, ktorý je v momentálnej pozícii korytnačky.
##  Kružnicu kresli ako pravidelný 36-uholník.
##  Uvedom si, že ak by strana tohto 36-uholníka bola d, tak obvod vypočítame ako 2*pi*r = 36*d.
##  Z tohto vzťahu vieš vypočítať d a teda nakresliť pravidelný 36-uholník.
##  Po skončení kreslenia, korytnačka bude v rovnakej pozícii ako začala.
##  Nepoužívaj metódu setpos.
##  Vyskúšaj:
##     t.dot(200, 'yellow')
##     kruznica(100)
##     t.pu()
##     t.fd(120)
##     t.lt(90)
##     t.fd(100)
##     t.rt(37)
##     t.pd()
##     t.dot(140, 'gold')
##     kruznica(70)
##  dostaneš (dva žlté kruhy kreslené pomocou dot sú tu len na kontrolu)


#úvodní a prázdný řádek:
print('2 ŽLUTÉ BODY OBTAŽENÉ 36 ÚHELNÍKEM')
print('''pouze k zobrazení - program postupně generuje 2 žluté body,
které obkreslí 36 úhelníkem.''')
print()


#prázdný řádek a příkaz pro spuštění okna grafické aplikace:
print()
input('[zmáčkni [Enter] pro zobrazení grafické aplikace]')
print()


#definice funkce:
def kruznica(r):            #definice fuknce pro nakreslení 36 úhelníku
    pi = math.pi                #hodnota Pi
    d = (2*pi*r) / 36           #hodnota délky čáry (strany 36 úhelníku
    uhel = 360 / 36             #hodnota úhlu

    t1.pu()                     #zvednutí pera
    t1.fd(r)                    #posunití dopředu o poloměr
    t1.pd()                     #položení pera
    t1.lt(90)                   #natočení pera směrem nahoru (o 90 stupňů)
    t1.fd(d/2)                  #nakreslení poloviny první čáry (pro vycentrování)
    
    for i in range(35):         #cyklus pro nakreslení 36 dalších čar
        t1.lt(uhel)                 #otočení o úhel
        t1.fd(d)                    #kreslení čáry

    t1.lt(uhel)                 #otočení o uhel
    t1.fd(d/2)                  #nakreslení druhé poloviny první čáry (pro vycentrování)
    t1.pu()                     #zvednutí pera
    t1.rt(90)                   #otočení doprava o úhel 90 stupňů
    t1.bk(r)                    #couvnutí na původní pozici
    t1.pd()                     #položení pera


#import modulů:
import turtle               #import modulu turtle
import math                 #import modulu math


#grafické okno:
t1 = turtle.Turtle()        #vytvoření grafické plochy a  pera
#turtle.delay(0)            #zrychlení vykresloení


#výpočet:
t1.dot(200, 'yellow')       #vytvoř žlutou tečku
kruznica(100)               #volání funkce pro nakreslení 36 úhelníku
t1.pu()                     #zvednutí pera
t1.fd(120)                  #posunutí na další pozici
t1.lt(90)                   #natočení doleva o 90 stupňů
t1.fd(100)                  #posunutí na další pozici
t1.rt(37)                   #natočení doprava o 37 stupňů
t1.pd()                     #položení pera
t1.dot(140, 'gold')         #vytvoř žlutou tečku
kruznica(70)                #volání funkce pro nakreslení 36 úhelníku

#aktivace grafické aplikace
turtle.done()               #hlavní smyčka grafického okna
