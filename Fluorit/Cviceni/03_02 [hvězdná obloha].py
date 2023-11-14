##  Na tmavomodré pozadie (napríklad 'navy')
##  nakresli na náhodné pozície n (napríklad n = 200) žltých hviezdičiek
##  (create_text) znak '*' - skús ich kresliť rôznymi veľkosťami fontu
##  (napr. veľkosť fontu nech je náhodne číslo od 10 do 20).


#úvodní a prázdný řádek:
print('HVĚZDNÉ NEBE')
print('(dle zadaného čísla se objeví hvězdičky náhodně rozeseté po obloze)')
print()


#vstupní data:
a = int(input('Zadej počet hvězdiček: '))                               #zadání počtu hvězdiček


#moduly:
import random                                                           #import modulu random
import tkinter                                                          #import grafické aplikace (modulu)


#grafické okno:
canvas = tkinter.Canvas(bg='navy')                                      #vytvoření plátna v modré barvě
canvas.pack()                                                           #umístění plátna do aplikace


#výpočet:
for i in range(a):                                                      #cyklus
    b = random.randint(10, 20)                                          #náhodné číslo velikosti hvězdiček
    x = random.randint(0, 380)                                          #náhodné číslo souřadnice x
    y = random.randint(0, 270)                                          #náhodné číslo souřadnice y
    canvas.create_text(x, y, text='*', font=f'arial {b}', fill='yellow')#zápis


#grafické okno:
tkinter.mainloop()                                                      #aktivace rozhraní grafické aplikace
