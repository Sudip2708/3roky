##  Napíš program, ktorý v grafickej ploche
##  najprv vygeneruje n náhodných bodiek(malé kruhy).
##  Potom nakreslí čo najmenší obdĺžnik tak,
##  aby sa v ňom nachádzali všetky nakreslené body.


#úvodní a prázdný řádek:
print('OBDELNÍK OHRANIČUJÍCÍ TEČKY')
print('program ze zadaného počtu vytvoří na ploše náhodně tečky a pak je uzavře do těsně obléhajícího obdelníku')
print()


#vstupní data:
a = int(input('Zadej počet teček: '))                   #vstup pro počet teček


#moduly:
import tkinter
import random


#grafické okno:
canvas = tkinter.Canvas()
canvas.pack()


#proměné:
x1 = 360                                                #nejzašší bod x-ové osy
y1 = 240                                                #nejzašší bod y-ové osy
x2 = 20                                                 #nejmenší bod x-ové osy
y2 = 20                                                 #nejmenší bod y-ové osy


#výpočet:
for i in range(a):                                      #cyklus
    x = random.randint(20, 360)                         #x-ová osa tečky
    y = random.randint(20, 240)                         #y-ová osa tečky
    canvas.create_oval(x-3, y-3, x+3, y+3, fill='red')  #vytvožení tečky
    if x < x1:                                          #podmínka - pokud je x menší než x1
        x1 = x                                          #použij pro x1 hodnotu x
    if x > x2:                                          #podmínka - pokud je x větší než x2
        x2 = x                                          #použij pro x2 hodnotu x  
    if y < y1:                                          #podmínka - pokud je y menší než y1
        y1 = y                                          #použij pro y1 hodnotu y
    if y > y2:                                          #podmínka - pokud je y větší než y1
        y2 = y                                          #použij pro y1 hodnotu y

canvas.create_rectangle(x1, y1, x2, y2, outline='blue') #nakreslení obdélnku


#aktivace grafické aplikace
tkinter.mainloop()                                                  
