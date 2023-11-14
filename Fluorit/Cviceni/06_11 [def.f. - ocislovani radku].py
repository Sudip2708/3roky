##  Napíš funkciu riadky(retazec), ktorá vypíše daný viacriadkový reťazec,
##  ale pritom každý riadok očísluje číslami od 1 do počet riadkov.
##
##  Napríklad:
##    >>>riadky('prvy riadok\n\ntreti je posledny')
##        1. prvy riadok
##        2.
##        3. treti je posledny
##    >>>riadky('len \\n jeden riadok')
##        1. len \n jeden riadok


#úvodní a prázdný řádek:
print('DEFINOVÁNÍ FUNKCE - OČÍSLOVÁNÍ ŘÁDKŮ')
print('pouze k zobrazení - funkce očísluje každý řádek ve textovém řetězci se znaky "\\n"')
print()


#definování funkce:
def riadky(retazec):
    n = 1                                               #proměná pro číslování
    vysledny_text = ''                                  #promněná pro výsledný text
    while retazec.find('\n') >= 0:                      #cyklus - dokud je v textu znak pro nový řádek "\n"
        retazec2 = retazec[:retazec.find("\n")]         #nalezni text před znakem "\n"
        vysledny_text += (f'{n}. {retazec2}') + '\n'    #dej před něj číslo řádku a za něj znak pro nový řádek a vlož ho do výsledného textu
        retazec = retazec[retazec.find('\n')+1:]        #odeber z púvodního řetězce již použitou část
        n += 1                                          #přípočet čísla pro další řádek
    vysledny_text += (f'{n}. {retazec}')                #vložení posledního řádku
    return vysledny_text                                #vrať výsledný text


#vstup 1:
print('--------------------------------------------')
print("text A: 'prvy riadok\\n\\ntreti je posledny'")
print()


#výstup 1:
print(riadky('prvy riadok\n\ntreti je posledny'))
print()


#vstup 2:
print('--------------------------------------------')
print("text B: 'len \\\\n jeden riadok'")
print()


#výstup 2:
print(riadky('len \\n jeden riadok'))
print()
        

#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]')  
