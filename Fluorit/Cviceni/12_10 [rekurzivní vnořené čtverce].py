##Rekurzívna krivka je popísaná takýmto predpisom:
##    
## >obrázek je v zadání<
## 
##Napíš funkciu vpisane4(n, a),
##v ktorej prvý parameter n označuje úroveň vnorenia štvorcov,
##druhý parameter a veľkosť vonkajšieho štvorca.
##Pre n = 0 funkcia nekreslí nič.


#úvodní a prázdný řádek:
print('REKURZIVNĚ ZAPUŠTĚNÉ ČTVERCE')
print(f'''Program dle zadaného počtu zanoření,
nakreslí do sebe zapuštěné čtverce.''')
print()


#vstupní data:
n = int(input('Zadej hodnotu zanoření: '))  


#import modulů:
import turtle


#definice funkce:
def vpisane4(a, n):         #rekurzivní funkce pro nakreslení vnořených čtverců - parametry velikost strany, počet vnoření
    if n == 0:                  #podmínka - když velikost strany je 0
        pass                        #nedělej nic
    else:                       #podmínka - dokud velikost strany není 0
        for i in range(4):          #cyklus - 4x
            t.fd(a)                     #nakresli čáru dle velikosti
            t.lt(90)                    #otoč se doleva o 90°
        t.pu()                      #zvedni pero
        t.fd(a/2)                   #posuň se o polovinu velikosti
        t.lt(45)                    #otoč se doleva o 45°
        t.pd()                      #polož pero
        c = (2*(a/2)**2)**.5        #vypočti novou hodnotu délky strany
        vpisane4(c, n-1)            #rekurzivní volání funkce s poníženými hodnotami


#výpočet:
a = 300                     #proměná pro velikost strany prvního trojúhelníku
t = turtle.Turtle()         #vytvoření želvy
#t.speed(0)                  #zrychlení vykreslení
t.pu()                      #zvedni pero
t.setpos(-a/2, -a/2)        #přesuň se na uvedenou pozici
t.pd()                      #polož pero
vpisane4(a, n)              #volání rekurzivní funkce pro nakreslení vnořených čtverců


#smyčka hlavního okna
turtle.mainloop()

