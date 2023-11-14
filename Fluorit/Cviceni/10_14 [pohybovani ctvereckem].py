##  V ploche sa nachádza jeden červený štvorček veľkosti 50x50.
##  Keď klikneme do jeho vnútra (počíta sa aj obvod),
##  môžeme ho ťahať, teda posúvať po ploche pomocou pohybov myši
##  (inak ťahanie s kliknutím mimo štvorček nerobí nič).
##    • daj pozor, aby aj malé posunutie myši počas ťahania neurobilo
##    jeho neúmerne veľký skok
##    (môžeme ho chytiť a ťahať napríklad aj za ľubovoľný vrchol)
##    • pri kliknutí do vnútra štvorčeka si môžeš niekde zapamätať
##    posunutie kliknutého bodu od ľavého horného rohu štvorčeka
##    a toto posunutie využiješ pri prekreslení štvorčeka
##    na nových pozíciách (pomocou canvas.coords() alebo canvas.move())


#úvodní a prázdný řádek:
print('POHYBOVÁNÍ ČTVEREČKEM')
print('''Program vytvoří uprostřed plochy modrý čtvereček, s kterým je možné
následně pohybovat po ploše.''')
print()


#prázdný řádek a příkaz pro spuštění okna grafické aplikace:
print()
input('[zmáčkni [Enter] pro zobrazení grafické aplikace]')


#definice funkcí:
def klik(event):
    global a, b                                             #odkaz na globální proměnnou "a", "b"   
    a = b = None                                            #nastav globální proměnné "a", "b" na hodnotu "None"

def tahaj(event):
    global x1, y1, a, b                                     #odkaz na globální proměnnou "x1", "y1", "a", "b"   
    x2, y2 = event.x, event.y                               #přiřazení proměných x2, y2 z eventu funkce
    if x2 in range(x1, x1+50) and y2 in range(y1, y1+50):   #podmínka - když osy "x2", "y2" (kliknutí) jsou uvnitř čtverce
        if a == None:                                       #podmínka - když gl. pr. "a" je má hodnotu "None"
            a = x2 - x1                                     #nastav hodnotu "a" (rozdíl mezi "x1 a "x2")
            b = y2 - y1                                     #nastav hodnotu "b" (rozdíl mezi "y1 a "y2")
        else:                                               #podmínka - když gl. pr. "a" je nemá hodnotu "None"
            x1 = x2 - a                                     #vypočti "x1" (rozdíl mezi "x2" a "a")
            y1 = y2 - b                                     #vypočti "y1" (rozdíl mezi "y2" a "b")
            canvas.coords(1, x1, y1, x1+50, y1+50)          #změň souřadnice
   

#import modulů:
import tkinter
import random

    
#grafické okno:
canvas = tkinter.Canvas()
canvas.pack()


#globální proměnná:
x1, y1 = 170, 100
a = b = None


#vytvoření čtverce
canvas.create_rectangle(x1, y1, x1+50, y1+50, fill='blue')


#propojení s funkcemi:
canvas.bind('<ButtonPress-1>', klik)
canvas.bind('<B1-Motion>', tahaj)


#aktivace grafické aplikace:
tkinter.mainloop()
