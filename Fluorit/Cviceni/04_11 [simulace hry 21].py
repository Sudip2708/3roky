##  Budem hrať takúto hru:
##  kladiem vedľa seba do radu mince s náhodnými hodnotami z <1, 4>;
##  skončím, keď ich súčet bude väčší alebo rovný k 21.
##  Ak skončil so súčtom, ktorý je rovný k 21,
##  vypíše text 'HURÁ' inak 'ŠKODA'.
##  Napíš program, ktorý túto hru odsimuluje 10-krát a zakreslí to pod seba.


#úvodní a prázdný řádek:
print('SIMULACE HRY 21')
print('program 10x simuluje hru náhodného losu hodnot 1-4 a oznámí v kterých případech se dosáhlo výsledku 21')
print()


#příkaz pro spuštění okna grafické aplikace:
print()
input('[zmáčkni [Enter] pro zobrazení grafické aplikace]')


#moduly:
import tkinter
import random


#grafické okno:
canvas = tkinter.Canvas()
canvas.pack()


#proměné:
a = 21                                                                          #počet kterého se hra snaží dosáhnout
r = 20                                                                          #velikost kroužky mince
b = 5                                                                           #odsazení od kraje plátna
c = 0                                                                           #součet padlých mincí
e = 0                                                                           #počátek další mince
f = 0                                                                           #počátek dalšího řádku


#výpočet:
for i in range(10):                                                             #cyklus řádkování
    while c < a:                                                                #cyklus losování mincí dokud nedosáhnou 21
        d = random.randint(1,4)                                                 #losování hodnoty mince
        canvas.create_oval(b+e, b+f, b+e+r, b+f+r, fill='white')                #vytvoření mince
        canvas.create_text(b+e+r/2, b+f+r/2, text=d, font=('arial black', 11))  #vepsání hodnoty
        c += d                                                                  #připočítání hodnoty do součtu padlých mincí
        e += (r + b)                                                            #přípočet pro počátek další mince
    if c == 21:                                                                 #podmínka pro vypsání textu v případě přesných 21
        canvas.create_text(14*(r+b)-10, b+f+r/2, text='HURA', font=('arial black', 12), fill='green')
    else:                                                                       #podmínka pro vypsání textu v případě ne 21
        canvas.create_text(14*(r+b)-10, b+f+r/2, text='ŠKODA', font=('arial black', 12), fill='red')
    c = 0                                                                       #vynulování součtu padlých mincí
    e = 0                                                                       #vynulování počátku další mince
    f += (r + b)                                                                #přípočet pro počátek dalšího řádku


#grafické okno:
tkinter.mainloop()                                                              #aktivace grafické aplikace
