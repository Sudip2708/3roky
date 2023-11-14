##  Napíš funkciu je_palindrom(reťazec), ktorá zistí (vráti True alebo
##  False), či je zadaný reťazec palindróm. Funkcia ignoruje medzery a
##  nerozlišuje medzi malými a veľkými písmenami.
##
##  Napríklad:
##    >>>je_palindrom('Python')
##        False
##    >>>je_palindrom('tahat')
##        True
##    >>>je_palindrom('Jelenovi Pivo Nelej')
##        True


#úvodní a prázdný řádek:
print('DEFINOVÁNÍ FUNKCE - JE PALINDROM')
print('funkce zjistí, zda námi zadaný text je palindrom')
print('(dá se číst ze předu i ze zadu stejně)')
print()


#definování funkce:
def je_palindrom(reťazec):
    reťazec = reťazec.lower()                       #převeď text na malá písmena
    vysledek = ''                                   #promněná pro výsledný text
    while reťazec.find(' ') != -1:                  #cyklus - dokud není řetězec prázdný
        vysledek += reťazec[:reťazec.find(' ')]     #přidej do výsledného textu vše před mezerou
        reťazec = reťazec[reťazec.find(' ')+1:]     #původní text zkrať o to, co jsi už použil a o mezeru
    vysledek += reťazec                             #přidej do výsledného textu konec textu (po odebrání všech mezer)
    if vysledek == vysledek[::-1]:                  #podmínka - pokud výsledný text je shodný svou obrácenou podobou
        return True                                 #vrať "True"
    else:                                           #jinak
        return False                                #vrať "False"

#vstup:
reťazec = input('Zadej text: ')


#výstup:
a = je_palindrom(reťazec)
if a == True:
    print('Zadané slovo je palindrom')
else:
    print('Zadané slovo není palindrom')


#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]')  
