##  Riešenie predchádzajúcej (14) úlohy uprav tak,
##  aby fungoval aj pre 2 rôzne veľké štvorce:
##  jeden červený veľkosti 50x50, druhý modrý veľkosti 100x100.
##  Vedel by si tento program upraviť tak,
##  aby fungoval pre ľubovoľný počet rôzne veľkých štvorcov v ploche?


#úvodní a prázdný řádek:
print('POHYBOVÁNÍ 4 OBJEKTY')
print('''Program vytvoří uprostřed plochy 4 objekty (2 čtverce a 2 kruhy),
s kterými je následně možné pohybovat po ploše.''')
print()


#prázdný řádek a příkaz pro spuštění okna grafické aplikace:
print()
input('[zmáčkni [Enter] pro zobrazení grafické aplikace]')


#definice funkcí:
def klik(event):
    'funkce je navázaná na kliknutí pravého tl. myši a resetuje nastavení globální proměnné "idx"'
    global idx                                                              #načtení globálních proměnných "a", "b", "idx"
    idx = None                                                              #nastavení proměnné "idx" na "None"

def hodnoty(n1, x1, y1, x2, y2):
    'funkce vypočítá a přiřadí do globálních proměnných "a", "b", "idx" příslušné hodnoty'
    global a, b, idx                                                        #načtení globálních proměnných "a", "b", "idx"
    idx = n1                                                                #nastav "idx" na číslo indexu prvku
    a = x2 - x1                                                             #přiřazení do proměnné "a" výpočet rozdílu v ose "x"
    b = y2 - y1                                                             #přiřazení do proměnné "b" výpočet rozdílu v ose "y"

def tahaj(event):
    'funkce je navázaná na táhnutí myši s pr. tl. a vybírá a vytváří hodnoty pro posun oběktu'
    global a, b, idx                                                        #načtení globálních proměnných "idx"
    x2, y2 = event.x, event.y                                               #přiřazení event "x", "y" do proměných "x"2, "y2"
    for n, prvk in enumerate(seznam[::-1]):                                 #cyklus - pro prvek z otočeného seznamu s jeho indexem
        if idx == None:                                                     #podmínka - pokud proměnná "idx" obsahuje hodnotu "None" (první průcho po kliknutí)
            x1, y1, vel, barva, tag = prvk                                  #přiřazení obsahu prvku do proměnných "x3", "y3", "vel", "barva", "tag"
            n1 = len(seznam)-(n+1)                                          #přiřazení proměné "n1" pro skutečný index položky seznamu
            if tag == 'ctvc':                                               #podmínka - pokud prvek ze seznamu je čtverec
                v1 = vel//2                                                 #výpočet a přiřazení proměnné "v1" pro odpočet os pro posun
                v2 = vel//2 + vel%2                                         #výpočet a přiřazení proměnné "v2" pro přípočet os pro posun
                if x2 in range(x1-v1, x1+v2) and y2 in range(y1-v1, y1+v2): #podmínka - pokud klik se nachází v pozici čtverce
                    hodnoty(n1, x1, y1, x2, y2)                             #volání funkce "hodnoty" která nastaví hodnoty globálních proměnných
            elif tag == 'kruh':                                             #podmínka - pokud prvek ze seznamu je kruh
                aa = abs(x1-x2)                                             #výpočet strany "A" pravoúhlého trojúhelníku dle osy "x1" a "x2"
                bb = abs(y1-y2)                                             #výpočet strany "B" pravoúhlého trojúhelníku dle osy "y1" a "y2"
                cc = int((aa**2+bb**2)**.5)                                 #výpočet strany "C" pravoúhlého trojúhelníku dle pytagorovy věty
                if cc < vel//2+1:                                           #podmínka - pokud klik se nachází v pozici kruhu
                    hodnoty(n1, x1, y1, x2, y2)                             #volání funkce "hodnoty" která nastaví hodnoty globálních proměnných
        else:                                                               #podmínka - pokud proměnná "idx" neobsahuje hodnotu "None" (obsahuje index objektu)
            x3 = x2 - a                                                     #výpočet a přiřazení proměnné "x3", x-ové osy pro posun
            y3 = y2 - b                                                     #výpočet a přiřazení proměnné "y3", y-ové osy pro posun
            v1 = seznam[idx][2]//2                                          #výpočet a přiřazení proměnné "v1" pro odpočet os pro posun
            v2 = seznam[idx][2]//2 + seznam[idx][2]%2                       #výpočet a přiřazení proměnné "v2" pro přípočet os pro posun
            canvas.coords(idx+1, x3-v1, y3-v1, x3+v2, y3+v2)                #posunu - změna souřadnic
            seznam[idx][0] = x3                                             #změna hodnot osy "x" v seznamu
            seznam[idx][1] = y3                                             #změna hodnot osy "y" v seznamu


#import modulů:
import tkinter    
        

#grafické okno:
canvas = tkinter.Canvas()
canvas.pack()


#provázání funkcí:
canvas.bind('<ButtonPress-1>', klik)
canvas.bind('<B1-Motion>', tahaj)


#globální proměnné:
a = b = None
idx = None


#parametry oběktů + seznam s objekty:
mod_ctv = [190, 130, 100, 'blue', 'ctvc']
zel_krh = [190, 130, 80, 'green', 'kruh']
cer_ctv = [190, 130, 50, 'red', 'ctvc']
zlt_krh = [190, 130, 40, 'yellow', 'kruh']
seznam = [mod_ctv, zel_krh, cer_ctv, zlt_krh]


#vykreslení oběktů:
for i in seznam:                                                            #cyklus - pro každý podseznam seznamu
    x, y, vel, barva, tag = i                                               #rozebrání podseznamu do příslušných proměnných
    v1 = vel//2                                                             #výpočet a přiřazení proměnné "v1" pro odpočet os pro posun
    v2 = vel//2 + vel%2                                                     #výpočet a přiřazení proměnné "v2" pro přípočet os pro posun
    if tag == 'kruh':                                                       #podmínka - pokud je objekt kruh
        canvas.create_oval(x-v1, y-v1, x+v2, y+v2, fill=barva)              #nakresli kruh dle parametrů
    elif tag == 'ctvc':                                                     #podmínka - pokud je objekt čtverec
        canvas.create_rectangle(x-v1, y-v1, x+v2, y+v2, fill=barva)         #nakresli čtverec dle parametrů


#aktivace grafické aplikace:
tkinter.mainloop()
