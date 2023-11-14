##Napíš rekurzívnu funkciu mocnina(n, k),
##ktorá vypočíta n**k pre celé nezáporné k len pomocou násobenia:
##o	mocnina(n, 0) = 1
##o	mocnina(n, k) = mocnina(n, k-1) * n
##Funkciu otestuj, napríklad pre mocnina(2, 900) a porovnaj s 2**900.


#úvodní a prázdný řádek:
print('REKURZIVNÍ VÝPOČET MOCNINY')
print(f'''Dle zadaných hodnot dojde k výpočtu mocniny rekurzivní funkcí''')
print()


#vstupní data:
n = int(input('Zadej celé kladné číslo, které chceš umocnit: '))  
k = int(input('Zadej celé kladné číslo kterým chceš mocnit: ')) 


#rekurzivní funkce:
def mocnina(n, k):
    if k < 1:
        return 1
    return n * mocnina(n, k-1)


#prázdný řádek, příkaz pro zobrazení výsledků a prázdný řádek
print()
input('[zmáčkni [Enter] pro zobrazení výsledků]')


#výstup:
print()
print(f'rekurzivní výpočet: {mocnina(n, k)}')
print(f'výpočet umocněním: {n**k}')


#prázdný řádek, příkaz pro zobrazení výsledků a prázdný řádek
print()
input('[zmáčkni [Enter] pro zobrazení rekurzivní funkce]')


#dovětek:
print()
print(f'''def mocnina(n, k):
    if k < 1:
        return 1
    return n * mocnina(n, k-1)
''')


#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]')
