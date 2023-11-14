##  Napíš pythonovský skript, ktorý:
##
##    1.) pomocou príkazu input('?') najprv prečíta nejaký reťazec
##    2.) vypíše jeho dĺžku (počet znakov reťazca) pomocou print('dlzka =', dlzka_retazca)
##    3.) vypíše prevrátený reťazec pomocou print('prevrat =', iny_retazec)
##    4.) vypíše šachovnicu (pomocou print()) zo znakov reťazca a znakov '*' a ' '
##        > striedajú sa v nej znaky načítaného reťazca a znaku '*'
##        > šachovnica má dvojnásobný počet riadkov (aj stĺpcov) v porovnaní s dĺžkou reťazca
##          (zrejme dĺžka textov v riadkoch bude približne 4-krát dĺžka vstupného reťazca)
##
##  Napríklad, ak zadáme reťazec abc, dostávame tento výstup:
##
##    ?abc
##    dlzka = 3
##    prevrat = cba
##    a * b * c *
##    * a * b * c
##    a * b * c *
##    * a * b * c
##    a * b * c *
##    * a * b * c
##
##  Ak zadáme reťazec x, dostávame tento výstup:
##
##    ?x
##    dlzka = 1
##    prevrat = x
##    x *
##    * x
##
##  Tvoj odovzdaný program s menom riesenie.py musí začínať tromi riadkami komentárov
##  (zmeň meno a dátum odovzdania):
##
##    # 1. zadanie: retazec
##    # autor: Janko Hraško
##    # datum: 7.10.2021
##
##  V programe používaj len konštrukcie jazyka Python, ktoré sme sa učili na prvých 2 prednáškach.
##  Nepoužívaj príkaz import.


# 1. zadanie: retazec
# autor: Dalibor Sudip Sova
# datum: 16.7.2022


#úvod a 2 prázdné řádky:
print('TÝDENNÍ PROJEKT PO 2. LEKCI')
print()
print()


#vstupní data a 2 prázdné řádky:
a = input('Zadej TEXT ŘETĚZCE a po té zmáční [Enter]: ')
print()
print()


#výpočet počtu znaků:
b = len(a)                                      #výpočet počtu znaků
print(f'Celkový počet znaků: {b}')              #výpis počtů znaků
print()                                         #prázdný řádek


#výpočet pro převrácení znaků:
c = ''                                          #kontejner na převrácené slovo
for i in a:                                     #cyklus pro převrácení slova
    c = i + c                                   #zápis do kontejneru v opačném pořadí
print(f'Opačné pořadí znaků: {c}')              #výpis v opačném pořadí
print()                                         #prázdný řádek


#výpočet šachovnice:
print('Šachovice ze znaků a hvězdiček: ')       #úvod
print()
for i in range(b):                              #cyklus dvojřádků šachovnice dle počtu zadaných znaků
    for i in a:                                 #cyklus pro první řádek šachovnice
        print(f'{i} * ', end='')                #výpis prvního řádku šachovnice
    print()                                     #odskočení na další řádek
    for i in a:                                 #cyklus pro druhý řádek šachovnice
        print(f'* {i} ', end='')                #výpis druhého řádku šachovnice
    print()                                     #odskočení na další řádek

       
#2 prázdné řádky a příkaz pro neuzavření okna
print()
print()
input('[zmáčkni [Enter] pro uzavření okna]')
