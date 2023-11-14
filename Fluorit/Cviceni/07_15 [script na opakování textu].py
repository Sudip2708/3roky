##  Napíš funkciu vyrob(meno_suboru, pocet, text), ktorá vytvorí textový súbor s daným menom.
##  Tento súbor bude pythonovským skriptom,
##  ktorý príslušný pocet krát vypíše (pomocou print()) zadaný text.
##  Tento skript by mal na opakovanie výpisu využiť while-cyklus (nie for-cyklus).
##
##  Napríklad:
##    >>> vyrob('skript.py', 20, 'Programujem v Pythone')
##  vytvorí nový program 'skript.py' a ten po spustení, výpíše 20-krát pod seba:
##    Programujem v Pythone
##    Programujem v Pythone
##    ...


#úvodní a prázdný řádek:
print('TEXTOVÉ SOUBORY - VYTVOŘENÍ SCRIPTU NA OPAKOVÁNÍ TEXTU')
print(''''funkce vytvoří pythonovský skript, který po spuštění,
dle zadaných parametrů, vypíše zadaný text''')
print()
print('jméno pro script pro otestování: 07_15')
print('text a počet opakování je zcela na nás :)')
print()


#definování funkce:
def vyrob(meno_suboru, pocet, text):
    soubor = open(meno_suboru, 'w')         #vytvoření souboru
    soubor.write(f'pocet = {pocet}\n')      #zapsání řádku s počtem
    soubor.write(f'text = "{text}"\n')      #zapsání řádku s textem
    soubor.write(f'while pocet != 0:\n')    #zapsání řádku caklu while
    soubor.write(f'    print(text)\n')      #zapsání řádku výpisu textu
    soubor.write(f'    pocet -= 1\n')       #zapsání řádku odečtení počtu
    soubor.write(f'input()\n')              #zapsání řádku s inputem, aby zůstal otevřený
    soubor.close()                          #zavření souboru


#vstup:
meno = input('Zadej název souboru: ')
meno_suboru = (f'{meno}_script.py')
text = input('Zadej text: ')
pocet = int(input('Zadej počet opakování: '))
vyrob(meno_suboru, pocet, text)


#výstup:
print()    
print(f'''Gratuluji, právě jsi vytvořil Pythonovský skript {meno_suboru},
který po zpuštění {pocet}x vypíše vámi zadaný text: {text}''')
print('Script najdeš uložen ve stejné složce jako je tento program.')

     

#prázdný řádek a příkaz pro neuzavření okna
print()
print()
input('[zmáčkni [Enter] pro uzavření okna]') 
