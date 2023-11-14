##  Napíš rekurzívnu funkciu palindrom(retazec),
##  ktorá zistí (vráti True alebo False), či je zadaný reťazec palindrom,
##  t.j. či sa číta rovnako od začiatku ako od konca.
##  Pri tomto zisťovaní sa ignorujú medzery
##  a nerozlišujú sa malé a veľké písmená, napríklad:
##    >>> palindrom('Jelenovi Pivo Nelej')
##	True
##  Rekurzia by mala pracovať na takomto princípe:
##  porovná prvé a posledné písmeno a ak sú zhodné ešte zistí,
##  či aj reťazec bez prvého a posledného písmena je palindrom.


#úvodní a prázdný řádek:
print('REKURZIVNÍ OVĚŘENÍ PALINDROMU')
print(f'''Program obsahuje rekurzivní funkce, která má za úkol
porovnat první a poslední znak řetězce a pokud jsou shodné
stejně pokračovat i se zbytkem textu.
na začátku funkce je text zbaven býlích znaků, mezer
a všechna písmena jsou změněna na malá.

Funkce nejprve prověří palindrom:
"Jelenovy Pivo Nelej"
a po té větu:
"Jelenovy Pivo Nalej"''')


#rekurzivní funkce:
def palindrom(retezec):
    novy_retezec = retezec.strip().replace(' ', '').lower()
    if novy_retezec[0] != novy_retezec[-1]:
        return False
    else:
        if len(novy_retezec) <= 1:
            return True
        else:
            return palindrom(novy_retezec[1:-1])


#prázdný řádek, příkaz pro zobrazení výsledků a prázdný řádek
print()
input('[zmáčkni [Enter] pro zobrazení výsledků]')


#výstup:
print()
print(f'Výsledek pro palindrom: {palindrom("Jelenovi Pivo Nelej")}')
print(f'Výsledek pro větu: {palindrom("Jelenovi Pivo Nalej")}')


#prázdný řádek, příkaz pro zobrazení výsledků a prázdný řádek
print()
input('[zmáčkni [Enter] pro zobrazení rekurzivní funkce]')


#dovětek:
print()
print(f'''def palindrom(retezec):
    novy_retezec = retezec.strip().replace(' ', '').lower()

    if novy_retezec[0] != novy_retezec[-1]:
        return False
    else:
        if len(novy_retezec) <= 1:
            return True
        else:
            return palindrom(novy_retezec[1:-1])
''')


#prázdný řádek a příkaz pro neuzavření okna
print()
input('[zmáčkni [Enter] pro uzavření okna]')
