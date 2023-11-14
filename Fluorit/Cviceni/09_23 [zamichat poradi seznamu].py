##  Napíš funkciu pomiesaj(zoznam),
##  ktorá náhodne pomieša poradie prvkov v pôvodnom zozname.
##  Funkcia nič nevypisuje ani nevracia, len zmení obsah zoznamu.
##  Funkcia by pre n-prvkový zoznam mala pracovať takto:	
##    najprv zvolí náhodné číslo x od 0 do n-1	
##    v zozname vymení x-tý a posledný prvok	
##    potom zvolí náhodné číslo x od 0 do n-2	
##    v zozname vymení x-tý a predposledný prvok (t.j. zoznam[-2])	
##    potom zvolí náhodné číslo x od 0 do n-3	
##    v zozname vymení x-tý a a tretí od konca	
##    takto to opakuje, kým sa dá	
##
##    Napríklad:	
##    for i in range(4):	
##        p = list(range(1, 11))	
##        pomiesaj(p)	
##        print(p)	
##    [2, 9, 6, 1, 7, 8, 10, 3, 5, 4]	
##    [7, 2, 10, 9, 6, 8, 4, 1, 3, 5]	
##    [3, 8, 7, 9, 4, 1, 6, 10, 5, 2]	
##    [2, 9, 4, 1, 8, 3, 5, 7, 6, 10]	


#úvodní a prázdný řádek:
print('FUNKCE - ZAMÍCHAT POŘADÍ')
print('''funkce náhodně zamíchá pořadím položek seznamu
pouze pro zobrzení''')
print()
input('>>zmáčkni [enter] pro zobrazení původního seznamu<<')
print()


#definování funkce:
def pomiesaj(zoznam):
    delka = (len(zoznam))-1
    pocitadlo = 0
    for i in range(delka):
#        print((0, delka-pocitadlo))
        zoznam.append(zoznam.pop(random.randint(0, delka-pocitadlo)))
        pocitadlo +=  1


#import modulu:
import random


#vstup a výstup:
p = list(range(1, 11))
print(p)
print()
input('>>zmáčkni [enter] pro zobrazení 10-ti výsledků<<')
print()
for i in range(10):	
    pomiesaj(p)	
    print(p)	
     

#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]') 	
