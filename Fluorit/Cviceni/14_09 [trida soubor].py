##Zadefinuj triedu Subor s metódami:
##inicializácia __init__(meno_suboru) vytvorí nový prázdny súbor
##metóda pripis(text) na koniec súboru pridá nový riadok so zadaným textom; použi open(..., 'a')
##metóda vypis() vypíše (print) momentálny obsah súboru
##Napríklad:
##>>> s = Subor('text.txt')
##>>> s.pripis('prvy riadok')
##>>> s.pripis('druhy riadok')
##>>> s.vypis()
##    prvy riadok
##    druhy riadok
##>>> s.pripis('posledny riadok')
##>>> s.vypis()
##    prvy riadok
##    druhy riadok
##    posledny riadok


#úvodní a prázdný řádek:                                                  
print('TŘÍDA - SOUBOR')                              
print('''
Třída Soubor obsahuje následující funkce:

1) inicializační funkce, která očekává jako hodnotu název souboru
, který uloží jako atribut 'meno' a soubor vytvoří a zavře

2) metoda pripis(text), která soubor otevře, připíše do něj text a zavře

3) metoda vypis(), která soubor otevře, načte a vytiskne z něj text a zavře''')

class Subor:
    def __init__(self, meno_suboru):
        self.meno = meno_suboru
        subor = open(self.meno, 'w')
        subor.close()
        print(f'>> soubor {self.meno} byl vytvořen')

    def pripis(self, text):
        subor = open(self.meno, 'a')
        subor.write(text + '\n')
        subor.close()
        print(f'>> do souboru {self.meno} byl přidán text:')
        print(f'>> {text}')

    def vypis(self):
        subor = open(self.meno, 'r')
        print(f'>> Text souboru {self.meno}:')
        print(subor.read())
        subor.close()
         
print()
input("""zmáčkni [enter] pro zadání příkazu: s = Subor('14-09.txt')
(který založí instanci třídy 's' a vytvoří prázdný textový soubor)""")
s = Subor('14_09.txt')

print()
input("""zmáčkni [enter] pro zadání příkazu: s.pripis('prvy riadok')
(který do souboru připíše zadaný text)""")
s.pripis('prvy riadok')

print()
input("""zmáčkni [enter] pro zadání příkazu: s.pripis('druhy riadok')
(který do souboru připíše zadaný text)""")
s.pripis('druhy riadok')

print()
input("""zmáčkni [enter] pro zadání příkazu: s.vypis()
(která vypíše text z textového souboru)""")
s.vypis()

print()
input("""zmáčkni [enter] pro zadání příkazu: s.pripis('posledny riadok')
(který do souboru připíše zadaný text)""")
s.pripis('posledny riadok')

print()
input("""zmáčkni [enter] pro zadání příkazu: s.vypis()
(která vypíše text z textového souboru)""")
s.vypis()

print()
input("""zmáčkni [enter] pro zavření programu""")
