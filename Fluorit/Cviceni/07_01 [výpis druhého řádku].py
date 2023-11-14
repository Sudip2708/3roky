##  Napíš program, ktorý si vypýta meno súboru a z tohto súboru vypíše druhý riadok.
##
##  Napríklad:
##    zadaj meno súboru: text1.txt
##    druhý riadok súboru: 'len jednu prednost'


#úvodní a prázdný řádek:
print('TEXTOVÉ SOUBORY - DRUHÝ ŘÁDEK')
print('program, který po zadání odkazu na soubor s textem, vypíše jeho druhý řádek')
print('jméno souboru pro otestování: 07_01.txt')
print()


#vstup + otevření souboru:
soubor = open(input('Zadej jméno souboru: '), 'r')  #načtení a otevření souboru


#prázdný řádek
print()


#proměnná:
vysledek = ''                                       #promněnná pro výsledná text


#výpočet:
for i in range(2):                                  #cyklus 2x
    vysledek = soubor.readline()                    #přiřazení řádků do výsledku
print(vysledek)                                     #výpis výsledku


#uzavření souboru
soubor.close()
        

#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]')      
    
