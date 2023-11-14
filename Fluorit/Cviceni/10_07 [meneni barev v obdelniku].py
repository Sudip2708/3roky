##  Najprv zadefinuj štyri premenné
##  (napríklad x1, y1, x2, y2 = 100, 50, 200, 100)
##  a pomocou nich nakresli farebný obdĺžnik.
##  Potom program pri každom kliknutí, ale len do vnútra obdĺžnika,
##  mu zmení farbu výplne.
##  Každé kliknutie do vnútra obdĺžnika cyklicky strieda jednu zo 4 farieb,
##  napríklad farby = ['blue', 'red', 'green', 'yellow'].
##  Nepoužívaj global.


#úvodní a prázdný řádek:
print('MĚNĚNÍ BAREV V OBDELNÍKU')
print('''Program obsahuje funkci, která při každém kliknutím levým tl. myši
dovnitř obdelníku, vykresleného v grafické ploše, změni jeho barvu,
postupným měněním těchto 4 barev: modrá, červená, zelená, žlutá.''')
print()


#prázdný řádek a příkaz pro spuštění okna grafické aplikace:
print()
input('[zmáčkni [Enter] pro zobrazení grafické aplikace]')


#definice funkcí:
def klik(event):
    x, y = event.x, event.y                                 #přiřazení proměných x, y z eventu funkce
    if x in range(x1, x2) and y in range(y1, y2):           #podmínka - pokud je "x" a "x" kliku uvnitř souřadnic obdelníku
        canvas.itemconfig('obdelnik', fil=farby[0])         #příkaz k změnění barvy obdelníku
        farby.append(farby.pop(0))                          #příkaz na vyjmutí první položky seznamu a vložení na poslední místo
    

#import modulů:
import tkinter


#grafické okno:
canvas = tkinter.Canvas(bg='white')
canvas.pack()


#proměnné a výpočet:
farby = ['blue', 'red', 'green', 'yellow']
x1, y1, x2, y2 = 70, 60, 310, 205
canvas.create_rectangle(x1, y1, x2, y2, tag='obdelnik')


#propojení s funkcemi:
canvas.bind('<ButtonPress-1>', klik)


#aktivace grafické aplikace:
tkinter.mainloop()
