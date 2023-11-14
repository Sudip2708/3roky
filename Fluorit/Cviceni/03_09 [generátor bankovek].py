##  Napíš program, ktorý pod seba vygeneruje n bankoviek s náhodnými hodnotami.
##
##  Na generovanie náhodnej hodnoty použi zápis:
##    hodnota = random.choice((1, 2, 5, 10, 20, 50))
##
##  pomocou ktorého sa náhodne vyberie jedno číslo zo zadanej postupnosti.
##  Program na záver spočíta výslednú sumu. Veľkosť obdĺžnikov nech je 50x20.


#úvodní a prázdný řádek:
print('GENERÁTOR BANKOVEK')
print('(dle zadaného počtu zobrazí bankovky s náhodnou hodnotou a sečte je)')
print()


#vstupní data:
a = int(input('Zadej číslo: '))                                     #počet bankovek


#moduly:
import tkinter                                                      #import modulu
import random                                                       #import modulu


#grafické okno:
canvas = tkinter.Canvas()                                           #vytvoření plátna
canvas.pack()                                                       #umístění plátna do aplikace


#promněné:
b = 50                                                              #délka bankovky
c = 20                                                              #výška bankovky
d = 0                                                               #přípočet výšky dalších bankovek
f = 0                                                               #sčítání bankovek


#výpočet:
for i in range(a):                                                  #cyklus
    e = random.choice((1, 2, 5, 10, 20, 50))                        #výběr hodnoty bankovky
    canvas.create_rectangle(100, 20+d, 150, 40+d, fill='green')     #kreslení obdelníku bankovky
    canvas.create_text(125, 30+d, text=(f'{e} €'))                  #vepsání hodnoty
    d += 20                                                         #přípočet výšky k umístění další bankovky
    f += e                                                          #přípočet k celkové hodnotě bankovek
canvas.create_text(200, 50, text=(f'spolu = {f} €'))                #výpis celkového součtu bankovek


#grafické okno:
tkinter.mainloop()                                                  #aktivace grafické aplikace
