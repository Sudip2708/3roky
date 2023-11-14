##  Napíš program, ktorý si vypýta meno súboru
##  a potom vypíše každý druhý znak z prvého riadka tohto súboru.
##
##  Napríklad:
##    zadaj meno súboru: text1.txt
##    každý druhý znak: 'oia aort useumzu'
##    zadaj meno súboru: text2.txt
##    každý druhý znak: 'r aldezkn ooiy'


#úvodní a prázdný řádek:
print('TEXTOVÉ SOUBORY - DRUHÉ ZNAKY PRVNÍHO ŘÁDKU')
print('program, který po zadání odkazu na soubor s textem, vypíše každý druhý znak z prvního řádku')
print('jméno souboru pro otestování: 07_02.txt')
print()


#vstup + otevření souboru:
soubor = open(input('Zadej jméno souboru: '), 'r')  #načtení a otevření souboru


#prázdný řádek
print()


#proměnné
řádek_1 = soubor.readline()                         #načtení prvního řádku
výsledek = ''                                       #promněnná pro výsledná text
počítadlo = 0                                       #počítadlo lichá/sudá


#výpočet:
for i in řádek_1:                                   #cyklus - pro znaky prvního řádku
    if počítadlo == 1:                              #podmínka - když je sudý znak
        výsledek += i                               #přičti znak do výsledku
        počítadlo = 0                               #počítadlo nastav na 0
    else:                                           #jinak
        počítadlo = 1                               #počítadlo nastav na 1
print(výsledek)                                     #výpis výsledku


#uzavření souboru
soubor.close()
        

#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]')  
