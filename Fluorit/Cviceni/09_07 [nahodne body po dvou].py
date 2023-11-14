##  Napíš funkciu nahodne_body(pocet),
##  ktorá vráti zadaný počet náhodných bodov v grafickej ploche (dvojíc čísel z 380x260).
##  Funkcia vráti zoznam, ktorý bude obsahovať dvojprvkové n-tice celých čísel.
##  Napríklad:
##    >>> nahodne_body(5)
##        [(118, 103), (299, 27), (247, 118), (166, 237), (269, 225)]


#úvodní a prázdný řádek:
print('FUNKCE - NÁHODNÉ BODY')
print('''funkce vytvoří dle zadaného počtu, seznam souřadnic náhodných bodů,
uložených v nticích po dvojcíh (x, y)''')
print()


#definování funkce:
def nahodne_body(pocet):
    x = []
    for i in range(pocet):
        a = random.randint(10, 380)
        b = random.randint(10, 260)
        x.append((a, b))
    return x

#imort modulů:
import random


#vstup:
a = int(input('Zadej počet: '))


#prázdný řádek a výstup:
print(nahodne_body(a))
     

#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]') 
