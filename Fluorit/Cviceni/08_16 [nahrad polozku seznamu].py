##  Napíš funkciu replace(zoznam, co, zaco),
##  ktorá v danom zozname všetky výskyty hodnoty co nahradí hodnotou zaco.
##  Funkcia nič nevracia ani nevypisuje, len modifikuje obsah zoznamu.
##  Napríklad:
##    >>>zoz = [12, 13, 14, 13, 11, 14, 15, 13]
##    >>>replace(zoz, 13, 'x')
##    >>>zoz
##        [12, 'x', 14, 'x', 11, 14, 15, 'x']
##    >>>zoz = [1, 2] *10
##    >>>replace(zoz, 1, 9)
##    >>>zoz
##        [9, 2, 9, 2, 9, 2, 9, 2, 9, 2, 9, 2, 9, 2, 9, 2, 9, 2, 9, 2]


#úvodní a prázdný řádek:
print('DEFINOVÁNÍ FUNKCE - NAHRAĎ POLOŽKU SEZNAMU')
print('funkce dohledá v seznamu zadanou hodnotu a nahradí ji jinou zadanou hodnotou')
print()


#definování funkce:
def replace(seznam, co, zaco):
    for i, prvek in enumerate(seznam):
        if prvek == co:
            seznam[i] = zaco


#intro:
print('Seznam pro ukázku funkce:')
print('[12, 13, 14, 13, 11, 14, 15, 13]')
print()


#vstup:
a = int(input('Zapiš číslo, které chceš nahradit a zmáčkni [enter]: '))
b = input('Zapiš znaky, kterým chceš uvedené číslo nagradit: ')

        
#výpočet:
zoz1 = [12, 13, 14, 13, 11, 14, 15, 13]
replace(zoz1, a, b)


#výstup:
print()
print('Výsledný seznam:')
print(zoz1)


#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]') 
