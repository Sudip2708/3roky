##  Gumený obdĺžnik: kliknutie naštartuje vytváranie obdĺžnika
##  (jeden vrchol je kliknutý bod a veľkosť je zatiaľ 0x0),
##  ťahanie aktualizuje jeho veľkosť, t.j. protiľahlý vrchol.
##    • prvé kliknutie nastaví náhodnú farbu výplne tohto obdĺžnika
##    • každé ďalšie kliknutie a ťahanie vytvára ďalší obdĺžnik
##    • otestuj tento program s „gumenou elipsou“:
##        - namiesto create_rectangle() daj create_oval()


#úvodní a prázdný řádek:
print('BAREVNÉ OBDELNÍKY 2 - "GUMOVÉ"')
print('''Program po kliknutí do grafické plochy lev. tl. myši a následným tažením,
vytváří obdelník vyplněný náhodnou barvou a po kliknutí pr. tl.
a následným tažením vytváří ovál vyplněný náhodnou barvou,
prostřední tl. maže plátno.''')
print()


#prázdný řádek a příkaz pro spuštění okna grafické aplikace:
print()
input('[zmáčkni [Enter] pro zobrazení grafické aplikace]')


#definice funkcí:
def proved_klik(x, y):                                      #výpočet hodnot pro tvorbu objektu
    global x1, y1, x2, y2, pocitadlo                        #odkaz na globální proměnnou 
    pocitadlo += 1                                          #přípočet do počítadlo objektů
    x1, y1 = x, y                                           #přiřazení proměných x1, y1 z eventu volající funkce
    x2, y2 = x, y                                           #přiřazení proměných x2, y2 z eventu volající funkce
    b = f'#{random.randrange(256**3):06x}'                  #vytvoření náhodné barvy
    return(x1, y1, x2, y2, b)                               #vrácení hodnot pro tvorbu objektu

def proved_tahej(x, y):                                     #provedení změny velikosti objektu
    global x1, y1, x2, y2, pocitadlo                        #odkaz na globální proměnnou
    x2, y2 = x, y                                           #přiřazení proměných x2, y2 z eventu volající funkce
    canvas.coords(pocitadlo, x1, y1, x2, y2)                #příkaz na změnu souřadnic

def klik1(event):                                           #tvorba objektu obdelník
    x1, y1, x2, y2, b = proved_klik(event.x, event.y)       #přiřaď proměnné pro tvorbu obdelníku voláním funkce"proved_klik"
    canvas.create_rectangle(x1, y1, x2, y2, fill=b)         #vytvoř obdelník

def tahaj1(event):                                          #změna velikosti objektu obdelník
    proved_tahej(event.x, event.y)                          #volání funkce "proved_tahej"

def klik2(event):                                           #vymazání plochy
    canvas.delete('all')                                    #příkaz na vymazání plochy    

def klik3(event):                                           #tvorba objektu ovál
    x1, y1, x2, y2, b = proved_klik(event.x, event.y)       #přiřaď proměnné pro tvorbu obdelníku voláním funkce"proved_klik"
    canvas.create_oval(x1, y1, x2, y2, fill=b)              #vytvoř ovál

def tahaj3(event):                                          #změna velikosti objektu ovál
    proved_tahej(event.x, event.y)                          #volání funkce "proved_tahej"

#import modulů:
import tkinter         
import random
        

#grafické okno:
canvas = tkinter.Canvas(bg='white', height=400, width=600)
canvas.pack()


#globální proměnná:
pocitadlo = 0                                               #proměnná pro počítadlo objektů
x1 = y1 = None                                              #prvotní nastavení os "x1" a "y1" na hodnotu "None"
x2 = y2 = None                                              #prvotní nastavení os "x2" a "y2" na hodnotu "None"
kruh = 0                                                    #proměnná pro přepínání mezi obdelníkem a kruhem


#propojení s funkcemi:
canvas.bind('<ButtonPress-1>', klik1)                       #tvorba objektu obdelník
canvas.bind('<B1-Motion>', tahaj1)                          #změna velikosti objektu obdelník
canvas.bind('<ButtonPress-2>', klik2)                       #vymazání plochy
canvas.bind('<ButtonPress-3>', klik3)                       #tvorba objektu ovál
canvas.bind('<B3-Motion>', tahaj3)                          #změna velikosti objektu ovál


#aktivace grafické aplikace:
tkinter.mainloop()
