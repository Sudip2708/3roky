##  Napíš funkciu kresli(r, zoznam),
##  ktorá z daného zoznamu farieb nakreslí rad farebných kruhov,
##  Každý kruh má polomer r.
##  Funkcia nemodifikuje vstupný zoznam.
##  Napríklad:
##    importtkinter
##    defkresli(r, zoznam):
##    ...
##    canvas = tkinter.Canvas()
##    canvas.pack()
##    kresli(20, ['red', 'red', 'blue', 'orange', 'green', 'yellow'])
##    tkinter.mainloop()
##    nakreslí:


#úvodní a prázdný řádek:
print('ŘADA BAREVNÝCH KRUHŮ')
print('''pouze k zobrazení - program obsahuje funkci, která našte seznam barev
a průměr kruhu a v grafickém prostředí vykreslí barevné kruhy''')
print()


#prázdný řádek a příkaz pro spuštění okna grafické aplikace:
print()
input('[zmáčkni [Enter] pro zobrazení grafické aplikace]')


#definice funkce:
def kresli(r, seznam):
    x = 2*r
    y = 130
    for i in seznam:
        canvas.create_oval(x-r, y-r, x+r, y+r, fill=i)
        x += 2*r 


#import modulů:
import tkinter


#grafické okno:
canvas = tkinter.Canvas()
canvas.pack()


#výpočet:
kresli(27, ['red', 'red', 'blue', 'orange', 'green', 'yellow'])


#aktivace grafické aplikace
tkinter.mainloop()  
