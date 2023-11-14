##  Podobne ako v (3) úlohe:
##  pri každom kliknutí sa na danej pozícii nakreslí '+' (create_text),
##  pritom pri prvých dvoch kliknutiach sa tieto body zapamätajú.
##  Tretie z týchto troch kliknutí nakreslí náhodne zafarbený trojuholník
##  (create_polygon).
##  Zoznam zapamätaných bodov má momentálne 3 vrcholy.
##  Teraz sa z tohto zapamätaného zoznamu vyhodí prvý prvok
##  a pokračuje sa ďalej s dvomi vrcholmi:
##  ďalšie kliknutie pridá do zoznamu 3. vrchol,
##  nakreslí trojuholník a prvý vrchol sa opäť vyhodí.
##  Môžeš dostať, napríklad:


#úvodní a prázdný řádek:
print('BAREVNÉ SPOJENÉ TROJŮHELNÍKY')
print('''Program obsahuje 2 funkce, první při prvním a druhém kliknutí
lev. tl. do grafické plochy, nakreslí na místo znak "+"
a zapamatuje si souřadnice, a při třetím kliknutí
nakreslí mezi body trojúhelník vyplněný náhodnou barvou,
a při každém dalším kliknutí, kreslí další trojůhelník
z posledních 3 pozic a vyplní ho náhodnou barvou a druhá,
po zmáčknutí pravého tlačítka smaže obsah plochy.''')
print()


#prázdný řádek a příkaz pro spuštění okna grafické aplikace:
print()
input('[zmáčkni [Enter] pro zobrazení grafické aplikace]')


#definice funkcí:
def klik(event):
    global x1, y1, x2, y2                                               #odkaz na globální proměnnou
    canvas.create_text(event.x, event.y, text='+')                      #příkaz na nakreslení znaku "+"
    if x1 == None:                                                      #podmínka - pokud "x1" obsahuje "None" (nemá v sobě souřadnice)
        x1, y1 = event.x, event.y                                       #zapiš do proměných "x1" a "y1" souřadnice daného místa
    elif x2 == None:                                                    #podmínka - pokud "x2" obsahuje "None" (nemá v sobě souřadnice)
        x2, y2 = event.x, event.y                                       #zapiš do proměných "x2" a "y2" souřadnice daného místa
    else:                                                               #podmínka - pokud "x1" a "x2" obsahují souřadnice
        b = f'#{random.randrange(256**3):06x}'                          #vytvoř náhodnou barvu
        canvas.create_polygon(x1, y1, x2, y2, event.x, event.y, fill=b) #vytvoř trojúhelník z těchto tří souřadnic
        x1, y1 = x2, y2                                                 #do proměnné "x1" a "y1" přidaj hodnoty z "x2" a "y2"
        x2, y2 = event.x, event.y                                       #do proměnné "x2" a "y2" přidaj hodnoty z "event.x" a "event.y"

def zmaz(event):
    'funkce po zmáčknutí pravého tl. smaže obsah plátna a nastaví gl. pr. na hodnotu "1"'
    global n                                                #odkaz na globální proměnnou
    canvas.delete('all')                                    #příkaz na smazání grafické plochy
    n = 1                                                   #nastavení gl. pr. na hodnotu "1"
    

#import modulů:
import tkinter
import random


#grafické okno:
canvas = tkinter.Canvas(bg='white', height=500, width=700)
canvas.pack()


#globální proměnná:
x1 = y1 = x2 = y2 = None


#propojení s funkcemi:
canvas.bind('<ButtonPress-1>', klik)
canvas.bind('<ButtonPress-3>', zmaz)


#aktivace grafické aplikace:
tkinter.mainloop()
