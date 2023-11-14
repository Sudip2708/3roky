##  Program nakreslí 25 obdĺžnikov veľkosti 15x250,
##  ktoré sú uložené tesne vedľa seba.
##  Tieto obdĺžniky postupne menia farby od červenej k modrej:
##  čím je väčšie x obdĺžnika tým menej červenej a viac modrej.


#úvodní a prázdný řádek:
print('PŘECHOD Z ČERVENÉ DO MODRÝ')
print('(pouze zobrazí přechod z červené do modré barvy)')
print()


#zobrazení výsledku:
input('Zmáčkni [ENTER] pro zobrazení')                              #přechod od grafického prostředí


#moduly:
import tkinter
import random


#grafické okno:
canvas = tkinter.Canvas()
canvas.pack()


#promněné:
a = 25                                                              #počet obdelníků
x = 15                                                              #šířka obdelníku
y = 250                                                             #výška obdelníku
z = 5                                                               #odsazení 
c = 0                                                               #přípočet pro umístění dalšího obdelníku
br = 255                                                            #červená barva
bg = 0                                                              #zelená barva
bb = 5                                                              #modrá barva


#výpočet:
for i in range(a):                                                  #cyklus
    b = f'#{br:02x}{bg:02x}{bb:02x}'                                #barva
    canvas.create_rectangle(z+c, z, z+x+c, z+y, fill=b, outline='') #nakreslení a zabarvení obdelníku
    c += 15                                                         #přípočet odsazení dalšího obdelníku
    br -= 10                                                        #odpočet červené barvy
    bb += 10                                                        #přípočet modré barvy


#grafické okno:
tkinter.mainloop()                                                  #aktivace grafické aplikace
