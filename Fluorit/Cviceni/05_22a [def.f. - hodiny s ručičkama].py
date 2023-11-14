##  Napíš funkcie rucicka(uhol, dlzka, hrubka, farba) a hodinky(hod, min, sek),
##  pomocou ktorých nakreslíme ručičkové hodinky.
##  Funkcia rucicka nakreslí len jednu ručičku ako úsečku z bodu (190, 130) pod daným uhlom,
##  danej farby a hrúbky (podobne ako sa kreslil vektor v 15. úlohe).
##  Funkcia hodinky nakreslí ciferník (stačí kruh s polomerom 100)
##  a tri ručičky pre hodiny (dĺžka 60, hrúbka 10, farba 'gray'),
##  pre minúty (dĺžka 70, hrúbka 6, farba 'black'), pre sekundy (dĺžka 80, hrúbka 2, farba 'red').
##
##  Napríklad volanie:
##    hodinky(8, 55, 10)


#úvodní a prázdný řádek:
print('VZHLED HODIN')
print('funkce na vytvoření vzhledu hodin \npouze zobrazení výsledku dle předem daného zadání')
print()


#prázdný řádek a příkaz pro spuštění okna grafické aplikace:
print()
input('[zmáčkni [Enter] pro zobrazení grafické aplikace]')


#moduly:
import tkinter
import math


#definice funkce:
def rucicka(uhol, dlzka, hrubka, farba):                                        #parametry - úhel, délka, tloušťka, barva
    x2 = x0 + dlzka * round(math.cos(math.radians(uhol)), 4)                    #x-ová osa 2. bodu
    y2 = y0 + dlzka * round(math.sin(math.radians(uhol)), 4)                    #y-ová osa 2. bodu
    canvas.create_line(x0 ,y0, x2, y2, width=hrubka, fill=farba, arrow='last' ) #vytvoření linky
    


def hodinky(hod, min, sek):
    canvas.create_oval(x0-100, y0-100, x0+100, y0+100)                          #vytvoření kruhu s poloměrem 100

    uholh = (360/12)*hod - 90                                                   #výpočet úhlu pro hodiny
    uholm = (360/60)*min - 90                                                   #výpočet úhlu pro minuty
    uhols = (360/60)*sek - 90                                                   #výpočet úhlu pro vteřiny

    rucicka(uholh, 60, 10, 'gray')                                              #volání funkce pro hodinovou ručičku
    rucicka(uholm, 70, 6, 'black')                                              #volání funkce pro minutovou ručičku
    rucicka(uhols, 80, 2, 'red')                                                #volání funkce pro vteřinovou ručičku


#vytvoření grafického prostředí:
canvas = tkinter.Canvas()
canvas.pack()


#proměné:
x0 = 190                                                                        #x-ová osa středu hodinek
y0 = 130                                                                        #y-ová osa středu hodinek


#výpočet:
hodinky(6, 55, 10)


#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]')    


#aktivace grafické aplikace:
tkinter.mainloop() 
