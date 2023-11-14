##  Napíš program, ktorý pri každom kliknutí do grafickej plochy
##  vypíše na toto miesto poradové číslo kliknutia,
##  teda postupne čísla 1, 2, 3, 4, …
##  Nepoužívaj global (môžeš využiť globálnu premennú s nejakým zoznamom).


#úvodní a prázdný řádek:
print('POŘADOVÉ ČÍSLO KLIKNUTÍ')
print('''Program obsahuje 2 funkce, první při kliknutí lev. tl. do grafické plochy,
napíše na toto místo pořadové číslo kliknutí a nad číslo nakreslí tečku,
(dá se tak vytvářet spojovací hra), druhá funkce po zmáčknutí pravého
tlačítka smaže obsah plochy.''')
print()


#prázdný řádek a příkaz pro spuštění okna grafické aplikace:
print()
input('[zmáčkni [Enter] pro zobrazení grafické aplikace]')


#definice funkcí:
def klik(event):
    x, y = event.x, event.y                                 #přiřazení proměných x, y z eventu funkce
    canvas.create_text(x, y, text=zoznam[0])                #příkaz na vypsání čísla v grafické ploše
    canvas.create_oval(x-3, y-8, x+1, y-12, fill='black')   #příkaz na nakreslení tečky
    zoznam.insert(0, zoznam[0]+1)                           #příkaz na přidání na začátek seznamu o jedno vyšší číslo

def zmaz(event):
    canvas.delete('all')                                    #příkaz na smazání grafické plochy
    zoznam = [1,]                                           #vymazání seznamu a nastavení hodnoty "1"
    

#import modulů:
import tkinter


#grafické okno:
canvas = tkinter.Canvas(bg='white', height=400, width=600)
canvas.pack()


#propojení s funkcí:
canvas.bind('<ButtonPress-1>', klik)
canvas.bind('<ButtonPress-3>', zmaz)


#globální proměnná:
zoznam = [1,]


#aktivace grafické aplikace:
tkinter.mainloop()
