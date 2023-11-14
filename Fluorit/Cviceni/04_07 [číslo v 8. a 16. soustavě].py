##  Uprav predchádzajúci program tak, aby sa číslo vypísalo v osmičkovej sústave
##  (zrejme namiesto delenia 10 budeš deliť 8)
##
##  Tento výsledok môžeš porovnať s volaním štandardnej funkcie oct
##  (resp. pomocou formátovacej šablóny):
##    >>> oct(1753)
##    '0o3331'
##    >>> f'{1753:o}'
##    '3331'
##
##  Vyskúšaj upraviť tento program tak, aby vypisoval cifry v dvojkovej sústave.
##  Aj tu môžeš pre kontrolu využiť štandardnú funkciu bin
##  (resp. formátovaciu šablónu):
##    >>> bin(479)
##    '0b111011111'
##    >>> f'{479:b}'
##    '111011111'
##
##Předcházející úloha:
####  Využi while-cyklus z predchádzajúcej úlohy
####  a vypíš cifry do grafickej plochy (zrejme sprava do ľava).
####  Program jednotlivé cifry vypíše do farebných štvorcov.
####
####  Předchozí úloha:
######  Napíš program, ktorý vypíše cifry zadaného čísla postupným delením desiatimi,
######  teda vo while-cykle vypíšeš poslednú cifru (číslo % 10)
######  a pritom ešte samotné číslo vydelíš 10.
######  Súčasne každú túto cifru pripočítaš do počítadla cs (ciferný súčet).
######
######  Môžeš dostať takýto výstup:
######    zadaj číslo: 4132
######    2
######    3
######    1
######    4
######    ciferný súčet = 10
######
######  Všimni si, že cifry sú vypísané v opačnom poradí ako sú v zadanom čísle.


#úvodní a prázdný řádek:
print('ČÍSLO V 8. A 16. SOUSTAVĚ')
print('program převede a do grafické plochy vykreslí zadané číslo v 8. a 16. soustavě')
print()

#vstupní data:
a = int(input('Zadej max. 4-místné číslo: '))                           #vstup - počet

#moduly:
import tkinter


#grafické okno:
canvas = tkinter.Canvas(bg='white', width=580)
canvas.pack()


#proměné:
a1 = a                                                                  #přepis čísla pro cyklus
a2 = int(f'{a1:o}')                                                     #přepis čísla pro cyklusv 8-mičkové soustavě
a3 = int(f'{a1:b}')                                                     #přepis čísla pro cyklusv 2-kové soustavě
x1 = 530                                                                #x-ová souřadnice levého horního rohu čísla
x2 = 530                                                                #x-ová souřadnice levého horního rohu čísla v 8-mičkové soustavě
x3 = 530                                                                #x-ová souřadnice levého horního rohu čísla v 2-kové soustavě
y = 130                                                                 #y-ová souřadnice levého horního rohu čísla v 8-mičkové soustavě
c = 35                                                                  #šířka obdelníku čísla
d = 40                                                                  #výška obdelníku čísla
e = 5                                                                   #mezera mezi obdelníky


#výpočet číslo:
while a1 != 0:                                                          #cyklus - dokuď nebude 0
    canvas.create_rectangle(x1, y-d-e, x1+c, y-e, fill='cyan')          #vytvoření obdelníku
    canvas.create_text(x1+c/2, y-e-d/2, text=a1%10, font='ariel 32')    #výpis čísla
    a1 //= 10                                                           #vyděl a deseti
    x1 -= 40                                                            #posunutí x-ové pozice pro další obdelník
canvas.create_text(x1+c/2, y-e-d/2, text='číslo:', font='ariel 8')      #popisek čísla


#výpočet číslo v 8-mičkové soustavě:
while a2 != 0:                                                          #cyklus - dokuď nebude 0
    canvas.create_rectangle(x2, y, x2+c, y+d, fill='cyan')              #vytvoření obdelníku
    canvas.create_text(x2+c/2, y+d/2, text=a2%10, font='ariel 32')      #výpis čísla
    a2 //= 10                                                           #vyděl a deseti
    x2 -= 40                                                            #posunutí x-ové pozice pro další obdelník
canvas.create_text(x2+c/2, y+d/2, text='v 8.s.:', font='ariel 8')       #popisek čísla


#výpočet číslo v 2-kové soustavě:
while a3 != 0:                                                          #cyklus - dokuď nebude 0
    canvas.create_rectangle(x3, y+d+e, x3+c, y+d+e+d, fill='cyan')      #vytvoření obdelníku
    canvas.create_text(x3+c/2, y+d+e+d/2, text=a3%10, font='ariel 32')  #výpis čísla
    a3 //= 10                                                           #vyděl a deseti
    x3 -= 40                                                            #posunutí x-ové pozice pro další obdelník
canvas.create_text(x3+c/2, y+d+e+d/2, text='v 2.s.:', font='ariel 8')   #popisek čísla


#aktivace grafické aplikace
tkinter.mainloop()                                                  
