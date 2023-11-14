##  Gumená úsečka:
##  kliknutie naštartuje vytváranie úsečky
##  (najprv prvý aj druhý bod úsečky je samotný kliknutý bod, teda jej veľkosť je 0),
##  ťahanie aktualizuje jej druhý bod (použi metódu canvas.coords()).
##  Každé ďalšie kliknutie a ťahanie vytvára ďalšiu úsečku.


#úvodní a prázdný řádek:
print('TAHÁNÍ ÚSEČKY')
print('''Program po kliknutí do grafické plochy vytvoří bod, z něhož po té
tažením myši táhne čáru a každým dalším kliknutím ji ukotvuje na plátně.
Pravým tl. myši ukončuje kreslení a prostředním tl., myši maže plátno.''')
print()


#prázdný řádek a příkaz pro spuštění okna grafické aplikace:
print()
input('[zmáčkni [Enter] pro zobrazení grafické aplikace]')


#definice funkcí:
def klik1(event):                           #bod z kterého bude tažena linka
    global x1, y1, n                        #odkaz na globální proměnnou    
    x1, y1 = event.x, event.y               #přiřazení proměných x1, y1 z eventu funkce
    canvas.create_line(x1, y1, x1, y1)      #příkaz na vytvoření linky
    n += 1                                  #přípočet do počítadla linek

def tahaj(event):                           #natahování linky
    global x1, y1, n                        #odkaz na globální proměnnou
    x2, y2 = event.x, event.y               #přiřazení proměných x2, y2 z eventu funkce
    if x1 != None:                          #podmínka - když proměnná "x1" není "None"
        canvas.coords(n, x1, y1, x2, y2)    #změň souřadnici druhého bodu u linky

def klik2(event):                           #vymazání plochy
    canvas.delete('all')                    #příkaz na vymazání plochy
    
def klik3(event):                           #ukončení kreslení
    global x1, y1, n                        #odkaz na globální proměnnou
    x2, y2 = event.x, event.y               #přiřazení proměných x2, y2 z eventu funkce
    canvas.coords(n, x1, y1, x2, y2)        #změň souřadnici druhého bodu u linky
    x1 = y1 = None                          #nastav globální proměnné "x1" a "y1" na hodnotu "None"

#import modulů:
import tkinter    
        

#grafické okno:
canvas = tkinter.Canvas(bg='white', height=400, width=600)
canvas.pack()


#globální proměnná:
n = 0                                       #počítadlo
x1 = y1 = None                              #proměnná "x1" a "y1"


#propojení s funkcemi:
canvas.bind('<ButtonPress-1>', klik1)       #bod z kterého bude tažena linka
canvas.bind('<ButtonPress-2>', klik2)       #vymazání plochy
canvas.bind('<ButtonPress-3>', klik3)       #ukončení kreslení
canvas.bind('<Motion>', tahaj)              #natahování linky


#aktivace grafické aplikace:
tkinter.mainloop()
