##  Napíš program, ktorý si vypýta meno súboru a potom vypíše všetky tie riadky súboru,
##  ktoré obsahujú práve tri slová.
##  V každom riadku je niekoľko slov, ktoré sú oddelené jednou medzerou.
##
##  Napríklad:
##    meno súboru: text3.txt
##    riadky s tromi slovami:
##    Stojí stojí mohyla
##    rastie kvety rozvíja
##    jedna žltá ľalija
##  Uvedom si, že stačí v každom riadku počítať počet medzier.


#úvodní a prázdný řádek:
print('TEXTOVÉ SOUBORY - VÝPIS ŘÁDKŮ S TŘEMI SLOVY')
print('''program, který po zadání odkazu na soubor s textem, vypíše ty řádky,
které obsahují pouze tři slova''')
print()
print('jméno souboru pro otestování: 07_04.txt')
print()


#vstup + otevření souboru:
soubor = open(input('Zadej jméno souboru: '), 'r')      #načtení a otevření souboru
print()


#proměnné:
výsledek = ''                                           #proměnná výsledku


#výpočet:
for řádek in soubor:                                    #cyklus - pro řádek v souboru
    if řádek.strip().count(' ') == 2:                   #podmínka - pokud řádek (očištěný od mezer před a za) má už jen 2 mezery
        výsledek += řádek                               #připočti tento řádek do výsledku
soubor.close()                                          #zavření souboru


#výpis
print('Řádky s třemi slovy: ')                          #výpis prvního řádku
print(výsledek)                                         #výpis výsledku
        

#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]')    
