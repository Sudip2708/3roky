##Rekurzívna krivka je popísaná takýmto predpisom:
##    
## >obrázek je v zadání<
## 
##Napíš funkciu pyramida3(n, a), v ktorej prvý parameter n označuje úroveň krivky,
##druhý parameter a veľkosť obrázka (dĺžka spodnej hrany).
##Na všetkých piatich obrázkov je rovnaké a.
##Obrázok vznikol rovnako ako v predchádzajúcej úlohe (funkcia pyramida),
##ale medzi kresleniami vnorených menších kriviek
##sa korytnačka otáčala vľavo 87, vpravo 174 a vľavo 87.


#úvodní a prázdný řádek:
print('REKURZIVNÍ PIRAMINA Z KOSTIČEK 2')
print(f'''Program nakreslí pyramidu z kostiček dle zadané velikosti,
nyní ale mezi čarou nahoru a dolu udělá malou uhlovou výchylku.''')
print()


#vstupní data:
n = int(input('Zadejvelikost kostičky (2 - 6): '))  


#import modulů:
import turtle


#definice funkce:
def pyramida(n, a):         #rekurzivní funkce pro nakreslení vnořených čtverců
    if n == 0:                  #podmínka - když velikost strany je 0
        t.fd(a)                     #nakresli čáru dle aktuální velikosti
    else:                       #podmínka - dokud velikost strany není 0
        pyramida(n-1, a/2)          #rekurzivní volání funkce s poníženými hodnotami
        t.lt(87)                    #otoč se doleva o 90° 
        pyramida(n-1, a/2)          #rekurzivní volání funkce s poníženými hodnotami
        t.rt(174)                   #otoč se doprava o 180° 
        pyramida(n-1, a/2)          #rekurzivní volání funkce s poníženými hodnotami
        t.lt(87)                    #otoč se doleva o 90° 
        pyramida(n-1, a/2)          #rekurzivní volání funkce s poníženými hodnotami


#výpočet:
a = 300                     #proměná pro velikost spodní strany
t = turtle.Turtle()         #vytvoření želvy
#t.speed(0)                  #zrychlení vykreslení
t.pu()                      #zvedni pero
t.setpos(-a/2, -a/3)        #přesuň se na uvedenou pozici
t.pd()                      #polož pero
pyramida(n, a)              #volání rekurzivní funkce pro nakreslení vnořených čtverců


#smyčka hlavního okna
turtle.mainloop()
