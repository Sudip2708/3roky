##  Predstav si, že celá grafická plocha je štvorcová sieť,
##  ktorej štvorčeky majú veľkosť 50x50.
##  Napíš program, ktorý pri každom kliknutí do grafickej plochy
##  nakreslí náhodne zafarbený príslušný štvorček tejto siete
##  (pomocou create_rectangle()).
##  Nepoužívaj global.


#úvodní a prázdný řádek:
print('PLOCHA JAKO BAREVNÁ SÍŤ')
print('''Program obsahuje 2 funkce, první při kliknutí lev. tl. do grafické plochy,
která je složena z neviditelné čtvercové sítě, vybarví příslušné
políčko náhodnou barvou, druhá funkce po zmáčknutí pravého tlačítka
smaže obsah plochy.''')
print()


#prázdný řádek a příkaz pro spuštění okna grafické aplikace:
print()
input('[zmáčkni [Enter] pro zobrazení grafické aplikace]')


#definice funkcí:
def klik(event):
    x, y = event.x, event.y                                 #přiřazení proměných x, y z eventu funkce
    x1, x2 = (x//50)*50, (x//50+1)*50                       #výpočet os x pro výsledný čtverec
    y1, y2 = (y//50)*50, (y//50+1)*50                       #výpočet os y pro výsledný čtverec
    b = f'#{random.randrange(256**3):06x}'                  #vytvoř náhodnou barvu
    canvas.create_rectangle(x1, y1, x2, y2, fill=b)         #nakresli čtverec

def zmaz(event):
    canvas.delete('all')                                    #příkaz na smazání grafické plochy
    

#import modulů:
import tkinter
import random


#grafické okno:
canvas = tkinter.Canvas(bg='white', height=398, width=598)
canvas.pack()


#propojení s funkcemi:
canvas.bind('<ButtonPress-1>', klik)
canvas.bind('<ButtonPress-3>', zmaz)


#aktivace grafické aplikace:
tkinter.mainloop()
