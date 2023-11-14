##Rekurzívna krivka je popísaná takýmto predpisom:
##    
## >obrázek je v zadání<
## 
##Napíš funkciu kriziky(n, a, pocet),
##v ktorej prvý parameter n označuje úroveň krivky,
##druhý parameter a dĺžku ramena kríža.
##Tretí parameter pocet označuje počet ramien
##kríža - na obrázku je pocet = 5.
##Predchádzajúca krivka kriziky4 by sa dala nakresliť
##aj touto funkciou pre pocet = 4.


#úvodní a prázdný řádek:
print('REKURZIVNÍ KRESLENÍ VÍCERAMENÍKU')
print(f'''Program dle zadaného počtu ramen (3 - 8), a dle počtu zanoření (1 - 5),
nakreslí mnohoramený rekurzivní útvar a dle hodnoty tento útvar
kreslí na každém konci čar.''')
print()


#vstupní data:
pocet = int(input('Zadej hodnotu počtu ramen: '))  
n = int(input('Zadej hodnotu zanoření: '))  


#import modulů:
import turtle


#definice funkce:
def kriziky(n, a, pocet):           #rekurzivní funkce pro nakreslení útvaru
    if n == 0:                          #podmínka - když velikost strany je 0
        pass                                #nedělej nic
    else:                               #podmínka - dokud velikost strany není 0
        t.lt((360/pocet)/2)                 #natoč se doleva o patřičný úhel
        for i in range(pocet):          #cyklus - dle počtu ramen   
            t.fd(a)                         #nakresli čáru dle velikosti
            kriziky(n-1, a/3, pocet)        #rekurzivní volání funkce s poníženými hodnotami
            t.fd(-(a))                  #nakresli čáru vedoucí zpátky dle aktuální rekurzivní velikosti
            t.lt(360/pocet)                 #natoč se doleva o patřičný úhel
        t.rt((360/pocet)/2)             #natoč se doprava o patřičný úhel
        
        

#výpočet:
a = 200                             #proměná pro velikost délky a výšky prvního kříže
t = turtle.Turtle()                 #vytvoření želvy
#t.speed(0)                          #zrychlení vykreslení
t.rt((360/pocet)/2)                 #natočení želvy doprava o patřičný úhel
kriziky(n, a, pocet)                #volání rekurzivní funkce pro nakreslení útvaru


#smyčka hlavního okna
turtle.mainloop()

