##Funkcia citaj_cisla(meno_suboru) bude podobná funkcii citaj(meno_suboru) z (9) úlohy,
##len táto predpokladá, že vstupný súbor obsahuje len celé čísla.
##Funkcia vráti dvojrozmernú tabuľku čísel.
##Napríklad, pre textový súbor 'cisla.txt' z (10) úlohy:
##>>> tab = citaj_cisla('cisla.txt')
##>>> tab
##    [[1, 11, 21], [345], [-5, 10]]


#úvodní a prázdný řádek:                                                  
print('ČÍSLA Z TEXTOVÉHO SOUBORU DO 2D TABULKY')                              
print('''
Program načte textový soubor s čísli a uloží je do 2D tabulky,
kde řákdy tabulky odpovídají řádkům v textu
a sloupce tabulky tvoří jednotlivá slova řádků.
''')


def citaj_cisla(meno_suboru):
    seznam = []
    text = open(meno_suboru, 'r')
    for radek in text:
        seznam.append([])
        radek = radek.strip().split()
        for cislo in radek:
            seznam[-1].append(int(cislo))
    text.close()
    return seznam


input('''
Zmáčkni [enter] pro zobrazení výsledku pro textový
soubor obsahující následující text:

"1 11 21 
345 
-5 10 "

''')


tab = citaj_cisla('13_11_cisla.txt')
print('Výsledná 2D tabulka: ', tab)


input('''
Zmáčkni [enter] pro ukončení programu
''')
