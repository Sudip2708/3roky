#import modulů:
import tkinter
import math



#grafické okno:
canvas = tkinter.Canvas(bg='black', width=180, height=160)
canvas.pack()

#_______________________________________________________________________________POMOCNÉ TABULKY_______________________________________________________________________________________
123456789012345678901234567890123456789012345+6789012345678901234567890123456789#
                                                                                #
##  [0]   [1]   [2][3][4]
z = [None, None, 0, 0, 0]
##[0]číslo zvoleného rozlišení: 0=800/600, 1=1080/720, 2=1920/1080
##[1]číslo zvoleného prostředí: 0=úvodní prostředí, 1=hra
##[2]počet cyklů
##[3]počet kliků
##[4]body celkem

#_______________________________________________________________________________TABULKA PLANET_______________________________________________________________________________________
123456789012345678901234567890123456789012345+6789012345678901234567890123456789#
                                                                                #
##vzdálenost:
##    [6][0]herní        [6][1]soustava    [6][2]slunce      [6][3]vnitřní
vs0 = [[0, 0, 0]]
vp1 = [[36, 45, 70],     [5, 6, 10],       [177, 224, 339],  [81, 107, 208]]
vp2 = [[40, 50, 78],     [8, 10, 17],      [180, 228, 345],  [152, 199, 389]]
vp3 = [[42, 54, 84],     [10, 14, 23],     [182, 230, 349],  [210, 276, 538]]
vm1 = [[4, 4, 5],        [2, 2, 2],        [4, 4, 5],        [21, 27, 41]]
vp4 = [[46, 59, 94],     [15, 20, 35],     [184, 233, 355],  [320, 420, 820]]
vp5 = [[93, 122, 205],   [45, 62, 113],    [221, 283, 440],  None]
vp6 = [[126, 169, 293],  [81, 112, 206],   [242, 313, 496],  None]
vp7 = [[198, 269, 483],  [161, 223, 412],  [288, 376, 618],  None]
vp8 = [[288, 394, 715],  [252, 348, 645],  [347, 459, 772],  None]
vp9 = [[360, 494, 903],  [329, 455, 844],  [394, 524, 894],  None]

##poloměr:
##    [5][0]herní       [5][1]soust. [5][2]vnitřní
rs0 = [[32, 40, 60],    [1, 1, 1],   [32, 40, 60]]
rp1 = [[1, 1, 1.5],     [1, 1, 1],   [6, 8, 12]]
rp2 = [[2, 2, 3],       [1, 1, 1],   [15, 20, 30]]
rp3 = [[2, 2, 3],       [1, 1, 1],   [16, 21, 31]]
rm1 = [[1, 1, 1],       [1, 1, 1],   [4, 5, 9]]
rp4 = [[1, 1, 1.5],     [1, 1, 1],   [8, 11, 17]]
rp5 = [[18, 22.5, 34],  [1, 1, 1],   None]
rp6 = [[15, 19, 29],    [1, 1, 1],   None]
rp7 = [[6.5, 8, 12.5],  [1, 1, 1],   None]  
rp8 = [[6, 7.5, 12],    [1, 1, 1],   None]
rp9 = [[1, 1, 1],       [1, 1, 1],   None] 

##souřadnice:
##    [4][0]osa "x"        [4][1]osa "y"         
os0 = [[400, 540, 960],    [300, 360, 540]] 
op1 = [[436, 585, 1030],   [300, 360, 540]] 
op2 = [[440, 590, 1038],   [300, 360, 540]]
op3 = [[442, 594, 1044],   [300, 360, 540]]
om1 = [[433, 581, 1021],   [300, 360, 540]]
op4 = [[446, 599, 1054],   [300, 360, 540]]
op5 = [[493, 662, 1165],   [300, 360, 540]] 
op6 = [[526, 709, 1253],   [300, 360, 540]]
op7 = [[598, 809, 1443],   [300, 360, 540]]
op8 = [[688, 934, 1675],   [300, 360, 540]]
op9 = [[760, 1034, 1863],  [300, 360, 540]]

##pohyb:
##    [3][0]     [3][1]    [3][2] [3][3]          
pp1 = [3600,     0.1,      -1,    0] 
pp2 = [9000,     0.04,     -1,    0]
pp3 = [12000,    0.03,     -1,    0]
pm1 = [36,       10.0,     -1,    0]
pp4 = [25000,    0.0144,   -1,    0]
pp5 = [150000,   0.0024,   -1,    0] 
pp6 = [375000,   0.00096,  -1,    0]
pp7 = [1125000,  0.00032,  -1,    0]
pp8 = [2250000,  0.00016,  -1,    0]
pp9 = [3000000,  0.00012,  -1,    0]
##  [0]cyklů celkem na 1 obeh
##  [1]úhel na jeden cyklus
##  [2]směr: 1=doprava, -1=doleva
##  [3]úhel celkem

##hlavní tabulka:
##   [0]   [1]      [2]        [3]   [4]   [5]   [6]   [7]   [8] 
s0 = [[],  [0, 0],  'yellow',  None, os0,  rs0,  vs0,  None, None]
p1 = [[],  [0, 0],  'yellow',  pp1,  op1,  rp1,  vp1,  s0,   None]
p2 = [[],  [0, 0],  'yellow',  pp2,  op2,  rp2,  vp2,  s0,   None]
p3 = [[],  [0, 0],  'yellow',  pp3,  op3,  rp3,  vp3,  s0,   None]
m1 = [[],  [0, 0],  'yellow',  pm1,  om1,  rm1,  vm1,  p3,   None]
p4 = [[],  [0, 0],  'yellow',  pp4,  op4,  rp4,  vp4,  s0,   None]
p5 = [[],  [0, 0],  'yellow',  pp5,  op5,  rp5,  vp5,  s0,   None]
p6 = [[],  [0, 0],  'yellow',  pp6,  op6,  rp6,  vp6,  s0,   None]
p7 = [[],  [0, 0],  'yellow',  pp7,  op7,  rp7,  vp7,  s0,   None]
p8 = [[],  [0, 0],  'yellow',  pp8,  op8,  rp8,  vp8,  s0,   None]
p9 = [[],  [0, 0],  'yellow',  pp9,  op9,  rp9,  vp9,  s0,   None]
##  [0]vybrané hodnoty ([0][0]x, [0][1]y, [0][2]r, [0][3]vzdálenost)
##  [1]body ([0][0]cos, [0][1]sin)
##  [2]barva
##  [3]tabulka pro pohyb
##  [4]tabulka pro souřadnice
##  [5]tabulka pro poloměr
##  [6]tabulka pro středovou vzdálenost
##  [7]střed o kolo kterého objekt obýhá
##  [8]číslo objektu

#_______________________________________________________________________________TABULKA POPISŮ UVODNÍHO A HERNÍHO PROSTŘEDDÍ_______________________________________________________________________________________
123456789012345678901234567890123456789012345+6789012345678901234567890123456789#
                                                                                #
##hodnoty:
##    [0][0]osa "x"      [0][1][0]osa y-a   [0][1][1]osa y-b   [0][2]délka        
hu1 = [[120, 140, 160],  [[35, 44, 52],     [35, 44, 52]],     [89, 99, 109]]
hu2 = [[120, 140, 160],  [[53, 64, 74],     [53, 64, 74]],     [89, 99, 109]]
hu3 = [[120, 140, 160],  [[71, 84, 96],     [71, 84, 96]],     [89, 99, 109]]
hu4 = [[60, 73, 87],     [[89, 104, 118],   [161, 184, 206]],  [29, 32, 36]]
hu5 = [[120, 140, 160],  [[89, 104, 118],   [161, 184, 206]],  [29, 33, 34]]
hu6 = [[180, 207, 233],  [[89, 104, 118],   [161, 184, 206]],  [29, 32, 36]]
hu7 = [[75, 90, 105],    [[107, 124, 140],  [179, 204, 228]],  [44, 49, 54]]
hu8 = [[165, 190, 215],  [[107, 124, 140],  [179, 204, 228]],  [44, 49, 54]]

##text:
##    [2][0]text úvodního pohledu   [2][1]text herního pohledu
tu1 = ['HERNÍ POHLED',              'CELÁ SLUNEČNÍ SOUSTAVA']
tu2 = ['SLUNCE VE STEJNÉM POMĚRU',  'POUZE VNITŘNÍ PLANETY']
tu3 = ['VŠE VE STEJNÉM POMĚRU',     'ZEMĚ A MĚSÍC']
tu4 = ['POMALU',                    'POMALU']
tu5 = ['NORMÁLNĚ',                  'NORMÁLNĚ']
tu6 = ['RYCHLE',                    'RYCHLE']
tu7 = ['NÁPOVĚDA',                  'NÁPOVĚDA']
tu8 = ['HRÁT HRU',                  'OPUSTIT HRU']

##hlavní tabulka:
##   [0]h.  [1]barva    [2]t.  [3]č. obj.
u1 = [hu1,  'yellow',   tu1,   None] 
u2 = [hu2,  'skyblue',  tu2,   None]
u3 = [hu3,  'skyblue',  tu3,   None]
u4 = [hu4,  'skyblue',  tu4,   None]
u5 = [hu5,  'yellow',   tu5,   None]
u6 = [hu6,  'skyblue',  tu6,   None]
u7 = [hu7,  'skyblue',  tu7,   None]
u8 = [hu8,  'skyblue',  tu8,   None]
##  [0]seznam hodnot ([0][0]x, [0][1][0]ya, [0][1][1]ya, [0][2]délka)
##  [1]barva
##  [2]seznam textu ([2][0]text-a, [2][1]text-b)
##  [3]číslo objektu


#_______________________________________________________________________________INFO TABULKA V HERNÍM PROSTŘEDÍ_______________________________________________________________________________________
123456789012345678901234567890123456789012345+6789012345678901234567890123456789#
                                                                                #
##hodnoty:
##    [0][0]osa "x"      [0][1]osa "y"     [0][2]délka        
hi1 = [[75, 90, 105],    [89, 104, 118],   [44, 49, 54]]
hi2 = [[165, 190, 215],  [89, 104, 118],   [44, 49, 54]]
hi3 = [[75, 90, 105],    [107, 124, 140],  [44, 49, 54]]
hi4 = [[165, 190, 215],  [107, 124, 140],  [44, 49, 54]]
hi5 = [[75, 90, 105],    [125, 144, 162],  [44, 49, 54]]
hi6 = [[165, 190, 215],  [125, 144, 162],  [44, 49, 54]]
hi7 = [[75, 90, 105],    [143, 164, 184],  [44, 49, 54]]
hi8 = [[165, 190, 215],  [143, 164, 184],  [44, 49, 54]]

##hlavní tabulka:
##   [0]h.  [1]barva    [2]text          [3]č. obj.
i1 = [hi1,  'skyblue',  'CYKL:',         None]
i2 = [hi2,  'skyblue',  'f{cykl}',       None]
i3 = [hi3,  'skyblue',  'DEN:',          None]
i4 = [hi4,  'skyblue',  'f{cykl//den}',  None]
i5 = [hi5,  'skyblue',  'KLIK:',         None]
i6 = [hi6,  'skyblue',  'f{klik}',       None]
i7 = [hi7,  'skyblue',  'BODY:',         None]
i8 = [hi8,  'skyblue',  'f{body}',       None]
##  [0]seznam hodnot ([0][0]x, [0][1]y, [0][2]délka)
##  [1]barva
##  [2]text 
##  [3]číslo objektu

#_______________________________________________________________________________TABULKA LINKY V HERNÍM PROSTŘEDÍ_______________________________________________________________________________________
123456789012345678901234567890123456789012345+6789012345678901234567890123456789#

##tabulka hodnot lišty:
l0a = [40,   111,  177,  243,  309,  375,   441,   507,   573,   639,   705]
l0b = [97,   163,  229,  295,  361,  427,   493,   559,   625,   691,   760]
l1a = [59,   153,  241,  329,  417,  505,   593,   681,   769,   857,   945]
l1b = [137,  225,  313,  401,  489,  577,   665,   753,   841,   929,   1021]
l2a = [107,  268,  424,  580,  736,  892,   1048,  1204,  1360,  1516,  1672]
l2b = [250,  406,  562,  718,  874,  1030,  1186,  1342,  1498,  1654,  1815]

##tabulka hodnot planet na liště:
pl0 = [103,  169,  235,  301,  367,  433,   499,   565,   631,   697]
pl1 = [144,  232,  320,  408,  496,  584,   672,   760,   848,   936]
pl2 = [258,  414,  570,  726,  882,  1038,  1194,  1350,  1506,  1662]

##tabulka hodnot popisů na liště:
t0a = [80,   145,  214,  280,  348,  410,   476,   546,   607,   677] 
t1a = [117,  203,  296,  384,  473,  557,   645,   738,   819,   913] 
t2a = [228,  382,  542,  698,  856,  1007,  1164,  1324,  1474,  1634] 
t0b = [82,   148,  214,  280,  346,  412,   478,   544,   610,   676] 
t1b = [120,  208,  296,  384,  472,  560,   648,   736,   824,   912] 
t2b = [230,  386,  542,  698,  854,  1010,  1166,  1322,  1478,  1634] 
tl3 = ['Merkur:', 'Venuše:', 'Země:', 'Měsíc:', 'Mars:', 'Jupiter:', 'Saturn:',
       'Uran:', 'Neptun:', 'Pluto:', '0,000']

##hodnoty lišty:
##    [0][0]osa "x1"      [0][1]osa "x2"     [0][2]osa "y"       
hli = [[l0a, l1a, l2a],   [l0b, l1b, l2b],   [510, 610, 910]]

##hodnoty sluncí na liště:
##    [0][0]osa "x"       [0][1]osa "y"      [0][2]poloměr      
hsl = [[43, 59, 100],     [510, 610, 910],   [4, 5, 6]]
hsp = [[757, 1021, 1820], [510, 610, 910],   [4, 5, 6]]

##hodnoty planet na liště:
##    [0][0]osa "x"       [0][1]osa "y"      [0][2]poloměr      
hpl = [[pl0, pl1, pl2],   [510, 610, 910],   [4, 5, 6]]

##hodnoty textů na liště:
##    [0][0]osa "x"       [0][1]osa "y"      [0][2]poloměr      
hta = [[t0a, t1a, t2a],   [503, 602, 900],   tl3]
htb = [[t0b, t1b, t2b],   [519, 619, 920],   '0,000']

##hlavní tabulka lišty:
##   [0]h.  [1]barva    [2]název  [3]č. obj.
li = [hli,  'yellow',   'lišta',  None]

##hlavní tabulka sluncí na liště:
##   [0]h.  [1]barva    [2]název         [3]č. obj. 
sl = [hsl,  'yellow',   'levé slunce',   None]
sp = [hsp,  'yellow',   'pravé slunce',  None]

##hlavní tabulka planet na liště:
##   [0]h.  [1]barva    [2]název             [3]č. obj.
pl = [hpl,  'blue',     'planety na liště',  []]

##hlavní tabulka textů na liště:
##   [0]h.  [1]barva    [2]název          [3]č. obj.
ta = [hta,  'yellow',   'text na liště',  None]
tb = [htb,  'yellow',   'text na liště',  []]

##  [0]seznam hodnot ([0][0]x, [0][1]y, [0][2]délka)
##  [1]barva
##  [2]text
##  [3]číslo objektu


#_______________________________________________________________________________NÁPOVĚDA__________________________________________________________________________
123456789012345678901234567890123456789012345+6789012345678901234567890123456789#                                                                                #
                                                                                #                                                                                #

def napoveda_uvod():
    barva = None

        
#_______________________________________________________________________________VYTVOŘENÍ HERNÍHO PROSTŘEDÍ_______________________________________________________
123456789012345678901234567890123456789012345+6789012345678901234567890123456789#                                                                                #
                                                                                #                                                                                #

#aktivace herního prostředí:
def herni_prostredi():                                                          #definice funkce - vytvoření prostředí pro herní prostředí
    canvas.delete('all')                                                            #změna - smaž všechny objekty
    zmena_nastaveni_pohledu(u1)                                                     #změna - úvodního zobrazení na pohled na celou sluneční soustavu
    z[1] = 1                                                                        #změna - vložení čísla označující uvodní prostředí 
    n = z[0]                                                                        #proměnná - pro hodnotu rozlišení prostředí
    q = z[1]

    #sluneční soustava:
    for i in (s0, p1, p2, p3, m1, p4, p5, p6, p7, p8, p9):                          #cyklus - pro každou položku ze seznamu
        x, y, r, b = i[0][0], i[0][1], i[0][2], i[2]                                    #proměnná - přiřazení hodnot osy "x" a "y", poloměr, barva
        cislo_objektu = canvas.create_oval(x-r, y-r, x+r, y+r, fill=b)                  #vytvoř objekt - ovál a přiřaď jeho číslo do proměnné
        i.pop()                                                                         #změna - odstraň číslo objektu z předchozího náhledu
        i.append(cislo_objektu)                                                         #změna - přidání čísla objektu do seznamu objektu

    #výběr možností:
    for i in (u1, u2, u3, u4, u5, u6, u7, u8):                                      #cyklus - pro každou položku ze seznamu
        x, y, xr, = i[0][0][n], i[0][1][q][n], i[0][2][n]                               #proměnná - přiřazení hodnot osy "x" a "y", velikost "x"
        b1, b2, t = i[1], 'blue', i[2][q]                                               #proměnná - přiřazení hodnot barva1, barva2 a text
        v1, v2 = [6, 7, 8], [8, 9, 10]                                                  #proměnná - na seznamy pro výběr hodnot
        f, yr, = ('Arial', v1[n]), v2[n]                                                #proměnná - přiřazení hodnot font, velikost "y"
        canvas.create_rectangle(x-xr, y-yr, x+xr, y+yr, outline=b2)                     #vytvoř objekt - obdelník
        cislo_objektu = canvas.create_text(x, y, text=t, fill=b1, font=f)               #vytvoř objekt - text a přiřaď jeho číslo do proměnné
        i.pop()                                                                         #změna - odstraň číslo objektu z předchozího náhledu
        i.append(cislo_objektu)                                                         #změna - přidání čísla objektu do seznamu objektu

    #informace o hře:
    for i in (i1, i2, i3, i4, i5, i6, i7, i8):                                      #cyklus - pro každou položku ze seznamu 
        x, y, xr, b, t = i[0][0][n], i[0][1][n], i[0][2][n], i[1], i[2]                 #proměnná - přiřazení hodnot osy "x" a "y", velikost "x", barva, text
        v1, v2 = [6, 7, 8], [8, 9, 10]                                                  #proměnná - na seznamy pro výběr hodnot
        f, yr, b2 = ('Arial', v1[n]), v2[n], 'blue'                                     #proměnná - přiřazení hodnot font, velikost "y", barvu obdelníku
        cislo_objektu = canvas.create_text(x, y, text=t, fill=b, font=f)                #vytvoř objekt - text a přiřaď jeho číslo do proměnné
        i.pop()                                                                         #změna - odstraň číslo objektu z předchozího náhledu
        i.append(cislo_objektu)                                                         #změna - přidání čísla objektu do seznamu objektu

    #linka:
    for i in range(11):                                                             #cyklus - 11x 
        x1, x2, y, b = hli[0][n][i], hli[1][n][i], hli[2][n], li[1]                     #proměnná - přiřazení hodnot osy "x1", "x2", "y" a barvy
        canvas.create_line(x1, y, x2, y, fill=b)                                        #vytvoř objekt - linku

    #slunce u linky:
    for i in (sl, sp):                                                              #cyklus - pro každou položku ze seznamu 
        x, y, r, b = i[0][0][n], i[0][1][n], i[0][2][n], i[1]                           #proměnná - přiřazení hodnot osy "x" a "y", poloměr, barva
        canvas.create_oval(x-r, y-r, x+r, y+r, fill=b)                                  #vytvoř objekt - ovál

    #planety a měsíc na liště        
    for i in range(10):                                                             #cyklus - 10x 
        x, y, r, b = hpl[0][n][i], hpl[1][n], hpl[2][n], pl[1]                          #proměnná - přiřazení hodnot osy "x" a "y", poloměr, barva
        c_ob = canvas.create_oval(x-r, y-r, x+r, y+r, fill=b)                           #vytvoř objekt - text & proměnná - pro číslo objektu
        pl[3].append(c_ob)                                                              #změna - zapiš číslo objektu do 4. položky seznamu

    #text a body na liště:        
    for i in range(10):                                                             #cyklus - 10x 
        v1 = [7, 8, 9]                                                                  #proměnná - pro seznam hodnot na výběr velikosti fontu
        f = ('Arial', v1[n])                                                            #proměnná - pro font
        x, y, tx, b = hta[0][n][i], hta[1][n], tl3[i], ta[1]                            #proměnná - přiřazení hodnot osy "x" a "y", textu, barva
        canvas.create_text(x, y, text=tx, fill=b, font=f)                               #vytvoř objekt - text
        x, y, tx, b = htb[0][n][i], htb[1][n], tl3[10], tb[1]                           #proměnná - přiřazení hodnot osy "x" a "y", textu, barva
        c_ob = canvas.create_text(x, y, text=tx, fill=b, font=f)                        #vytvoř objekt - text & proměnná - pro číslo objektu
        tb[3].append(c_ob)                                                              #změna - zapiš číslo objektu do 4. položky seznamu


#_______________________________________________________________________________FUNKCE PRO ZMĚNU MEZI ÚVODNÍM A HERNÍM PROSTŘEDÍM_________________________________
123456789012345678901234567890123456789012345+6789012345678901234567890123456789#                                                                                #
                                                                                #                                                                                #

def uvod_nebo_hra():                                                            #definice funkce - pro přechod z úvodního prostředí do hry a zpět
    if z[1] == 0:                                                                   #podmínka - pokud je zobrazeno úvodní prostředí
        zmena_nastaveni_rychlosti(u5)                                                   #volání funkce - pro změnu rychlosti na normální
        zmena_nastaveni_pohledu(u1)                                                     #volání funkce - pro změnu na základní herní pohled
        herni_prostredi()                                                               #volání funkce - pro herní prostředí
    else:                                                                           #podmínka - pokud je zobrazeno hrací prostředí
        zmena_nastaveni_rychlosti(u5)                                                   #volání funkce - pro změnu rychlosti na normální
        zmena_nastaveni_pohledu(u1)                                                     #volání funkce - pro změnu na základní herní pohled
        tb[3].clear(), pl[3].clear()                                                    #změna - vymazání složky pro čísla objektů textů a planet na liště
        uvodni_prostredi()                                                              #volání funkce - pro úvodní prostředí

#_______________________________________________________________________________FUNKCE PRO ZMĚNU RYCHLOSTI________________________________________________________
123456789012345678901234567890123456789012345+6789012345678901234567890123456789#                                                                                #
                                                                                #                                                                                #

##změna nastavení rychlosti:   
def zmena_nastaveni_rychlosti(vybrany_objekt):                                  #definice funkce - pro změnu rychlosti
    ix = z[0]                                                                       #proměnná - pro index rozlišení
    new = vybrany_objekt                                                            #proměnná - pro aktuální volbu
    for i in u4, u5, u6:                                                            #cyklus - pro každou položku ze seznamu
        if i[1] == 'yellow':                                                            #podmínka - pokud je barva objektu "žlutá"
            old = i                                                                         #proměnná - pro předchozí volbu

    if new != old:                                                                  #podmínka - pokud nově vybranný a předchozí objekt není stejný
        new[1] = 'yellow'                                                               #změna - název barvy ve seznamu pro danou rychlost na žlutou
        old[1] = 'skyblue'                                                              #změna - název barvy ve seznamu pro danou rychlost na bledě modrou
        canvas.itemconfig(new[3], fill='yellow')                                        #změna - barva textu na obrazovce na žlutou
        canvas.itemconfig(old[3], fill='skyblue')                                       #změna - barva textu na obrazovce na bledě modrou
        pomaleji, normalne, rychleji = u4, u5, u6
        
        if new == pomaleji and old == normalne:                                         #podmínka - pokud hodnoty "new" a "old" odpovídají tomuto nastavení
            for i in (p1, p2, p3, m1, p4, p5, p6, p7, p8, p9):                              #cyklus - pro každou položku ze seznamu
                i[3][1] = i[3][1] /  10                                                         #změna - vyděl přípočtový úhel o uvedenou hodnotu
        elif new == pomaleji and old == rychleji:                                       #podmínka - pokud hodnoty "new" a "old" odpovídají tomuto nastavení
            for i in (p1, p2, p3, m1, p4, p5, p6, p7, p8, p9):                              #cyklus - pro každou položku ze seznamu
                i[3][1] = i[3][1] /  100                                                        #změna - vyděl přípočtový úhel o uvedenou hodnotu
        elif new == normalne and old == pomaleji:                                       #podmínka - pokud hodnoty "new" a "old" odpovídají tomuto nastavení
            for i in (p1, p2, p3, m1, p4, p5, p6, p7, p8, p9):                              #cyklus - pro každou položku ze seznamu
                i[3][1] = i[3][1] *  10                                                         #změna - vynásob přípočtový úhel o uvedenou hodnotu
        elif new == normalne and old == rychleji:                                       #podmínka - pokud hodnoty "new" a "old" odpovídají tomuto nastavení
            for i in (p1, p2, p3, m1, p4, p5, p6, p7, p8, p9):                              #cyklus - pro každou položku ze seznamu
                i[3][1] = i[3][1] /  10                                                         #změna - vyděl přípočtový úhel o uvedenou hodnotu
        elif new == rychleji and old == pomaleji:                                       #podmínka - pokud hodnoty "new" a "old" odpovídají tomuto nastavení
            for i in (p1, p2, p3, m1, p4, p5, p6, p7, p8, p9):                              #cyklus - pro každou položku ze seznamu
                i[3][1] = i[3][1] *  100                                                        #změna - vynásob přípočtový úhel o uvedenou hodnotu
        elif new == rychleji and old == normalne:                                       #podmínka - pokud hodnoty "new" a "old" odpovídají tomuto nastavení
            for i in (p1, p2, p3, m1, p4, p5, p6, p7, p8, p9):                              #cyklus - pro každou položku ze seznamu
                i[3][1] = i[3][1] *  10                                                         #změna - vynásob přípočtový úhel o uvedenou hodnotu


#_______________________________________________________________________________FUNKCE PRO ZMĚNU POHLEDU__________________________________________________________
123456789012345678901234567890123456789012345+6789012345678901234567890123456789#                                                                                #
                                                                                #                                                                                #

##zobrazení objektů:
def zobrazeni_obj(sez_obj):                                                     #definice funkce - pro zobrazení skrytýchg objektů
    for i in sez_obj:                                                               #cyklus - pro každou položku ze seznamu
        canvas.itemconfig(i[8], state='normal')                                     #změna - zobraz objekt

##skrytí objektů:
def skryti_obj(sez_obj):                                                        #definice funkce - pro skrytí objektů
    for i in sez_obj:                                                               #cyklus - pro každou položku ze seznamu
        canvas.itemconfig(i[8], state='hidden')                                     #změna - skryj objekt                            

##změna poloměru objektů:
def zmena_vzd_r_objektu(vix, rix, n, sez_obj):                                  #definice funkce - pro změnu poloměru objektů
    for i in sez_obj:                                                               #cyklus - pro každou položku ze seznamu
        i[0][3], i[6][vix][n] = i[6][vix][n], i[0][3]                               #změna - prohození hodnot velikosti v tabulce objektu
        i[0][2], i[5][rix][n] = i[5][rix][n], i[0][2]                               #změna - prohození hodnot poloměru v tabulce objektu

##změna vzdálenosti objektů:
def zmena_vzdalenosti_objektu(ix, n, sez_obj):                                  #definice funkce - pro změnu vzdálenosti objektů
    for i in sez_obj:                                                               #cyklus - pro každou položku ze seznamu
        i[0][3], i[6][ix][n] = i[6][ix][n], i[0][3]                                 #změna - prohození hodnot velikosti v tabulce objektu

##změna měsíce:
def zmena_mesice(r, vzd, stred, rychlost):                                      #definice funkce - pro změnu měsíce
    m1[0][2], m1[0][3], m1[7] = r, vzd, stred                                       #změna - přepsání hodnot poloměru, vzdálenosti a středového tělesa
    for i in (p1, p2, p3, m1, p4, p5, p6, p7, p8, p9):                              #cyklus - pro každou položku ze seznamu
        i[3][1] = i[3][1] *  rychlost                                                   #změna - vynásob přípočtový úhel o uvedenou hodnotu

##změna velikosti slunce:
def zmena_velikosti_slunce(rsl):                                                #definice funkce - pro změnu slunce
    x, y, r = s0[0][0], s0[0][1], rsl                                               #proměnná - přiřazení hodnot osy "x" a "y" a poloměru slunce
    canvas.coords(s0[8], x-r, y-r, x+r, y+r)                                        #změna - vytvoř slunce s novým poloměrem

##změna barvy popisu při výběru:
def zmena_barvy_text(new, old):                                                 #definice funkce - pro barvy textu při přepínání pohledu
    canvas.itemconfig(new[3], fill='yellow')                                        #změna - změň barvu prvního objektu na žlutou
    canvas.itemconfig(old[3], fill='skyblue')                                       #změna - změň barvu druhého objektu na bledě modrou
    new[1], old[1] = 'yellow', 'skyblue'                                            #změna - změň barvy v tabulce objektu

##změna nastavení pohledů:
def zmena_nastaveni_pohledu(vybr_obj):                                          #definice funkce - pro změnu pohledu
    n = z[0]                                                                        #proměnná - pro hodnotu rozlišení
    q = z[1]                                                                        #proměnná - pro hodnotu úvodního, nebo herního prostředí
    radek1, radek2, radek3 = u1, u2, u3                                             #proměnná - pro pojmenování řádků
    sezn_pl = (p1, p2, p3, m1, p4, p5, p6, p7, p8, p9)                              #proměnná - pro základní seznam

    if vybr_obj == radek1 and radek2[1] == 'yellow':                                #podmínka - pokud vybraná a předchozí řádek odpovídají tomuto nastavení
        zmena_barvy_text(u1, u2)                                                        #volání funkce - pro změnu barvy textu
        if q == 0:                                                                      #podmínka - pokud je zobrazené úvodní prostředí
            zmena_velikosti_slunce(s0[0][2])                                                #volání funkce - pro změnu velikosti slunce
            zmena_vzdalenosti_objektu(2, n, sezn_pl)                                        #volání funkce - pro změnu vzdáleností objektů
        else:                                                                           #podmínka - pokud je zobrazené herní prostředí
            zobrazeni_obj((p5, p6, p7, p8, p9))                                             #volání funkce - pro zobrazení skrytých objektů
            zmena_vzd_r_objektu(3, 2, n, (p1, p2, p3, m1, p4))                              #volání funkce - pro změnu poloměru a vzdálenosti objektů

    elif vybr_obj == radek1 and radek3[1] == 'yellow':                              #podmínka - pokud vybraná a předchozí řádek odpovídají tomuto nastavení
        zmena_barvy_text(u1, u3)                                                        #volání funkce - pro změnu barvy textu
        if q == 0:                                                                      #podmínka - pokud je zobrazené úvodní prostředí
            zmena_velikosti_slunce(s0[0][2])                                                #volání funkce - pro změnu velikosti slunce
            zmena_vzd_r_objektu(1, 1, n, sezn_pl)                                           #volání funkce - pro změnu poloměru a vzdálenosti objektů
        else:                                                                           #podmínka - pokud je zobrazené herní prostředí
            zobrazeni_obj((p1, p2, p3, p4, p5, p6, p7, p8, p9))                             #volání funkce - pro zobrazení skrytých objektů                  
            zmena_velikosti_slunce(s0[0][2])                                                #volání funkce - pro změnu velikosti slunce
            vzd, r = [4, 4, 5], [1, 1, 1]                                                   #proměnné - pro seznamy hodnot na výběr vzdálenosti a poloměru 
            zmena_mesice(r[n], vzd[n], p3, 100)                                            #volání funkce - pro změnu velikosti a vzdálenosti měsíce

    elif vybr_obj == radek2 and radek1[1] == 'yellow':                              #podmínka - pokud vybraná a předchozí řádek odpovídají tomuto nastavení
        zmena_barvy_text(u2, u1)                                                        #volání funkce - pro změnu barvy textu
        if q == 0:                                                                      #podmínka - pokud je zobrazené úvodní prostředí
            v1 = [174, 220, 331]                                                            #proměnná - pro seznam hodnot na výběr velikosti slunce
            zmena_velikosti_slunce(v1[n])                                                   #volání funkce - pro změnu velikosti slunce
            zmena_vzdalenosti_objektu(2, n, sezn_pl)                                        #volání funkce - pro změnu vzdáleností objektů
        else:                                                                           #podmínka - pokud je zobrazené herní prostředí
            skryti_obj((p5, p6, p7, p8, p9))                                                #volání funkce - pro skrytí objektů                                          
            zmena_vzd_r_objektu(3, 2, n, (p1, p2, p3, m1, p4))                              #volání funkce - pro změnu poloměru a vzdálenosti objektů
            
    elif vybr_obj == radek2 and radek3[1] == 'yellow':                              #podmínka - pokud vybraná a předchozí řádek odpovídají tomuto nastavení
        zmena_barvy_text(u2, u3)                                                        #volání funkce - pro změnu barvy textu
        if q == 0:                                                                      #podmínka - pokud je zobrazené úvodní prostředí
            zmena_velikosti_slunce(s0[0][2])                                                #volání funkce - pro změnu velikosti slunce
            zmena_vzd_r_objektu(1, 1, n, sezn_pl)                                           #volání funkce - pro změnu poloměru a vzdálenosti objektů
            v1 = [174, 220, 331]                                                            #proměnná - pro seznam hodnot na výběr velikosti slunce
            zmena_velikosti_slunce(v1[n])                                                   #volání funkce - pro změnu velikosti slunce
            zmena_vzdalenosti_objektu(2, n, sezn_pl)                                        #volání funkce - pro změnu vzdáleností objektů
        else:                                                                           #podmínka - pokud je zobrazené herní prostředí                          
            zobrazeni_obj((p1, p2, p3, p4))                                                 #volání funkce - pro zobrazení skrytých objektů                  
            zmena_velikosti_slunce(s0[0][2])                                                #volání funkce - pro změnu velikosti slunce
            vzd, r = [4, 4, 5], [1, 1, 1]                                                   #proměnné - pro seznamy hodnot na výběr vzdálenosti a poloměru 
            zmena_mesice(r[n], vzd[n], p3, 100)                                             #volání funkce - pro změnu velikosti a vzdálenosti měsíce
            zmena_vzd_r_objektu(3, 2, n, (p1, p2, p3, m1, p4))                              #volání funkce - pro změnu poloměru a vzdálenosti objektů
             
    elif vybr_obj == radek3 and radek1[1] == 'yellow':                              #podmínka - pokud vybraná a předchozí řádek odpovídají tomuto nastavení
        zmena_barvy_text(u3, u1)                                                        #volání funkce - pro změnu barvy textu
        if q == 0:                                                                      #podmínka - pokud je zobrazené úvodní prostředí
            zmena_velikosti_slunce(1)                                                       #volání funkce - pro změnu velikosti slunce
            zmena_vzd_r_objektu(1, 1, n, sezn_pl)                                           #volání funkce - pro změnu poloměru a vzdálenosti objektů
        else:                                                                           #podmínka - pokud je zobrazené herní prostředí
            skryti_obj((p1, p2, p3, p4, p5, p6, p7, p8, p9))                                #volání funkce - pro skrytí objektů                            
            v1 = [8, 10, 16]                                                                #proměnná - pro seznam hodnot na výběr velikosti slunce                                                       
            zmena_velikosti_slunce(v1[n])                                                   #volání funkce - pro změnu velikosti slunce
            vzd, r = [231, 345, 462], [2, 3, 4.5]                                           #proměnné - pro seznamy hodnot na výběr vzdálenosti a poloměru 
            zmena_mesice(r[n], vzd[n], s0, 0.01)                                            #volání funkce - pro změnu velikosti a vzdálenosti měsíce

    elif vybr_obj == radek3 and radek2[1] == 'yellow':                              #podmínka - pokud vybraná a předchozí řádek odpovídají tomuto nastavení
        zmena_barvy_text(u3, u2)                                                        #volání funkce - pro změnu barvy textu
        if q == 0:                                                                      #podmínka - pokud je zobrazené úvodní prostředí
            zmena_velikosti_slunce(s0[0][2])                                                #volání funkce - pro změnu velikosti slunce
            zmena_vzdalenosti_objektu(2, n, sezn_pl)                                        #volání funkce - pro změnu vzdáleností objektů
            zmena_velikosti_slunce(1)                                                       #volání funkce - pro změnu velikosti slunce
            zmena_vzd_r_objektu(1, 1, n, sezn_pl)                                           #volání funkce - pro změnu poloměru a vzdálenosti objektů
        else:                                                                           #podmínka - pokud je zobrazené herní prostředí
            zmena_vzd_r_objektu(3, 2, n, (p1, p2, p3, m1, p4))                              #volání funkce - pro změnu poloměru a vzdálenosti objektů
            skryti_obj((p1, p2, p3, p4, ))                                                  #volání funkce - pro skrytí objektů                            
            v1 = [8, 10, 16]                                                                #proměnná - pro seznam hodnot na výběr velikosti slunce                                                       
            zmena_velikosti_slunce(v1[n])                                                   #volání funkce - pro změnu velikosti slunce
            vzd, r = [231, 345, 462], [2, 3, 4.5]                                           #proměnné - pro seznamy hodnot na výběr vzdálenosti a poloměru 
            zmena_mesice(r[n], vzd[n], s0, 0.01)                                            #volání funkce - pro změnu velikosti a vzdálenosti měsíce


#_______________________________________________________________________________FUNKCE PRO ZMĚNU POHYBU PLANET____________________________________________________
123456789012345678901234567890123456789012345+6789012345678901234567890123456789#                                                                                #
                                                                                #                                                                                #

##změna pohybu planet sluneční soustavy:
def zmena_pohybu(objekt):                                                       #definice funkce - pro změnu pohybu  
    objekt[3][2] = objekt[3][2] * -1                                                 #změna - změna hodnoty pro směr pohybu


#_______________________________________________________________________________KONTROLA KLIKNUTÍ_________________________________________________________________
123456789012345678901234567890123456789012345+6789012345678901234567890123456789#                                                                                #
                                                                                #                                                                                #

##kontrola kliknutí a volání příslušných úkonů:
def kontrola_kliknuti1(event):                                                  #definice funkce - pro kontrolu kliknutí v úvodním prodtředí 
    z[3] = z[3] + 1                                                                 #změna - přípočet hodnoty cyklu
    x_kl, y_kl = event.x, event.y                                                   #proměnná - hodnoty "x" a "y" místa kliknutí
    n = z[0]                                                                        #proměnná - pro hodnotu rozlišení prostředí
    q = z[1] 

    ##klik na planety sluneční soustavy:
    for i in (p1, p2, p3, m1, p4, p5, p6, p7, p8, p9):                              #cyklus - pro každou položku ze seznamu
        x, y, r = i[0][0]+1, i[0][1]+1, i[0][2]+1                                       #proměnná - přiřazení hodnot osy "x" a "y" a poloměru
        if abs(x_kl - x) < (r + 1) and abs(y_kl - y) < (r + 1):                         #podmínka - pokud je kliknutí v rozmezí os objektu
            zmena_pohybu(i)                                                                 #volání funkce - pro změnu pohybu

    ##klik na výběr z možností:
    for i in (u1, u2, u3, u4, u5, u6, u7, u8):                                      #cyklus - pro každou položku ze seznamu
        x, y, rx = i[0][0][n]+1, i[0][1][q][n]+1, i[0][2][n]+1                          #proměnná - přiřazení hodnot osy "x" a "y" a velikost "x"
        v1 = [8, 9, 10]                                                                 #proměnná - pro seznam na výběr velikosti "y" 
        ry = v1[n]                                                                      #proměnná - pro velikost "y"
        if x_kl in range(x-rx, x+rx) and y_kl in range(y-ry, y+ry):                     #podmínka - pokud je kliknutí v rozmezí os objektu
            if i in (u1, u2, u3):                                                           #podmínka - pokud objekt je v tomto seznamu
                zmena_nastaveni_pohledu(i)                                                      #volání funkce - pro nastavení velikosti těles
            elif i in (u4, u5, u6):                                                         #podmínka - pokud objekt je v tomto seznamu
                zmena_nastaveni_rychlosti(i)                                                    #volání funkce - pro změnu rychlosti
            elif i == u7:                                                                   #podmínka - pokud objekt je u7
                print("napoveda()")                                                                 #volání funkce - pro nápovědu
            elif i == u8:                                                                   #podmínka - pokud objekt je u8
                uvod_nebo_hra()                                                               #volání funkce - pro vstup do hry


#_______________________________________________________________________________CYKLUS POHYBU PLANET______________________________________________________________
123456789012345678901234567890123456789012345+6789012345678901234567890123456789#                                                                                #
                                                                                #                                                                                #

##aktivace cyklu pro pohyb planet:
def cyklus_soustavy():                                                          #definice funkce - cyklus pro úvodní prostředí    
    z[2] = z[2] + 1                                                                 #změna - přípočet hodnoty cyklu
    z[4] = 0                                                                        #změna - vymazání hodnoty celkových bodů
    n = z[0]                                                                        #proměnná - pro hodnotu rozlišení
    q = z[1]                                                                        #proměnná - pro hodnotu úvodního, nebo herního prostředí
    
    for i in (p1, p2, p3, m1, p4, p5, p6, p7, p8, p9):                              #cyklus - pro každou položku ze seznamu
        uhel_na_cykl, smer, uhel_celkem = i[3][1], i[3][2], i[3][3]                     #proměnná - přiřazení hodnot uhlu na cykl, směr posunu, uhel celkem
        novy_uhel = round((uhel_na_cykl * smer) + uhel_celkem, 5)                       #proměnná - pro výpočet nového úhlu
        i[3][3] = novy_uhel                                                             #změna - zapsání nového úhlu do tabulky
        x_st, y_st, vzd = i[7][0][0], i[7][0][1], i[0][3]                               #proměnná - pro osu "x" a "y" středu a vzdálenost
        cos = math.cos(math.radians(novy_uhel))                                         #proměnná - pro výpočet hodnoty cos
        sin = math.sin(math.radians(novy_uhel))                                         #proměnná - pro výpočet hodnoty sin
        x = round(x_st + vzd * cos, 4)                                                  #proměnná - pro výpočet nové osy "x"
        y = round(y_st + vzd * sin, 4)                                                  #proměnná - pro výpočet nové osy "y"
    
        cob, r = i[8], i[0][2]                                                          #proměnná - pročíslo objektu, poloměr
        canvas.coords(cob, x-r, y-r, x+r, y+r)                                          #změna - posun na nové souřadnice
        i[0][0] = x                                                                     #změna - zápis nové souřadnice "x"
        i[0][1] = y                                                                     #změna - zápis nové souřadnice "y"
        i[1][0] = int(sin * 100 * -1)                                                   #změna - zápis nové hodnoty bodů
        i[1][1] = round(sin * -1, 4)                                                    #změna - zápis nové hodnoty pro lištu
        if i != m1:                                                                     #podmínka - pokud zpracovávaný objekt není měsíc
            z[4] = z[4] + int(sin * 100 * -1)                                           #připočti body do celkových bodů

    z[4] = 100 - (z[4] // 9)                                                        #změna - celkové body vyděl počtem planet a odečti od hodnoty 100 bodů
        
    if q == 1:                                                                      #podmínka - pokud je aktivní herní prostředí
        canvas.itemconfig(i2[3], text=z[2])                                             #změna - změň hodnotu cyklu
        canvas.itemconfig(i4[3], text='')                                               #změna - změň hodnotu dnů
        canvas.itemconfig(i6[3], text=z[3])                                             #změna - změň hodnotu kliků                                     
        canvas.itemconfig(i8[3], text=z[4])                                             #změna - změň hodnotu bodů
        sez = [p1, p2, p3, m1, p4, p5, p6, p7, p8, p9]                                  #proměnná - pro seznam pro další úkony
        for c, i in enumerate(tb[3]):                                                   #cyklus - pro každou položku seznamu a její pořadí
            canvas.itemconfig(i, text=f'{sez[c][1][1]:.4f}')                                #změna - hodnoty pohybu planet na liště
        for c, i in enumerate(pl[3]):                                                   #cyklus - pro každou položku seznamu a její pořadí
            x, r = hpl[0][n][c], hpl[2][n]                                                  #proměnná - přiřazení hodnot osy "x" a poloměri
            y = hpl[1][n] - sez[c][1][1] * 50                                               #proměnná - výpočet a přiřazení hodnot osy "y" 
            canvas.coords(i, x-r, y-r, x+r, y+r)                                            #změna - poloha planety na liště

    canvas.after(1, cyklus_soustavy)                                                #časovač - opětovné volání funkce pro cyklus
        

#_______________________________________________________________________________VYTVOŘENÍ ÚVODNÍHO PROSTŘEDÍ______________________________________________________
123456789012345678901234567890123456789012345+6789012345678901234567890123456789#                                                                                #
                                                                                #                                                                                #

##aktivace úvodního prostředí a klikání:
def uvodni_prostredi():                                                         #definice funkce - vytvoření prostředí pro úvodní prostředí
    canvas.delete('all')                                                            #změna - smaž všechny objekty
    z[1] = 0                                                                        #změna - vložení čísla označující uvodní prostředí 
    n = z[0]                                                                        #proměnná - pro hodnotu rozlišení prostředí
    q = z[1]                                                                        #proměnná - pro hodnotu úvodního, nebo herního prostředí

    ##sluneční soustava:
    for i in (s0, p1, p2, p3, m1, p4, p5, p6, p7, p8, p9):                          #cyklus - pro každou položku ze seznamu
        i[0][0] = s0[0][0]
        x, y, r, b = i[0][0], i[0][1], i[0][2], i[2]                                    #proměnná - přiřazení hodnot osy "x" a "y", poloměr, barva
        cislo_objektu = canvas.create_oval(x-r, y-r, x+r, y+r, fill=b)                  #vytvoř objekt - ovál a přiřaď jeho číslo do proměnné
        i.pop()                                                                         #změna - odstraň číslo objektu z předchozího náhledu
        i.append(cislo_objektu)                                                         #změna - přidání čísla objektu do seznamu objektu

    ##výběr možností:
    for i in (u1, u2, u3, u4, u5, u6, u7, u8):                                      #cyklus - pro každou položku ze seznamu
        x, y, xr, = i[0][0][n], i[0][1][q][n], i[0][2][n]                               #proměnná - přiřazení hodnot osy "x" a "y", velikost "x"
        b1, b2, t = i[1], 'blue', i[2][q]                                               #proměnná - přiřazení hodnot barva1, barva2 a text
        v1, v2 = [6, 7, 8], [8, 9, 10]                                                  #proměnná - na seznamy pro výběr hodnot
        f, yr, = ('Arial', v1[n]), v2[n]                                                #proměnná - přiřazení hodnot font, velikost "y"
        canvas.create_rectangle(x-xr, y-yr, x+xr, y+yr, outline=b2)                     #vytvoř objekt - obdelník
        cislo_objektu = canvas.create_text(x, y, text=t, fill=b1, font=f)               #vytvoř objekt - text a přiřaď jeho číslo do proměnné
        i.pop()                                                                         #změna - odstraň číslo objektu z předchozího náhledu
        i.append(cislo_objektu)                                                         #změna - přidání čísla objektu do seznamu objektu

    ##aktivace klikání a volání cyklu pohybu planet:
    canvas.bind('<ButtonPress-1>', kontrola_kliknuti1)                              #provázání - kliknutí levým tl. myši s funkcí pro kontrolu kliknutí
    cyklus_soustavy()                                                               #volání funkce - pro pohyb soustavy

        
#_______________________________________________________________________________VÝBĚR ROZLIŠENÍ___________________________________________________________________
123456789012345678901234567890123456789012345+6789012345678901234567890123456789#                                                                                #
                                                                                #                                                                                #

##změna prostředí dle vybraného rozlišení a volání úvodního prostředí:
def zmena_rozliseni(x, y, n):                                                   #definice funkce - pro vytvoření plochy dle zvoleného rozlišení
    canvas.config(width = x, height = y,)                                           #změna - změň velikost plochy dle uvedených parametrů
    canvas.unbind('<ButtonPress-1>')                                                #změna - zrušení kontroli klikání
    z[0] = n                                                                        #změna - vložení pořadí rozlišení prostředí

    for i in (s0, p1, p2, p3, m1, p4, p5, p6, p7, p8, p9):                          #cyklus - pro každou položku ze seznamu
        i[0].append(i[4][0][n])                                                         #změna - přidej do umístění hodnotu osy "x"
        i[0].append(i[4][1][n])                                                         #změna - přidej do umístění hodnotu osy "y"
        i[0].append(i[5][0][n])                                                         #změna - přidej do umístění hodnotu poloměru
        i[0].append(i[6][0][n])                                                         #změna - přidej do umístění hodnotu středové vzdálenosti
    uvodni_prostredi()                                                              #volání funkce - vytvoření úvodního prostředí

##kontrola kliknutí a výběr hodnot:
def kontrola_kliknuti(event):                                                   #definice funkce - pro kliknutí levým tlačítkem myši při výběru rozlišení
    x, y = event.x, event.y                                                         #proměnná - hodnoty "x" a "y" místa kliknutí
    if x in range(20, 160) and y in range(30, 70):                                  #podmínka - pokud jsou hodnoty "x" a "y" kliku v rozmezí uvedených hodnot
        zmena_rozliseni(800, 600, 0)                                                    #volání funkce - pro změnu prostředí
    elif x in range(20, 160) and y in range(70, 110):                               #podmínka - pokud jsou hodnoty "x" a "y" kliku v rozmezí uvedených hodnot
        zmena_rozliseni(1080, 720, 1)                                                   #volání funkce - pro změnu prostředí
    elif x in range(20, 160) and y in range(110, 150):                              #podmínka - pokud jsou hodnoty "x" a "y" kliku v rozmezí uvedených hodnot
        zmena_rozliseni(1920, 1080, 2)                                                  #volání funkce - pro změnu prostředí

##vytvoření tabulky na výběr rozlišení a provázání kliku:
def vyber_rozliseni():                                                          #definice funkce - vytvoření prostředí pro výběr rozlišení
    for i in (50, 90, 130):                                                         #cyklus - pro uvedené hodnoty
        x, y, xr, yr = 90, i, 70, 18                                                    #proměnná - "x" a "y" pro nakreslení obdelníku + hodnota poloměru strany("r")  "x" a "y" 
        canvas.create_rectangle(x-xr, y-yr, x+xr, y+yr, fill='gray' )                   #vytvoř objekt - obdelník

    vr1 = 20,   'Vyber rozlišení:',  ('Arial Black', 8),   'gray'                   #proměnná- 1. řádek
    vr2 = 50,   '800 x 600',         ('Arial Black', 10),  'black'                  #proměnná- 2. řádek
    vr3 = 90,   '1080 x 720',        ('Arial Black', 10),  'black'                  #proměnná- 3. řádek
    vr4 = 130,  '1920 x 1080',       ('Arial Black', 10),  'black'                  #proměnná- 4. řádek

    for i in (vr1, vr2, vr3, vr4):                                                  #cyklus - pro uvedené seznamy hodnot
        x, y, t, f, b = 90, i[0], i[1], i[2], i[3]                                      #proměnná - hodnoty osy "x" a "y", text, font, barva
        canvas.create_text(x, y, text=t, font=f, fill=b)                                #vytvoř objekt - text

    canvas.bind('<ButtonPress-1>', kontrola_kliknuti)                               #provázání - kliknutí levým tl. myši s funkcí pro kontrolu kliknutí

##aktivace programu:
vyber_rozliseni()                                                               #volání funkce - vytvoř prostředí pro výběr rozlišení

##aktivace grafické aplikace:
tkinter.mainloop()






