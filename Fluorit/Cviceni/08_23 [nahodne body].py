##  Napíš funkciu nahodne_body(n),
##  ktorá vygeneruje (vráti) zoznam čísel dĺžky 2*n v tvare [x, y, x, y, …].
##  Tieto čísla sú súradnicami n náhodných vrcholov štvorca v grafickej ploche.
##  x-ové súradnice generuj z intervalu <10, 370>
##  a y-ové z intervalu <10, 250>.
##  Ak by si tento zoznam poslal ako parameter do grafického príkazu
##  canvas.create_polygon, dostaneš vyfarbený náhodný n-uholník.
##  Napríklad:
##    import tkinter
##    import random
##    def nahodne_body(n):
##        ...
##    canvas = tkinter.Canvas()
##    canvas.pack()
##    canvas.create_polygon(nahodne_body(10), fill='yellow', outline='blue')
##    tkinter.mainloop()
##    nakreslí:


#úvodní a prázdný řádek:
print('NÁHODNÉ BODY')
print('''program obsahuje funkci, která vygeneruje dle zadaného počtu, náhodný
seznam souřadnic, které pak grafický program překreslý do grafického prostředí,
pospojuje modrou čárou a vyplní žlutou barvou.''')
print()


#vstup:
print()
n = int(input('Zadej počet bodů: '))


#definice funkce:
def nahodne_body(n):
    seznam = []
    for i in range(n):
        seznam.append(random.randint(10, 370))
        seznam.append(random.randint(10, 250))
    return seznam


#import modulů:
import tkinter
import random


#grafické okno:
canvas = tkinter.Canvas()
canvas.pack()


#výpočet
canvas.create_polygon(nahodne_body(n), fill='yellow', outline='blue')


#aktivace grafické aplikace
tkinter.mainloop() 
