##  Unicode 0x2654 a ďalších päť za ním sú obrázky šachových figúrok.
##  Napíš program, ktorý do grafickej plochy
##  nakresli vedľa seba všetkých 6 figúrok náhodnými farbami
##  väčším fontom (napríklad 'arial 50').


#úvodní a prázdný řádek:
print('ŠACHOVÉ FIGURKY')
print('pouze k zobrazení - program zobrazí 6 šachových figurek v náhodných barvách')
print()


#prázdný řádek a příkaz pro spuštění okna grafické aplikace:
print()
input('[zmáčkni [Enter] pro zobrazení grafické aplikace]')


#import modulů:
import tkinter
import random


#grafické okno:
canvas = tkinter.Canvas()
canvas.pack()


#proměné
unc = 0x2654                                        #Unicode kód první figurky                                 
x = 400 // 12                                       #x-ová pozice středu první figurky
y = 260 // 2                                        #y-ová pozice středu první figurky


#výpočet
for i in range(6):                                  #cyklus
    text = unc + i                                  #text - unicode figurky
    fill = f'#{random.randrange(256**3):06x}'       #náhodná barva
    canvas.create_text(x + (2*x*i), y, text=chr(text), font='arial 50', fill=fill)  #vytvoření figurky


#aktivace grafické aplikace
tkinter.mainloop()  
