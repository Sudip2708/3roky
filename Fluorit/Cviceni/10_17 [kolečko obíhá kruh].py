##  Do grafickej plochy nakresli kružnicu (napríklad pre r, x0, y0 = 100, 150, 120).
##  Potom naprogramuj časovač, ktorý bude rovnomerne posúvať červenú bodku
##  (kruh s polomerom 5) na obvode tejto kružnice
##  (po každom tiknutí časovača posunie jeho pozíciu na kružnici o uhol 10 stupňov).
##  Posúvanie kruhu budeš robiť pomocou canvas.coords().


#úvodní a prázdný řádek:
print('ČERVENÉ KOLEČKO OBÍHÁ MODRÝ KRUH')
print('''Program vytvoří uprostřed plochy větší modrý kruh
a malé červené kolečko, které ho obíhá.''')
print()


#prázdný řádek a příkaz pro spuštění okna grafické aplikace:
print()
input('[zmáčkni [Enter] pro zobrazení grafické aplikace]')


#definice funkcí:
def casovac():
    u = uhol[0]                                         #načtení úhlu ze seznamu
    x2 = x0 + r0 * round(math.cos(math.radians(u)), 4)  #výpočet osy "x" dle načteného úhlu a osy "x" většího kruhu
    y2 = y0 + r0 * round(math.sin(math.radians(u)), 4)  #výpočet osy "y" dle načteného úhlu a osy "y" většího kruhu
    canvas.coords(2, x2-r, y2-r, x2+r, y2+r)            #změna souřadnic menšího kruhu
    uhol.append(uhol.pop(0))                            #odebrání první položky seznamu "uhel" a vložení na konec
    canvas.after(10, casovac)                           #nastavení časovače pro další zpuštění funkce "casovac"
   

#import modulů:
import tkinter
import math

    
#grafické okno:
canvas = tkinter.Canvas()
canvas.pack()


#proměnné:
r0, x0, y0 = 100, 190, 130
uhol = list(range(0,360,1))
r, x2, y2 = 5, 180, 15


#vytvoření kruhů a volání funkce
canvas.create_oval(x0-r0, y0-r0, x0+r0, y0+r0, fill='blue', outline='')
canvas.create_oval(x2-r, y2-r, x2+r, y2+r, fill='red', outline='')
casovac()


#aktivace grafické aplikace:
tkinter.mainloop()
