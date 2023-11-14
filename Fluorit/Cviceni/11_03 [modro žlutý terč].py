##  Napíš funkciu terc(pocet),
##  ktorá pomocou korytnačej metódy t.dot(...) nakreslí zadaný počet rôzne veľkých bodiek:
##  najmenšia má veľkosť 15, každá ďalšia je o 15 väčšia.
##  Najväčšia bodka nech je modrá, menšia žltá a takto sa ďalej striedajú tieto dve farby na všetky bodky.
##  Otestuj napríklad terc(40):


#úvodní a prázdný řádek:
print('MODRU ŽLUTÝ TERČ')
print('''pouze k zobrazení - program generuje v modulu turle
40 do sebe zapušťěných modrých a žlutých kruhů (teček). ''')
print()


#prázdný řádek a příkaz pro spuštění okna grafické aplikace:
print()
input('[zmáčkni [Enter] pro zobrazení grafické aplikace]')


#definice funkce:
def terc(pocet):                            #definice funkce pro nakreslení terče
    barva1, barva2 = 'blue', 'yellow'           #proměnné pro barvy
    sirka = 15                                  #hodnota šířky zmenčení
    for i in range(pocet):                      #cyklus dle počtu
        velikost = pocet*sirka - i*sirka            #výpočet velikosti pro nakreslení bodu
        t1.dot(velikost, barva1)                    #nakreslení bodu
        barva1, barva2 = barva2, barva1             #prohození barev


#import modulů:
import turtle                               #import modulu turtle


#grafické okno:
t1 = turtle.Turtle()                        #vytvoření grafického plátna a pera
#turtle.delay(0)                             #zrychlení vykresloení


#výpočet:
terc(40)                                    #volání funkce pro nakreslení terče


#aktivace grafické aplikace
turtle.done()                               #hlavní smyčka grafického okna
