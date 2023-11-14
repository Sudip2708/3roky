##  Napíš funkciu vzostupne(zoznam),
##  ktorá zistí, či sú prvky vstupného zoznamu usporiadané vzostupne.
##  Funkcia vráti (return) True alebo False,
##  nemodifikuje vstupný zoznam a nič nevypisuje.
##  Nepoužívaj sort ani sorted.
##  Napríklad:
##    >>>vzostupne([1, 5, 5, 8, 100])
##        True
##    >>>vzostupne(['pyton', 'python', 'pytliak'])
##        False


#úvodní a prázdný řádek:
print('DEFINOVÁNÍ FUNKCE - VZESTUPNĚ')
print('''funkce zkontroluje seznam a pokud je zapsán vzestupně
vrátí hodnotu "True", v opačném případě vrátí hodnotu "False"''')
print()


#definování funkce:
def vzostupne(seznam):
    'funkce vrátí True / False zda jsou hodnoty seznamu v zestupném púořadí'
    predesla_h = ''
    for i in seznam:
        if predesla_h == '':
            predesla_h = i
        else:
            if i > predesla_h:
                pass
            else:
                return False
    return True


#vstup:
zoz = []
a = input('Zapiš první slovo, nebo znak a zmáčkni [enter]): ')
while a != '':
    zoz.append(a)
    print()
    a = input('''Zapiš další slovo, nebo znak a zmáčkni [enter]: 
(pro ukončení zmáčkni pouze [enter])''')


#seznam:
print()
print('Vytvořený seznam obsahuje tyto položky:')
print(zoz)
print()

    
#výstup:
if vzostupne(zoz):
    print('Seznam je seřazen vzestupně')
else:
    print('Seznam není seřazen vzestupně')
        

#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]') 
