##  2. Týždenný projekt
##
##  Napíš pythonovský skript, ktorý najprv pomocou jedného volania príkazu input()
##  prečíta tri celé čísla (oddelene medzerou):
##  štartová_dĺžka, inkrement a súčet_dĺžok.
##  Potom do grafickej plochy nakreslí štvorcovú špirálu,
##  v ktorej prvá najkratšia úsečka má dĺžku štartová_dĺžka,
##  každá ďalšia úsečka špirály je o inkrement dlhšia.
##  Kreslenie špirály končí vtedy, keď bude súčet všetkých úsečiek
##  presne zadaný súčet_dĺžok. Posledná úsečka špirály môže byť aj kratšia,
##  ale zrejme tak, aby súčet všetkých spolu bol presne zadané číslo
##  (dokonca aj prvá úsečka môže mať kratšiu ako štartová_dĺžka,
##  ak je zároveň poslednou úsečkou). Štvorcová špirála označuje,
##  že susedné úsečky zvierajú 90 stupňov (je jedno, či smerom vľavo alebo vpravo).
##  Špirálu môžeš začať kresliť na ľubovoľnej pozícii
##  s ľubovoľným počiatočným natočením.
##  Nemusí sa zmestiť do grafickej plochy.
##
##  V tvojom riešení nepoužívaj žiaden iný modul okrem tkinter.
##  Z Pythonu používaj len príkazy z prvých štyroch prednášok.
##  Do grafického plátna (canvas) kresli len pomocou create_line,
##  do ktorého pošleš 4 čísla ako súradnice dvoch bodov.
##
##  Ak štvorcová špirála bude mať úsečky rovnobežné s osami,
##  môžeš takto získať maximálne 75% bodov z maximálneho počtu 3 body.
##  100% bodov získaš len vtedy, keď bude špirála nejako natočená.
##
##  Tvoj odovzdaný program s menom riesenie.py musí začínať tromi riadkami
##  komentárov (zmeň meno a dátum odovzdania):
##    # 2. zadanie: spirala
##    # autor: Janko Hraško
##    # datum: 15.10.2021


# 2. zadanie: spirala
# autor: Dalibor Sova
# datum: 5.8.2022


#úvodní a prázdný řádek:
print('TÝDENNÍ PROJEKT PRO 4. LEKCI')
print('program dle námi zapsaných hodnot vytvoří natočenou čtvercovou spirálu')
print()


#vstupní data a proměné:
a = input('Zadej tři celá čísla oddělená mezerou a zmáčkni [Enter] \n(ideálně: 2-místné, 1-místné, 4-místné, ale můžeš i jinak): ') #vstup 3 čísel oddělených mezerou


#moduly:
import tkinter


#grafické okno:
canvas = tkinter.Canvas()
canvas.pack()


#výpočet - rozdělení čísla:
b = ''                                  #proměná pro 1. číslo - startovací délka
c = ''                                  #proměná pro 2. číslo - přírůstek
d = ''                                  #proměná pro 3. číslo - konečný součet délek
e = 1                                   #počítadlo pro přidělených čísel do promněných

for i in a:                             #cyklus pro rozdělení čísla do 3 proměných
    if e == 1:                          #podmínka1 - když v "x" je 1
        if i != ' ':                    #podmínka2 - dokud není načtena mezera
            b += i                      #přičti číslo do první promněné
        else:                           #podmínka2 - v případě načtení mezery
            e += 1                      #přípočet do počítadla 
    elif e == 2:                        #podmínka1 - když v "x" je 2
        if i != ' ':                    #podmínka3 - dokud není načtena mezera
            c += i                      #přičti číslo do druhé promněné
        else:                           #podmínka3 - v případě načtení mezery
            e += 1                      #přípočet do počítadla 
    else:                               #podmínka1 - ve všech ostatních případech (3)
        d += i                          #přičti číslo do třetí promněné


#přiřazení hodnot:
sd = int(b)                             #startovací délka
pr = int(c)                             #přírůstek
ks = int(d)                             #konečný součet délek


#výpočet první úsečky:
if sd < ks:                             #podmínka - pokud je startovací délka menší než konečný součet délek
    ks = ks - sd                        #odečti od konečného součtu délek první úsečku
else:                                   #v opačném případě
    sd = ks                             #použij pro délku úsečky hodnotu konečného součtu délek

#přiřazení hodnot:
x = sd*3                                #x-ová strana prvního bodu příčky
y = sd*2                                #y-ová strana prvního bodu příčky
p = 1                                   #počítadlo kol
sin15 = 0.2588                          #hodnota sinus 15
sin30 = 0.5                             #hodnota sinus 30
sin45 = 0.7071                          #hodnota sinus 45
sin60 = 0.8660                          #hodnota sinus 60
sin75 = 0.9659                          #hodnota sinus 75


#výpočet úhlu:
if int(b) < 20:                         #podmínka - když je startovací délka menší než 20
    u1, u2 = sin15, sin75               #přiřaď tyto hodnoty
elif int(b) <40:                        #podmínka - když je startovací délka menší než 40
    u1, u2 = sin30, sin60               #přiřaď tyto hodnoty
elif int(b) <60:                        #podmínka - když je startovací délka menší než 60
    u1, u2 = sin45, sin45               #přiřaď tyto hodnoty
elif int(b) <80:                        #podmínka - když je startovací délka menší než 80
    u1, u2 = sin60, sin30               #přiřaď tyto hodnoty
else:                                   #podmínka - když je startovací délka větší než 80
    u1, u2 = sin75, sin15               #přiřaď tyto hodnoty


#výpočet pro natočenou spirálu:
while sd > 0:                           #podmínka - dokud konečný součet délek není menší než 0
    if p == 1:                          #podmínka - pokud je na počítadlu č. 1
        x1 = x + (sd * u2)              #zadej tuto hodnotu pro x
        y1 = y - (sd * u1)              #zadej tuto hodnotu pro y
    elif p == 2:                        #podmínka - pokud je na počítadlu č. 2
        x1 = x - (sd * u1)              #zadej tuto hodnotu pro x 
        y1 = y - (sd * u2)              #zadej tuto hodnotu pro y
    elif p == 3:                        #podmínka - pokud je na počítadlu č. 3
        x1 = x - (sd * u2)              #zadej tuto hodnotu pro x 
        y1 = y + (sd * u1)              #zadej tuto hodnotu pro y
    else:                               #podmínka - pokud je na počítadlu č. 4
        x1 = x + (sd * u1)              #zadej tuto hodnotu pro x 
        y1 = y + (sd * u2)              #zadej tuto hodnotu pro y
        
    canvas.create_line(x, y, x1, y1)    #nakreslení úsečky

    x, y = x1, y1                       #přiřazení počátečních souřadnic pro další příčku

    if sd == ks:                        #podmínka - pokud se startovací délka shoduje s konečným součtem délek
        sd = 0                          #vynuluj startovací délku (protože již byla použita)
    else:                               #jinak
        sd += pr                        #připočti k délce úsečky přírůstek

    if sd > ks:                         #podmínka - pokud je hodnota další úsečky menší než zbytek v konečném součtu délek
        sd = ks                         #další úsečka má hodnotu zbytku z konečného součtu délek
        
    ks -= sd                            #odpočet další úsečky od celkové délky (konečného součtu délek)

    if p == 4:                          #podmínka - když je na počítadle č. 4
        p = 1                           #přepiš ho na č. 1
    else:                               #jinak
        p += 1                          #přičti 1


###Výpočet pro rovnoběžnou spirálu:
##x = 150                                 #počáteční hodnota x 
##y = 100                                 #počáteční hodnota y
##
##while ks > 0:                           #cyklus - dokud není konečný součet na nule
##
##    canvas.create_line(x, y, x+sd, y)   #vytvoř úsečku
##    x = x + sd                          #přepiš hodnotu x pro kreslení další úsečky
##    ks -= sd                            #odečti hodnotu nakreslené úsečky od konečného součtu
##    sd = sd + pr                        #přičti k délce úsečky hodnotu přírústku
##    if ks < sd:                         #pokud je číslo konečné délky menší než kreslená úsečka
##        sd = ks                         #vyměň délku úsečky za zbytkovou délku 
##
##    canvas.create_line(x, y, x, y+sd)   #vytvoř úsečku
##    y = y + sd                          #přepiš hodnotu y pro kreslení další úsečky
##    ks -= sd                            #odečti hodnotu nakreslené úsečky od konečného součtu
##    sd = sd + pr                        #přičti k délce úsečky hodnotu přírústku
##    if ks < sd:                         #pokud je číslo konečné délky menší než kreslená úsečka
##        sd = ks                         #vyměň délku úsečky za zbytkovou délku
##
##    canvas.create_line(x, y, x-sd, y)   #vytvoř úsečku
##    x = x - sd                          #přepiš hodnotu x pro kreslení další úsečky
##    ks -= sd                            #odečti hodnotu nakreslené úsečky od konečného součtu
##    sd = sd + pr                        #přičti k délce úsečky hodnotu přírústku
##    if ks < sd:                         #pokud je číslo konečné délky menší než kreslená úsečka
##        sd = ks                         #vyměň délku úsečky za zbytkovou délku 
##
##    canvas.create_line(x, y, x, y-sd)   #vytvoř úsečku
##    y = y - sd                          #přepiš hodnotu y pro kreslení další úsečky
##    ks -= sd                            #odečti hodnotu nakreslené úsečky od konečného součtu
##    sd = sd + pr                        #přičti k délce úsečky hodnotu přírústku
##    if ks < sd:                         #pokud je číslo konečné délky menší než kreslená úsečka
##        sd = ks                         #vyměň délku úsečky za zbytkovou délku 


#aktivace grafické aplikace:
tkinter.mainloop()
    

