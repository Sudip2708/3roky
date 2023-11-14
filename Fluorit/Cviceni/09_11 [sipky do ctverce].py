##  Napíš funkciu sipka(xy1, xy2),
##  ktorá do grafickej plochy nakreslí šípku z bodu xy1 do bodu xy2.
##  Oba tieto parametre sú dvojice čísel (tuple), t.j. súradnice bodov.
##  Šípku kresli pomocou create_line,
##  v ktorej využiješ ďalší pomenovaný parameter arrow='last'
##  (podobné šípky sme kreslili v 15. úlohe z 5.cvičenia).
##  Teraz nakresli štyri šípky, ktoré nakreslia obrys takéhoto štvorca:	
##    import tkinter	
##            
##    def sipka(xy1, xy2):	
##        ...	
##            
##    canvas = tkinter.Canvas()	
##    canvas.pack()	
##            
##    canvas.create_rectangle(150, 50, 250, 150, fill='gold')	
##    sipka(...)	
##    sipka(...)	
##    sipka(...)	
##    sipka(...)	
##            
##    tkinter.mainloop()	
##    Mal by si dostať takýto obrázok:	


#úvodní a prázdný řádek:
print('ŠIPKY DO ČTVERCE')
print('''pouze k zobrazení - program obsahuje funkci, která kreslí šipku
z bodu A do bodu B, a v programu je použita k vykreslení čtverce.''')
print()


#prázdný řádek a příkaz pro spuštění okna grafické aplikace:
print()
input('[zmáčkni [Enter] pro zobrazení grafické aplikace]')


#definice funkce:
def sipka(xy1, xy2):
    canvas.create_line(xy1, xy2, arrow='last', width=4)     #příkaz na nakreslení šipky


#import modulů:
import random
import tkinter


#grafické okno:
canvas = tkinter.Canvas()
canvas.pack()


#proměnné:
a = (150, 50)                                               #proměná bodu čtverce
b = (250, 50)                                               #proměná bodu čtverce
c = (150, 150)                                              #proměná bodu čtverce
d = (250, 150)                                              #proměná bodu čtverce
sekvence = ((a, b), (b, d), (d, c), (c, a))                 #proměná pro sekvenci bodů pro kreslení šipek


#výpočet:
canvas.create_rectangle(a, d, fill='gold')                  #příkaz na nakreslení čtverce
for x, y in sekvence:                                       #cyklus - dle položek sekvence bodů pro kreslení šipek
    sipka(x, y)                                             #pvolání funkce sipka pro nakreslení šipky


#aktivace grafické aplikace:
tkinter.mainloop()  
