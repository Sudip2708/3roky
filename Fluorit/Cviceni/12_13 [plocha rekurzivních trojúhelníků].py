##Rekurzívna krivka je popísaná takýmto predpisom:
##    
## >obrázek je v zadání<
## 
##Napíš funkciu troj3(n, a),
##v ktorej prvý parameter n označuje úroveň krivky,
##druhý parameter a veľkosť obrázka (dĺžka spodnej hrany).
##Na všetkých piatich obrázkov je rovnaké a.


#úvodní a prázdný řádek:
print('PLOCHA REKURZIVNÍCH TROJÚHELNÍKŮ')
print(f'''Program dle zadaného počtu zanoření (1 - 6),
postupně vyplní plochu trojúhelníku menšími trojúhelníkami.''')
print()


#vstupní data:
n = int(input('Zadej hodnotu zanoření: '))  


#import modulů:
import turtle


#definice funkce:
def troj3(n, a):            #rekurzivní funkce pro nakreslení plochy z rekurzivních trojúhelníků
    if n == 0:                  #podmínka - když velikost strany je 0
        t.fd(a)                     #nakresli čáru s aktuální velikostí
    else:                       #podmínka - dokud velikost strany není 0
        t.fd(a/2)                   #nakresli čáru s polovinou aktuální velikostí
        t.lt(120)                   #otoč se doleva o 120°
        troj3(n-1, a/2)          #rekurzivní volání funkce s poníženými hodnotami
        t.rt(120)                   #otoč se doleva o 120°
        troj3(n-1, a/2)          #rekurzivní volání funkce s poníženými hodnotami
        t.rt(120)                   #otoč se doleva o 120°
        troj3(n-1, a/2)          #rekurzivní volání funkce s poníženými hodnotami
        t.lt(120)                   #otoč se doleva o 120°
        t.fd(a/2)                   #nakresli čáru s polovinou aktuální velikostí
        

#výpočet:
a = 300                     #proměná pro velikost strany prvního trojúhelníku
t = turtle.Turtle()         #vytvoření želvy
#t.speed(0)                  #zrychlení vykreslení
t.pu()                      #zvedni pero
t.setpos(-a/2, -a/3)        #přesuň se na uvedenou pozici
t.pd()                      #polož pero
troj3(n, a)                 #volání rekurzivní funkce pro nakreslení plochy z rekurzivních trojúhelníků


#smyčka hlavního okna
turtle.mainloop()
