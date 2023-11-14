##  Podobný príklad predchádzajúcemu,
##  lenže teraz budeme hádzať ľubovoľným počtom kociek:
##  Napíš program, ktorý si najprv vypýta n (počet hádzaní) a počet kociek.
##  Potom n-krát vypíše čísla na kockách a ich súčet.
##
##  Môžeš dostať takýto výstup:
##
##    zadaj n: 3
##    zadaj počet kociek: 4
##    na 1. kocke padla 3
##    na 2. kocke padla 2
##    na 3. kocke padla 2
##    na 4. kocke padla 2
##    ich súčet je 9
##    ======================
##    na 1. kocke padla 4
##    na 2. kocke padla 6
##    na 3. kocke padla 1
##    na 4. kocke padla 5
##    ich súčet je 16
##    ======================
##    na 1. kocke padla 1
##    na 2. kocke padla 4
##    na 3. kocke padla 6
##    na 4. kocke padla 3
##    ich súčet je 14
##    ======================


#úvodní a prázdný řádek:
print('HOD LIBOVOLNÝM POČTEM KOSTEK A JEJICH SOUČET')
print()


#vstupní data:
a = int(input('Zadej POČET KOSTEK a po té zmáční [Enter]: '))   #vstup na počet kostek
b = int(input('Zadej POČET HODŮ a po té zmáční [Enter]: '))     #vstup na počet hodů


#prázdný řádek
print()


#výpočet:
import random                                                   #import modulu random
for i in range(b):                                              #cyklus pro počet hodů
    c = 1                                                       #pořadové číslo kostky
    d = 0                                                       #součet hodnot hozených kostek
    for j in range(a):                                          #cyklus pro počet kostek v hodu
        e = random.randint(1,6)                                 #náhodné číslo od 1 do 6
        print(f'na {c}. kostce padla {random.randint(1,6)}')    #výpis hodu
        c += 1                                                  #přípočet kostky v pořadí
        d += e                                                  #přípočet hodnot hozených kostek v jednom hodu
    print(f'jejich součet je {d}')                              #výpis jejich součtu
    print(20 * '=')                                             #oddělení jednotlivých sad hodů


#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]')
