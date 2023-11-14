##  (trochu matematiky)
##  Budeš kresliť obrázok, ktorý demonštruje Pytagorovu vetu:
##  súčet štvorcov nad odvesnami sa rovná štvorcu nad preponou.
##  Napíš funkciu pytagoras(prepona, uhol), ktorá nakresli štvorec nad preponou,
##  vypočíta dĺžky oboch odvesien a nakreslí oba štvorce.
##  uhol je vnútorný uhol pravouhlého trojuholníka.
##  Uvedom si, že dĺžky odvesien môžeš počítať ako prepona * cos(uhol) a prepona * sin(uhol),
##  daj pozor na radiány.
##  Funkcia potom vypíše (do shellu) obsah štvorca nad preponou
##  a obsahy oboch štvorcov nad odvesnami.
##  Pri kreslení štvorcov môžeš použiť funkciu na kreslenie náhodne vyfarbeného štvorca (z úlohy (5)).
##  Pre volanie pytagoras(150, 17) by si mohol dostať takýto výstup:
##    stvorec nad preponou = 22500
##    stvorec nad 1. odvesnou = 20576.672691244217
##    stvorec nad 2. odvesnou = 1923.3273087557814
##    sucet = 22500.0


#úvodní a prázdný řádek:
print('PYTAGOROVA VĚTA')
print('''pouze k zobrazení - program generuje v modulu turle trojůhelník,
na základě hodnoty přepony (strana c = 150) a vnitřního úhlu pravoúhlého
trojůhelníku (úhel β = 17) a to tak, že nad každou ze stran nakreslí
přilehlý čtverec a v shelu vypíše hodnoty obsahu čtverců a součet
pro porovnání pravdivosti tvrzení, že obsahy čtverců nad odvěsnami
se rovná obsahu čtverců nad přeponou.''')
print()


#prázdný řádek a příkaz pro spuštění okna grafické aplikace:
print()
input('[zmáčkni [Enter] pro zobrazení grafické aplikace]')
print()


#definice funkce:
def ctverec(strana, smer):                              #definice funkce pro nakreslení čtverce
    barva = f'#{random.randrange(256**3):06x}'              #proměná pro náhodnou barvu
    t1.fillcolor(barva)                                     #zvolení barvy výplně
    t1.begin_fill()                                         #začátek úseku pro barevnou výplň
    for i in range(4):                                      #cyklus 4x
        t1.fd(strana)                                           #jdi dopředu
        t1.rt(90*smer)                                          #natoč se o 90 stupňů
    t1.end_fill()                                           #konec úseku pro barevnou výplň


def pytagoras(prepona, uhol):                           #definice funkce pro nakreslení útvaru
    c = prepona                                             #hodnota přepony c
    cos = math.cos(math.radians(uhol))                      #výpočet cos
    sin = math.sin(math.radians(uhol))                      #výpočet sin

    a = c * cos                                             #výpočet strany a
    b = c * sin                                             #výpočet strany b

    ctverec_a = a**2                                        #výpočet obsahu čtverce nad stranou a
    ctverec_b = b**2                                        #výpočet obsahu čtverce nad stranou b
    ctverec_c = c**2                                        #výpočet obsahu čtverce nad stranou c

    print(f'stvorec nad preponou = {ctverec_c}')            #výpis pro hodnotu obsahu nad stranou c
    print(f'stvorec nad 1. odvesnou = {ctverec_a}')         #výpis pro hodnotu obsahu nad stranou a
    print(f'stvorec nad 2. odvesnou = {ctverec_b}')         #výpis pro hodnotu obsahu nad stranou b
    print(f'sucet = {ctverec_a + ctverec_b}')               #výpis pro hodnotu součtů obsahů čtverců nad stranou a a b

    ctverec(c, 1)                                           #volání funkce pro nakreslení čtverce
    t1.lt(uhol)                                             #natočení o hodnotu uhlu
    ctverec(a, -1)                                          #volání funkce pro nakreslení čtverce
    t1.pu()                                                 #zvednutí pera
    t1.fd(a)                                                #přechod na další pozici
    t1.pd()                                                 #položení pera pera
    t1.rt(90)                                               #natočení o 90 stupňů
    ctverec(b, -1)                                          #volání funkce pro nakreslení čtverce

    
#import modulů:
import turtle                                           #import modulu turtle
import math                                             #import modulu math
import random                                           #import modulu random


#grafické okno:
t1 = turtle.Turtle()                                    #vytvoření grafické plochy a  pera
turtle.delay(0)                                         #zrychlení vykresloení


#výpočet:
pytagoras(150, 17)                                      #volání funkce pro nakreslení útvaru


#aktivace grafické aplikace
turtle.done()                                           #hlavní smyčka grafického okna
