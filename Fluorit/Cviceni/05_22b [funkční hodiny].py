##  Napíš funkcie rucicka(uhol, dlzka, hrubka, farba) a hodinky(hod, min, sek),
##  pomocou ktorých nakreslíme ručičkové hodinky.
##  Funkcia rucicka nakreslí len jednu ručičku ako úsečku z bodu (190, 130) pod daným uhlom,
##  danej farby a hrúbky (podobne ako sa kreslil vektor v 15. úlohe).
##  Funkcia hodinky nakreslí ciferník (stačí kruh s polomerom 100)
##  a tri ručičky pre hodiny (dĺžka 60, hrúbka 10, farba 'gray'),
##  pre minúty (dĺžka 70, hrúbka 6, farba 'black'), pre sekundy (dĺžka 80, hrúbka 2, farba 'red').
##
##  Ak by si hodinky zavolal takto:
##    import time
##
##    while True:
##        canvas.delete('all')
##        h, m, s = time.localtime()[3:6]
##        hodinky(h, m, s)
##        canvas.update()
##        canvas.after(1000)
##
##  ukazovali by aktuálny čas.


#úvodní a prázdný řádek:
print('FUNKČNÍ HODINY')
print('program spustí hodiny')
print()


#prázdný řádek a příkaz pro spuštění okna grafické aplikace:
print()
input('[zmáčkni [Enter] pro zobrazení grafické aplikace]')


#moduly:
import tkinter
import math
import time


#vytvoření grafického prostředí:
canvas = tkinter.Canvas()
canvas.pack()


#proměné:
x0 = 190                                                                        #x-ová osa středu hodinek
y0 = 130                                                                        #y-ová osa středu hodinek


#definice funkce "hodinky":
def hodinky(hod, min, sek):
            
    canvas.create_oval(x0-110, y0-110, x0+110, y0+110, width=10, fill='grey')   #vytvoření vnějšího kruhu s poloměrem 110
    canvas.create_oval(x0-100, y0-100, x0+100, y0+100,  fill='light grey')      #vytvoření vnitřního kruhu s poloměrem 100
    
    for i in range(60):                                                         #cyklus 60x
        x1 = x0 + 90 * round(math.cos(math.radians((360/60)*(i+1) - 90)), 4)    #x-ová osa 2. bodu
        y1 = y0 + 90 * round(math.sin(math.radians((360/60)*(i+1) - 90)), 4)    #y-ová osa 2. bodu
        if s == i+1:                                                            #podmínka - pokus hodnota vteřin se shoduje s hodnotou i
            canvas.create_oval(x1-2, y1-2, x1+2, y1+2, fill='black')            #vykresli větší plný puntík
        else:                                                                   #ve všech ostatních případech
            canvas.create_oval(x1-1, y1-1, x1+1, y1+1)                          #vykresli malí prázdný puntík
        
    for i in range(12):                                                         #cyklus 12x
        x1 = x0 + 90 * round(math.cos(math.radians((360/12)*(i+1) - 90)), 4)    #x-ová osa 2. bodu
        y1 = y0 + 90 * round(math.sin(math.radians((360/12)*(i+1) - 90)), 4)    #y-ová osa 2. bodu
        if h == i+1 or h-12 == i+1:                                             #podmínka - pokus hodnota hodin se shoduje s hodnotou i
            canvas.create_oval(x1-7, y1-7, x1+7, y1+7, width=0, fill='light grey') 
            canvas.create_text(x1, y1, text=i+1, font=('arial black', 10))      #vykresli číslo
        else:                                                                   #ve všech ostatních případech
            canvas.create_oval(x1-2, y1-2, x1+2, y1+2)                          #vykresli větší prázdný puntík

    for i in range(60):                                                         #cyklus 60x
        x1 = x0 + 90 * round(math.cos(math.radians((360/60)*(i+1) - 90)), 4)    #x-ová osa 2. bodu
        y1 = y0 + 90 * round(math.sin(math.radians((360/60)*(i+1) - 90)), 4)    #y-ová osa 2. bodu
        if m == i+1:                                                            #podmínka - pokus hodnota minut se shoduje s hodnotou i
            canvas.create_oval(x1-7, y1-7, x1+7, y1+7, width=0, fill='light grey') 
            canvas.create_text(x1, y1, text=m, font=('arial black', 8))         #vykresli číslo


    uholh = (360/12)*hod - 90                                                   #výpočet úhlu pro hodiny
    uholm = (360/60)*min - 90                                                   #výpočet úhlu pro minuty
    uhols = (360/60)*sek - 90                                                   #výpočet úhlu pro vteřiny

    rucicka(uhols, 80, 2, 'red')                                                #volání funkce pro vteřinovou ručičku
    rucicka(uholm, 80, 6, 'black')                                              #volání funkce pro minutovou ručičku
    rucicka(uholh, 55, 10, 'black')                                             #volání funkce pro hodinovou ručičku

    canvas.create_oval(x0-5, y0-5, x0+5, y0+5, fill='black')                    #vytvoření kruhu ve středu kolem ručiček


#definice podfunkce "rucicka":
def rucicka(uhol, dlzka, hrubka, farba):                                        #parametry - úhel, délka, tloušťka, barva
    x2 = x0 + dlzka * round(math.cos(math.radians(uhol)), 4)                    #x-ová osa 2. bodu
    y2 = y0 + dlzka * round(math.sin(math.radians(uhol)), 4)                    #y-ová osa 2. bodu
    canvas.create_line(x0 ,y0, x2, y2, width=hrubka, fill=farba, arrow='last' ) #vytvoření linky


#výpočet:
while True:                                                                     #cyklus - dokud nevypnu okno
    canvas.delete('all')                                                        #vše nakreslené smazat
    h, m, s = time.localtime()[3:6]                                             #z modulu čas vytáhnout h, m, s
    hodinky(h, m, s)                                                            #zavolat funkci hodinky
    ts = time.strftime("%m. %d. %Y", time.localtime())                          #proměná pro datum
    
    canvas.create_rectangle(152, 160, 176, 180, fill='light grey')              #vytvoř pole pro hodiny
    canvas.create_text(165, 170, text=h, font=('arial black', 10))              #vepiš hodiny
    canvas.create_rectangle(178, 160, 202, 180, fill='light grey')              #vytvoř pole pro minuty
    canvas.create_text(190, 170, text=m, font=('arial black', 10))              #vepiš minuty
    canvas.create_rectangle(204, 160, 228, 180, fill='light grey')              #vytvoř pole pro vteřiny
    canvas.create_text(216, 170, text=s, font=('arial black', 10))              #vepiš vteřiny
    canvas.create_rectangle(162, 183, 218, 195, width=0, fill='light grey')     #vytvoř neviditelné pole pro datum
    canvas.create_text(190, 190, text=ts, font='arial 7' )                      #vepiš datum

    canvas.update()                                                             #aktualizovat canvas
    canvas.after(1000)                                                          #každou jednu vteřinu


#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]')    


#aktivace grafické aplikace:
tkinter.mainloop() 
