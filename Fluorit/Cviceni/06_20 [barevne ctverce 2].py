##  Úloha bude podobná predchádzajúcej: napíš funkciu stvorce(retazec),
##  ktorá dostáva v reťazci informáciu o veľkosti a farbe štvorcov. Funkcia
##  bude tieto štvorce kresliť vedľa seba, ale len dovtedy, kým by
##  nasledovný nevypadol z grafickej plochy (tento reťazec sa stále opakuje
##  od začiatku).
##
##  Do premennej sirka nastav nejakú šírku grafickej plochy a zavolaj funkciu,
##  napríklad takto:
##    sirka =450
##    canvas = tkinter.Canvas(width=sirka)
##    canvas.pack()
##
##    stvorce('40 red 20 blue 60 purple 40 red 30 gold')


#úvodní a prázdný řádek:
print('BAREVNÉ ČTVERCE 2')
print('pouze k zobrazení - funkce opakovaně (dokud stačí kreslící plocha) vytváří barevné čtverce dle zadaných barev a velikostí')
print()


#prázdný řádek a příkaz pro spuštění okna grafické aplikace:
print()
input('[zmáčkni [Enter] pro zobrazení grafické aplikace]')


#import modulů:
import tkinter


#grafické okno:
canvas = tkinter.Canvas(width=450)
canvas.pack()


#definice funkce:

def stvorce(retazec):
    r1 = retazec                                    #vytvoření dočasné proměné
    x = 5                                           #x levého strany čtverce
    y = 130                                         #y středu všech čtverců

    while x + (int(r1[:r1.find(' ')])) < 450:       #cyklus - dokud šířka čtverců nepřekročí šířku plochy
        šířka = int(r1[:r1.find(' ')])              #šířka čtverce
        r1 = r1[r1.find(' ')+1:]                    #odebrání šířky z dočasné promněné
        if r1.find(' ') != -1:                      #podmínka - dokud řetězec obsahuje mezeru
            barva = r1[:r1.find(' ')]               #použij tuto část pro barvu
            r1 = r1[r1.find(' ')+1:]                #odebrání barvy z dočasné promněné
        else:                                       #jinak
            barva = r1                              #použij zbytek řetězce jako barvu
            r1 = retazec                            #znovunastavení celého řetězce
        canvas.create_rectangle(x, y-(šířka//2), x+(šířka), y+(šířka//2), outline='', fill=barva )    #vytvoření čtverce
        x += šířka                                  #přípočet šířky pro další čtverec
    

#výpočet
stvorce('40 red 20 blue 60 purple 40 red 30 gold') 


#aktivace grafické aplikace
tkinter.mainloop()  
