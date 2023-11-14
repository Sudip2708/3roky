##  Do riešenia predchádzajúcej (17) úlohy pridaj ďalší pohybujúci sa modrý kruh,
##  ktorého uhol posunu bude iný, napríklad 15 stupňov.
##    • experimentuj s rôznymi rýchlosťami pohybu oboch kruhov po kružnici
##    (prípadne sa jeden z nich pohybuje opačným smerom)
##    • ak by sa farebné kruhy pohybovali po rôznych kružniciach,
##    mohli by sme simulovať pohyb planét okolo slnka




#úvodní a prázdný řádek:
print('KOLEČKO ZRYCHLUJE A ZPOMALUJE KOLEČKEM MYŠI')
print('''Program vytvoří uprostřed plochy větší modrý kruh
a malé červené a bílé kolečko, které ho obíhají. Červené kolečko
obíhá stejnou rychlostí a bílé, které je pod ním se ovládá kolečkem
myši, kdy 10x může zrychlit a nebo zpomalit a to i opačným směrem''')
print()


#prázdný řádek a příkaz pro spuštění okna grafické aplikace:
print()
input('[zmáčkni [Enter] pro zobrazení grafické aplikace]')


#import modulů:
import tkinter
import math

    
#grafické okno:
canvas = tkinter.Canvas()
canvas.pack()

def kolecko_mys(event):                                                                 #definice funkce - pro čtení kolečka myši
    if event.delta > 0:                                                                 #podmínka - pokud pohyb dává kladné číslo
        if u2[1] < 10:                                                                  #podmínka - pokud není přírůstek úhlu posunu větší než 10
            u2[1] += 1                                                                  #připočti k hodnotě posunu úhlu 1
    else:                                                                               #podmínka - pokud pohyb kolečkem myši dává zápornou hodnotu
        if u2[1] > -10:                                                                 #podmínka - pokud není přírůstek úhlu posunu menší než 10
            u2[1] -= 1                                                                  #odečti od hodnoty posunu 1

#definice funkcí:
def casovac():
    x2 = x0 + r0 * round(math.cos(math.radians(u1[0])), 4)                              #výpočet osy "x" dle načteného úhlu a osy "x" většího kruhu
    y2 = y0 + r0 * round(math.sin(math.radians(u1[0])), 4)                              #výpočet osy "y" dle načteného úhlu a osy "y" většího kruhu
    canvas.coords(cislo_obj1, x2-r1, y2-r1, x2+r1, y2+r1)                               #změna souřadnic 1 menšího kruhu
    u1[0] += 1                                                                          #výpočet úhlu pro příští posun

    x3 = x0 + r0 * round(math.cos(math.radians(u2[0])), 4)                              #výpočet osy "x" dle načteného úhlu a osy "x" většího kruhu
    y3 = y0 + r0 * round(math.sin(math.radians(u2[0])), 4)                              #výpočet osy "y" dle načteného úhlu a osy "y" většího kruhu
    canvas.coords(cislo_obj2, x3-r1, y3-r1, x3+r1, y3+r1)                               #změna souřadnic 2 menšího kruhu
    u2[0] += u2[1]                                                                      #výpočet úhlu pro příští posun

    canvas.after(10, casovac)                                                           #nastavení časovače pro další zpuštění funkce "casovac"


#proměnné:
r0, x0, y0 = 100, 190, 130                                                              #proměné - pro hodnoty x, y a r většího kruhu
r1, x1, y1 = 5, 180, 15                                                                 #proměné - pro hodnoty x, y a r menších kruhů
u1 = [1]                                                                                #proměná (seznam) pro hodnotu úhlu prvního pohyblivého kruhu
u2 = [10, 1]                                                                            #proměná (seznam) pro hodnotu úhlu a posunu druhého pohyblivého kruhu

#vytvoření kruhů a volání funkce
canvas.create_oval(x0-r0, y0-r0, x0+r0, y0+r0, fill='blue', outline='')                 #vytvoření velkého kruhu
cislo_obj1 = canvas.create_oval(x1-r1, y1-r1, x1+r1, y1+r1, fill='red', outline='')     #vytvoření 1. menšího pohyblivého kruhu a vytvoření proměné s jeho číslem
cislo_obj2 = canvas.create_oval(x1-r1, y1-r1, x1+r1, y1+r1, fill='white')               #vytvoření 2. menšího pohyblivého kruhu a vytvoření proměné s jeho číslem
canvas.bind('<MouseWheel>', kolecko_mys)                                                #provázání pohybu kolečka myši
casovac()                                                                               #aktivace časovače

#aktivace grafické aplikace:
tkinter.mainloop()
