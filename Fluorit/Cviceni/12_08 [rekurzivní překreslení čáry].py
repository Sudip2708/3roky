##Funkcia kmit(a) kreslí stále dlhšie nadväzujúce úsečky:
##    import turtle
##    
##    def kmit(a):
##        if a > 230:
##            pass
##        else:
##            t.fd(a)
##            t.rt(170)
##            t.fd(a+5)
##            t.lt(170)
##            kmit(a+10)
##            pass
##    
##    t = turtle.Turtle()
##    t.pu()
##    t.setpos(-250, 0)
##    t.pd()
##    t.lt(85)
##    kmit(100)
##Nahraď oba príkazy pass tak, aby sa po nakreslení všetkých čiar
##tieto spätne prefarbili na šedo ('lightgray'),
##teda pri návrate z rekurzie sa prejde
##po tých istých čiarach znovu ale inou farbou.


#úvodní a prázdný řádek:
print('REKURZIVNÍ PŘEBARVENÍ ČÁRY')
print(f'''Program rekurzivně nakreslí klikatou čáru,
po které změní barvu pera a při zpětné cetě překreslí
tuto klikatou čáru novou barvou.''')
print()
input('[zmáčkni [Enter] pro zobrazení]')


#import modulů:
import turtle


#definice funkce:
def kmit(a):                #definice funkce pro nakreslení klikaté čáry - parametr velikost první čáry
    if a > 230:                 #podmínka - když velikost je větší než 230
        t.color('lightgray')        #změň barvu pera
        t.rt(170)                   #otoč se o 170°- do opačného směru poslední nakreslené čáry
    else:                       #podmínka - pokud velikost není větší než 230
        t.fd(a)                     #nakresli čáru dle hodnoty velikosti
        t.rt(170)                   #otoč se doprava o 170°
        t.fd(a+5)                   #nakresli čáru, ale k hodnotě velikosti púřipočti 5
        t.lt(170)                   #otoč se doleva o 170°
        kmit(a+10)                  #rekurzivní volání funkce s povýšenou hodnotou o 10
        t.bk(a+5)                   #zpětné kreslení čáry s délkou o 5 větší než je aktuální hodnota velikosti
        t.lt(170)                   #otoč se doleva o 170°
        t.bk(a)                     #zpětné kreslení čáry dle aktuální rekurzivní délky
        t.rt(170)                   #otoč se doprava o 170°


#výpočet:
t = turtle.Turtle()         #vytvoř želvu
#t.speed(0)                  #zrychlení vykreslování
t.pu()                      #zvedni pero
t.setpos(-250, 0)           #přesuň se na uvedenou pozici
t.pd()                      #polož pero
t.lt(85)                    #otoč se doleva o 85°
kmit(100)                   #volání rekurzivní funkce na nakreslení klikaté čáry


#smyčka hlavního okna
turtle.mainloop()
