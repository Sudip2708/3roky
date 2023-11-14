##Napíš funkciu kruh(tab, r, r1, s1, hodnota),
##ktorá bude vypĺňať nejakú oblasť dvojrozmernej tabuľky zadanou hodnotou hodnota.
##Touto oblasťou bude kruh s polomerom r a so stredom r1, s1 (riadok, stĺpec).
##Funkcia by mohla fungovať tak, že postupne skontroluje všetky prvky tabuľky,
##či ich „vzdialenosť“ od stredu je menšia alebo rovná r a vtedy im zmení hodnoty.
##Funkcia nič nevracia ani nevypisuje. Funkcia modifikuje obsah tabuľky.
##Napríklad po nakreslení štyroch kruhov v tabuľke 50x50 môžeš dostať:


#úvodní a prázdný řádek:                                                  
print('KRESLENÍ KRUHŮ DLE 2D TABULKY')                              
print('''
Program vytvoří v 2D tabulku, kde po jejím vykreslení do grafické plochy
budou zopbrazeny kruhy zadaný funkcí kruh,
kde jsou následující parametry:
1. poloměr
2. číslo řádeku umístění středu kruhu
3. číslo sloupce umístění středu kruhu
4. číslo reprezentující určitou barvu
''')


input('''
Zmáčkni [enter] pro zobrazení výsledku pro zadání:

kruh_1 = (17, 30, 20, 3)
kruh_2 = (13, 25, 40, 2)
kruh_3 = (10, 15, 15, 1)
kruh_4 = (8, 15, 15, 0)

''')


def vyrob_tabulku(n):
    tab = []
    for radek in range(n):
        tab.append([])
        for sloupec in range(n):
            tab[-1].append((0))
    return tab
        
def kruh(tab, r, r1, s1, hodnota):
    nova_tab = tab[:]
    x, y, r = r1, s1, r
    for ixr, radek in enumerate(nova_tab):
        for ixs, sloupec in enumerate(radek):
            a = abs(r1 - ixr)
            b = abs(s1 - ixs)
            c = (a**2 + b**2)**.5
            if c <= r:
                nova_tab[ixr][ixs] = hodnota
    return nova_tab

def nakresli_tabulku(tab, vel=10):
    barva = 'light gray', 'black', 'blue', 'red'
    for ixr, radek in enumerate(tab):
        for ixs, sloupec in enumerate(radek):
            x, y, b2 = ixr*vel+5, ixs*vel+5, barva[0]
            canvas.create_rectangle(x, y, x+vel, y+vel, outline=b2)
            if sloupec == 0:
                canvas.create_rectangle(x, y, x+vel, y+vel, outline=b2)
            else:
                b1 = barva[sloupec]
                canvas.create_rectangle(x, y, x+vel, y+vel, fill=b1, outline=b2)

import tkinter
canvas = tkinter.Canvas(height=510, width=510)
canvas.pack()

plocha = vyrob_tabulku(50)
kruh_1 = (17, 30, 20, 3)
kruh_2 = (13, 25, 40, 2)
kruh_3 = (10, 15, 15, 1)
kruh_4 = (8, 15, 15, 0)
for i in (kruh_1, kruh_2, kruh_3, kruh_4):
    kruh(plocha, i[0], i[1], i[2], i[3])
nakresli_tabulku(plocha)

tkinter.mainloop()
