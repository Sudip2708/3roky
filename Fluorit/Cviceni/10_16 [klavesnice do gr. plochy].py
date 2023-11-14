##  Stláčaním malých a veľkých písmen abecedy
##  sa tieto vypisujú nejakým väčším fontom vedľa seba (Napríklad 'arial 30').
##  Využi jeden grafický objekt pre text (create_text)
##  a tomuto budeš pri stláčaní písmen pridávať vypisovaný text
##  (pomocou canvas.itemconfig()).
##  Program by mal akceptovať aj stláčanie medzery a Enteru (do textu vloží '\n').
##  Použi metódu bind_all('<KeyPress>', ...)
##  pričom vo viazanej funkcii pracuj s hodnotou event.char.


#úvodní a prázdný řádek:
print('PSANÍ KLÁVESNICÍ DO GRAFICKÉ PLOCHY')
print('''Program vypisuje text z klávesnice do grafické plochy,
klávesou "delete" se maže celý text,
klávesou "backspace" se maže poslední znak''')
print()


#prázdný řádek a příkaz pro spuštění okna grafické aplikace:
print()
input('[zmáčkni [Enter] pro zobrazení grafické aplikace]')


#definice funkcí:
def text(event):
    'funkce přepisuje do grafické plochy text z klávecnice'
    global tx                                       #odkaz na globální proměnnou
    if event.keysym not in ('BackSpace', 'Delete'): #podmínka - když psaný znak není: (v závorce)
        tx +=  event.char                           #přidej do proměnné "tx" psaný znak
        canvas.itemconfig(1, text=tx)               #uprav údaj "text" v grafickém programu
    elif event.keysym == 'BackSpace':               #podmínka - když psaný znak je "BackSpace"
        tx = tx[:-1]                                #odeber z proměnné "tx" poslední znak
        canvas.itemconfig(1, text=tx)               #uprav údaj "text" v grafickém programu
    elif event.keysym == 'Delete':                  #podmínka - když psaný znak je "Delete"
        tx = ''                                     #vymaž z proměnné "tx" všechen text
        canvas.itemconfig(1, text=tx)               #uprav údaj "text" v grafickém programu


#import modulů:
import tkinter

    
#grafické okno:
canvas = tkinter.Canvas(bg='white', height=400, width=600)
canvas.pack()


#globální proměnná:
tx = ''


#výpočet:
canvas.create_text(50, 40, text=tx, font='arial 30', anchor='nw', width=500) 


#propojení s funkcemi:
canvas.bind_all('<KeyPress>', text)


#aktivace grafické aplikace:
tkinter.mainloop()

