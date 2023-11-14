##  Napíš program, ktorý si vypýta meno súboru a potom z každého riadku,
##  ktorý obsahuje aspoň tri slová, vypíše druhé slovo.
##
##  Napríklad:
##    meno súboru: text2.txt
##    druhé slová:
##    zakladne
##    prve,
##    druhe,
##    tretie,


#úvodní a prázdný řádek:
print('TEXTOVÉ SOUBORY - DRUHÉ SLOVO ŘÁDKU')
print('''program, který po zadání odkazu na soubor s textem, vypíše z každého řádku,
který obsahuje alespoň 3 slova, druhé slovo''')
print()
print('jméno souboru pro otestování: 07_05.txt')
print()


#vstup + otevření souboru:
soubor = open(input('Zadej jméno souboru: '), 'r')      #načtení a otevření souboru


#proměnné:
výsledek = ''                                           #proměnná výsledku


#výpočet:
for řádek in soubor:                                    #cyklus - pro řádek v souboru
    if řádek.strip().count(' ') >= 2:                   #podmínka - pokud řádek (očištěný od mezer před a za) má už jen 2 mezery
        a = řádek[řádek.find(' ')+1:]                   #proměná pro řádek bez prvního slova
        výsledek += a[:a.find(' ')] + '\n'              #přiřazení druhého slova do výsledku
soubor.close()                                          #zavření souboru


#výpis
print('Druhá slova: ')                                  #výpis prvního řádku
print(výsledek)                                         #výpis výsledku
         

#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]')    
 
