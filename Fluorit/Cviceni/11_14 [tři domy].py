##  Napíš funkciu dom(d),
##  ktorá nakreslí domček zo štvorca a rovnostranného trojuholníka tak, že po každej čiare prejde len raz.
##  Pozícia korytnačky na obrázku je pri štarte.
##  Po skončení kreslenia domčeka bude asi inde.
##  Teraz napíš ďalšie dve funkcie prerusovana_ciara(d) a cikcakova_ciara(d),
##  pomocou ktorých nakreslíme buď prerušovanú čiaru alebo cikcakovú čiaru.
##  Prerušovaná čiara označuje rozdelenie úsečky dĺžky d na 11 rovnakoveľkých častí,
##  pričom každá druhá sa prejde so zdvihnutým perom.
##  Cikcaková čiara označuje, že úsečka dĺžky d sa rozdelí na úseky dĺžky 5
##  a každý úsek sa nakreslí pod uhlom 60 ako dve strany rovnostranného trojuholníka
##  so stranou 5 (predpokladáme, že d je deliteľné číslom 5).
##  Ak by sme teraz vo funkcii dom nahradili volanie metódy t.fd(d)
##  buď volaním prerusovana_ciara(d) alebo cikcakova_ciara(d),
##  dostaneme domček z prerušovaných alebo cikcakových čiar.
##  Nepoužívaj metódu setpos.


#úvodní a prázdný řádek:
print('TŘI DOMY')
print('''pouze k zobrazení - program nakreslí v modulu turle 3 domy.
První normální čárou, druhý přerušovanou a třetí klikatou. ''')
print()


#prázdný řádek a příkaz pro spuštění okna grafické aplikace:
print()
input('[zmáčkni [Enter] pro zobrazení grafické aplikace]')


#definice funkce:
def prerusovana_ciara(d):           #definice funkce pro nakreslení přeručované čáry
    for i in range(11):                 #cyklus dle počtu úseků
        if i%2 == 0:                        #pokud jede o lichý úsek  
            t1.fd(d/11)                         #kresli čáru
        else:                               #pokud jede o sudý úsek  
            t1.pu()                             #zvedni pero
            t1.fd(d/11)                         #posuň se
            t1.pd()                             #polož pero

def cikcakova_ciara(d):             #definice funkce pro nakreslení přeručované čáry
    odpocet = d                         #proměnná pro odpočítávání zbylé části
    t1.fd(2)                            #posun dopředu pro vystředění klikaté čáry
    while odpocet:                      #cyklus dokud není odpočet prázdný
        t1.lt(130)                          #otoč se do leva
        t1.fd(5)                            #udělej čáru
        t1.rt(130)                          #otoč se do prava
        t1.fd(5)                            #udělej čáru
        odpocet -= 5                        #odečti z odpočtu 5
        
def dom1(d):                        #definice funkce pro kreslen domu rovnou čárou
    for i in range(2):                  #cyklus 2x
        t1.lt(120)                          #otoč se do leva
        t1.fd(d)                            #udělej čáru
    t1.lt(120)                          #otoč se do leva
    for i in range(4):                  #cyklus 4x
        t1.fd(d)                            #udělej čáru
        t1.rt(90)                           #otoč se doprava

def dom2(d):                        #definice funkce pro kreslen domu přerušovanou čárou
    for i in range(2):                  #cyklus 2x
        t1.lt(120)                          #otoč se do leva
        prerusovana_ciara(d)                #volání funkce pro nakreslení přerušované čáry
    t1.lt(120)                          #otoč se do leva
    for i in range(4):                  #cyklus 4x
        prerusovana_ciara(d)                #volání funkce pro nakreslení přerušované čáry
        t1.rt(90)                           #otoč se doprava

def dom3(d):                        #definice funkce pro kreslen domu klikatou čárou
    t1.rt(65)
    t1.fd(5)
    for i in range(2):                  #cyklus 2x
        t1.lt(120)                          #otoč se do leva
        cikcakova_ciara(d+10)               #volání funkce pro nakreslení klikaté čáry
    t1.lt(120)                          #otoč se do leva
    t1.fd(5)                            #posun dopředu pro vystředění klikaté čáry
    for i in range(4):                  #cyklus 4x
        cikcakova_ciara(d+10)               #volání funkce pro nakreslení klikaté čáry
        t1.rt(90)                           #otoč se doprava


#import modulů:
import turtle                       #import modulu turtle


#grafické okno:
t1 = turtle.Turtle()                #vytvoření grafického plátna a pera
#turtle.delay(0)                     #zrychlení vykresloení


#výpočet:
t1.pu()                             #zvedni pero
t1.bk(120)                          #posuň se dozadu
t1.pd()                             #polož pero
dom1(100)                           #volání funkce pro nakreslení věže z čtverců
t1.pu()                             #zvedni pero
t1.fd(240)                          #posuň se dopředu
t1.pd()                             #polož pero
dom2(100)                           #volání funkce pro nakreslení věže z čtverců
t1.pu()                             #zvedni pero
t1.fd(240)                          #posuň se dopředu
t1.lt(90)                           #otoč se doleva
t1.fd(5)                            #posuň se dopředu
t1.rt(90)                           #otoč se doprava
t1.pd()                             #polož pero
dom3(100)                           #volání funkce pro nakreslení věže z čtverců


#aktivace grafické aplikace
turtle.done()                       #hlavní smyčka grafického okna
