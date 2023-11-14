##  Napíš program, ktorý si vypýta meno súboru
##  a potom vypíše počet riadkov a dĺžku najdlhšieho riadka (aj s koncovým '\n').
##
##  Napríklad:
##    meno súboru: text2.txt
##    počet riadkov súboru: 6
##    najdlhší riadok má 127 znakov
##    meno súboru: text3.txt
##    počet riadkov súboru: 13
##    najdlhší riadok má 28 znakov
##    
##  Zapíš tri rôzne riešenia tejto úlohy:
##    a. čítaním pomocou readline() a while-cyklu
##    b. čítaním riadkov pomocou for-cyklu
##    c. prečítaním naraz celého súboru pomocou read() a potom kontrolovaním pozícií znaku '\n'


#úvodní a prázdný řádek:
print('TEXTOVÉ SOUBORY - POČET ŘÁDKŮ - 3 ŘEŠENÍ')
print('''program, který po zadání odkazu na soubor s textem, vypíše kolik znaků
má nejdelší řádek, a to včetně i netisknutelného znaku pro nový řádek''')
print()
print('jméno souboru pro otestování: 07_03.txt')
print('(v tomto souboru je 6 řádků a nejdelší má 127 znaků)')
print()
print()


#vstup + otevření souboru:
soubor = open(input('Zadej jméno souboru: '), 'r')              #načtení a otevření souboru


#promněné:
počet_řádků = 0                                                 #proměnná pro počet řádků
nejdelší_řádek = 0                                              #proměnná pro hodnotu nejdelšího řádku


###řešení A:
##řádek = soubor.readline()                                       #přečtení prvního řádku
##while řádek:                                                    #cyklus - dokud není řádek prázdný
##    počet_řádků += 1                                            #přičti 1 do počet řádků
##    if len(řádek) > nejdelší_řádek:                             #podmínka - pokud je čtený řádek větší než hodnota v proměnné nejdelšího řádku
##        nejdelší_řádek = len(řádek)                             #zapiš tuto hodnotu jako hodnotu nejdelšího řádku
##    řádek = soubor.readline()                                   #přečtení dalšího řádku
##soubor.close()                                                  #zavření souboru


###řešení B:
##for i in soubor:                                                #cyklus - pro řádek v souboru
##    počet_řádků += 1                                            #přičti 1 do počet řádků
##    if len(i) > nejdelší_řádek:                                 #podmínka - pokud je čtený řádek větší než hodnota v proměnné nejdelšího řádku
##        nejdelší_řádek = len(i)                                 #zapiš tuto hodnotu jako hodnotu nejdelšího řádku
##soubor.close()                                                  #zavření souboru


#řešení C:
celý_soubor = soubor.read()                                     #přečtení celého souboru do proměnné
soubor.close()                                                  #zavření souboru
počet_řádků = celý_soubor.count('\n')                           #přiřazení hodnoty do počtu řádků
for i in range(počet_řádků):                                    #cyklus - dle počtu řádků
    if celý_soubor.find('\n')+1 > nejdelší_řádek:               #podmínka - pokud je čtený řádek větší než hodnota v proměnné nejdelšího řádku
        nejdelší_řádek = celý_soubor.find('\n')+1               #zapiš tuto hodnotu jako hodnotu nejdelšího řádku
    celý_soubor = celý_soubor[celý_soubor.find('\n')+1:]        #odseknutí již přečtené části


#výpis hodnot
print()
print(f'Počet řádků v souboru: {počet_řádků}')                  #výpis počtu řádků
print()
print(f'Nejdelší řádek má {nejdelší_řádek} znaků')              #výpis délky nejdelšího řádku
        

#prázdný řádek a příkaz pro neuzavření okna
print()
print()
input('[zmáčkni [Enter] pro uzavření okna]')  
