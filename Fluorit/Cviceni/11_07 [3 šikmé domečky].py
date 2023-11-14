##  Napíš funkciu domcek(d),
##  ktorá nakreslí domček jedným ťahom, bez dvíhania pera a bez setpos,
##  teda pomocou 8 úsečiek (príkazov forward).
##  Veľkosť štvorca je d, všetky vnútorné uhly sú 45 stupňov.
##  Otestuj:
##    t.rt(5)
##    domcek(100)
##    domcek(50)
##    domcek(80)


#úvodní a prázdný řádek:
print('ŠIKMÉ DOMEČKY')
print('''pouze k zobrazení - program kreslí v modulu turle
3 šikmé domečky jedním tahem. ''')
print()


#prázdný řádek a příkaz pro spuštění okna grafické aplikace:
print()
input('[zmáčkni [Enter] pro zobrazení grafické aplikace]')


#definice funkce:
def domcek(s):                              #definice funkce pro kreslení domečku jedním tahem
    x = (2*(s**2))**.5                      #výpočet strany 'c' pravoůhlého trojůhelníku (str 'a' a 'b' jsou stejné)
    a = (45, x)                             #hodnoty délky a úhlu pro 1. čáru
    b = (90, x/2)                           #hodnoty délky a úhlu pro 2. a 3. čáru
    c = (90, x)                             #hodnoty délky a úhlu pro 4. čáru
    d = (135, s)                            #hodnoty délky a úhlu pro 5. čáru
    e = (90, s)                             #hodnoty délky a úhlu pro 6., 7. a 8. čáru
    for u, v in a, b, b, c, d, e, e, e:     #cyklus dle počtu čar (8)
        t1.lt(u)                                #natočení o hodnotu úhlu
        t1.fd(v)                                #nakreslení čáry


#import modulů:
import turtle                               #import modulu turtle


#grafické okno:
t1 = turtle.Turtle()                        #vytvoření grafického plátna a pera
#turtle.delay(0)                             #zrychlení vykresloení


#výpočet:
t1.rt(5)                                    #natočení úhlu pera
domcek(100)                                 #volání funkce pro 1. domeček
domcek(50)                                  #volání funkce pro 2. domeček
domcek(80)                                  #volání funkce pro 3. domeček


#aktivace grafické aplikace
turtle.done()                               #hlavní smyčka grafického okna
