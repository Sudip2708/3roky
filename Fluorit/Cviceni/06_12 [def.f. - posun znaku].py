##  Napíš funkciu posun_znak(znak, posun), ktorá posunie daný znak v abecede
##  o p znakov vpravo (resp. vľavo, ak je záporné). Na konci abecedy sa
##  pokračuje od začiatku. Funkcia posúva len písmená malej abecedy, ostatné
##  znaky nemení.
##
##  Napríklad:
##    >>>posun_znak('c', 4)
##        'g'
##    >>>posun_znak('g', -4)
##        'c'
##    >>>posun_znak('x', 10)
##        'h'
##    >>>posun_znak('A', 10)
##        'A'


#úvodní a prázdný řádek:
print('DEFINOVÁNÍ FUNKCE - POSUN ZNAKU')
print('funkce posune námi zadaný znak o námi zadanou polohu')
print('(funkce posouvá pouze malé znaky a na konci abecedy se pokračuje od začátku)')
print()


#definování funkce:
def posun_znak(znak, posun):
    abc = 'abcdefghijklmnopqrstuvwxyz'                      #výčet znaků, které se budou posouvat
    if abc.find(znak) != -1:                                #podmínka - pokud je znak ve výčtu
        if abc.find(znak) + posun > len(abc):               #podmínka - pokud by posun přesáhl konec výčtu
            posun = ((abc.find(znak) + posun)-len(abc))     #poniž posun o počet do konce
            znak = 'a'                                      #znak nastav na "a"
        return(abc[abc.find(znak)+posun])                   #vrať posunutý znak
    return(znak)                                            #vrať původní znak


#vstup:
znak = input('Zadej znak (malé písmeno): ')
posun = int(input('Zadej číslo o kolik se má znak posunout: '))


#výstup:
print()
print(f'Když znak "{znak}" posuneme o {posun} pozic, dostaneme znak "{posun_znak(znak, posun)}".')

        

#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]')  
