##  Nakresli n sústredných štvorcov (štvorce majú spoločný stred),
##  v ktorých sa striedajú tri dané farby ('red', 'blue', 'yellow').
##  Veľkosti štvorcov nech sú 10, 20, 30, …


#úvodní a prázdný řádek:
print('DČTVERCE UVNITŘ SEBE')
print('(vykreslí čtverce uvnitř sebe v zadaném počtu s 3 střídajícími se barvami)')
print()


#vstupní data:
a = int(input('Zadej počet čtverců: '))                         #zadání počtu čtverců


#moduly:
import tkinter                                                  #import grafické aplikace (modulu


#grafické okno:
canvas = tkinter.Canvas()                                       #vytvoření plátna
canvas.pack()                                                   #umístění plátna do aplikace


#proměné:
b1 = 'red'                                                      #červená barva
b2 = 'blue'                                                     #modrá barva
b3 = 'yellow'                                                   #žlutá barva

d = b1                                                          #střídač barvy

z = a * 10                                                      #velikost strany prvního čtverce
x = 380/2 - z/2                                                 #x-ová souřadnice 1. čtverce
y = 270/2 - z/2                                                 #y-ová souřadnice 1. čtverce


#výpočet:
for i in range(a):                                              #cyklus
    canvas.create_rectangle(x, y, x+z, y+z, fill=f'{d}')        #kreslení čtverců
    x += 5                                                      #přípočet x-ové souřadnice pro další čtverec
    y += 5                                                      #přípočet y-ové souřadnice pro další čtverec
    z -= 10                                                     #odpočet z velikosti strany dalšího čtverce
    if d == b1:                                                 #změna barvy
        d = b2
    elif d == b2:
        d = b3
    else:
        d = b1

                                    
#grafické okno:
tkinter.mainloop()                                              #aktivace grafické aplikace




