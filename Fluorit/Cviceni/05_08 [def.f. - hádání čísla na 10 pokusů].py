##  Napíš funkciu hadanie(od, do), pomocou ktorej sa budeš vedieť zahrať s počítačom takúto hru:
##  počítač si náhodne pomyslí číslo z intervalu <od, do> (neprezradí nám ho)
##  a my sa ho budeme na maximálne 10 pokusov snažiť uhádnuť.
##  Po každom pokuse nám oznámi, či náš typ je menší ako jeho číslo alebo väčší.
##
##  Priebeh hry by mohol vyzerať, napríklad takto:
##    >>> hadanie(1, 100)
##    Myslím si číslo, uhádni ho!
##    tvoj tip: 50
##    *** pridaj
##    tvoj tip: 75
##    *** pridaj
##    tvoj tip: 88
##    *** uber
##    tvoj tip: 81
##    *** uber
##    tvoj tip: 78
##    *** uber
##    tvoj tip: 77
##    Uhádol si na 6. pokus. Gratulujem.


#úvodní a prázdný řádek:
print('DEFINOVÁNÍ FUNKCE - HÁDÁNÍ 21')
print('hra na tipování hledaného čísla na 10 pokusů')
print()


#import modulu:
import random   


#definování funkce:
def hadanie(od=1, do=100):                                                            
    c = 1                                                       #počítadlo pokusů
    d = 0                                                       #proměná pro tipované číslo
    e = random.randint(od, do)                                  #přidělení hledaného čísla

    print()                                                     #prázdný řádek a úvodní věta
    print(f'Myslím si číslo od {od} do {do} a ty máš 10 pokusů na to, abys ho uhádnul.')

    while c < 11:                                               #cyklus na 10 pokusů
        d = int(input(f'Jaký je tvůj {c} tip: '))               #vstup tipovaného čísla
        if e < d:                                               #podmínka - pokud je tipované číslo větší
            print('**** uber ****')                             #vypiš "uber"
        if e > d:                                               #podmínka - pokud je tipované číslo menší
            print('*** přidej ***')                             #vypiš "přidej"
        if e == d:                                              #podmínka - pokud jsi číslo uhádl
            print('!GRATULUJI!')                                #vypiš "Gratuluji"
            print(f'Uhádl jsi na {c}. pokus')                   #vypiš na kolíkátý pokus se podařilo
            break                                               #vyskoč z cyklu
        c += 1                                                  #přípočet do počítadla pokusů
    if e != d:                                                  #podmínka - pokud jsi číslo neuhodl ani na 10 pokusů (while cyklus)
        print('Neuhádl jsi ani na 10. pokus')                   #oznam  - o neuhodnuutí čísla
        print(f'Hledané číslo bylo číslo: {e}')                 #oznam  - jaké číslo bylo hledáno


#vstup:
x = input('Pokud chceš hrát hru 1 - 100, zmáčkni [enter] \nPro volbu rozpětí, zmáčkni libovolnou kávesu a [enter]')
if x == '':
    hadanie(1, 100)
else:
    od = int(input('Zadej číslo "od" a zmáčkni [enter]: '))
    do = int(input('Zadej číslo "do"a zmáčkni [enter]: '))
    hadanie(od, do)
      

#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]')  
