##  Napiš program, který zadané číslo rozloží na prvočinitele
##  (vyjádří ho jako součin prvočísel).
##
##  Tento rozklad zapiš ve tvaru rovnosti s násobením: 
##    zadaj číslo: 60
##    60 = 2 * 2 * 3 * 5
##
##  V programu bude while-cyklus,
##  ve kterém budeš postupně zkoušet dělit zadané číslo různými děliteli:
##  je-li číslo tímto dělitelem dělitelné,
##  tak ho vypíšeš a samotné číslo vydělíš těmto dělitelům,
##  jinak dělitel zvýšíš o 1 a celé se to opakuje. 


#úvodní a prázdný řádek:
print('PRVOČINITELE')
print('program rozebere zadané číslo na jeho prvočinitele')
print()


#vstupní data a proměné:
a = int(input('Zadej číslo: '))     #vstup čísla
b = a                               #součin čísel prvodělitelů
c = 0                               #údaj pro první if


#výpočet a výstup:
print(b, '= ', end='')              #výpis první části
while b != 1:                       #hlavní cyklus - dokud po dělení nezůstane 1
    for i in range(2, b+1):         #jdi číslo po číslu od 2 do konečného čísla
        if b % i == 0 and c == 0:   #pokud po dělení je 0 a v "c" je také 0
            print(i, end='')        #vypiš číslo
            b = int(b / i)          #poděl s ním zadanou hodnotu
            c = 1                   #změň c na 1 (takže už není 0)
            break                   #přeruš proces a vrať se k hlavnímu cyklu
        if b % i == 0:              #pokud po dělení je 0 
            print(' *', i, end='')  #vypiš číslo a před něj hvězdičku
            b = int(b / i)          #poděl s ním zadanou hodnotu
            break                   #přeruš proces a vrať se k hlavnímu cyklu        
        

#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]')    

        
        
##Nový vzorec:
##a = int(input('Zadej číslo: '))
##for i in range(2, a+1):
##    if a % i == 0:
##        while a % i == 0:
##            print(i, end=', ')
##            a //= i
