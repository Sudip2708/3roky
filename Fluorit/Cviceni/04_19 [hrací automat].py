##  Hrací automat mi pri každom zatlačení (hodil som do neho 1 euro)
##  dá 3 náhodné čísla z intervalu <1, 20>.
##  Ak sú medzi týmito tromi číslami dve rovnaké, vyhrávam 5 euro,
##  ak sú všetky tri rovnaké vyhrávam 100 euro.
##  Začal som s nejakou sumou a hral som maximálne 1000 zatlačení,
##  prípadne som skončil skôr, keď som všetko prehral.
##  Napíš program, ktorý to všetko odsimuluje:
##  pri každom zatlačení vypíše '+5' alebo '+100',
##  ak som niečo vyhral, alebo '-1', ak som nič nevyhral.
##
##  Napríklad:
##    začínam so sumou: 20
##    štart -1-1-1-1-1-1-1+5-1-1-1-1+5-1-1-1-1-1-1-1-1+5-1+5-1-1-1-1-1-1+5-1+5
##    -1-1-1-1-1-1-1-1-1+5+5-1-1-1-1+5-1-1-1+5-1-1-1+5+5-1-1+5+5-1-1+5-1-1-1-1
##    -1-1-1-1+5-1-1-1+5-1+5-1-1-1-1+5-1+5-1-1+5-1-1-1-1-1-1-1+5-1+5-1-1-1-1-1
##    +5-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1+5-1-1-1-1-1+5-1
##    -1-1-1+5-1-1+5-1-1-1-1-1-1-1-1-1-1-1-1
##    zostalo mi 0 euro


#úvodní a prázdný řádek:
print('HRACÍ AUTOMAT')
print('program simuluje hru na automatu, kde po zadání vstupní hodnoty za tebe odehraje 100 her')
print()


#načtení modulu:
import random


#vstupní data a proměné:
a = int(input('Zadej počáteční sumu: '))        #vstup počáteční sumy
b = 0                                           #počet zatočení


#výpočet a výstup:
for i in range(100):                            #cyklus pro max 100 opakování
    if a > 0:                                   #podmínka - když je moje suma větší než 0
        h1 = random.randint(1, 20)              #1. hod
        h2 = random.randint(1, 20)              #2. hod
        h3 = random.randint(1, 20)              #3. hod
        if h1 == h2 == h3:                      #podmínka - pokud jsou všechny hody stejný
            a += 100                            #připiš 100
            print('+100', end='')               #vypiš sumu
        elif h1 == h2 or h2 == h3 or h3 == h1:  #podmínka - pokud jsou jen dvě čísla stejný
            a += 5                              #připiš 5
            print('+5', end='')                 #vypiš sumu
        else:                                   #ve všech ostatních případech (čísla nejsou stejná)
            a += -1                             #odepiš 1
            print('-1', end='')                 #vypiš sumu
        b += 1                                  #přípočet k počtu zatočení
    else:                                       #v případě, že je moje suma 0
        break                                   #přerušit hraní
print()                                         #odskočení na další řádek
print(f'Zůstalo mi {a} euro')                   #výpis jak jsem dopadl
print(f'{b} jsem si zatočil.')                  #výpis kolikrát jsem si zahrál
        

#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]')    




    

