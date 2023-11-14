##Pridaj do triedy Zlomok z úlohy (6) dve metódy:
##metóda str() vráti (nič nevypisuje) reťazec v tvare 3/8
##metóda float() vráti (nič nevypisuje) desatinné číslo, ktoré reprezentuje daný zlomok
##Napríklad:
##>>> z = Zlomok(3, 8)
##>>> print('z je', z.str())
##    z je 3/8
##>>> print('z je', z.float())
##    z je 0.375
##>>> w = Zlomok(2, 4)
##>>> print('w je', w.str())
##    w je 2/4
##>>> print('w je', w.float())
##    w je 0.5


#úvodní a prázdný řádek:                                                  
print('TŘÍDA - ZLOMEK - 02')                              
print('''
Třída Zlomek obsahuje následující funkce:

1) inicializační funkce, očekávající hodnotu citatele a jmenovatele

2) metoda vypis(), která vypíše text s zlomkem

3) metoda str(), která vrátí pouze zlomek

4) metoda float(), která vrátí výpočet''')


class Zlomok:
    def __init__(self, citatel, jmenovatel):
        self.citatel = citatel
        self.jmenovatel = jmenovatel
        print(f'''>> Vytvořena instance třídy Zlomek s hodnotami:
              citatel - {self.citatel}
              jmenovatel - {self. jmenovatel}''')

    def vypis(self):
        print(f'>> zlomek je {self.citatel }/{self.jmenovatel}')

    def str(self):
        return f'{self.citatel }/{self.jmenovatel}'

    def float(self):
        return self.citatel/self.jmenovatel

print()
input("""zmáčkni [enter] pro zadání příkazu: z = Zlomok(3, 8)
(která založí instanci třídy 'z' s danými hodnotami zlomku)""")
z = Zlomok(3, 8)

print()
input("""zmáčkni [enter] pro zadání příkazu: print('z je', z.str())
(která vypíše text se zlomkem)""")
print('z je', z.str())

print()
input("""zmáčkni [enter] pro zadání příkazu: print('z je', z.float())
(která vypíše text s vypočítaným zlomkem)""")
print('z je', z.float())

print()
input("""zmáčkni [enter] pro zadání příkazu: w = Zlomok(2, 4)
(která založí instanci třídy 'w' s danými hodnotami zlomku)""")
w = Zlomok(2, 4)

print()
input("""zmáčkni [enter] pro zadání příkazu: print('w je', w.str())
(která vypíše text se zlomkem)""")
print('w je', w.str())

print()
input("""zmáčkni [enter] pro zadání příkazu: print('w je', w.float())
(která vypíše text s vypočítaným zlomkem)""")
print('w je', w.float())

print()
input("""zmáčkni [enter] pro zavření programu""")
