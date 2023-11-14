##  Napíš program, ktorý zabezpečí ťahanie myši:
##  pri ťahaní so zatlačeným ľavým tlačidlom sa kreslia vodorovné úsečky
##  (z kliknutej pozície dĺžky 100).
##  Pravým klikom sa obrazovka zmaže.
##  V programe zabezpeč zviazanie týchto dvoch ovládačov:
##    canvas.bind('<B1-Motion>', kresli)
##    canvas.bind('<ButtonPress-3>', zmaz)
##    Po spustení a ťahaní môžeš dostať, napríklad:


#úvodní a prázdný řádek:
print('VODOROVNÉ BAREVNÉ ČÁRY')
print('''Program obsahuje 2 funkce, první při tažení myši se zmáčknutým
levým tlačítkem kreslí barevné vodorovné čáry a druhá,
po zmáčknutí pravého tlačítka smaže obsah plochy.''')
print()


#prázdný řádek a příkaz pro spuštění okna grafické aplikace:
print()
input('[zmáčkni [Enter] pro zobrazení grafické aplikace]')


#definice funkcí:
def kresli(event):
    'funkce kreslí barevné vodorovné čáry při pohybu myši se zmáčknutým levým tl.'
    x, y = event.x, event.y                                 #přiřazení proměných x, y z eventu funkce
    b = f'#{random.randrange(256**3):06x}'                  #náhodná barva
    canvas.create_line(x-50, y, x+50, y, width=2, fill=b)   #příkaz na tvorbu linky

def zmaz(event):
    'funkce smaže obsah plátna po zmáčknutí pravého tl.'
    canvas.delete('all')                                    #příkaz na smazání grafické plochy


#import modulů:
import tkinter
import random


#grafické okno:
canvas = tkinter.Canvas(bg='white', height=500, width=700)
canvas.pack()


#propojení s funkcemi:
canvas.bind('<B1-Motion>', kresli) 
canvas.bind('<ButtonPress-3>', zmaz)


#aktivace grafické aplikace:
tkinter.mainloop()
