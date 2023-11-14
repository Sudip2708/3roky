##Aj ďalšia verzia programu generuje náhodné bodky v 300 x 300.
##Bodiek teraz vygeneruj aspoň 10000 a zmenši ich na polomer 2.
##Červené bodky budú tie, pre ktoré platí x*x+y*y<=300*300,
##zvyšné budú modré.
##Program ma záver vypíše podiel počtu červených ku všetkým bodkám krát 4.
##Zamysli sa nad tým, prečo sa tento podiel blíži k číslu pi. 
##
##Úloha z které se vychází:
####  Využi program z prednášky, v ktorom sa vykresľovalo 1000 farebných bodiek
####  (malé krúžky s polomerom 5 bez obrysu) podľa toho či mali x-ovú,
####  alebo y-ovú súradnicu menšiu alebo väčšiu ako 150.
####  Veľkosť grafickej plochy bola 300x300.
####  Zmeň v tomto programe sériu príkazov if tak,
####  aby kreslené bodky vytvorili vnútorný červený štvorec s rozmermi 150x150.
####  Vykresli s 4000 farebnými bodkami.


#úvodní a prázdný řádek:
print('ČVRTINA KRUHU V ČTVERCI')
print('program z červených a modrých teček vytvoří čtvrtinu kruhu a po té vypíše jejich poměr násobený 4-mi')
print()


#prázdný řádek a příkaz pro spuštění okna grafické aplikace:
print()
input('[zmáčkni [Enter] pro zobrazení grafické aplikace]')


#moduly:
import tkinter
import random


#grafické okno:
canvas = tkinter.Canvas()
canvas.pack()


#proměné:
r = 0                                                           #počítadlo červených teček
b = 0                                                           #počítadlo modrých teček


#výpočet:
for i in range(10000):                                          #cyklus pro 4000 teček
    x = random.randint(1, 300)                                  #x-ová osa tečky
    y = random.randint(1, 300)                                  #y-ová osa tečky
    if x**2+y**2<=300**2:                                       #podmínka - když se c menší nebo roven poloměru kružnice
        farba = 'red'                                           #použij červenou barvu
        r += 1                                                  #a připočítej 1 k modrým
    else:                                                       #a pokud je delší
        farba = 'blue'                                          #pouužij modrou barvu
        b += 1                                                  #a připočítej 1 k modrým
    canvas.create_oval(x-2, y-2, x+2, y+2, fill=farba, width=0) #vytvožení tečky


#prázdný řádek
print()


#výstup:
print(f'Podíl červených teček: {r}, ku všem {r+b}, násobený 4-mi je: {r/(r+b)*4}')


#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]')    


#aktivace grafické aplikace:
tkinter.mainloop()                                              




