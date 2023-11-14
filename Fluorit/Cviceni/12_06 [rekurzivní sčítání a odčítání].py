##Napíš rekurzívnu funkciu sucet2(zoznam),
##ktorá bez cyklov zistí súčet záporných prvkov zoznamu a súčet kladných prvkov zoznamu.
##Prvkami sú len celé čísla.
##Funkcia vráti dvojicu (tuple): tieto dva súčty. Otestuj, napríklad:
##>>> sucet2([0, 1, -2, 3, 4, -5, -6, 7])
##    (-13, 15)
##>>> sucet2(list(range(100)) + list(range(0, -100, -1)))
##    (-4950, 4950)
##>>> sucet2([0]*1000+[1]+[0]*1000+[-1]+[0]*1000)
##    (-1, 1)


#úvodní a prázdný řádek:
print('REKURZIVNÍ SČÍTÁNÍ A ODČÍTÁNÍ')
print(f'''Program provede rekurzivně výpočet součtu hodnot.

K ukázce výpočtu budou použity tyto 3 zadání:
    1) sucet2([0, 1, -2, 3, 4, -5, -6, 7])
    2) sucet2(list(range(100)) + list(range(0, -100, -1)))
    3) sucet2([0]*1000+[1]+[0]*1000+[-1]+[0]*1000)''')
print()
input('[zmáčkni [Enter] pro zobrazení výsledků]')


#rekurzivní funkce:
def sucet2(zoznam):                                                     #definice funkce pro součet kladnách a záporných čísel - vstup seznam čísel
    if zoznam[-1] == 'x':                                                   #podmínka - pokud na konci seznamu je uveden znak 'x'
        if len(zoznam) <= 2:                                                    #podmínka - pokud má seznam 2 a méně položek
            return zoznam[0]                                                        #vrať do rekurzivního výpočtu hodnotu prvního znaku
        else:                                                                   #podmínka - pokud má seznam více než 2 znaky
            pulka = len(zoznam)//2                                                  #vypočti index půlky
            zoznam.insert(pulka, 'x')                                               #na toto místo vlož znak 'x'
            return  sucet2(zoznam[:pulka+1]) + sucet2(zoznam[pulka+1:])             #rekurzivně zavolej tuto funksi s první a druhou půlkou seznamu
    else:                                                                   #podmínka - pokud seznam nemá na konci znak 'x'   
        zoznam.append(0)                                                        #přidej na konec seznamu 0 (pro zjištění rozmezí kladných a záporných čísel
        zoznam.sort()                                                           #utřiď seznam vzestupně
        prvni_nula = zoznam.index(0)                                            #najdi index prvního výskytu nuly
        zaporna = zoznam[:prvni_nula]                                           #nový seznam pro záporná čísla
        zaporna.append('x')                                                     #přidej na konec seznamu znak 'x'
        kladna = zoznam[prvni_nula+1:]                                          #nový seznam pro kladná čísla
        kladna.append('x')                                                      #přidej na konec seznamu znak 'x'
        return(sucet2(zaporna), sucet2(kladna))                                 #rekurzivní volání funkce s nově vytvořenými seznami


#výstup:
print()
print(f'''Výsledky:
    1) sucet2([0, 1, -2, 3, 4, -5, -6, 7]) = {sucet2([0, 1, -2, 3, 4, -5, -6, 7])}
    2) sucet2(list(range(100)) + list(range(0, -100, -1))) = {sucet2(list(range(100)) + list(range(0, -100, -1)))}
    3) sucet2([0]*1000+[1]+[0]*1000+[-1]+[0]*1000) = {sucet2([0]*1000+[1]+[0]*1000+[-1]+[0]*1000)}''')


#prázdný řádek, příkaz pro zobrazení výsledků a prázdný řádek
print()
input('[zmáčkni [Enter] pro zobrazení rekurzivní funkce]')


#dovětek:
print()
print(f'''def sucet2(zoznam):
    if zoznam[-1] == 'x':
        if len(zoznam) <= 2:
            return zoznam[0]
        else:
            pulka = len(zoznam)//2
            zoznam.insert(pulka, 'x')
            return  sucet2(zoznam[:pulka+1]) + sucet2(zoznam[pulka+1:])
    else:
        zoznam.append(0)
        zoznam.sort()
        prvni_nula = zoznam.index(0)
        zaporna = zoznam[:prvni_nula]
        zaporna.append('x')
        kladna = zoznam[prvni_nula+1:]
        kladna.append('x')
        return(sucet2(zaporna), sucet2(kladna))
''')


#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]')
