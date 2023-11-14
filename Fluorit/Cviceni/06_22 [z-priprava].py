#import modulů:
import tkinter


canvas = tkinter.Canvas()
canvas.pack()

retazec = '4v4j4z4sh5vd'*5

r = retazec                                 #řetězec
násobení = 0                                #násobení
psaní = 1                                   #psaní 
x, y = 70, 100                              #přiřazení x a y prvního bodu

while len(r) != 0:                          #cyklus - dokud řetězec není prázdný
    
#násobení: 
    if r[0] in  ('123456789'):              #podmínka - když je znak číslo
        násobení = int(r[0])                #přiřaď ho do násobení
        r = r[1:]                           #odečti 1 znak z řetězce

#souřadnice:
    x1, y1 = x, y                           #srovnání souřadnic posledního a dalšího bodu
    if r[0] =='s':                          #podmínka - pokud je znak "s"
        y1 -= 10 + (10*násobení-10)         #jdi na sever
    if r[0] =='v':                          #podmínka - pokud je znak "v"
        x1 += 10 + (10*násobení-10)         #jdi na víchod
    if r[0] =='j':                          #podmínka - pokud je znak "j"
        y1 += 10 + (10*násobení-10)         #jdi na jih
    if r[0] =='z':                          #podmínka - pokud je znak "z"
        x1 -= 10 + (10*násobení-10)         #jdi na západ
    násobení = 0                            #vynuluj násobení

#čára:
    if psaní == 1:                          #podmínka - je-li v psaní "1"
        canvas.create_line(x, y, x1, y1)    #vytvoř čáru
        x, y = x1, y1                       #přiřaď novou pozici jako výchozí pozici
        r = r[1:]                           #odečti 1 znak z řetězce   
    else:                                   #jinak
        x, y = x1, y1                       #přiřaď novou pozici jako výchozí pozici
        r = r[1:]                           #odečti 1 znak z řetězce  

#psaní:
    if len(r) != 0:                         #podmínka - pokud není řetězec prázdný
        if r[0] == 'h':                     #podmínka -  - pokud je znak "h"
            psaní = 0                       #přiřaď k proměnné "psaní" "0"
            r = r[1:]                       #odečti 1 znak z řetězce  
        if r[0] == 'd':                     #podmínka -  - pokud je znak "d"
            psaní = 1                       #přiřaď k proměnné "psaní" "1"
            r = r[1:]                       #odečti 1 znak z řetězce  

#zbytek:
    if len(r) != 0:                         #podmínka - pokud není řetězec prázdný
        if r[0] not in ('123456789dhjsvz'): #podmínka - pokud je zde jiný znak než které jsou očekávané
            print(f'''Řetězec obsahuje znak "{r[0]}", který bude ignorován,
        protože není platným příkazem.''')  #vypiš oznam
            r = r[1:]                       #odečti 1 znak z řetězcea pokračuj


tkinter.mainloop()
    
