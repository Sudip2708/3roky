##  Program zabezpečí klikanie myšou:
##  prvé kliknutie si zapamätá súradnice,
##  druhé kliknutie nakreslí obdĺžnik (create_rectangle),
##  v ktorom jeden vrchol je zapamätaný a druhý vrchol je práve kliknutý.
##  Obdĺžnik je zafarbený náhodnou farbou.
##  Toto sa opakuje pri ďalších klikaniach.
##    canvas.bind('<ButtonPress-1>', klik)
##    Napríklad:


#úvodní a prázdný řádek:
print('BAREVNÉ OBDELNÍKY')
print('''Program obsahuje 2 funkce, první při prvním kliknutí lev. tl.
do grafické plochy, si zapamatuje souřadnici místa,
a při druhém kliknutí vytvoří mezi těmito dvěma body
obdelník, který vyplná náhodnou barvou a druhá,
po zmáčknutí pravého tlačítka smaže obsah plochy.''')
print()


#prázdný řádek a příkaz pro spuštění okna grafické aplikace:
print()
input('[zmáčkni [Enter] pro zobrazení grafické aplikace]')


#definice funkcí:
def klik(event):
    global x, y                                                 #odkaz na globální proměnnou
    if x == None:                                               #podmínka - když proměná "x" obsahuje "None"
        x, y = event.x, event.y                                 #přiřaď souřadnice místa, do gl. proměnné "x" a "y"
    else:                                                       #podmínka - když proměná "x" neobsahuje "None" (obsahuje souřadnice)
        b = f'#{random.randrange(256**3):06x}'                  #vytvoř náhodnou barvu
        canvas.create_rectangle(x, y, event.x, event.y, fill=b) #vytvoř obdelním mezi 1. a 2. bodem
        x = y = None                                            #nastav gl. proměnné "x" a "y" na "None"

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
x = y = None


#propojení s funkcemi:
canvas.bind('<ButtonPress-1>', klik)
canvas.bind('<ButtonPress-3>', zmaz)


#aktivace grafické aplikace:
tkinter.mainloop()

