##  Využi program z prednášky, v ktorom sa vykresľovalo 1000 farebných bodiek
##  (malé krúžky s polomerom 5 bez obrysu) podľa toho či mali x-ovú,
##  alebo y-ovú súradnicu menšiu alebo väčšiu ako 150.
##  Veľkosť grafickej plochy bola 300x300.
##  Zmeň v tomto programe sériu príkazov if tak,
##  aby kreslené bodky vytvorili vnútorný červený štvorec s rozmermi 150x150.
##  Vykresli s 4000 farebnými bodkami.


#úvodní a prázdný řádek:
print('ČTVEREC V ČTVERCI')
print('program vytečkuje do červeného čtvercového pozadí menší červený čtverec')
print()


#prázdný řádek a příkaz pro spuštění okna grafické aplikace:
print()
input('[zmáčkni [Enter] pro zobrazení grafické aplikace]')


#moduly:
import tkinter
import random


#grafické okno:
canvas = tkinter.Canvas(bg='white', width=300, height=300)
canvas.pack()


#výpočet:
for i in range(4000):
    x = random.randint(1, 300)
    y = random.randint(1, 300)
    if x < 75 or x > 225 or y < 75 or y > 225:
        farba = 'blue'
    else:
        farba = 'red'
    canvas.create_oval(x-5, y-5, x+5, y+5, fill=farba, width=0)


#grafické okno:
tkinter.mainloop()                                                  #aktivace grafické aplikace
