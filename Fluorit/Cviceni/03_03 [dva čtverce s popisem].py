##  Napíš program, ktorý najprv nakreslí dva štvorce:
##  prvý štvorec má ľavý horný roh (x, y) a veľkosť strany a1.
##  Druhý štvorec má rovnaký stred ale veľkosť a2 (menšiu od a1).
##
##  Potom postupne:
##    
##    zafarbí ich na niektorý odtieň červenej a bledomodrej (napríklad 'indian red' a 'light blue')
##
##    k vrcholom vonkajšieho štvorca pripíše pomenovania A, B, C, D
##
##    k pravej zvislej hrane väčšieho štvorca pripíše veľkosť tohto štvorca
##
##    k spodnej hrane menšieho štvorca pripíše veľkosť tohto menšieho štvorca
##
##
##  Malo by to fungovať aj vtedy, keď zmeníme hociktorú z premenných x, y, a1, a2.
##
##  Napríklad pre premenné:
##    x, y = 50, 50
##    a1, a2 = 180, 100


#úvodní a prázdný řádek:
print('DVA ČTVERCE S POPISEM')
print('(zobrazí 2 čtverce uvnitř sebe s ukázkou základního popisu)')
print()


#vstupní data:
a = int(input('Zadej velikost 1. čtverce (101-200): '))         #délka hrany 1. čtverce
b = int(input('Zadej velikost 2. čtverce (50-100): '))          #délka hrany 2. čtverce


#moduly:
import tkinter                                                  #import grafické aplikace (modulu


#grafické okno:
canvas = tkinter.Canvas()                                       #vytvoření plátna
canvas.pack()                                                   #umístění plátna do aplikace


#proměné:
x1 = 50                                                         #x-ová souřadnice 1. čtverce
y1 = 50                                                         #y-ová souřadnice 1. čtverce
x2 = x1+(a-b)/2                                                 #x-ová souřadnice 2. čtverce
y2 = x1+(a-b)/2                                                 #y-ová souřadnice 2. čtverce


#výpočet:                                
canvas.create_rectangle(x1, y1, x1+a, y1+a, fill='indian red')  #vytvoření 1. čtverce
canvas.create_rectangle(x2, y2, x2+b, y2+b, fill='light blue')  #vytvoření 2. čtverce
                                    
canvas.create_text(x1, y1, text='A', anchor='se' )              #vytvoření textu A
canvas.create_text(x1+a, y1, text='B', anchor='sw' )            #vytvoření textu B
canvas.create_text(x1, y1+a, text='C', anchor='ne' )            #vytvoření textu C
canvas.create_text(x1+a, y1+a, text='D', anchor='nw' )          #vytvoření textu D

canvas.create_text(x1+a, y1+a/2, text=f'{a}', anchor='w' )      #vytvoření textu délky prvního čtverce
canvas.create_text(x2+b/2, y2+b, text=f'{b}', anchor='s' )      #vytvoření textu délky druhého čtverce


#grafické okno:
tkinter.mainloop()                                              #aktivace grafické aplikace

