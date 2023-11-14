##  Najprv nakresli kruh so stredom (x0, y0) a polomerom r
##  (napríklad pre r, x0, y0 = 120, 150, 130).
##  Potom každé kliknutie do vnútra kruhu zmení farbu výplne
##  na odtieň šedej - čím bližšie do stredu tým tmavšie (v strede kruhu čierne),
##  ku okraju svetlejšie (na obvode biele).
##  Zrejme pri kliknutí vypočítaš vzdialenosť od stredu kruhu
##  a toto číslo potom prepočítaš na celé číslo od 0 do 255
##  (napríklad f = int(255 * vzd / r)).
##  Z tohto čísla vyrobíš šedý odtieň pre farbu kruhu (zrejme rgb(f, f, f)).
##  Nepoužívaj global.
##  Namiesto klikania môžeš otestovať ťahanie myšou.


#úvodní a prázdný řádek:
print('ČERNO-BÍLÝ KRUH')
print('''Program obsahuje 3 funkce, první při kliknutí lev. tl. do grafické plochy,
trefíli se do místa, kde je vytvořen zatím neviditelný kruh, ten změní barvu
ze škály od bílé po černou, podle toho, kde směrem od středu se klikne,
střed je černý, druhá funkce dělá to samé, ale plynule a to při stlačení
lev. tl. myši a následném tažení, třetí funkce kruh opět zneviditelní
a aktivuje se zmáčknutím pr. tl..''')
print()


#prázdný řádek a příkaz pro spuštění okna grafické aplikace:
print()
input('[zmáčkni [Enter] pro zobrazení grafické aplikace]')


#definice funkcí:
def proved(x, y):
    r, x0, y0 = 180, 200, 200                               #střed a poloměr kružnice
    a = abs(x0 - x)                                         #výpočet strany a
    b = abs(y0 - y)                                         #výpočet strany b
    c = (a**2 + b**2)**.5                                   #výpočet strany c, pro ověření vzdálenosti od středu kruhu
    if c < r:                                               #podmínka - pokud je klik uvnitř kruhu
        barva = int(255*c/r)                                #výpočet odstínu barvy
        barva2 = f'#{barva:02x}{barva:02x}{barva:02x}'      #výpočet textového zápisu barvy
        canvas.itemconfig('kruh', fill=barva2)              #příkaz na změnu barvy kruhu

def klik(event):
    proved(event.x, event.y)                                #volání funkce proveď

def tahaj(event):
    proved(event.x, event.y)                                #volání funkce proveď

def zmaz(event):
    canvas.itemconfig('kruh', fill='')                      #příkaz na smazání barvy kruhu


#import modulů:
import tkinter

        
#grafické okno:
canvas = tkinter.Canvas(height=400, width=400)
canvas.pack()


#proměnné a výpočet:
r, x0, y0 = 180, 200, 200
canvas.create_oval(x0-r, y0-r, x0+r, y0+r, tag='kruh', outline='')


#propojení s funkcemi:
canvas.bind('<ButtonPress-1>', klik)
canvas.bind('<B1-Motion>', tahaj)
canvas.bind('<ButtonPress-3>', zmaz)


#aktivace grafické aplikace:
tkinter.mainloop()

