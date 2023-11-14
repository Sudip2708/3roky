import tkinter                                                                  #import modulu tkinter
import random                                                                   #import modulu random

def nahodne(n):                                                                 #definice funkce pro vytvoření dvojrozměrné tabulky s náhodnými hodnotami 1 a 0 (parametr - počet řádků/sloupců)
    vysl = []                                                                       #seznam na výsledek
    for i in range(n):                                                              #cyklus pro řádky dle počtu 'n'
        vysl.append([])                                                                 #vlož do seznamu 'vysl' prázdný seznam
        for j in range(n):                                                              #cyklus pro sloupce (seznam v seznamu) dle počtu 'n'
            vysl[-1].append(random.randrange(2)) #(10)==1)                                        #vlož do posledního vytvořené položky seznamu náhodně 1 nebo 0 (v poměru 10:1)
    return vysl                                                                     #vrať seznam 'vysl'

def kresli(tab, d=8):                                                           #definice funkce na nakreslení sítě tabulky do grafické plochy (parametr - tabulka, velikost pole)
    canvas.delete('all')                                                            #zmaž celý obsah grafické plochy
    for r, riadok in enumerate(tab):                                                #pro každý (řádek) prvek první tabulky a jeho index
        for s, prvok in enumerate(riadok):                                              #pro každý (sloupec) prvek druhé tabulky a jeho index
            x, y = s*d +5, r*d +5                                                           #přiřazení hodnoty x a y dle hodnoty velikosti pole a s odsazením od kraje (hodnota 5)
            farba = ('white', 'black')[prvok]                                               #výběr barvy (dle hodnoty prvku - 0 = bílá, 1 = černá)
            canvas.create_rectangle(x, y, x+d, y+d, fill=farba, outline='lightgray')        #vytvoř pole dle zadaných údajů
    canvas.update()                                                                 #aktualizuj plochu kreslícího plátna

def nova_generacia(p):                                                          #definice funkce pro vytvoření seznamu pro novou generaci (parametr - tabulka)
    nova = []                                                                       #seznam pro nové hodnoty
    for r in range(len(p)):                                                         #cyklus pro každý (řádek) prvek první tabulky, dle jejich počtu (hodnoty indexu)
        nova.append([0] *len(p[r]))                                                     #přidej do každého 'řádku' počet sloupců, dle počtu (hodnoty indexu)
    for r in range(1, len(p)-1):                                                    #cyklus pro každý (řádek) prvek první tabulky, dle jejich počtu (hodnoty indexu), ale bez prvního a posledního 
        for s in range(1, len(p[r])-1):                                                 #cyklus pro každý (sloupec) prvek druhé tabulky, dle jejich počtu (hodnoty indexu), ale bez prvního a posledního 
            ps = (  p[r-1][s-1] + p[r-1][s] + p[r-1][s+1]  +
                    p[r][s-1]   + 0         + p[r][s+1]    +
                    p[r+1][s-1] + p[r+1][s] + p[r+1][s+1]  )                                #součet hodnot všech přilehlých polí
            #if ps==3 or (ps==2 and p[r][s]==1):                                            #podmínka - pokud součet hodnot všech přilehlých polí je 3, nebo 2, ale pole bylo v minulé generaci aktivní (hodnota 1)
            if ps==3 or ps==2 and p[r][s]:                                                  #podmínka - zkrácený zápis
                nova[r][s] = 1                                                              #zapič na dané místo hodnotu 1
    return nova                                                                     #vrať seznam 'nova'

canvas = tkinter.Canvas(width=410, height=410)                                  #vytvoř plátno canvasu
canvas.pack()                                                                   #aktivuj plátno canvasu

plocha = nahodne(50)                                                            #vytvoření prvního seznamu pro nultou generaci 
kresli(plocha)                                                                  #vykreslení seznamu do grafické plochy
#for i in range(1000):                                                           #cyklus - dle zadané hodnoty
while True:                                                                     #věčný cyklus
    plocha = nova_generacia(plocha)                                                 #vytvoření seznamu pro další generaci
    kresli(plocha)                                                                  #vykreslení seznamu do kreslící plochy

tkinter.mainloop()                                                              #hlavní smyčka grafického plátny
