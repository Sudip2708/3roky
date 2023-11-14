##Rekurzívna krivka je popísaná takýmto predpisom:
## >obrázek je v zadání<
## 
##Napíš funkciu vpisane3(n, a),
##v ktorej prvý parameter n označuje úroveň vnorenia trojuholníkov,
##druhý parameter a veľkosť vonkajšieho trojuholníka.
##Pre n = 0 funkcia nekreslí nič.


#úvodní a prázdný řádek:
print('REKURZIVNĚ ZAPUŠTĚNÉ TROJŮHELNÍKY')
print(f'''Program dle zadaného počtu zanoření,
nakreslí trojůhelníky v trojůhelníku.''')
print()


#vstupní data:
n = int(input('Zadej hodnotu zanoření: '))  


#import modulů:
import turtle


#definice funkce:
def vpisane3(a, n):         #rekurzivní funkce pro nakreslení vnořených trojúhelníků - parametry velikost strany, počet vnoření
    if n == 0:                  #podmínka - když velikost strany je 0
        pass                        #nedělej nic
    else:                       #podmínka - dokud velikost strany není 0
        for i in range(3):          #cyklus - 3x
            t.fd(a)                     #nakresli čáru dle velikosti
            t.lt(120)                   #otoč se doleva o 120°
        t.pu()                      #zvedni pero
        t.fd(a/2)                   #posuň se o polovinu velikosti
        t.lt(60)                    #otoč se doleva o 60°        
        t.pd()                      #polož pero
        vpisane3(a/2, n-1)          #rekurzivní volání funkce s poníženými hodnotami


#výpočet:
a = 300                     #proměná pro velikost strany prvního trojúhelníku
t = turtle.Turtle()         #vytvoření želvy
#t.speed(0)                  #zrychlení vykreslení
t.pu()                      #zvedni pero
t.setpos(-a/2, -a/3)        #přesuň se na uvedenou pozici
t.pd()                      #polož pero
vpisane3(a, n)              #volání rekurzivní funkce pro nakreslení vnořených trojúhelníků


#smyčka hlavního okna
turtle.mainloop()
