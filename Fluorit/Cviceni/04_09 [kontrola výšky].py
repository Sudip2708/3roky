##  Žiaci sú v rad100e zoradení podľa veľkosti (od najmenšieho).
##  Napíš program, ktorému najprv postupne oznamujeme (pomocou input)
##  výšky žiakov a ten na záver (zadali sme „prázdnu“ výšku) vypíše,
##  či boli zoradení správne. Použi príkaz while (dopredu nepoznáme počet žiakov),
##  v ktorom bude príkaz if.
##
##  Mali by fungovať takéto spustenia programu:
##    
##    zadávaj výšky žiakov
##       výška 1. žiaka: 100
##       výška 2. žiaka: 110
##       výška 3. žiaka: 110
##       výška 4. žiaka: 120
##       výška 5. žiaka:
##    všetci žiaci sú zoradení správne
##
##    zadávaj výšky žiakov
##       výška 1. žiaka: 100
##       výška 2. žiaka: 120
##       výška 3. žiaka: 110
##       výška 4. žiaka: 140
##       výška 5. žiaka: 145
##       výška 6. žiaka:
##    žiaci nie sú správne zoradení


#úvodní a prázdný řádek:
print('KONTROLY VÝŠKY')
print('program zkontroluje, zda zadávání výšky je vzestupného charakteru')
print()


#vstupní data a proměné:
print('Zadávej výšky žáků: ')                       #výpis úvodního řádku
a = input('    výška 1. žáka: ')                    #vstup na první hodnotu
b = 0                                               #předcházející hodnota pro porovnání
c = 1                                               #počítadlo 
d = 1                                               #ověření, zda všechny údaje jsou seřazeny vzestupně 0/1


#výpočet a výstup:
if a == '':                                         #kontrola zda nebyl zmáčknutý enter
    a = 0                                           #pokud ano, pak zapsat 0
else:
    a = int(a)                                      #pokud ne, pak převést na číslo

while a != 0:                                       #cyklus - dokud "a" není 0
    if b > a:                                       #porovnat, zda je nové číslo stejné nebo větší 
        d = 0                                       #pokud ne zapsat do "d" 0
    b = a                                           #dát novou hodnotu do "b" pro kontrolu v příštím kole
    c += 1                                          #přičti k počítadli 1
    a = input(f'    výška {c}. žáka: ')             #vstup dalšího čísla
    if a == '':                                     #kontrola zda nebyl zmáčknutý enter
        a = 0                                       #pokud ano, pak zapsat 0
    else:
        a = int(a)                                  #pokud ne, pak převést na číslo

if d > 0:                                           #pokud jsou správně seřazeni, vypiš následující řádek.
    print('Všichni žáci jsou seřazeni správně.')
else:                                               #pokud nejsou správně seřazeni, vypiš následující řádek.
    print('Žáci nejsou seřazeni správně.')
        

#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]')    
