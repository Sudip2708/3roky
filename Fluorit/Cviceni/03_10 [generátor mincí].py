##  Program nakreslí n náhodných mincí. Mincami sú farebné kruhy s polomerom 20,
##  v ktorých sú veľké ('arial 30') náhodné číslice od 1 do 9. 


#úvodní a prázdný řádek:
print('GENERÁTOR MINCÍ')
print('(dle zadaného počtu zobrazí mince s náhodnou hodnotou)')
print()


#vstupní data:
a = int(input('Zadej počet: '))                             #počet mincí


#moduly:
import tkinter                                              #import modulu
import random                                               #import modulu


#grafické okno:
canvas = tkinter.Canvas()                                   #vytvoření plátna
canvas.pack()                                               #umístění plátna do aplikace


#promněné:
r = 20                                                      #poloměr mincí


#výpočet:
for i in range(a):                                          #cyklus
    x = random.randint(20, 350)                             #náhodná volba x-ové osy
    y = random.randint(20, 240)                             #náhodná volba y-ové osy
    b = f'#{random.randrange(256**3):06x}'                  #náhodná volba barvy
    c = random.randint(1, 10)                               #náhodná volba hodnoty mince
    canvas.create_oval(x-r, y-r, x+r, y+r, fill=b)          #nakreslení mince
    canvas.create_text(x, y, text=c, font=('arial', 30))    #vepsání hodnoty


#grafické okno:
tkinter.mainloop()                                          #aktivace grafické aplikace
