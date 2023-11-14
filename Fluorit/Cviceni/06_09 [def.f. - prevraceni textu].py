##  Znakový reťazec vieme prevrátiť pomocou zápisu retazec[::-1].
##  Napíš funkciu prevrat(retazec),
##  ktorá len pomocou cyklu a zreťazovania prevráti zadaný reťazec.
##
##  Napríklad:
##    >>>x = prevrat('tseb eht si nohtyP')
##    >>>x
##        'Python is the best'


#úvodní a prázdný řádek:
print('DEFINOVÁNÍ FUNKCE - PŘEVRÁCENÍ TEXTU')
print('funkce převrátí námi zadaný text')
print()


#definování funkce:
def prevrat(retazec):
    c = ''                  #promněná pro výsledný text
    for i in retazec:       #cyklus - dle znaků v řetězci
        c = i + c           #znak přidej na začátek výsledného řetězce
    return(c)               #vrať výsledný řetězec

##def prevrat(retazec):
##    return(retazec[::-1])


#vstup:
retazec = input('Zadej text, který chceš převrátit: ')
print()


#výstup:
print(f'Výsledný text: {prevrat(retazec)}')     


#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]')  
