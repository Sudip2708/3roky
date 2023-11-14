##Rekurzívna krivka je popísaná takýmto predpisom:
##    
## >obrázek je v zadání<
## 
##Napíš funkciu kriziky4(n, a),
##v ktorej prvý parameter n označuje úroveň krivky,
##druhý parameter a dĺžku ramena kríža.
##Na všetkých piatich obrázkov je rovnaké a.
##Vnorené krížiky majú tretinovú dĺžku.
##Pre n = 0 funkcia nekreslí nič.


#úvodní a prázdný řádek:
print('REKURZIVNĚ KRESLENÉ KŘÍŽE')
print(f'''Program dle zadaného počtu zanoření (1 - 5),
nakreslí křiž a dle hodnoty zapučtění nakreslí
na každém konci další kříž..''')
print()


#vstupní data:
n = int(input('Zadej hodnotu zanoření: '))  


#import modulů:
import turtle


#definice funkce:
def kriziky4(a, n):         #rekurzivní funkce pro nakreslení křížů
    if n == 0:                  #podmínka - když velikost strany je 0
        pass                        #nedělej nic
    else:                       #podmínka - dokud velikost strany není 0
        t.lt(45)                    #natoč se doleva o 45°
        for i in range(4):          #cyklus - 4x          
            t.fd(a)                     #nakresli čáru dle velikosti
            kriziky4(a/3, n-1)          #rekurzivní volání funkce s poníženými hodnotami
            t.fd(-(a))                  #nakresli čáru vedoucí zpátky dle aktuální rekurzivní velikosti
            t.lt(90)                    #otoč se doleva o 90°   
        t.rt(45)                    #natoč se doprava o 45°
        

#výpočet:
a = 200                     #proměná pro velikost délky a výšky prvního kříže
t = turtle.Turtle()         #vytvoření želvy
#t.speed(0)                  #zrychlení vykreslení
t.rt(45)                    #natoč se doprava o 45°
kriziky4(a, n)              #volání rekurzivní funkce pro nakreslení křížů


#smyčka hlavního okna
turtle.mainloop()
