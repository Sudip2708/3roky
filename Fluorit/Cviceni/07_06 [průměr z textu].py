##  Napíš funkciu priemer(meno_suboru), ktorá otvorí a číta zadaný súbor.
##  V každom riadku tohto súboru je jedno celé číslo.
##  Funkcia zistí priemer týchto hodnôt.
##
##  Napríklad, pre takýto súbor 'cisla.txt':
##    554
##    -8
##    27
##    4448
##    7
##    92
##    144
##  dostaneš:
##    >>> print('priemer =', priemer('cisla.txt'))
##    priemer = 752.0


#úvodní a prázdný řádek:
print('TEXTOVÉ SOUBORY - FUNKCE PRŮMĚR')
print('funkce vrátí průměr čísel načtených ze souboru')
print('jméno souboru pro otestování: 07_06.txt')
print()


#definování funkce:
def priemer(meno_suboru): 
    soubor = open(meno_suboru)                  #proměnná pro otevření souboru
    součet = 0                                  #proměnná pro součet všech čísel
    řádků = 0                                   #proměnná pro počet řádků
    for řádek in soubor:                        #cyklus - pro řádek v souboru
        součet += int(řádek)                    #přičti hodnotu v řádku do součtu
        řádků += 1                              #připočítej 1 do počtu řádků
    soubor.close()                              #zavření souboru
    print()                                     #prázdný řádek
    print('Počet řádků v souboru =', řádků)     #výpis počtu řádků
    print('Celkový součet =', součet)           #výpis celkového součtu
    print('----------------------')             #oddělující linka
    print('Průměr =', součet / řádků)           #výpis průměru

#vstup:
priemer(input('Zadej název souboru: '))
    

#prázdný řádek a příkaz pro neuzavření okna
print()
print()
input('[zmáčkni [Enter] pro uzavření okna]')          
    
