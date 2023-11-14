##  Napíš program, ktorý bude robiť efekt spreja:
##  ťahanie myšou so zatlačeným ľavým tlačidlom nakreslí 20 farebných bodiek
##  (farba podľa globálnej premennej, napríklad farba = 'blue') na náhodných pozíciách.
##  Tieto náhodné bodky budú mať od kliknutého miesta takúto vzdialenosť:
##  x-ová súradnica bude z intervalu <x-30, x+30> a y-ová z <y-30, y+30>.
##  Najlepšie je ich kresliť ako kruhy s polomerom 2 bez obrysu (width=0).
##  Do programu pridaj aj spracovanie ľavého kliknutia myši:
##  vtedy sa nastaví premenná farba na náhodnú farbu.
##  Vďaka tomuto každé ťahanie myšou bude sprejovať inou farbou.


#úvodní a prázdný řádek:
print('KRESLENÍ SPREJEM')
print('''Program umožňuje kreslit na grafickou plochu jakoby sprayem, kde:
1) tažením myši se zmáčknutým lev. tl, kreslíme
2) kliknutím na lev. tl jednou stříknem aktuální barvu
3) kliknutím na pr. tl. náhodně změníme barvu
4) kliknutím na prostř. tl. změníme barvu na mix
5) tažením myši se zmáčknutým prostř. tl.  smažeme plochu
6 tažením myši se zmáčknutým pr. tl stříkáme bílou barvu''')
print()


#prázdný řádek a příkaz pro spuštění okna grafické aplikace:
print()
input('[zmáčkni [Enter] pro zobrazení grafické aplikace]')


#definice funkcí:
def proved(x, y):
    global barva                                            #odkaz na globální proměnnou
    pocet = 20                                              #počet teček na jedno stříknutí
    if barva == 'mix':                                      #podmínka - je-li v proměné "barva" uvedeno "mix"
        b1 = f'#{random.randrange(256**3):06x}'             #použij generování náhodné barvy pro každou tečku
    else:                                                   #podmínka - není-li v proměné "barva" uvedeno "mix"
        b1 = barva                                          #použij uvedenou barvu
    for i in range(pocet):                                  #cyklus dle poctu
        x1 = random.randint(x-30, x+30)                     #výpočet náhodné osy "x" pro tečku
        y1 = random.randint(y-30, y+30)                     #výpočet náhodné osy "y" pro tečku
        canvas.create_oval(x1-2, y1-2, x1+2, y1+2, fill=b1, width=0)    #nakreslení tečky

def klik1(event):                                           #stříknutí vybrané barvy 
    proved(event.x, event.y)                                #volání funkce proved

def klik2(event):                                           #změna barvy na "mix"
    global barva                                            #odkaz na globální proměnnou
    barva = 'mix'                                           #změna na mix barev

def klik3(event):                                           #náhodná změna barvy
    global barva                                            #odkaz na globální proměnnou
    barva = f'#{random.randrange(256**3):06x}'              #změna na náhodnou barvu
    proved(event.x, event.y)                                #volání funkce proved

def tahaj1(event):                                          #stříkání barvy
    proved(event.x, event.y)                                #volání funkce proved

def tahaj2(event):                                          #vymazání plochy
    canvas.delete('all')                                    #příkaz na smazání grafické plochy

def tahaj3(event):                                          #stříkání bílou barvou
    global barva                                            #odkaz na globální proměnnou
    a = barva                                               #načtení barvy
    barva = 'white'                                         #změna na bílou barvu
    proved(event.x, event.y)                                #volání funkce proved
    barva = 'white'                                         #změna na původní barvu
   

#import modulů:
import tkinter
import random


#grafické okno:
canvas = tkinter.Canvas(bg='white', height=500, width=700)
canvas.pack()


#globální proměnná:
barva = 'mix'


#propojení s funkcemi:
canvas.bind('<B1-Motion>', tahaj1)                          #stříkání barvy
canvas.bind('<B2-Motion>', tahaj2)                          #vymazání plochy
canvas.bind('<B3-Motion>', tahaj3)                          #stříkání bílou barvou
canvas.bind('<ButtonPress-1>', klik1)                       #stříknutí vybrané barvy 
canvas.bind('<ButtonPress-2>', klik2)                       #změna barvy na "mix"
canvas.bind('<ButtonPress-3>', klik3)                       #náhodná změna barvy


#aktivace grafické aplikace:
tkinter.mainloop()
