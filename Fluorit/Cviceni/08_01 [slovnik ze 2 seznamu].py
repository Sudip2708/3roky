##  Do zoznamových premenných den a day priraď 7 názvov dní v týždni
##  v slovenčine a v angličtine ('pondelok', … ):
##    den =...
##    day =...
##  Teraz napíš príkazy, ktoré vypíšu tieto dva zoznamy každý
##  do jedného riadku (slová v riadku odděľ medzerami):
##    pondelok utorok ...
##    Monday Tuesday ...
##  Ďalej napíš for-cyklus, pomocou ktorého sa do 7 riadkov
##  postupne vedľa seba vypíšu slovenský a anglický názov dňa v týždni.
##  Použi obe premenné den a day:
##    pondelok Monday
##    utorok Tuesday


#úvodní a prázdný řádek:
print('DEFINOVÁNÍ FUNKCE - SLOVNÍK ZE DVOU SEZNAMŮ')
print('funkce vypíše ze dvou seznamů dvojice nacházející se na stejné pozici obou seznamů')
print()


#definování funkce:
def radek(jmeno_souboru):
    for i in jmeno_souboru:
        print(i, end=' ')
    
def vice_radku(soubor1, soubor2):
    if soubor1 >= soubor2:
        for i in range(len(soubor1)):
            print(soubor1[i], soubor2[i])
    else:
        for i in range(len(soubor1)):
            print(soubor1[i], soubor2[i])
        

#intro:
print('1. Seznam (jména dnů v týdnu v češtině):')
print("['Pondělí', 'Úterý', 'Středa', 'Čtvrtek', 'Pátek', 'Sobota', 'Neděle']")
print()
print('2. Seznam (jména dnů v týdnu v angličtině):')
print("['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']")
print()
input('zmáčkni [enter] pro zobrazení výsledku')
print()


#seznam:
den = ['Pondělí', 'Úterý', 'Středa', 'Čtvrtek', 'Pátek', 'Sobota', 'Neděle']
day = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


#výstup:
##radek(den)
##print()
##radek(day)
##print()
vice_radku(den, day)
        

#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]') 
