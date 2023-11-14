##  Dopíš do tejto funkcie spracovanie týchto ďalších znakov:
##  'h' - kresliace pero sa bude odteraz pohybovať bez kreslenia (pero hore)
##  'd' - kresliace pero bude odteraz pri pohybe kresliť (pero dole)
##  číslice od '1' do '9' - nasledovný príkaz (jeden z 'svjz') sa vykoná príslušný počet krát
##
##  napríklad:
##    >>>kresli('4v4j4z4sh5vd'*5)
##    nakreslí vedľa seba 5 štvorcov:


#úvodní a prázdný řádek:
print('5 ČTVERCŮ VEDLE SEBE')
print('''funkce vytváří obrazce dle následujících instrukcí:

číslice od '1' do '9' určují počet opakování příkazu
(pokud není uvedena, posouvá se 1x)

Určení směru:
s = +10 na sever
j = +10 na jih
v = +10 na víchod
z = +10 na západ

Určení, zda při pohybu kreslit, nebo nekreslit
h = pohyb bez kreslení
d = pohyb s kreslením
''')
print()


#vstup:
vstup = input("Zadej svůj kód, nebo zmáčkni [Enter] pro zobrazení výsledku pro '4v4j4z4sh5vd'*5: ")


#import modulů:
import tkinter


#grafické okno:
canvas = tkinter.Canvas()
canvas.pack()


#definice funkce:
def kontrola(retezec):
    poloha = 1                                      #proměná polohy pro určení chybného znaku
    while len(retezec) != 0:                        #cyklus - dokud není řetězec prázdný
        if retezec[0] not in ('123456789dhjsvz'):   #podmínka - pokud je zde jiný znak než které jsou očekávané
            print(f'''Řetězec obsahuje znak "{r[0]}" na pozici {poloha}, který bude ignorován,
        protože není platným příkazem.''')          #vypiš oznam
        retezec = retezec[1:]                       #odečti 1 znak z řetězcea pokračuj
        poloha += 1

def prepis(retezec):
    ra = retezec                                    #přiřazení řetězce do dočasné promněnné
    rb = ''                                         #promněnná pro nový řetězec
    while len(ra) != 0:                             #cyklus - dokud není řetězec prázdný
        if ra[0] in ('123456789'):                  #podmínka - pokud je znak číslo
            rb += ra[1] * int(ra[0])                #vynásob následující znak tímto číslem a přiřaď výsledek do nového řetězce
            ra = ra[2:]                             #odečti tito dva znaky od procházeného řetě
        else:                                       #jinak
            rb += ra[0]                             #přiřaď znak do nového řetězce
            ra = ra[1:]                             #odečti znak od procházeného řetězce
    return rb                                       #vrať nový řetězec

def kresli(retezec):
    kontrola(retezec)                               #volání funkce kontrola()
    r = prepis(retezec)                             #volání funkce přepis()
    x, y = 70, 100                                  #přiřazení x a y prvního bodu
    x1, y1 = x, y                                   #srovnání souřadnic posledního a dalšího bodu
    psaní = 1                                       #psaní/nepsaní
    while len(r) != 0:                              #cyklus - dokud není řetězec prázdný
        if r[0] == 'h':                             #podmínka -  - pokud je znak "h"
            psaní = 0                               #přiřaď k proměnné "psaní" "0"
            r = r[1:]                               #odečti 1 znak z řetězce  
        if r[0] == 'd':                             #podmínka -  - pokud je znak "d"
            psaní = 1                               #přiřaď k proměnné "psaní" "1"
            r = r[1:]                               #odečti 1 znak z řetězce  
        if len(r) != 0:                             #podmínka - pokud není řetězec prázdný
            if r[0] =='s':                          #podmínka - pokud je znak "s"
                y1 -= 10                            #jdi na sever
            if r[0] =='v':                          #podmínka - pokud je znak "v"
                x1 += 10                            #jdi na víchod
            if r[0] =='j':                          #podmínka - pokud je znak "j"
                y1 += 10                            #jdi na jih
            if r[0] =='z':                          #podmínka - pokud je znak "z"
                x1 -= 10                            #jdi na západ
            if psaní == 1:                          #podmínka - je-li v psaní "1"
                canvas.create_line(x, y, x1, y1)    #vytvoř čáru
                x, y = x1, y1                       #přiřaď novou pozici jako výchozí pozici
                r = r[1:]                           #odečti 1 znak z řetězce   
            else:                                   #jinak
                x, y = x1, y1                       #přiřaď novou pozici jako výchozí pozici
                r = r[1:]                           #odečti 1 znak z řetězce  
        

#výpočet:
if vstup != '':
    kresli(vstup)
else:   
    kresli('4v4j4z4sh5vd'*5)


#aktivace grafické aplikace
tkinter.mainloop()  
