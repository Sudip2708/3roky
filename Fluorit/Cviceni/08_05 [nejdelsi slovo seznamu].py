##  Napíš funkciu najdlhsie(zoznam),
##  ktorá zo zoznamu slov vráti (return) najdlhšie slovo.
##  Funkcia nemodifikuje vstupný zoznam a nič nevypisuje.
##  Napríklad:
##    >>>zoz = ['prvy', 'druhy', 'treti', 'stvrty', 'piaty']
##    >>>naj = najdlhsie(zoz)
##    >>>naj
##        'stvrty'
##    >>>najdlhsie(den)           # den z prvej úlohy
##        'pondelok'


#úvodní a prázdný řádek:
print('DEFINOVÁNÍ FUNKCE - NEJDELŠÍ SLOVO SEZNAMU')
print('funkce dohledá a vrátí položku ze seznamu, která má nejvíce znaků')
print()


#definování funkce:
def najdlhsie(seznam):
    'funkce vrátí nejdelší slovo/a ze seznamu'
    nejdelsi_pocet = 0
    nejdelsi_slovo = ''
    for i in zoz:
        if len(i) == nejdelsi_pocet:
            nejdelsi_slovo += '\n' + i
        else:
            if len(i) > nejdelsi_pocet:
                nejdelsi_pocet = len(i)
                nejdelsi_slovo = i

    return nejdelsi_slovo


#vstup:
zoz = []
a = input('Zapiš slovo do seznamu a zmáčkni [enter]): ')
while a != '':
    zoz.append(a)
    print()
    a = input('''Zapiš další slovo seznamu a zmáčkni [enter]: 
(pro ukončení zmáčkni pouze [enter])''')


#seznam:
print()
print('Vytvořený seznam obsahuje tyto položky:')
print(zoz)


#výstup:
print()
print('Nejdelší slovo/a ze seznamu je:')
print(najdlhsie(zoz))
        

#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]') 
        
