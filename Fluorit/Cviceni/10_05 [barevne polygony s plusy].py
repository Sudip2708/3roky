##  Podobne ako v (4) úlohe:
##  klikanie do plochy kreslí '+' a zapamätáva tieto body.
##  Ak mám aspoň 3 zapamätané body a pritom prvý a posledný
##  majú vzdialenosť menšiu ako 5, ukončí sa zapamätávanie bodov,
##  nakreslí sa z nich náhodne zafarbený polygon a všetko sa začne od začiatku.
##  Môžeš dostať, napríklad:


#úvodní a prázdný řádek:
print('BAREVNÉ POLYHGONY S PLUSY')
print('''Program obsahuje 2 funkce, první při kliknutí lev. tl. do grafické plochy,
nakreslí na místo znak "+" a vloží souřadnice do seznamu, a takto pokračuje
dokud se některýmn kliknutím těsně nepřiblíží k prvnímu bod, a po té
na místě vaznačeném body vytvoří polygon vyplněný náhodnou barvou
a po té začíná od znovu, druhá funkce po zmáčknutí pravého tlačítka
smaže obsah plochy.''')
print()


#prázdný řádek a příkaz pro spuštění okna grafické aplikace:
print()
input('[zmáčkni [Enter] pro zobrazení grafické aplikace]')


#definice funkcí:
def klik(event):
    global poc, sez                                         #odkaz na globální proměnnou
    x, y = event.x, event.y                                 #přiřazení proměných x, y z eventu funkce
    canvas.create_text(x, y, text='+')                      #příkaz na nakreslení znaku "+"
    sez.append((x, y))                                      #přidej souřadnice do seznamu
    if poc > 2:                                             #podmínka - pokud počítadlo má minimálně hodnotu 2 (jede se třetí kolo)
        if abs(sum(sez[0])-(x+y)) < 5:                      #podmínka - pokud je aktuální souřadnice na 5 bodů od první souřadnice
            b = f'#{random.randrange(256**3):06x}'          #vytvoř náhodnou barvu
            canvas.create_polygon(sez, fill=b)              #nakresli polygon mezy body
            sez = []                                        #smaž seznam se souřadnicemi
            poc = 0                                         #vynuluj počítadlo
    poc += 1                                                #připočti do počítadlo hodnotu "1"

def zmaz(event):
    'funkce po zmáčknutí pravého tl. smaže obsah plátna a nastaví gl. pr. na hodnotu "1"'
    global n                                                #odkaz na globální proměnnou
    canvas.delete('all')                                    #příkaz na smazání grafické plochy
    n = 1                                                   #nastavení gl. pr. na hodnotu "1"
    

#import modulů:
import tkinter
import random


#grafické okno:
canvas = tkinter.Canvas(bg='white', height=500, width=700)
canvas.pack()


#globální proměnná:
poc = 1
sez = []


#propojení s funkcemi:
canvas.bind('<ButtonPress-1>', klik)
canvas.bind('<ButtonPress-3>', zmaz)


#aktivace grafické aplikace:
tkinter.mainloop()
