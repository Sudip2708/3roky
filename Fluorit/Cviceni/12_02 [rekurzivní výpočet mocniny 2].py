##Rekurzívne riešenie predchádzajúcej funkcie mocnina(n, k) môžeš vylepšiť,
##ak máme povolené použiť okrem násobenia aj umocňovanie na 2
##(čo je opäť len násobením so samým sebou):
##o	mocnina(n, 0) = 1
##o	mocnina(n, k) = mocnina(n, k//2) ** 2 … pre párne k
##o	mocnina(n, k) = mocnina(n, k-1) * n … pre nepárne k
##Funkciu otestuj, napríklad pre mocnina(2, 10000) a porovnaj s 2**10000.


#úvodní a prázdný řádek:
print('REKURZIVNÍ VÝPOČET MOCNINY S UMOCŇOVÁNÍM')
print(f'''Dle zadaných hodnot dojde k výpočtu mocniny rekurzivní funkcí.
Oproti mnulému zadání přibude řádek, kde bude bude použito
normálního umocnění pro zkrácení procesu.
A ano, nedává moc smysl v rekurzivním výpočtu mocniny
používat výpočet mocniny, nicméně v tomto příkladě jde
o demonstraci rozdělení výpočtu do menších větví
a snižení hodnoty zanoření rekurze.''')
print()


#vstupní data:
n = int(input('Zadej celé kladné číslo, které chceš umocnit: '))
k = int(input('Zadej celé kladné číslo kterým chceš mocnit: ')) 


#rekurzivní funkce:
def mocnina(n, k):
    if k >= 1:
        if k%2 == 0:
            return mocnina(n, k//2) ** 2
        else:
            return mocnina(n, k-1) * n
    return 1


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
    if k >= 1:
        if k%2 == 0:
            return mocnina(n, k//2) ** 2
        else:
            return mocnina(n, k-1) * n
    return 1
''')


#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]')
