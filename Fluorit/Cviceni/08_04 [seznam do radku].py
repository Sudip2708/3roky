##  Napíš funkciu vypis(zoznam, pocet), ktorá prvky daného zoznamu vypíše tak,
##  že v každom riadku (možno okrem posledného)
##  vypíše presne zadaný pocet prvkov zoznamu.
##  Funkcia nemodifikuje vstupný zoznam.
##  Napríklad:
##    >>>zoz =list(range(1, 19))
##    >>>vypis(zoz, 4)
##        1 2 3 4
##        5 6 7 8
##        9 10 11 12
##        13 14 15 16
##        17 18
##    >>>zoz
##        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
##    >>>vypis(list('Python'), 2)
##        P y
##        t h
##        o n


#úvodní a prázdný řádek:
print('DEFINOVÁNÍ FUNKCE - SEZNAM DO ŘÁDKŮ')
print('funkce vypíše seznam do námi definovaného počtu položek na řádek')
print()


#definování funkce:
def vypis(seznam, pocet):
    for i in range(len(seznam)):
        if (i+1) != len(seznam):
            if (i+1) % pocet != 0:
                print(seznam[i], end=' ')
            else:
                print(seznam[i])
        else:
            print(seznam[i])


#vstup:
a = input('Zapiš text, z kterého bude vytvořen seznam znaků: ')
b = int(input('Zapiš hodnotu počtu položek na řádek: '))

        
#seznam:
z = list(a)


#výstup:
print()
print('Výstup:')
vypis(z, b)


#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]') 
