##  Program počas ťahania myši zabezpečí kreslenie žltých krúžkov,
##  prvý s polomerom 1, každý ďalší je o 1 väčší.
##  Pravým klikom sa obrazovka zmaže a nastaví sa kreslenie
##  od najmenšieho krúžku (s polomerom 1).
##  V programe zabezpeč zviazanie dvoch ovládačov:
##    canvas.bind('<B1-Motion>', kresli)
##    canvas.bind('<ButtonPress-3>', zmaz)
##    Po spustení a ťahaní môžeš dostať, napríklad:


#úvodní a prázdný řádek:
print('ZVĚČUJÍCÍ SE ŽLUTÝ KRUH')
print('''Program obsahuje 2 funkce, první při tažení myši se zmáčknutým
levým tlačítkem kreslí zvěčující se žlutý kruh a druhá,
po zmáčknutí pravého tlačítka smaže obsah plochy.''')
print()


#prázdný řádek a příkaz pro spuštění okna grafické aplikace:
print()
input('[zmáčkni [Enter] pro zobrazení grafické aplikace]')


#definice funkcí:
def kresli(event):
    'funkce při tažení myši se zmáčknutým levým tl. kreslí zvěčující se žlutý kruh'
    global n                                                #odkaz na globální proměnnou
    x, y = event.x, event.y                                 #přiřazení proměných x, y z eventu funkce
    canvas.create_oval(x-n, y-n, x+n, y+n, fill='yellow')   #příkaz na tvorbu kruhu
    n += 1                                                  #přičtení hodnoty"1" do globální proměnné

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
n = 1


#propojení s funkcemi:
canvas.bind('<B1-Motion>', kresli) 
canvas.bind('<ButtonPress-3>', zmaz)


#aktivace grafické aplikace:
tkinter.mainloop()
