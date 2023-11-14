##Funkcia zapis(tab, meno_suboru)
##je opačná k funkcii citaj v predchádzajúcej úlohe:
##zapíše danú dvojrozmernú tabuľku slov do súboru.
##Napríklad:
##>>> x = [['Anička', 'dušička'], ['kde', 'si', 'bola'], ['keď', 'si', 'si', 'čižmičky'], ['zarosila']]
##>>> zapis(x, 'text1.txt')
##vytvorí rovnaký súbor ako bol 'text.txt'.
##Uvedom si, že ak by vstupná dvojrozmerná tabuľka obsahovala čísla,
##táto funkcia vytvorí korektný súbor čísel,
##napríklad:
##>>> zapis([[1, 11, 21], [345], [-5, 10]], 'cisla.txt')
##vytvorí súbor 'cisla.txt':
##1 11 21
##345
##-5 10


#úvodní a prázdný řádek:                                                  
print('2D TABULKA DO TEXTOVÉHGO SOUBORU')                              
print('''
Program uloží obsah 2D tabulky do textového souboru
''')


def zapis(tabulka, jmeno_suboru):
    vysledny_text = ''
    for seznam_slov in tabulka:
        for slovo in seznam_slov:
            vysledny_text += str(slovo) + ' '
        vysledny_text += '\n'
    soubor = open(jmeno_suboru, 'w')
    soubor.write(vysledny_text)
    soubor.close()
    print(f'Textový soubor {jmeno_suboru} vytvořen')


input('''
Zmáčkni [enter] pro vytvoření textového souboru z tabulky:
x = [['Anička', 'dušička'], ['kde', 'si', 'bola'], ['keď', 'si', 'si', 'čižmičky'], ['zarosila']]
''')
x = [['Anička', 'dušička'], ['kde', 'si', 'bola'], ['keď', 'si', 'si', 'čižmičky'], ['zarosila']]
zapis(x, '13_10_text.txt')
input('''
Zmáčkni [enter] pro zobrazení textového souboru:
''')
print('''Anička dušička 
kde si bola 
keď si si čižmičky 
zarosila
''')


input('''
Zmáčkni [enter] pro vytvoření textového souboru z tabulky:
[[1, 11, 21], [345], [-5, 10]]
''')
y = [[1, 11, 21], [345], [-5, 10]]
zapis(y, '13_10_cisla.txt')
input('''
Zmáčkni [enter] pro zobrazení textového souboru:
''')
print('''1 11 21 
345 
-5 10 
''')


input('''
Zmáčkni [enter] pro ukončení programu
''')


