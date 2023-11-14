##  Ak by si celú postupnosť 100 náhodných bodov
##  z predchádzajúcej úlohy vykreslil pomocou jediného create_line,
##  dostal by si nejakú čmáranicu (vyskúšaj).
##  Ďalej otestuj, ako sa vykreslí táto postupnosť,
##  keď sa najprv usporiada pomocou funkcie sorted.
##  Napríklad, náhodná postupnosť 100 bodov:
## 
##    a po usporiadaní pomocou sorted:
##
##  Předchozí úloha:
####  Napíš funkciu nahodne_body(pocet),
####  ktorá vráti zadaný počet náhodných bodov v grafickej ploche (dvojíc čísel z 380x260).
####  Funkcia vráti zoznam, ktorý bude obsahovať dvojprvkové n-tice celých čísel.
####  Napríklad:
####    >>> nahodne_body(5)
####        [(118, 103), (299, 27), (247, 118), (166, 237), (269, 225)]


#úvodní a prázdný řádek:
print('X-OVÁ KLIKATICE')
print('''pouze k zobrazení - program obsahuje funkci, která vygeneruje 100 položkový 
seznam (x, y) souřadnic, které následně program setřídí dle x-ové pozice
a v grafickém prostředí propojí všechny body linkou.''')
print()


#prázdný řádek a příkaz pro spuštění okna grafické aplikace:
print()
input('[zmáčkni [Enter] pro zobrazení grafické aplikace]')


#definice funkce:
def nahodne_body(pocet):
    a = []                              #proměnná pro tvořený seznam
    for i in range(pocet):              #cyklus - dle poctu
        x = random.randint(10, 380)     #proměnná pro náhodnou hodnotu x-ové pozice
        y = random.randint(10, 260)     #proměnná pro náhodnou hodnotu y-ové pozice
        a.append((x, y))                #přidání dvojce do seznamu
    return a                            #vrácení seznamu dvojic bodů x a y


#import modulů:
import random
import tkinter


#grafické okno:
canvas = tkinter.Canvas()
canvas.pack()


#výpočet:
a = sorted(nahodne_body(100))           #volání funkce "náhodné body" a setřídění výsledku (dle osy x)
b = ''                                  #proměnná pro první bod přímky
for i in a:                             #cyklus - pro každou položku seznamu "a"
    if b != '':                         #podmínka - pokud proměnná "b" je prázdná
        canvas.create_line(b, i)        #vytvoř linky z předešlé hodnoty (proměnná "b") do načtených souřadnic
    b = i                               #přiřaď načtené souřadnice do proměnné "b"


#aktivace grafické aplikace
tkinter.mainloop()  
