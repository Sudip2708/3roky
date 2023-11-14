##  Napíš funkciu zakoduj(text, posun),
##  ktorá posunie v abecede všetky znaky (pomocou funkcie posun_znak).
##
##  Napríklad:
##    >>>x = zakoduj('pyThon', 10)
##    >>>x
##        'ziTryx'
##    >>>zakoduj(x, -10)
##        'pyThon'
##    >>>zakoduj(x, 16)
##        'foTxed'
##
##  Předchozí úloha:
####  Napíš funkciu posun_znak(znak, posun), ktorá posunie daný znak v abecede
####  o p znakov vpravo (resp. vľavo, ak je záporné). Na konci abecedy sa
####  pokračuje od začiatku. Funkcia posúva len písmená malej abecedy, ostatné
####  znaky nemení.
####
####  Napríklad:
####    >>>posun_znak('c', 4)
####        'g'
####    >>>posun_znak('g', -4)
####        'c'
####    >>>posun_znak('x', 10)
####        'h'
####    >>>posun_znak('A', 10)
####        'A'


#úvodní a prázdný řádek:
print('DEFINOVÁNÍ FUNKCE - ZAŠIFROVÁNÍ TEXTU')
print('funkce posune v zadaném textu všechny malé znaky o zadaný počet')
print()


#definování funkcí:
def posun_znak(znak, posun):
    abc = 'abcdefghijklmnopqrstuvwxyz'                      #výčet znaků, které se budou posouvat
    if abc.find(znak) != -1:                                #podmínka - pokud je znak ve výčtu
        if abc.find(znak) + posun > len(abc):               #podmínka - pokud by posun přesáhl konec výčtu
            posun = ((abc.find(znak) + posun)-len(abc))     #poniž posun o počet do konce
            znak = 'a'                                      #znak nastav na "a"
        return(abc[abc.find(znak)+posun])                   #vrať posunutý znak
    return(znak)                                            #vrať původní znak

def zakoduj(text, posun):
    vysledek = ''                                           #promněná pro výsledný text
    for i in text:                                          #cyklus - dle znaků v textu
        vysledek += posun_znak(i, posun)                    #každý znak projeť funkcí posun_znak()
    return(vysledek)                                        #vrať výsledný text


#vstup:
text = input('Zadej text který chceš zašifrovat: ')
posun = int(input('Zadej číslo o které chceš znaky v textu posunout: '))


#výstup:
print()
print(f'Výsledný posunutý text: "{zakoduj(text, posun)}"')

        

#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]')  
