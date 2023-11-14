##  V nejakej obci je jediná ulica, na ktorej je n domov.
##  Na miestnom úrade majú v zozname (typu list) pre každý dom
##  zaznačený počet obyvateľov. Pomocou len štyroch print vypíš,
##  koľko obyvateľov žije v celej obci, koľko domov je neobývaných,
##  aký je maximálny počet obyvateľov v dome
##  a v koľkých domoch býva tento maximálny počet.
##  Napríklad, pre:
##    domy = [4, 2, 0, 5, 0, 1, 5, 4]
##  vypíše:
##    počet obyvateľov je 21
##    neobývaných domov je 2
##    maximálny počet obyvateľov v dome je 5
##    počet maximálnych domov je 2
##  Teraz do premennej domy priraď nejaký iný zoznam aspoň 15 čísel
##  z intervalu <0, 10> a opäť zisti všetky predchádzajúce informácie.


#úvodní a prázdný řádek:
print('DEFINOVÁNÍ FUNKCE - STATISTIKA OBYVATEL')
print('''funkce dle zadaného počtu domů vytvoří náhodný seznam obyvatel,
na základě kterého je posléze učiněn statistický výstup''')
print()


#definování funkce:
def domy(pocet):
    'Vytvoří seznam obyvatel pro domy v ulici s náhodným počtem 0 - 10 osob'
    seznam = [None] * pocet
    for i in range(pocet):
        seznam[i] = random.randint(0, 10)
    return seznam


#vstup:
n = int(input('Zadej počet domů: '))
print()


#import modulu:
import random


#výstup:
ulice = domy(n)
print(f'Seznam počtu obyvatelů v jednotlivých domech: ')
print(ulice)
print(f'Počet obyvatel v ulici je {sum(ulice)}')
print(f'Neobyvaných domů v ulici je {ulice.count(0)}')
print(f'Maximální počet obyvatelů v 1 domě je {max(ulice)}')
print(f'Počet domů s maximálním počtem obyvatelů je {ulice.count(max(ulice))}')
        

#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]') 
