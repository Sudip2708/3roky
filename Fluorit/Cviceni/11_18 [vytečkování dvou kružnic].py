##  Napíš funkciu prechadzka(n),
##  ktorá zrealizuje n krokov náhodnej prechádzky:
##    • korytnačka chodí náhodne so zdvihnutým perom s krokom 20
##    • ak sa vzdiali od (0, 0) o viac ako 70, cúvne 20
##    • inak, ak sa vzdiali od (0, 0) o viac ako 50, na momentálnej pozícii nakreslí červenú bodku
##    (veľkosti 5)
##    • inak na momentálnej pozícii nakreslí modrú bodku (veľkosti 5)
##  Vyskúšaj:
##    turtle.tracer(0)
##    prechadzka(2000)
##    turtle.tracer(1)


#úvodní a prázdný řádek:
print('VYTEČKOVÁNÍ DVOU KRUŽNIC')
print('''pouze k zobrazení -
Program 2000x náhodně prochází plochou o předem stanovený krok (20).
Pokud není dále než 50 bodů od středu kreslí modrou tečku.
Pokud je dále než 50 bodů od středu, ale není dále než 70, kreslí červenou tečku.
Pokud překročí hranici 70 bodů, nekreslí nic a jen se vrátí o krok zpět. ''')
print()


#prázdný řádek a příkaz pro spuštění okna grafické aplikace:
print()
input('[zmáčkni [Enter] pro zobrazení grafické aplikace]')
print()


#definice funkce:
def prechadzka(n):                      #definice funkce pro vytečkování dvou kružnic             
    t1.pu()                                 #zvednutí pera
    krok = 20                               #hodnota kroku o kterou se pero posouvá na další pozici
    for i in range(n):                      #cyklus dle zadané hodnoty
        uhel = random.randrange(360)            #náhodný výpočet úhlu
        t1.lt(uhel)                             #otočení lera o patřičný uhel
        t1.fd(krok)                             #posunutí o 1 krok
        x2 = abs(t1.xcor())**2                  #výpočet strany a (osy x) na druhou
        y2 = abs(t1.ycor())**2                  #výpočet strany b (osy y) na druhou
        vzd_od_str = (x2 + y2)**.5              #výpočet vzdálenosti od středu (strana c)
        if vzd_od_str < 50:                     #pokud je vzdálenost od středu menší než 50
            t1.dot(5, 'blue')                       #udělej modrou tečku
        elif vzd_od_str < 70:                   #pokud je vzdálenost od středu větší než 50, ale menší než 70
            t1.dot(5, 'red')                        #udělej červenou tečku
        else:                                   #ve všech ostatních případech
            t1.bk(krok)                             #couvni o 1 krok (vrať se ny výchozí pozici před tímto krokem)
    t1.pd                                   #položení pera
    

#import modulů:
import turtle                           #import modulu turtle
import random                           #import modulu random


#grafické okno:
t1 = turtle.Turtle()                    #vytvoření grafické plochy a  pera
turtle.delay(0)                         #zrychlení vykresloení


#výpočet:
#turtle.tracer(0)                       #pozastavení vykreslování 
prechadzka(2000)                        #volání funkce pro vytečkování dvou kružnic
#turtle.tracer(1)                       #znovuspuštění vykreslování 


#aktivace grafické aplikace
turtle.done()                           #hlavní smyčka grafického okna
